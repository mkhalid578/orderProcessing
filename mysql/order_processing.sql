-- MySQL dump 10.13  Distrib 5.7.17, for macos10.12 (x86_64)
--
-- Host: 127.0.0.1    Database: oder_processing_data
-- ------------------------------------------------------
-- Server version	5.7.17

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `company`
--

DROP TABLE IF EXISTS `company`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `company` (
  `name` varchar(500) NOT NULL,
  `password` varchar(12) NOT NULL,
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `company`
--

LOCK TABLES `company` WRITE;
/*!40000 ALTER TABLE `company` DISABLE KEYS */;
INSERT INTO `company` VALUES ('railpod','1811');
/*!40000 ALTER TABLE `company` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employinfo`
--

DROP TABLE IF EXISTS `employinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `employinfo` (
  `first-name` varchar(100) NOT NULL,
  `last-name` varchar(100) NOT NULL,
  `email-id` varchar(100) NOT NULL,
  `user-id` varchar(45) NOT NULL,
  `password` varchar(10) NOT NULL,
  `position` varchar(45) NOT NULL,
  `department` varchar(100) NOT NULL,
  `company-name` varchar(500) NOT NULL,
  `order-handler` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`user-id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employinfo`
--

LOCK TABLES `employinfo` WRITE;
/*!40000 ALTER TABLE `employinfo` DISABLE KEYS */;
INSERT INTO `employinfo` VALUES ('vibhuti','patel','vibhuti_patel1@student.uml.edu','vibhuti_patel1','1811','student','eecs','uml',0);
/*!40000 ALTER TABLE `employinfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `item-order`
--

DROP TABLE IF EXISTS `item-order`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `item-order` (
  `item_id` int(11) NOT NULL AUTO_INCREMENT,
  `first-name` varchar(100) NOT NULL,
  `last-name` varchar(100) NOT NULL,
  `email-id` varchar(100) NOT NULL,
  `position` varchar(45) NOT NULL,
  `department` varchar(100) NOT NULL,
  `item-name` varchar(500) NOT NULL,
  `item-detail` varchar(1000) DEFAULT NULL,
  `item-quentities` int(11) NOT NULL,
  `from-where` varchar(500) NOT NULL,
  `time-period` varchar(50) NOT NULL,
  `use-reason` varchar(100) NOT NULL,
  `place-order-date` datetime DEFAULT NULL,
  `order-status` varchar(45) DEFAULT NULL,
  `shipment-company` varchar(45) DEFAULT NULL,
  `tracking-number` varchar(45) DEFAULT NULL,
  `tracking-webside` varchar(1000) DEFAULT NULL,
  `expected-arriving-date` datetime DEFAULT NULL,
  `arrived-date` datetime DEFAULT NULL,
  `comment` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`item_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `item-order`
--

LOCK TABLES `item-order` WRITE;
/*!40000 ALTER TABLE `item-order` DISABLE KEYS */;
/*!40000 ALTER TABLE `item-order` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-02-21 16:50:59
