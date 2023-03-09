-- MySQL dump 10.13  Distrib 8.0.28, for macos11 (x86_64)
--
-- Host: localhost    Database: ir_policy_db
-- ------------------------------------------------------
-- Server version	8.0.28

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Apps_table`
--

DROP TABLE IF EXISTS `Apps_table`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Apps_table` (
  `App_Id` int NOT NULL,
  `type_id` int NOT NULL,
  `App_Name` varchar(45) NOT NULL,
  `Privacy_policy` longtext NOT NULL,
  `Summary` longtext NOT NULL,
  `Score` int NOT NULL,
  `Rating` int NOT NULL,
  `Paid` int NOT NULL,
  PRIMARY KEY (`App_Id`),
  KEY `type_fk_idx` (`type_id`),
  CONSTRAINT `type_fk` FOREIGN KEY (`type_id`) REFERENCES `type` (`type_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Apps_table`
--

LOCK TABLES `Apps_table` WRITE;
/*!40000 ALTER TABLE `Apps_table` DISABLE KEYS */;
INSERT INTO `Apps_table` VALUES (1,1,'Whatsapp','\"NA\"','\"NA\"',0,4,0),(2,1,'WeChat','\"NA\"','\"NA\"',0,2,0),(3,1,'SnapChat','\"NA\"','\"NA\"',0,4,0),(4,10,'Instagram','\"NA\"','\"NA\"',0,4,0),(5,10,'Facebook','\"NA\"','\"NA\"',0,4,0),(6,1,'Telegram','\"NA\"','\"NA\"',0,4,0),(7,10,'Tumblr','\"NA\"','\"NA\"',0,5,0),(8,10,'Twitter','\"NA\"','\"NA\"',0,4,0),(9,2,'Google Maps','\"NA\"','\"NA\"',0,4,0),(10,3,'Google Meet','\"NA\"','\"NA\"',0,4,0),(11,3,'Zoom','\"NA\"','\"NA\"',0,4,0),(12,3,'Microsoft Teams','\"NA\"','\"NA\"',0,5,0),(13,3,'Discord','\"NA\"','\"NA\"',0,4,0),(14,3,'Skype','\"NA\"','\"NA\"',0,4,0),(15,4,'Spotify','\"NA\"','\"NA\"',0,4,2),(16,4,'YT music','\"NA\"','\"NA\"',0,4,2),(17,4,'Prime music','\"NA\"','\"NA\"',0,4,2),(18,4,'Gaana','\"NA\"','\"NA\"',0,4,2),(19,4,'Saavn','\"NA\"','\"NA\"',0,4,2),(20,5,'Netflix','\"NA\"','\"NA\"',0,4,1),(21,5,'Amazon Prime Video','\"NA\"','\"NA\"',0,4,1),(22,5,'Disney Hotstar','\"NA\"','\"NA\"',0,4,1),(23,5,'Youtube','\"NA\"','\"NA\"',0,4,0),(24,5,'Dailymotion','\"NA\"','\"NA\"',0,4,0),(25,5,'Vimeo','\"NA\"','\"NA\"',0,4,0),(26,6,'Google Photos','\"NA\"','\"NA\"',0,4,0),(27,6,'Google Drive','\"NA\"','\"NA\"',0,4,2),(28,6,'Google Keep - Notes','\"NA\"','\"NA\"',0,4,0),(29,6,'Adobe Cloud','\"NA\"','\"NA\"',0,4,1),(30,6,'Microsoft OneDrive','\"NA\"','\"NA\"',0,5,2),(31,6,'DropBox','\"NA\"','\"NA\"',0,5,2),(32,7,'Zomato','\"NA\"','\"NA\"',0,5,2),(33,7,'Swiggy','\"NA\"','\"NA\"',0,4,2),(34,7,'Zepto','\"NA\"','\"NA\"',0,5,0),(35,7,'Blinkit','\"NA\"','\"NA\"',0,4,0),(36,7,'Big Basket','\"NA\"','\"NA\"',0,5,0),(37,7,'Uber Eats','\"NA\"','\"NA\"',0,4,0),(38,7,'Amazon','\"NA\"','\"NA\"',0,4,2),(39,7,'Flipkart','\"NA\"','\"NA\"',0,4,0),(40,7,'Myntra','\"NA\"','\"NA\"',0,4,0),(41,7,'Urbanic','\"NA\"','\"NA\"',0,5,0),(42,8,'Google Fit','\"NA\"','\"NA\"',0,4,0),(43,8,'MyFitnesspal','\"NA\"','\"NA\"',0,4,0),(44,8,'Health','\"NA\"','\"NA\"',0,4,0),(45,9,'Uber','\"NA\"','\"NA\"',0,4,0),(46,9,'Ola','\"NA\"','\"NA\"',0,4,0),(47,11,'PayTM','\"NA\"','\"NA\"',0,5,0),(48,11,'Phonepe','\"NA\"','\"NA\"',0,4,0),(49,11,'GPay','\"NA\"','\"NA\"',0,4,0);
/*!40000 ALTER TABLE `Apps_table` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-03-09 22:53:17
