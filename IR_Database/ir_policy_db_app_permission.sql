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
-- Table structure for table `app_permission`
--

DROP TABLE IF EXISTS `app_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `app_permission` (
  `appID` int NOT NULL,
  `permissionID` int NOT NULL,
  PRIMARY KEY (`appID`,`permissionID`),
  KEY `permissionID_idx` (`permissionID`),
  KEY `permissionID_idx1` (`permissionID`),
  CONSTRAINT `appID_fk` FOREIGN KEY (`appID`) REFERENCES `Apps_table` (`App_Id`),
  CONSTRAINT `permissionID_fk` FOREIGN KEY (`permissionID`) REFERENCES `Permission` (`PermissionID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_permission`
--

LOCK TABLES `app_permission` WRITE;
/*!40000 ALTER TABLE `app_permission` DISABLE KEYS */;
INSERT INTO `app_permission` VALUES (1,1),(4,1),(5,1),(6,1),(8,1),(9,1),(10,1),(11,1),(12,1),(13,1),(15,1),(18,1),(19,1),(22,1),(23,1),(24,1),(25,1),(27,1),(30,1),(32,1),(33,1),(34,1),(35,1),(36,1),(37,1),(38,1),(39,1),(40,1),(41,1),(42,1),(43,1),(44,1),(45,1),(46,1),(47,1),(48,1),(49,1),(1,2),(4,2),(5,2),(6,2),(8,2),(9,2),(10,2),(11,2),(12,2),(13,2),(16,2),(17,2),(18,2),(19,2),(20,2),(23,2),(24,2),(25,2),(28,2),(32,2),(33,2),(35,2),(36,2),(37,2),(38,2),(39,2),(40,2),(44,2),(45,2),(47,2),(48,2),(49,2),(1,3),(4,3),(5,3),(6,3),(8,3),(9,3),(10,3),(11,3),(12,3),(13,3),(15,3),(17,3),(18,3),(21,3),(22,3),(23,3),(26,3),(27,3),(28,3),(30,3),(32,3),(33,3),(35,3),(36,3),(37,3),(38,3),(39,3),(43,3),(44,3),(45,3),(46,3),(47,3),(48,3),(49,3),(1,4),(4,4),(5,4),(6,4),(8,4),(9,4),(10,4),(11,4),(12,4),(13,4),(15,4),(16,4),(17,4),(18,4),(19,4),(20,4),(21,4),(22,4),(23,4),(24,4),(25,4),(26,4),(27,4),(30,4),(32,4),(33,4),(34,4),(35,4),(36,4),(37,4),(38,4),(39,4),(40,4),(41,4),(43,4),(44,4),(45,4),(46,4),(47,4),(48,4),(1,5),(4,5),(5,5),(6,5),(8,5),(9,5),(11,5),(12,5),(16,5),(17,5),(18,5),(19,5),(21,5),(22,5),(23,5),(26,5),(28,5),(32,5),(33,5),(34,5),(35,5),(36,5),(37,5),(38,5),(39,5),(40,5),(41,5),(42,5),(44,5),(45,5),(46,5),(47,5),(48,5),(49,5),(5,6),(11,6),(18,6),(40,6),(6,8),(8,8),(9,8),(11,8),(12,8),(13,8),(15,8),(16,8),(17,8),(19,8),(20,8),(38,8),(44,8),(45,8),(1,9),(4,9),(5,9),(6,9),(8,9),(10,9),(11,9),(12,9),(17,9),(18,9),(21,9),(22,9),(23,9),(25,9),(26,9),(30,9),(32,9),(33,9),(34,9),(35,9),(36,9),(37,9),(38,9),(39,9),(41,9),(43,9),(44,9),(45,9),(46,9),(47,9),(48,9),(49,9),(1,10),(33,10),(35,10),(38,10),(39,10),(40,10),(45,10),(46,10),(47,10),(48,10),(49,10),(9,11),(42,11),(43,11),(1,12),(6,12),(10,12),(44,12);
/*!40000 ALTER TABLE `app_permission` ENABLE KEYS */;
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
