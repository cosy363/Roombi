-- MySQL dump 10.13  Distrib 8.0.31, for macos12 (x86_64)
--
-- Host: database-1.cnxa3k5tfaa9.ap-northeast-2.rds.amazonaws.com    Database: furniture_DB
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
SET @MYSQLDUMP_TEMP_LOG_BIN = @@SESSION.SQL_LOG_BIN;
SET @@SESSION.SQL_LOG_BIN= 0;

--
-- GTID state at the beginning of the backup 
--

SET @@GLOBAL.GTID_PURGED=/*!80000 '+'*/ '';

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` varchar(45) NOT NULL,
  `user_number` varchar(45) NOT NULL,
  `encrypted_pwd` blob NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'fsef','123',_binary 'encrypted_password'),(2,'fsef','123',_binary 'encrypted_password'),(3,'fsef','123',_binary '$2a$10$asd5ibKkUMu4SQ1JGJNRd.vbGqGpvs.3N.31fO'),(4,'kimjinkwon','e50be91a-5d74-4976-8ea6-03bc656804ed',_binary '$2a$10$a.rJ64KKCxqrxVwxW5D/yeAesRiQSrmwbYcQ8k'),(5,'mkseg','26e5da66-8acb-4ec8-97b9-f8702cf580f8',_binary '$2a$10$o78VAvPDtayMbC9v9cjmhetwhdK.8BD2Q3n32H'),(6,'mksegseg','d8aa39a6-c44f-4de5-bbda-51f1010aea5d',_binary '$2a$10$zd8SLADslYl3JV0QbH.hHeT6/tCvPbLZ31NIx8'),(7,'testmyid','be311a44-f5d6-45a0-826d-bdb281514a82',_binary '$2a$10$JytD1T9FKu4RIBBHOQMu3uTkR7Li.kyFt/BIrs'),(8,'helloworld','4c314710-3168-4380-97e5-b521e3386d82',_binary '$2a$10$mliIHDa8.TMI6VnJ.M833OkC9kVuanhEiRncQ8'),(9,'helloworldweg','f144f8af-e797-4661-ae57-4d47305fa493',_binary '$2a$10$LojLQmNlVPG8Gz7gL5gwNe9sR.Q9ZHKHydWfh7'),(10,'helloworldweg','1412f8c2-0a9d-48b1-a2cc-82414d7bcd62',_binary '$2a$10$yi6Yv8qP5hz44nWwCIU5t.7l7fyf2GjOLTA6fN9Ypu0u8Y9FS/lAi'),(11,'iamdocker','11a90363-1fe2-42de-9c0b-87ad524d3fd7',_binary '$2a$10$w4o34nLsn2Yjxyw7UElIZeTwBYr9yA9gjWfF3s6U55Tj3U8WNn0hO'),(12,'iamdocke2r','ef37f086-94eb-4551-841d-d90580c58adc',_binary '$2a$10$8904lK.yEdV.EENy7SiPM.JDfuV3.4JnkWfXAOCjsWJ.2Mz4nabW.'),(13,'iamdocke2r','4b70b5b5-8e41-49f6-aef6-be60c308f948',_binary '$2a$10$W9xQSdJqotEkJFGy1w06FOri.YvYh1P701Ri2Uiuqe8YaJ/4S70Uq'),(14,'kimjinkwon','21215f8b-ad76-4f0b-9abe-aae7d25bcda9',_binary '$2a$10$HeWq2YzOGvPEI1d8vlsixuuDhHqOkFrLcGxA4b3UIVPHXbM4n1aKq'),(15,'kimjinkwon1','9ce50e35-f76a-4dfd-b923-0dc272680a01',_binary '$2a$10$EmZOMkCw1Y59U1yWNMM2j.0vzToQ26y4QPRpDZCXpGfK.8aMnlfOu'),(16,'imgroot','bf96864c-7edd-4a50-b90e-6a8f14f0bc85',_binary '$2a$10$MfLWoIX5Lq78Yr/qe6/nxu0vjZs5axkMfJNdjQwQH5OHjkNJ6pbka');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
SET @@SESSION.SQL_LOG_BIN = @MYSQLDUMP_TEMP_LOG_BIN;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-02-27 12:37:30
