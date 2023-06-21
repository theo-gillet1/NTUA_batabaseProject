import mysql.connector
import time

def save_new_user(name,username,password,age,school,status):

    try :
        connection = mysql.connector.connect(
        host="localhost",
        user="Admin",
        password="Databasentua23",
        database="school_library_network",
        )
        cursor = connection.cursor()

        print(type(connection))
        print(type(cursor))

        #Select all the user of my sql
        cursor.execute("SELECT User, Host FROM mysql.user;")
        result = cursor.fetchall()
        print(result)
        #SELECT OP
        cursor.execute('Select Id_operator, Name_operator from t_operator WHERE School_operator = %s',[school])
        result = cursor.fetchall()
        id_operator = result[0][0]
        name_operator = result[0][1]
        

        #ADD USER INTO USER TABLE
        user = (cursor.lastrowid,name,username,password,age,school,status,0,None,id_operator,name_operator)
        req = "INSERT INTO t_user() VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
        #print(req , user)
        cursor.execute(req, user)
        connection.commit()

        #SELECT ALL USER FROM ADMIN
        cursor.execute('Select * from t_user')
        result = cursor.fetchall()
        print('######################################################')
        print(result)

        

    except Exception as e:
        print(['ERROR'], e)
        connection.rollback()

    finally:
        connection.close()


def login_user(username,password):
    try :
        connection = mysql.connector.connect(
        host="localhost",
        user="Admin",
        password="Databasentua23",
        database="school_library_network",
        )
        cursor = connection.cursor()

        user = (username,password)
        
        print(type(connection))
        print(type(cursor))

        ###################   Admin login   ###################
        query = "SELECT Username_admin, Password_admin FROM t_admin WHERE Username_admin = %s AND Password_admin = %s"
        cursor.execute(query, (username, password))
        result = cursor.fetchall()
        if result != []:
            cursor.execute("SELECT * FROM t_operator")
            data = cursor.fetchall()
            return 1,data,0
        
        ###################  Operator login  ###################
        query = "SELECT * FROM t_operator WHERE Username_operator = %s AND Password_operator = %s"
        cursor.execute(query, (username, password))
        operator = cursor.fetchall()
        if operator != []:
            #Selection of the list of waiters
            query = "SELECT * FROM t_user WHERE Approved_user IS NOT %s AND Operator_ID_user = %s"
            cursor.execute(query, [True,operator[0][0]])
            user_waitingList = cursor.fetchall()
            #Selection of the books
            cursor.execute("SELECT * FROM t_book WHERE Operator_ID_book = %s",[operator[0][0]])
            book = cursor.fetchall()
            if book == []:
                book=[[0,"No Book available","",""," "," ","","","","","","",operator[0][0]]]
            return 2,book,user_waitingList
        
        ###################   User login   ###################
        query = "SELECT * FROM t_user WHERE Username_user = %s AND Password_user = %s"
        cursor.execute(query, (username, password))
        user = cursor.fetchall()
        if user != []:
            if user[0][8]==1:
                cursor.execute("SELECT * FROM t_book WHERE Operator_ID_book = %s",[user[0][9]])
                book = cursor.fetchall()
                return 3,book,user
            else :
                return 4,"NaN",0
        else:
            return 0,"NaN",0
        

    except Exception as e:
        print(['ERROR'], e)
        connection.rollback()

    finally:
        connection.close()


def add_OP(name,username,password,age,school):
    try :
        connection = mysql.connector.connect(
        host="localhost",
        user="Admin",
        password="Databasentua23",
        database="school_library_network",
        )
        cursor = connection.cursor()
        
        #ADD NEW OP
        user = (cursor.lastrowid,name,username,password,age,school)
        req = "INSERT INTO t_operator() VALUES (%s,%s,%s,%s,%s,%s);"
        print(req , user)
        cursor.execute(req, user)
        connection.commit()

        cursor.execute("SELECT * FROM t_operator")
        data = cursor.fetchall()

        return data

    except Exception as e:
        print(['ERROR'], e)
        connection.rollback()

    finally:
        connection.close()

def del_OP(name):
    try :
        connection = mysql.connector.connect(
        host="localhost",
        user="Admin",
        password="Databasentua23",
        database="school_library_network",
        )
        cursor = connection.cursor()
        
        #DEL OP

        query = "DELETE FROM t_operator WHERE `Name_operator` = %s;"
        cursor.execute(query, [name])
        connection.commit()

        cursor.execute("SELECT * FROM t_operator")
        data = cursor.fetchall()

        print("Data :",data)
        return data

    except Exception as e:
        print(['ERROR'], e)
        connection.rollback()

    finally:
        connection.close()

def get_op():
    try :
        connection = mysql.connector.connect(
        host="localhost",
        user="Admin",
        password="Databasentua23",
        database="school_library_network",
        )
        cursor = connection.cursor()
        
        #GEt OPERATOR

        cursor.execute("SELECT * FROM t_operator")
        data = cursor.fetchall()

        return data

    except Exception as e:
        print(['ERROR'], e)
        connection.rollback()

    finally:
        connection.close()


def add_book(title,author,publisher,isbn,nmbP,SUM,copies,imgage,category,language,keyword,operator):
    try :
        connection = mysql.connector.connect(
        host="localhost",
        user="Admin",
        password="Databasentua23",
        database="school_library_network",
        )
        cursor = connection.cursor()
        #No validate user
        query = "SELECT * FROM t_user WHERE Approved_user IS NOT %s"
        cursor.execute(query, [True])
        user_approved = cursor.fetchall()
        user = (cursor.lastrowid,title,publisher,isbn,author,nmbP,SUM,copies,imgage,category,language,keyword,operator)
        req = "INSERT INTO t_book() VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"

        cursor.execute(req, user)
        connection.commit()

        cursor.execute("SELECT * FROM t_book WHERE Operator_ID_book = %s",[operator])
        data = cursor.fetchall()
        print("Book in data base", data )

        return data,user_approved

    except Exception as e:
        print(['ERROR'], e)
        connection.rollback()

    finally:
        connection.close()

def val_user(Id_user):
    try :
        connection = mysql.connector.connect(
        host="localhost",
        user="Admin",
        password="Databasentua23",
        database="school_library_network",
        )
        cursor = connection.cursor()
        query = "UPDATE t_user SET Approved_user = %s WHERE Id_user = %s"
        cursor.execute(query, [True,Id_user])
        connection.commit()



    except Exception as e:
        print(['ERROR'], e)
        connection.rollback()

    finally:
        connection.close()

def rej_user(Id_user):
    try :
        connection = mysql.connector.connect(
        host="localhost",
        user="Admin",
        password="Databasentua23",
        database="school_library_network",
        )
        cursor = connection.cursor()
        query = "UPDATE t_user SET Approved_user = %s WHERE Id_user = %s"
        cursor.execute(query, [False,Id_user])
        connection.commit()

    except Exception as e:
        print(['ERROR'], e)
        connection.rollback()

    finally:
        connection.close()

def get_books(Op_id):
    try :
        connection = mysql.connector.connect(
        host="localhost",
        user="Admin",
        password="Databasentua23",
        database="school_library_network",
        )
        cursor = connection.cursor()
        print("ID operator ",Op_id)
        req = "SELECT * FROM t_book WHERE Operator_ID_book = %s"
        cursor.execute(req,[Op_id])
        data = cursor.fetchall()
        if data == []:
            if data == []:
                data=[[0,"No Book available","",""," "," ","","","","","","",Op_id]]
        return data
    
    except Exception as e:
        print(['ERROR'], e)
        connection.rollback()

    finally:
        connection.close()

def get_user_approval(Op_id):
    try :
        connection = mysql.connector.connect(
        host="localhost",
        user="Admin",
        password="Databasentua23",
        database="school_library_network",
        )
        cursor = connection.cursor()

        #No validate user
        query = "SELECT * FROM t_user WHERE Approved_user IS NULL AND Operator_ID_user = %s"
        cursor.execute(query, [Op_id])
        user_approved = cursor.fetchall()
        return user_approved
    

    except Exception as e:
        print(['ERROR'], e)
        connection.rollback()

    finally:
        connection.close()

def get_user(id_user):
    try :
        connection = mysql.connector.connect(
        host="localhost",
        user="Admin",
        password="Databasentua23",
        database="school_library_network",
        )
        
        cursor = connection.cursor()

        #No validate user
        query = "SELECT * FROM t_user WHERE Id_user = %s"
        cursor.execute(query, [id_user])
        user = cursor.fetchall()
        print("USER GET USER ",user)
        return user
    

    except Exception as e:
        print(['ERROR'], e)
        connection.rollback()

    finally:
        connection.close()

def new_resa(book_user):
    try :
        connection = mysql.connector.connect(
        host="localhost",
        user="Admin",
        password="Databasentua23",
        database="school_library_network",
        )
        
        cursor = connection.cursor()

        #Check if book is available
        req = "SELECT * FROM t_book WHERE Id_book = %s"
        cursor.execute(req, [book_user[0]])
        book = cursor.fetchall()
        available = book[0][7]
        print("INVENTORY = ",available)

        #check if user can borrow the book
        query = "SELECT * FROM t_user WHERE Id_user = %s"
        cursor.execute(query, [book_user[1]])
        user = cursor.fetchall()
        reservation = user[0][7]
        print("RESERVATION = ",reservation)

        #Get all the book from the library
        query = "SELECT Operator_ID_user FROM t_user WHERE Id_user = %s"
        cursor.execute(query, [book_user[1]])
        op_id = cursor.fetchall()

        query = "SELECT * FROM t_book WHERE  Operator_ID_book = %s"
        cursor.execute(query, [op_id[0][0]])
        books = cursor.fetchall()
        print("books ; ",books)
        if available > 0 and reservation < 2:
            print("Condition validate")
            #Create a reservation
            state = True
            print("Operator ; ",op_id[0][0])
            resa = (cursor.lastrowid,book_user[1],book_user[0],state,op_id[0][0])
            req = "INSERT INTO t_reservation() VALUES (%s,%s,%s,%s,%s);"
            cursor.execute(req, resa)
            connection.commit()

            #Change value of reservation and available
            print("Reservation Before = ",reservation)
            print("available Before = ",available)
            reservation = reservation+1
            available = available-1
            print("Reservation After = ",reservation)
            print("available Before = ",available)

            req = "UPDATE t_book SET `Inventory_book` = %s WHERE `Id_book` = %s;"
            cursor.execute(req, [available, book_user[0]])
            connection.commit()

            req = "UPDATE t_user SET `Borrow_user` = %s WHERE `Id_user` = %s;"
            cursor.execute(req, [reservation, book_user[1]])
            connection.commit()

        return user, books
   

    except Exception as e:
        print(['ERROR'], e)
        connection.rollback()

    finally:
        connection.close()

def research_user(category, info,op_id):
    try :
        connection = mysql.connector.connect(
        host="localhost",
        user="Admin",
        password="Databasentua23",
        database="school_library_network",
        )
        cursor = connection.cursor()
        query1 = "SELECT * FROM t_user WHERE "
        query2 = "= %s and Operator_ID_user = %s;"
        query = query1 + category + query2
        cursor.execute(query, [info,op_id])
        user = cursor.fetchall()
        return user
    

    except Exception as e:
        print(['ERROR'], e)
        connection.rollback()

    finally:
        connection.close()


def update_user(column, newValue,userID):
    try :
        connection = mysql.connector.connect(
        host="localhost",
        user="Admin",
        password="Databasentua23",
        database="school_library_network",
        )
        cursor = connection.cursor()
        
        category = column+'_user'
        query1 = "UPDATE t_user SET "
        query2 = "= %s  WHERE `Id_user` = %s;"
        query = query1 + category + query2
        cursor.execute(query, [newValue,userID])
        connection.commit()
    

    except Exception as e:
        print(['ERROR'], e)
        connection.rollback()

    finally:
        connection.close()


def research_book(category, info,op_id):
    try :
        connection = mysql.connector.connect(
        host="localhost",
        user="Admin",
        password="Databasentua23",
        database="school_library_network",
        )
        cursor = connection.cursor()

        if category == "All":
            query = "SELECT * FROM t_book WHERE Operator_ID_book = %s;"
            cursor.execute(query, [op_id])
            book = cursor.fetchall()
            return book
        
        query1 = "SELECT * FROM t_book WHERE "
        query2 = "= %s and Operator_ID_book = %s;"
        query = query1 + category + query2
        cursor.execute(query, [info,op_id])
        book = cursor.fetchall()
        return book
    

    except Exception as e:
        print(['ERROR'], e)
        connection.rollback()

    finally:
        connection.close()

def update_book(column, newValue,userID):

    try :
        connection = mysql.connector.connect(
        host="localhost",
        user="Admin",
        password="Databasentua23",
        database="school_library_network",
        )
        cursor = connection.cursor()

        if column == 'Nmb_Page' or column == 'Inventory':
            newValue = int(newValue)
            print("new val TYPER", type(newValue))
        
        category = column+'_book'
        query1 = "UPDATE t_book SET "
        query2 = "= %s  WHERE `Id_book` = %s;"
        query = query1 + category + query2
        cursor.execute(query, [newValue,userID])
        connection.commit()
    

    except Exception as e:
        print(['ERROR'], e)
        connection.rollback()

    finally:
        connection.close()

def research_resa(category, info,op_id):
    try :
        connection = mysql.connector.connect(
        host="localhost",
        user="Admin",
        password="Databasentua23",
        database="school_library_network",
        )
        cursor = connection.cursor()
        
        query1 = "SELECT * FROM t_reservation WHERE "
        query2 = "= %s and Operator_ID_reser = %s;"
        query = query1 + category + query2
        cursor.execute(query, [info,op_id])
        resa = cursor.fetchall()
        return resa
    

    except Exception as e:
        print(['ERROR'], e)
        connection.rollback()

    finally:
        connection.close()

def update_resa(column,resaID,newValue):

    try :
        connection = mysql.connector.connect(
        host="localhost",
        user="Admin",
        password="Databasentua23",
        database="school_library_network",
        )
        cursor = connection.cursor()

        

        if column == "State" :
            #Get the user how borrow the book
            query1 = "SELECT Id_user_reser FROM t_reservation WHERE Id_reser = %s;"
            cursor.execute(query1, [resaID])
            user = cursor.fetchall()
            #Get the book
            query2 = "SELECT Id_book_reser FROM t_reservation WHERE Id_reser = %s;"
            cursor.execute(query2, [resaID])
            book = cursor.fetchall()

            print("resad ID ",resaID)
            print("book[0] ", book[0])
            print("user[0]", user[0])

            if newValue == 1:
                query = "UPDATE t_book SET Inventory_book = Inventory_book-1 WHERE `Id_book` = %s;"
                cursor.execute(query, [book[0][0]])
                connection.commit()

                query = "UPDATE t_user SET Borrow_user = Borrow_user+1 WHERE `Id_user` = %s;"
                cursor.execute(query, [user[0][0]])
                connection.commit()
            
            elif newValue == 0:
                query = "UPDATE t_book SET Inventory_book = Inventory_book+1 WHERE `Id_book` = %s;"
                cursor.execute(query, [book[0][0]])
                connection.commit()

                query = "UPDATE t_user SET Borrow_user = Borrow_user-1 WHERE `Id_user` = %s;"
                cursor.execute(query, [user[0][0]])
                connection.commit()

        
        
        category = column+'_reser'
        query1 = "UPDATE t_reservation SET "
        query2 = "= %s  WHERE `Id_reser` = %s;"
        query = query1 + category + query2
        cursor.execute(query, [newValue,resaID])
        connection.commit()

        #Get ID op
        query3 = "SELECT Operator_ID_user FROM t_user WHERE Id_user = %s;"
        cursor.execute(query3, [user[0][0]])
        Idop = cursor.fetchall()

        Id_op = Idop[0][0]

        return Id_op
    

    except Exception as e:
        print(['ERROR'], e)
        connection.rollback()

    finally:
        connection.close()
