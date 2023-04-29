CREATE DATABASE  IF NOT EXISTS `universities_database` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `universities_database`;
-- MySQL dump 10.13  Distrib 8.0.28, for macos11 (x86_64)
--
-- Host: 127.0.0.1    Database: universities_database
-- ------------------------------------------------------
-- Server version	5.7.39

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
-- Table structure for table `indian_states`
--

DROP TABLE IF EXISTS `indian_states`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `indian_states` (
  `state_id` int(11) NOT NULL AUTO_INCREMENT,
  `state` varchar(100) NOT NULL,
  PRIMARY KEY (`state_id`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `indian_states`
--

LOCK TABLES `indian_states` WRITE;
/*!40000 ALTER TABLE `indian_states` DISABLE KEYS */;
INSERT INTO `indian_states` VALUES (1,'Tripura'),(2,'Kerala'),(3,'Mizoram'),(4,'Chhattisgarh'),(5,'Arunachal Pradesh'),(6,'Odisha'),(7,'Gujarat'),(8,'Puducherry'),(9,'Goa'),(10,'Madhya Pradesh'),(11,'Punjab'),(12,'Jammu and Kashmir'),(13,'Uttarakhand'),(14,'Tamil Nadu'),(15,'Rajasthan'),(16,'Jharkhand'),(17,'Nagaland'),(18,'Uttar Pradesh'),(19,'Dadra and Nagar Haveli'),(20,'Bihar'),(21,'Haryana'),(22,'Assam'),(23,'Maharashtra'),(24,'Manipur'),(25,'Delhi'),(26,'Karnataka'),(27,'Meghalaya'),(28,'Telangana'),(29,'Chandigarh'),(30,'West Bengal'),(31,'Sikkim'),(32,'Andaman and Nicobar Islands'),(33,'Andhra Pradesh'),(34,'Himachal Pradesh');
/*!40000 ALTER TABLE `indian_states` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-04-04 22:11:07
