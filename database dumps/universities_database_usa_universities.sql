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
-- Table structure for table `usa_universities`
--

DROP TABLE IF EXISTS `usa_universities`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usa_universities` (
  `university_id` int(11) NOT NULL AUTO_INCREMENT,
  `university_object_id` int(11) DEFAULT NULL,
  `geo_point` varchar(400) DEFAULT NULL,
  `geo_shape` varchar(400) DEFAULT NULL,
  `ipedsid` int(11) DEFAULT NULL,
  `university_name` varchar(500) DEFAULT NULL,
  `university_address` varchar(1000) DEFAULT NULL,
  `city_id` int(11) DEFAULT NULL,
  `state_id` int(11) DEFAULT NULL,
  `zipcode` int(11) DEFAULT NULL,
  `zip4` varchar(200) DEFAULT NULL,
  `telephone` varchar(15) DEFAULT NULL,
  `university_type` int(11) DEFAULT NULL,
  `status_id` int(11) DEFAULT NULL,
  `population` int(11) DEFAULT NULL,
  `county_id` int(11) DEFAULT NULL,
  `county_fips` varchar(400) DEFAULT NULL,
  `country_id` int(11) DEFAULT NULL,
  `latitude` double DEFAULT NULL,
  `longitude` double DEFAULT NULL,
  `naics_id` int(11) DEFAULT NULL,
  `source` varchar(400) DEFAULT NULL,
  `source_date` date DEFAULT NULL,
  `validation_method` varchar(400) DEFAULT NULL,
  `validation_date` date DEFAULT NULL,
  `website` varchar(400) DEFAULT NULL,
  `stfips` varchar(400) DEFAULT NULL,
  `cofips` varchar(400) DEFAULT NULL,
  `sector` int(11) DEFAULT NULL,
  `level` int(11) DEFAULT NULL,
  `hi_offer` int(11) DEFAULT NULL,
  `degree_grant` int(11) DEFAULT NULL,
  `locale` int(11) DEFAULT NULL,
  `close_date` date DEFAULT NULL,
  `merge_id` int(11) DEFAULT NULL,
  `alias` varchar(400) DEFAULT NULL,
  `size_set` int(11) DEFAULT NULL,
  `inst_size` int(11) DEFAULT NULL,
  `part_time_enroll` int(11) DEFAULT NULL,
  `full_time_enroll` int(11) DEFAULT NULL,
  `total_enroll` int(11) DEFAULT NULL,
  `housing` int(11) DEFAULT NULL,
  `dorm_capacity` int(11) DEFAULT NULL,
  `shelter_id` varchar(400) DEFAULT NULL,
  PRIMARY KEY (`university_id`),
  KEY `city_us_id_fk` (`city_id`),
  KEY `state_us_id_fk` (`state_id`),
  KEY `status_us_id_fk` (`status_id`),
  KEY `county_us_id_fk` (`county_id`),
  KEY `country_us_id_fk` (`country_id`),
  CONSTRAINT `city_us_id_fk` FOREIGN KEY (`city_id`) REFERENCES `us_cities` (`city_id`),
  CONSTRAINT `country_us_id_fk` FOREIGN KEY (`country_id`) REFERENCES `country` (`country_id`),
  CONSTRAINT `county_us_id_fk` FOREIGN KEY (`county_id`) REFERENCES `us_county` (`county_id`),
  CONSTRAINT `state_us_id_fk` FOREIGN KEY (`state_id`) REFERENCES `us_states` (`state_id`),
  CONSTRAINT `status_us_id_fk` FOREIGN KEY (`status_id`) REFERENCES `university_status` (`status_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usa_universities`
--

LOCK TABLES `usa_universities` WRITE;
/*!40000 ALTER TABLE `usa_universities` DISABLE KEYS */;
/*!40000 ALTER TABLE `usa_universities` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-04-04 22:11:08
