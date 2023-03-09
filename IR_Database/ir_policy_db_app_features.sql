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
-- Table structure for table `app_features`
--

DROP TABLE IF EXISTS `app_features`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `app_features` (
  `appID` int NOT NULL,
  `featureID` int NOT NULL,
  PRIMARY KEY (`appID`,`featureID`),
  KEY `featureID_idx` (`featureID`),
  CONSTRAINT `appId` FOREIGN KEY (`appID`) REFERENCES `Apps_table` (`App_Id`),
  CONSTRAINT `featureID` FOREIGN KEY (`featureID`) REFERENCES `feature` (`featureID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_features`
--

LOCK TABLES `app_features` WRITE;
/*!40000 ALTER TABLE `app_features` DISABLE KEYS */;
INSERT INTO `app_features` VALUES (1,1),(2,1),(3,1),(4,1),(5,1),(6,1),(13,1),(1,2),(2,2),(3,2),(4,2),(5,2),(6,2),(13,2),(1,3),(2,3),(3,3),(4,3),(5,3),(7,3),(8,3),(2,4),(4,4),(5,4),(7,4),(8,4),(3,5),(9,5),(9,6),(1,7),(2,7),(3,7),(4,7),(5,7),(3,8),(4,8),(5,8),(4,9),(1,10),(2,10),(3,10),(4,10),(10,10),(11,10),(12,10),(13,10),(14,10),(15,11),(16,11),(17,11),(18,11),(19,11),(15,12),(16,12),(17,12),(18,12),(19,12),(20,13),(21,13),(22,13),(23,13),(24,13),(25,13),(20,14),(21,14),(22,14),(24,14),(25,14),(26,15),(27,15),(29,15),(30,15),(31,15),(27,16),(28,16),(29,16),(30,16),(31,16),(38,17),(39,17),(40,17),(41,17),(32,18),(33,18),(37,18),(34,19),(35,19),(36,19),(38,19),(42,20),(43,20),(44,20),(45,21),(46,21),(46,22),(47,23),(48,23),(49,23),(47,24),(48,24),(49,24);
/*!40000 ALTER TABLE `app_features` ENABLE KEYS */;
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
