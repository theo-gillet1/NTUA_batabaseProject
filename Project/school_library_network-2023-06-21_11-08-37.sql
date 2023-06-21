-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: localhost    Database: school_library_network
-- ------------------------------------------------------
-- Server version	8.0.33

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `t_admin`
--

DROP TABLE IF EXISTS `t_admin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `t_admin` (
  `Id_admin` int unsigned NOT NULL AUTO_INCREMENT,
  `Name_admin` varchar(50) NOT NULL,
  `Username_admin` varchar(50) NOT NULL,
  `Password_admin` varchar(50) NOT NULL,
  `Age_admin` tinyint NOT NULL,
  PRIMARY KEY (`Id_admin`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_admin`
--

LOCK TABLES `t_admin` WRITE;
/*!40000 ALTER TABLE `t_admin` DISABLE KEYS */;
INSERT INTO `t_admin` VALUES (34,'Theo','Admin','Databasentua23',23),(40,'Johan','Admin2','1',21);
/*!40000 ALTER TABLE `t_admin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t_book`
--

DROP TABLE IF EXISTS `t_book`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `t_book` (
  `Id_book` int unsigned NOT NULL AUTO_INCREMENT,
  `Title_book` varchar(255) NOT NULL,
  `Publisher_book` varchar(255) NOT NULL,
  `ISBN_book` varchar(30) NOT NULL,
  `Authors_book` varchar(255) NOT NULL,
  `Nmb_Page_book` int NOT NULL,
  `Summary_book` varchar(1000) NOT NULL,
  `Inventory_book` int NOT NULL,
  `Image_book` varchar(1000) DEFAULT NULL,
  `Category_book` varchar(100) NOT NULL,
  `Language_book` varchar(20) NOT NULL,
  `Keywords_book` varchar(255) NOT NULL,
  `Operator_ID_book` int unsigned NOT NULL,
  PRIMARY KEY (`Id_book`),
  KEY `Operator_ID_book` (`Operator_ID_book`),
  CONSTRAINT `t_book_ibfk_1` FOREIGN KEY (`Operator_ID_book`) REFERENCES `t_operator` (`Id_operator`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_book`
--

LOCK TABLES `t_book` WRITE;
/*!40000 ALTER TABLE `t_book` DISABLE KEYS */;
INSERT INTO `t_book` VALUES (4,'The Sword of Destiny','Mystical Books Publishing','978-0-987654-32-1','Samuel Morgan',400,'Join the heroic journey of a young warrior destined to wield the legendary Sword of Destiny and save the realm from an ancient evil.',1,'NaN','Mystery/Thriller','English','Sword, Destiny, Warrior, Ancient Evil',1),(6,'The Enigma of Shadows','Mystical Books Publishing','978-1-234567-89-0','Emily Nightshade',260,'A gripping tale of a detective\'s pursuit to unravel the secrets hidden within the shadowy depths of a small town.',2,'NaN','Mystery/Thriller','English','Shadows, Detective, Secrets',1),(7,'Beyond the Stars','Stellar Publishing House','978-3-210987-65-4','Aurora Nova',280,'Venture into the unknown as a group of explorers embarks on a space odyssey, encountering alien civilizations and the wonders of the universe.',2,'NaN','Science Fiction','English/Greek','Stars, Space, Exploration, Alien Civilizations',1),(8,'The Forgotten Kingdom','Historical Tales Press','978-6-543210-98-7','William Greenwood',450,'Set in a time of kings and queens, this epic saga follows the journey of a lost prince as he reclaims his birthright and restores a forgotten kingdom.',1,'NaN','Historical Fiction','English','Kingdom, Prince, Saga, Birthright',1),(9,'Whispers in the Wind',' Serenity Books','978-9-876543-21-0','Sophia Rivers',320,'In a quaint seaside town, a woman unravels a series of mysterious whispers that lead her on a captivating journey of love, loss, and self-discovery.',2,'NaN','Romance/Drama','English/Greek','Whispers, Wind, Seaside, Love, Self-discovery',1),(10,'The Chronicles of Eldoria',' Fantasy Realm Publishing','978-5-432109-87-6','Ethan Fireheart',560,'Immerse yourself in a richly detailed world of magic and adventure as heroes battle ancient creatures and uncover the secrets of the mystical land of Eldoria.',1,'NaN','Fantasy/Adventure','Greek','Chronicles, Eldoria, Magic',1),(11,'The Crimson Cipher','Enigma Publishing','978-1-876543-21-0','Julian Blackwood',400,'A gripping espionage thriller where a brilliant cryptographer races against time to decode a mysterious message that holds the key to global security.',1,'NaN','Suspense/Thriller','Greek','Cipher, Cryptographer, Espionage, Global Security',1),(12,'Echoes of Eternity','Timeless Tales Press','978-0-987654-32-3','Amelia Hart',320,'A mesmerizing tale that weaves together the lives of characters across different time periods, connected by echoes of love, destiny, and the power of human connection.',2,'NaN','Historical Fiction/Romance','English/Greek','Echoes, Eternity, Time, Love, Destiny',1),(13,'The Quantum Paradox','Infinity Books','978-3-210987-67-4','Xavier Blake',280,'Enter the mind-bending realm of quantum physics as a brilliant scientist unravels the secrets of time, space, and the enigmatic nature of reality.',1,'NaN','Science Fiction/Thriller','Greek','Quantum, Paradox, Scientist, Reality, Physics',1),(14,'The Silent Symphony','Harmony Publications','978-6-785210-98-7','Lily Mitchell',355,'Follow the journey of a gifted musician as she navigates a world of passion, loss, and the transformative power of music, expressed through a silent symphony.',2,'NaN','Contemporary Fiction/Drama','English/Greek','Silent Symphony, Musician, Passion, Loss',1),(15,'Infinite Horizons','Voyager Books',' 978-9-872373-21-0','Sebastian Reed',450,' Embark on an epic adventure across vast and diverse landscapes, where heroes face unimaginable challenges and discover the limitless possibilities that lie beyond the horizon.',2,'NaN','Fantasy/Adventure','Greek','Infinite, Horizons, Epic Adventure, Heroes',2),(16,'Quantum Computing: Exploring the Future','Scientific Press','975-1-234567-89-0','Dr. Alexander Hamilton',320,' Dive into the world of quantum computing and its potential applications in revolutionizing computation and data processing.',4,'NaN','Science/Informatics','English/Greek','Quantum Computing',2),(17,'Introduction to Data Structures and Algorithms','TechPub','978-0-987654-32-7','Dr. Emily Martinez',400,'A comprehensive guide for computer science students, providing a solid foundation in understanding data structures and algorithms essential for efficient programming.',3,'NaN','Informatics/Database','English','Algorithms, Data',2),(18,'Strategic Management in Global Business',' BusinessWorld Publishers','978-6-543447-98-7','Sophia Roberts',450,'Offering insights into strategic decision-making and its impact on international business, this book equips students with tools and frameworks to navigate the complexities of the global marketplace.',3,'NaN','Business/Management ','English/Greek','Financial Management, Strategies, Success, Money',2),(19,'Constitutional Law: Principles and Cases','Legal Eagle Press',' 918-9-886543-21-0','Emma Harrison',550,'Exploring fundamental principles and landmark cases, this book offers a comprehensive overview of constitutional law, examining the balance between individual rights and government power.',4,'NaN','Law','English','Constitutional Law, Principles, Cases, Individual Rights, Government Power',2),(20,'The Art of Expression: Exploring Creativity in the Modern Age','ArtWorks Publishing','978-1-230269-89-0','Sophia Turner',320,'This book delves into the realm of art, examining different forms of expression, exploring the impact of art in society, and showcasing the works of renowned artists.',2,'NaN','Art','Greek','Expression, Creativity, Modern Age, Society, Artists',2),(21,'Power and Politics: Understanding the Dynamics of Governance','PoliSci Books','234-0-987654-32-1','Benjamin Davis',400,'Analyzing the intricate relationship between power and politics, this book explores different political systems, ideologies, and the dynamics of governance in contemporary societies.',2,'NaN','Politics','Greek','Power, Politics, Governance, Political Systems, Ideologies',1),(22,'Social Science Research Methods: A Comprehensive Guide','Sociological Publications','978-3-210987-65-7','Emily Johnson',325,'This book provides a comprehensive overview of research methods used in the social sciences, offering practical guidance on designing studies, collecting data, and analyzing findings.',3,'NaN','Social Science','English/Greek','Social Science, Research Methods, Comprehensive Guide, Study Design, Data Analysis',1),(23,'Architecture Through the Ages: From Ancient Wonders to Modern Marvels','ArchiBooks Ltd.','978-6-555210-98-7',' Christopher Moore',415,'Tracing the evolution of architecture, this book explores iconic structures from different historical periods, showcasing the brilliance of architectural design and its impact on society.',2,'NaN','Architecture','Greek','Architecture, Ages, Ancient Wonders, Modern Marvels, Architectural Design',1),(24,'The Future of Informatics: Emerging Technologies and Applications','TechTrends Publishing',' 018-1-234567-89-0','Dr. Alexander Roberts',320,'This book explores the latest advancements in informatics, including emerging technologies such as artificial intelligence, big data, and cybersecurity, and their applications in various industries.',3,'NaN','Informatics/Technology','English','Informatics, Emerging Technologies, Artificial Intelligence, Big Data, Cybersecurity',1);
/*!40000 ALTER TABLE `t_book` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t_operator`
--

DROP TABLE IF EXISTS `t_operator`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `t_operator` (
  `Id_operator` int unsigned NOT NULL AUTO_INCREMENT,
  `Name_operator` varchar(50) NOT NULL,
  `Username_operator` varchar(50) NOT NULL,
  `Password_operator` varchar(50) NOT NULL,
  `Age_operator` tinyint NOT NULL,
  `School_operator` varchar(50) NOT NULL,
  PRIMARY KEY (`Id_operator`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_operator`
--

LOCK TABLES `t_operator` WRITE;
/*!40000 ALTER TABLE `t_operator` DISABLE KEYS */;
INSERT INTO `t_operator` VALUES (1,'Leon','Op1','passe',26,'NTUA'),(2,'Lena','Op2','123',21,'AUEB'),(3,'Pascal','Pascal29','Mypasse',40,'ENIB');
/*!40000 ALTER TABLE `t_operator` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t_reservation`
--

DROP TABLE IF EXISTS `t_reservation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `t_reservation` (
  `Id_reser` int unsigned NOT NULL AUTO_INCREMENT,
  `Id_user_reser` int unsigned NOT NULL,
  `Id_book_reser` int unsigned NOT NULL,
  `State_reser` tinyint(1) DEFAULT NULL,
  `Operator_ID_reser` int DEFAULT NULL,
  PRIMARY KEY (`Id_reser`),
  KEY `Id_user_reser` (`Id_user_reser`),
  KEY `Id_book_reser` (`Id_book_reser`),
  CONSTRAINT `t_reservation_ibfk_1` FOREIGN KEY (`Id_user_reser`) REFERENCES `t_user` (`Id_user`),
  CONSTRAINT `t_reservation_ibfk_2` FOREIGN KEY (`Id_book_reser`) REFERENCES `t_book` (`Id_book`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_reservation`
--

LOCK TABLES `t_reservation` WRITE;
/*!40000 ALTER TABLE `t_reservation` DISABLE KEYS */;
INSERT INTO `t_reservation` VALUES (12,10,6,0,1),(13,10,4,0,1),(14,4,4,1,1),(15,4,4,0,1),(16,3,9,0,1),(17,23,21,0,1),(18,23,24,0,1),(19,21,21,0,1);
/*!40000 ALTER TABLE `t_reservation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t_school`
--

DROP TABLE IF EXISTS `t_school`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `t_school` (
  `Id_school` int unsigned NOT NULL AUTO_INCREMENT,
  `Name_school` varchar(50) NOT NULL,
  `Adress_school` varchar(100) NOT NULL,
  `City_school` varchar(20) NOT NULL,
  `Phone_school` varchar(15) NOT NULL,
  `Email_school` varchar(30) NOT NULL,
  `Director_school` varchar(50) NOT NULL,
  `Operator_ID_school` int unsigned NOT NULL,
  `Operator_school` varchar(50) NOT NULL,
  PRIMARY KEY (`Id_school`),
  KEY `Operator_ID_school` (`Operator_ID_school`),
  CONSTRAINT `t_school_ibfk_1` FOREIGN KEY (`Operator_ID_school`) REFERENCES `t_operator` (`Id_operator`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_school`
--

LOCK TABLES `t_school` WRITE;
/*!40000 ALTER TABLE `t_school` DISABLE KEYS */;
/*!40000 ALTER TABLE `t_school` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t_user`
--

DROP TABLE IF EXISTS `t_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `t_user` (
  `Id_user` int unsigned NOT NULL AUTO_INCREMENT,
  `Name_user` varchar(50) NOT NULL,
  `Username_user` varchar(50) NOT NULL,
  `Password_user` varchar(50) NOT NULL,
  `Age_user` tinyint NOT NULL,
  `School_user` varchar(50) NOT NULL,
  `Status_user` enum('Student','Teacher') NOT NULL,
  `Borrow_user` tinyint DEFAULT NULL,
  `Approved_user` tinyint(1) DEFAULT NULL,
  `Operator_ID_user` int unsigned NOT NULL,
  `Operator_user` varchar(50) NOT NULL,
  PRIMARY KEY (`Id_user`),
  KEY `Operator_ID_user` (`Operator_ID_user`),
  CONSTRAINT `t_user_ibfk_1` FOREIGN KEY (`Operator_ID_user`) REFERENCES `t_operator` (`Id_operator`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_user`
--

LOCK TABLES `t_user` WRITE;
/*!40000 ALTER TABLE `t_user` DISABLE KEYS */;
INSERT INTO `t_user` VALUES (1,'John','Jonny','Mypasse',21,'NTUA','Student',0,1,1,'Leon'),(3,'Alex','Alex22','5543',22,'NTUA','Student',0,1,1,'Leon'),(4,'Lea','aela','11446',25,'NTUA','Student',1,1,1,'Leon'),(5,'Daniel','Dann','8955',55,'NTUA','Teacher',0,1,1,'Leon'),(6,'Marco','marco20','!kM8_-Vv~5_ZLvM',20,'NTUA','Student',0,1,1,'Leon'),(7,'Katerina','kati','qwer',25,'NTUA','Student',0,1,1,'Leon'),(10,'Leon','Leonidas','1',26,'NTUA','Student',0,1,1,'Leon'),(11,'Sofia','Sofia000','51684512',25,'ENIB','Student',0,1,3,'Pascal'),(12,'Joseph','jojo','4845+9',23,'NTUA','Student',0,1,1,'Leon'),(13,'Roger','ro','1',25,'NTUA','Student',0,1,1,'Leon'),(14,'Jule','Juju','123',23,'NTUA','Student',0,1,1,'Leon'),(15,'Mathieux','Math01','123',24,'ENIB','Student',0,1,3,'Pascal'),(16,'Yann','Yaya','1598',22,'NTUA','Student',0,1,1,'Leon'),(17,'Emma','Emma11','159',23,'NTUA','Student',0,1,1,'Leon'),(18,'Noah','Noah14','764',22,'NTUA','Student',0,1,1,'Leon'),(19,'Ava','Ava57','957',22,'NTUA','Student',0,1,1,'Leon'),(20,'Liam','Liam59','845',22,'NTUA','Student',0,1,1,'Leon'),(21,'Isabella','Isa','112',35,'NTUA','Teacher',0,1,1,'Leon'),(22,'Jackson','Jack','445',29,'NTUA','Teacher',0,1,1,'Leon'),(23,'Olivia','Oli','556',31,'NTUA','Teacher',0,1,1,'Leon'),(24,'Oliver','oli55','887',23,'AUEB','Student',0,NULL,2,'Lena'),(25,'Charlotte','charl88','987',25,'AUEB','Student',0,NULL,2,'Lena'),(26,'Elijah','Eli001','864',33,'AUEB','Teacher',0,NULL,2,'Lena'),(27,'Lily','Lily22','215',37,'AUEB','Teacher',0,NULL,2,'Lena');
/*!40000 ALTER TABLE `t_user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-06-21 11:08:37
