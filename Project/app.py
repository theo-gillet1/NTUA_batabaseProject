from flask import Flask, render_template, request,redirect, url_for, Response
import database
import re
import os
import time

app = Flask(__name__,template_folder='templates')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/save', methods=['POST'])
def save():
    #Save a new user
    signup_name = request.form['name']
    signup_username = request.form['username']
    signup_password = request.form['password']
    signup_age = request.form['age']
    signup_school = request.form['school']
    signup_status = request.form['status']
    database.save_new_user(signup_name,signup_username,signup_password,signup_age,signup_school,signup_status)

    return render_template('login.html')

@app.route('/log', methods=['POST'])
def log():
    login_username = request.form['username']
    login_password = request.form['password']
    val,data,user = database.login_user(login_username,login_password)
    if val == 3:
        print("USER successfully connected")
        return render_template('home.html',book=data, user=user)
    elif val == 2:
        print("OPERATOR successfully connected")
        return render_template('op-home.html',data=data, users=user,research_user=[[]])
    elif val == 1:
        print("ADMIN successfully connected")
        return render_template('admin-home.html',data=data)
    elif val == 4:
        return render_template('rejected.html')

    else :
         return render_template('error.html')
    
#add a new operator
@app.route('/add', methods=['POST'])
def Add_Operator():
    newOp_name = request.form['Name']
    newOp_username = request.form['username']
    newOp_password = request.form['Password']
    newOp_age = request.form['Age']
    newOp_school = request.form['School']
    data = database.add_OP(newOp_name,newOp_username,newOp_password,newOp_age,newOp_school)
    return render_template('admin-home.html',data=data)

#delete an operator
@app.route('/del', methods=['POST'])
def Del_Operator():
    delOp_name = request.form['delOP']
    data = database.del_OP(delOp_name)
    return render_template('admin-home.html',data=data)

#add a new book in the library
@app.route('/add_book', methods=['POST'])
def Add_book():
    newBook_title = request.form["Title"]
    newBook_author = request.form["Author"]
    newBook_publisher = request.form["Publisher"]
    newBook_isbn = request.form["ISBN"]
    newBook_nmbP = int(request.form["number of pages"])
    newBook_sum = request.form["Summary"]
    newBook_copies = int(request.form["available copies"])
    newBook_img = request.form["image"]
    newBook_cat = request.form["thematic category"]
    newBook_lang = request.form["language"]
    newBook_key = request.form["keywords"]
    newBook_op = request.form["newBook_bt"]
    newBook,user_approved = database.add_book(newBook_title,newBook_author,newBook_publisher,newBook_isbn,newBook_nmbP,newBook_sum,newBook_copies,newBook_img,newBook_cat,newBook_lang,newBook_key,newBook_op)
    data = newBook
    #user_approved = [user_approved]
    return render_template('op-home.html',data=data,users=user_approved,research_user=[[]])

#Accept new user
@app.route('/val_user', methods=['POST'])
def Val_user():
    userId = int(request.form["Accept_bt"])
    database.val_user(userId)
    user = database.get_user(userId)
    data = database.get_books(user[0][9])
    user_list = database.get_user_approval(user[0][9])
    return render_template('op-home.html',data=data,users=user_list,research_user=[[]])


@app.route('/reject_user', methods=['POST'])
def Rej_user():
    userId = int(request.form["Reject_bt"])
    database.rej_user(userId)
    user = database.get_user(userId)
    data = database.get_books(user[0][9])
    user_list = database.get_user_approval(user[0][9])
    return render_template('op-home.html',data=data,users=user_list,research_user=[[]])

@app.route('/reservation', methods=['POST'])
def Borrow():
    bookuser_id = request.form["Resa_bt"]
    bookuser_id = [int(s) for s in re.findall(r'\b\d+\b', bookuser_id)]
    
    user,books = database.new_resa(bookuser_id)
    return render_template('home.html',book=books, user=user)


@app.route('/search_user', methods=['POST'])
def Find_User():
    user_column = request.form["options"]
    user_info = request.form["Research_in"]
    op_id = request.form["Research_bt"]
    op_id = [int(s) for s in re.findall(r'\b\d+\b', op_id)]
    find_user= database.research_user(user_column,user_info,op_id[0])
    data = database.get_books(op_id[0])
    user = database.get_user_approval(op_id[0])

    return render_template('op-home.html',data=data, users=user, research_user = find_user)

@app.route('/modif_user', methods=['POST'])
def Modif_user():

    selected_value = request.form.get('selectedRowInput')
    selected_id = request.form.get('additionalItemInput')
    selected_column = request.form.get('columnNameInput')
    new_value = request.form["NewValue"]

    Selected_value = list(selected_value.split(', '))
    Selected_id = list(selected_id.split(': '))
    Selected_column = list(selected_column.split(': '))

    """print("New Value ",new_value)
    print("Select Value ",selected_value)
    print("ITEM 1->",Selected_value)
    print("ITEM 2->",Selected_value[9] )
    print("ITEM 3->",Selected_column[1] )"""

    database.update_user(Selected_column[1],new_value,Selected_id[1])

    data = database.get_books(Selected_value[9])
    user = database.get_user_approval(Selected_value[9])
    print("Database ",data)
    print("User ",user)
    return render_template('op-home.html',data=data, users=user, research_user = [[]])


@app.route('/search_book', methods=['POST'])
def Find_Book():
    book_column = request.form["optionsbook"]
    book_info = request.form["ResearchBook_in"]
    op_id = request.form["ResearchBook_bt"]
    op_id = [int(s) for s in re.findall(r'\b\d+\b', op_id)]
    find_book= database.research_book(book_column,book_info,op_id[0])
    data = database.get_books(op_id[0])
    user = database.get_user_approval(op_id[0])

    return render_template('op-home.html',data=data, users=user, research_book = find_book)


@app.route('/modif_book', methods=['POST'])
def Modif_book():

    selected_value = request.form.get('hiddenRow')
    selected_id = request.form.get('hiddenId')
    selected_column = request.form.get('hiddencolumn')
    new_value = request.form["NewValueBook"]

    Selected_value = list(selected_value.split(': '))
    Selected_id = list(selected_id.split(': '))
    Selected_column = list(selected_column.split(': '))

    database.update_book(Selected_column[1],new_value,Selected_value[1])


    data = database.get_books(Selected_id[1])
    user = database.get_user_approval(Selected_id[1])
    return render_template('op-home.html',data=data, users=user)


@app.route('/search_resa', methods=['POST'])
def Find_Resa():
    resa_column = request.form["optionsResa"]
    resa_info = request.form["ResearchResa_in"]
    op_id = request.form["ResearchResa_bt"]
    op_id = [int(s) for s in re.findall(r'\b\d+\b', op_id)]

    reservation = database.research_resa(resa_column,resa_info,op_id[0])

    data = database.get_books(op_id[0])
    user = database.get_user_approval(op_id[0])

    return render_template('op-home.html',data=data, users=user, research_resa = reservation)

@app.route('/modif_resa', methods=['POST'])
def Modif_resa():

    selected_value = request.form.get('selectedValueInput')
    selected_id = request.form.get('selectedIdInput')
    selected_column = request.form.get('selectedColInput')
    new_value = request.form["UpdateValue"]


    Selected_value = list(selected_value.split(': '))
    Selected_id = list(selected_id.split(': '))
    Selected_column = list(selected_column.split(': '))

    id_resa = int(Selected_id[1])
    new_value = int(new_value)

    id_op = database.update_resa(Selected_column[1],id_resa,new_value)

    data = database.get_books(id_op)
    user = database.get_user_approval(id_op)

    return render_template('op-home.html',data=data, users=user)

@app.route('/backup', methods=['POST'])
def Backup():
    DB_HOST = 'localhost'
    DB_USER = 'Admin'
    DB_PASS = 'Databasentua23'
    DB_NAME = 'school_library_network'

    BACKUP_DIR = os.getcwd()
    date_format = '%Y-%m-%d_%H-%M-%S'

    current_time = time.strftime(date_format)

    backup_file = f'{DB_NAME}-{current_time}.sql'

    backup_file_path = os.path.join(BACKUP_DIR, backup_file)

    mysqldump_cmd = f'mysqldump -h {DB_HOST} -u {DB_USER} -p{DB_PASS} {DB_NAME} > {backup_file}'
    os.system(mysqldump_cmd)

    gzip_cmd = f'gzip {backup_file_path}'
    os.system(gzip_cmd)

    find_cmd  = f'find {BACKUP_DIR} -type f -name "*.gz" -mtime +7 -delete'
    os.system(find_cmd)

    print("BACKUP SAVED")
    data = database.get_op()

    return render_template('admin-home.html',data=data)



if __name__ == '__main__':
    app.run(debug=True)
