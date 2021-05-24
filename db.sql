/*
SQLyog Community v13.1.2 (64 bit)
MySQL - 5.5.29 : Database - speechtotext
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`speechtotext` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `speechtotext`;

/*Table structure for table `combined` */

DROP TABLE IF EXISTS `combined`;

CREATE TABLE `combined` (
  `meeting` varchar(100) DEFAULT NULL,
  `chats` text
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `combined` */

LOCK TABLES `combined` WRITE;

insert  into `combined`(`meeting`,`chats`) values 
('Client Meeting',' The book is narrated by Hari, with some small passages by his friends Ryan and Alok, as well as a letter by Haris girlfriend Neha Cherian. It deals with the lives of the 3 friends, whose elation on making it to one of the best engineering colleges in India is quickly deflated by the rigor and monotony of the academic work. Most of the book deals with the numerous attempts by the trio to cope with and/or beat the system as well as Haris fling with Neha who just happens to be the daughter of Prof. Cherian, the domineering head of the Mechanical Engineering Department of their college.. It takes some dark turns every now and then, especially when it comes to the families of the protagonists. Most of the action, however, takes place inside the campus as the boys, led by the ever creative Ryan, frequently lamenting how the internationally lauded IIT system has stifled their creativity by forcing them to value grades more than anything else. Uninspiring teaching and numerous assignments add to their woes, though the boys do find a sympathizer in Prof. Veera, the new fluid mechanics professor..'),
('Client Meeting',' The book is narrated by Hari, with some small passages by his friends Ryan and Alok, as well as a letter by Haris girlfriend Neha Cherian. It deals with the lives of the 3 friends, whose elation on making it to one of the best engineering colleges in India is quickly deflated by the rigor and monotony of the academic work. Most of the book deals with the numerous attempts by the trio to cope with and/or beat the system as well as Haris fling with Neha who just happens to be the daughter of Prof. Cherian, the domineering head of the Mechanical Engineering Department of their college.. It takes some dark turns every now and then, especially when it comes to the families of the protagonists. Most of the action, however, takes place inside the campus as the boys, led by the ever creative Ryan, frequently lamenting how the internationally lauded IIT system has stifled their creativity by forcing them to value grades more than anything else. Uninspiring teaching and numerous assignments add to their woes, though the boys do find a sympathizer in Prof. Veera, the new fluid mechanics professor..');

UNLOCK TABLES;

/*Table structure for table `meetings` */

DROP TABLE IF EXISTS `meetings`;

CREATE TABLE `meetings` (
  `meetingname` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `meetings` */

LOCK TABLES `meetings` WRITE;

insert  into `meetings`(`meetingname`) values 
('Client Meeting'),
('Manager Meeting');

UNLOCK TABLES;

/*Table structure for table `speechdata` */

DROP TABLE IF EXISTS `speechdata`;

CREATE TABLE `speechdata` (
  `name` varchar(100) DEFAULT NULL,
  `voice` text,
  `meeting` varchar(100) DEFAULT NULL,
  `time` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `speechdata` */

LOCK TABLES `speechdata` WRITE;

insert  into `speechdata`(`name`,`voice`,`meeting`,`time`) values 
('Krishna','The book is narrated by Hari, with some small passages by his friends Ryan and Alok, as well as a letter by Haris girlfriend Neha Cherian. It deals with the lives of the 3 friends, whose elation on making it to one of the best engineering colleges in India is quickly deflated by the rigor and monotony of the academic work. Most of the book deals with the numerous attempts by the trio to cope with and/or beat the system as well as Haris fling with Neha who just happens to be the daughter of Prof. Cherian, the domineering head of the Mechanical Engineering Department of their college.','Client Meeting','29/02/2020 17:37:40'),
('Shantan','It takes some dark turns every now and then, especially when it comes to the families of the protagonists. Most of the action, however, takes place inside the campus as the boys, led by the ever creative Ryan, frequently lamenting how the internationally lauded IIT system has stifled their creativity by forcing them to value grades more than anything else. Uninspiring teaching and numerous assignments add to their woes, though the boys do find a sympathizer in Prof. Veera, the new fluid mechanics professor.','Client Meeting','29/02/2020 17:37:40');

UNLOCK TABLES;

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `id` varchar(100) NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `mob` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `user` */

LOCK TABLES `user` WRITE;

insert  into `user`(`id`,`name`,`email`,`password`,`mob`) values 
('IVfY9cnUNf','Krishna','hk.1000projects@gmail.com','1234','7978418005');

UNLOCK TABLES;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
