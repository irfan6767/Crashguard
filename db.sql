/*
SQLyog Community v13.0.1 (64 bit)
MySQL - 8.0.35 : Database - projectx
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`projectx` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `projectx`;

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_group` */

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_group_permissions` */

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=65 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_permission` */

insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values 
(1,'Can add log entry',1,'add_logentry'),
(2,'Can change log entry',1,'change_logentry'),
(3,'Can delete log entry',1,'delete_logentry'),
(4,'Can view log entry',1,'view_logentry'),
(5,'Can add permission',2,'add_permission'),
(6,'Can change permission',2,'change_permission'),
(7,'Can delete permission',2,'delete_permission'),
(8,'Can view permission',2,'view_permission'),
(9,'Can add group',3,'add_group'),
(10,'Can change group',3,'change_group'),
(11,'Can delete group',3,'delete_group'),
(12,'Can view group',3,'view_group'),
(13,'Can add user',4,'add_user'),
(14,'Can change user',4,'change_user'),
(15,'Can delete user',4,'delete_user'),
(16,'Can view user',4,'view_user'),
(17,'Can add content type',5,'add_contenttype'),
(18,'Can change content type',5,'change_contenttype'),
(19,'Can delete content type',5,'delete_contenttype'),
(20,'Can view content type',5,'view_contenttype'),
(21,'Can add session',6,'add_session'),
(22,'Can change session',6,'change_session'),
(23,'Can delete session',6,'delete_session'),
(24,'Can view session',6,'view_session'),
(25,'Can add accidentreport_table',7,'add_accidentreport_table'),
(26,'Can change accidentreport_table',7,'change_accidentreport_table'),
(27,'Can delete accidentreport_table',7,'delete_accidentreport_table'),
(28,'Can view accidentreport_table',7,'view_accidentreport_table'),
(29,'Can add ambulance_table',8,'add_ambulance_table'),
(30,'Can change ambulance_table',8,'change_ambulance_table'),
(31,'Can delete ambulance_table',8,'delete_ambulance_table'),
(32,'Can view ambulance_table',8,'view_ambulance_table'),
(33,'Can add hospital_table',9,'add_hospital_table'),
(34,'Can change hospital_table',9,'change_hospital_table'),
(35,'Can delete hospital_table',9,'delete_hospital_table'),
(36,'Can view hospital_table',9,'view_hospital_table'),
(37,'Can add login_table',10,'add_login_table'),
(38,'Can change login_table',10,'change_login_table'),
(39,'Can delete login_table',10,'delete_login_table'),
(40,'Can view login_table',10,'view_login_table'),
(41,'Can add trafficpoolice_table',11,'add_trafficpoolice_table'),
(42,'Can change trafficpoolice_table',11,'change_trafficpoolice_table'),
(43,'Can delete trafficpoolice_table',11,'delete_trafficpoolice_table'),
(44,'Can view trafficpoolice_table',11,'view_trafficpoolice_table'),
(45,'Can add location_table',12,'add_location_table'),
(46,'Can change location_table',12,'change_location_table'),
(47,'Can delete location_table',12,'delete_location_table'),
(48,'Can view location_table',12,'view_location_table'),
(49,'Can add emargency_table',13,'add_emargency_table'),
(50,'Can change emargency_table',13,'change_emargency_table'),
(51,'Can delete emargency_table',13,'delete_emargency_table'),
(52,'Can view emargency_table',13,'view_emargency_table'),
(53,'Can add driver_table',14,'add_driver_table'),
(54,'Can change driver_table',14,'change_driver_table'),
(55,'Can delete driver_table',14,'delete_driver_table'),
(56,'Can view driver_table',14,'view_driver_table'),
(57,'Can add complaint_table',15,'add_complaint_table'),
(58,'Can change complaint_table',15,'change_complaint_table'),
(59,'Can delete complaint_table',15,'delete_complaint_table'),
(60,'Can view complaint_table',15,'view_complaint_table'),
(61,'Can add emergency_number',16,'add_emergency_number'),
(62,'Can change emergency_number',16,'change_emergency_number'),
(63,'Can delete emergency_number',16,'delete_emergency_number'),
(64,'Can view emergency_number',16,'view_emergency_number');

/*Table structure for table `auth_user` */

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user` */

insert  into `auth_user`(`id`,`password`,`last_login`,`is_superuser`,`username`,`first_name`,`last_name`,`email`,`is_staff`,`is_active`,`date_joined`) values 
(1,'pbkdf2_sha256$260000$lkH2samatqykpHRCn799Ze$7BIEY6z+D3mm46ZraPQpxnFEuC+DQom/IkJcOj5H9K0=','2024-01-21 07:10:03.338303',1,'admin','','','admin@gmail.com',1,1,'2023-12-19 09:52:56.852969');

/*Table structure for table `auth_user_groups` */

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user_groups` */

/*Table structure for table `auth_user_user_permissions` */

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user_user_permissions` */

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_admin_log` */

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`app_label`,`model`) values 
(1,'admin','logentry'),
(3,'auth','group'),
(2,'auth','permission'),
(4,'auth','user'),
(5,'contenttypes','contenttype'),
(7,'sapp','accidentreport_table'),
(8,'sapp','ambulance_table'),
(15,'sapp','complaint_table'),
(14,'sapp','driver_table'),
(13,'sapp','emargency_table'),
(16,'sapp','emergency_number'),
(9,'sapp','hospital_table'),
(12,'sapp','location_table'),
(10,'sapp','login_table'),
(11,'sapp','trafficpoolice_table'),
(6,'sessions','session');

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_migrations` */

insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values 
(1,'contenttypes','0001_initial','2023-12-14 09:14:37.555988'),
(2,'auth','0001_initial','2023-12-14 09:14:38.815458'),
(3,'admin','0001_initial','2023-12-14 09:14:39.135810'),
(4,'admin','0002_logentry_remove_auto_add','2023-12-14 09:14:39.144357'),
(5,'admin','0003_logentry_add_action_flag_choices','2023-12-14 09:14:39.157787'),
(6,'contenttypes','0002_remove_content_type_name','2023-12-14 09:14:39.326494'),
(7,'auth','0002_alter_permission_name_max_length','2023-12-14 09:14:39.447069'),
(8,'auth','0003_alter_user_email_max_length','2023-12-14 09:14:39.485121'),
(9,'auth','0004_alter_user_username_opts','2023-12-14 09:14:39.495747'),
(10,'auth','0005_alter_user_last_login_null','2023-12-14 09:14:39.648443'),
(11,'auth','0006_require_contenttypes_0002','2023-12-14 09:14:39.654477'),
(12,'auth','0007_alter_validators_add_error_messages','2023-12-14 09:14:39.660859'),
(13,'auth','0008_alter_user_username_max_length','2023-12-14 09:14:39.777648'),
(14,'auth','0009_alter_user_last_name_max_length','2023-12-14 09:14:39.932079'),
(15,'auth','0010_alter_group_name_max_length','2023-12-14 09:14:39.968328'),
(16,'auth','0011_update_proxy_permissions','2023-12-14 09:14:39.988232'),
(17,'auth','0012_alter_user_first_name_max_length','2023-12-14 09:14:40.161632'),
(18,'sapp','0001_initial','2023-12-14 09:14:41.484137'),
(19,'sessions','0001_initial','2023-12-14 09:14:41.545974'),
(20,'sapp','0002_alter_trafficpoolice_table_phone','2023-12-26 06:37:01.135751'),
(21,'sapp','0003_complaint_table','2023-12-26 09:16:12.696099'),
(22,'sapp','0004_emergency_number','2024-01-02 07:11:26.434309'),
(23,'sapp','0005_trafficpoolice_table_station','2024-01-21 05:03:16.712031');

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_session` */

insert  into `django_session`(`session_key`,`session_data`,`expire_date`) values 
('16iqgooxf9qsjfa3pcdjc0qdrpvlvbf0','.eJxVjEEOwiAQRe_C2hBABgaX7nsGMgMoVUOT0q6Md7dNutDtf--_t4i0LjWuvcxxzOIitDj9bkzpWdoO8oPafZJpass8stwVedAuhymX1_Vw_wKVet3e1jiPVrFyXLAA-azPyJq1TyFTsAUTBFKQDSqTMBAB3La8ATAuaBKfL9QLN58:1rJUQg:JkkFTSBfs916fVZvlF2DbrJ-pMxXPbKhxOG9nRreF14','2024-01-13 08:10:46.305431'),
('7wduwkmhhyfeyekr64okj98bog27d78i','.eJxVjEEOwiAQRe_C2hBABgaX7nsGMgMoVUOT0q6Md7dNutDtf--_t4i0LjWuvcxxzOIitDj9bkzpWdoO8oPafZJpass8stwVedAuhymX1_Vw_wKVet3e1jiPVrFyXLAA-azPyJq1TyFTsAUTBFKQDSqTMBAB3La8ATAuaBKfL9QLN58:1rFx2b:3c-L8DFQCwU89PwEnHNG6d3tas5SI9FcspHVYaLviyQ','2024-01-03 13:55:17.100559'),
('g9g4jcowyllq39ahyfd6phla08h65w7n','.eJxVjEEOwiAQRe_C2hBABgaX7nsGMgMoVUOT0q6Md7dNutDtf--_t4i0LjWuvcxxzOIitDj9bkzpWdoO8oPafZJpass8stwVedAuhymX1_Vw_wKVet3e1jiPVrFyXLAA-azPyJq1TyFTsAUTBFKQDSqTMBAB3La8ATAuaBKfL9QLN58:1rRRxz:nxJz5nIaBtX13S9bnSyN1kzAvaCbpy_s4hneNtCOTKQ','2024-02-04 07:10:03.351498'),
('gexsxfu7zzs4adh73lbzsct620a31x6j','eyJhbWlkIjoxfQ:1rFW66:YgigETas8uWeuxwEc8oAxBXW_uPNXwMs4DlEyH-JFGU','2024-01-02 09:09:06.639885'),
('iii3pxkro3g9txm018hzuy2pgft5ad88','.eJxVjEEOwiAQRe_C2hBABgaX7nsGMgMoVUOT0q6Md7dNutDtf--_t4i0LjWuvcxxzOIitDj9bkzpWdoO8oPafZJpass8stwVedAuhymX1_Vw_wKVet3e1jiPVrFyXLAA-azPyJq1TyFTsAUTBFKQDSqTMBAB3La8ATAuaBKfL9QLN58:1rFXS3:2fyPymYHqSt8WwuQRzP7PiJ5I8ib3pZtBY_zMYMjbQg','2024-01-02 10:35:51.980060'),
('jpd50l53gsxhzq9t6fkwehx5a12f1yxp','.eJxVjsEOwiAQRP-FsyGAbLt49N5vIMtCLWpoUtqT8d-lpge9zpt5mZfwtK2T32pafI7iIrQ4_WaB-JHKDuKdym2WPJd1yUHuFXnQKoc5puf16P4JJqpTW1vT9WhVUF1ImID6qM8YdNA9u0jOJmRwpCAaVIbREQGMTW8ATOc0Nem60Jj5-1K_P_9LPB8:1rFXRX:Yaq7WLGxRRljXVI0TpkKqil6EtKdHOoKmOXM3Dl_ByA','2024-01-02 10:35:19.615583'),
('m21fn00bd95h5ipngkwgvb6v3trquwde','.eJxVjEEOwiAQRe_C2hBABgaX7nsGMgMoVUOT0q6Md7dNutDtf--_t4i0LjWuvcxxzOIitDj9bkzpWdoO8oPafZJpass8stwVedAuhymX1_Vw_wKVet3e1jiPVrFyXLAA-azPyJq1TyFTsAUTBFKQDSqTMBAB3La8ATAuaBKfL9QLN58:1rFwxl:5XjiXEd8n9Hy6L5pu6qtEPj5dhAG9AdggttqfNJM-uk','2024-01-03 13:50:17.481362'),
('o6gn00tgj2y3h6da5yshpms6tp4wh3d7','.eJxVjDsOwyAQBe9CHSHAXj4p0_sMaGFJcGKBZOwqyt1jJDduZ-a9L1tmYnc53JjHfct-b2n1HTHJLixg_KTSBb2xvCqPtWzrHHhP-Gkbnyql5XG2l4OMLR_rUWljRxGEDskmQENysEEGaaIjdGOyERwKIGWFitYhAjyPewWgtJPIfn9oKznm:1rLR34:vwQ-rFCPpvJ5qMCj_jJ42OHGNTexq5PRBZHCA7cNqA8','2024-01-18 16:58:26.516052'),
('rxdqc8uzyof9fxpm5y2jsjd3wy449g7z','.eJxVjDsOwyAQBe9CHSHAXj4p0_sMaGFJcGKBZOwqyt1jJDduZ-a9L1tmYnc53JjHfct-b2n1HTHJLixg_KTSBb2xvCqPtWzrHHhP-Gkbnyql5XG2l4OMLR_rUWljRxGEDskmQENysEEGaaIjdGOyERwKIGWFitYhAjyPewWgtJPIfn9oKznm:1rLRe3:kKhKGToQkETHV9cE6jNuh2qVH4I9dncLR_L5L_5rayA','2024-01-18 17:36:39.389646'),
('swh4xcf4a4a3kxagafjko63qryhowl0d','.eJxVjMsOwiAUBf-FtSGAXB4u3fcbyOVRQQ0klK6M_25ruul2Zs75kNFxLsGVSG78QhyuI7t1Sf1PCCcn5jG8Ut1FfGJ9NBpaHb14uif0sAudWkzv-9GeDjIueVtLobSRzDPlk0mAOvKr8dxzHWxEK5MJYJFBFIaJYCwiwLzdCwChLEfy_QH8zzwf:1rFwdi:PST66BYxccNUo-Ag5Xw6SaWN1sUgpI7o-Nm-LjmgB9A','2024-01-03 13:29:34.439638'),
('vevkslrwsgsfs9j1kau2q0pmm4xnhm3k','.eJxVjrkOwjAQRP_FNbK8jtcHJRUNEhL00foAB6JYylEh_h0HpUk7b-ZpPqzvIjtCc2AtLXNulymN7RoxYLvMU3inYQXxRcOz8FCGeew8Xyt8oxO_lJj609bdCTJNua6V1MYq4YX2ySYkE6GxHjyY4CI5lWxARwKjtEIG64gQH1UvEaV2QFV6vl3v_4_w_QExeT0s:1rR4MO:V2c6jJw5YeWMxVnKFug-WDX7Ld4WfWYLgN08zw2_bL8','2024-02-03 05:57:40.686437'),
('xfbj6pz6trbusjn1ua9h1j93fu8m79yk','.eJxVjEEOwiAQRe_C2hBABgaX7nsGMgMoVUOT0q6Md7dNutDtf--_t4i0LjWuvcxxzOIitDj9bkzpWdoO8oPafZJpass8stwVedAuhymX1_Vw_wKVet3e1jiPVrFyXLAA-azPyJq1TyFTsAUTBFKQDSqTMBAB3La8ATAuaBKfL9QLN58:1rFwsT:HT3UTsxlqav6XZc3w_K7NjWsBMiWGeWLibEwiX2mjqo','2024-01-03 13:44:49.863246');

/*Table structure for table `sapp_accidentreport_table` */

DROP TABLE IF EXISTS `sapp_accidentreport_table`;

CREATE TABLE `sapp_accidentreport_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `latitude` double NOT NULL,
  `longitude` double NOT NULL,
  `date` date NOT NULL,
  `time` time(6) NOT NULL,
  `status` varchar(100) NOT NULL,
  `type` varchar(100) NOT NULL,
  `DRIVER_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `sapp_accidentreport__DRIVER_id_528bbd06_fk_sapp_driv` (`DRIVER_id`),
  CONSTRAINT `sapp_accidentreport__DRIVER_id_528bbd06_fk_sapp_driv` FOREIGN KEY (`DRIVER_id`) REFERENCES `sapp_driver_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `sapp_accidentreport_table` */

insert  into `sapp_accidentreport_table`(`id`,`latitude`,`longitude`,`date`,`time`,`status`,`type`,`DRIVER_id`) values 
(2,0,77.5946,'2023-11-15','12:54:00.000000','pending','76',1);

/*Table structure for table `sapp_ambulance_table` */

DROP TABLE IF EXISTS `sapp_ambulance_table`;

CREATE TABLE `sapp_ambulance_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `vehicle_no` varchar(100) NOT NULL,
  `phone` bigint NOT NULL,
  `photo` varchar(100) NOT NULL,
  `proof` varchar(100) NOT NULL,
  `LOGIN_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `sapp_ambulance_table_LOGIN_id_2e132944_fk_sapp_login_table_id` (`LOGIN_id`),
  CONSTRAINT `sapp_ambulance_table_LOGIN_id_2e132944_fk_sapp_login_table_id` FOREIGN KEY (`LOGIN_id`) REFERENCES `sapp_login_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `sapp_ambulance_table` */

insert  into `sapp_ambulance_table`(`id`,`name`,`vehicle_no`,`phone`,`photo`,`proof`,`LOGIN_id`) values 
(2,'vvv','kl-55-k-7787',9327737388,'download_sQPLLEK (1).jpg','pexels-pixabay-210182.jpg',19);

/*Table structure for table `sapp_complaint_table` */

DROP TABLE IF EXISTS `sapp_complaint_table`;

CREATE TABLE `sapp_complaint_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `complaint` varchar(100) NOT NULL,
  `date` date NOT NULL,
  `reply` varchar(100) NOT NULL,
  `DRIVER_id` bigint NOT NULL,
  `TRAFFICPOLICE_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `sapp_complaint_table_DRIVER_id_54caf270_fk_sapp_driver_table_id` (`DRIVER_id`),
  KEY `sapp_complaint_table_TRAFFICPOLICE_id_ec98a2ac_fk_sapp_traf` (`TRAFFICPOLICE_id`),
  CONSTRAINT `sapp_complaint_table_DRIVER_id_54caf270_fk_sapp_driver_table_id` FOREIGN KEY (`DRIVER_id`) REFERENCES `sapp_driver_table` (`id`),
  CONSTRAINT `sapp_complaint_table_TRAFFICPOLICE_id_ec98a2ac_fk_sapp_traf` FOREIGN KEY (`TRAFFICPOLICE_id`) REFERENCES `sapp_trafficpoolice_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `sapp_complaint_table` */

insert  into `sapp_complaint_table`(`id`,`complaint`,`date`,`reply`,`DRIVER_id`,`TRAFFICPOLICE_id`) values 
(2,'fghj','2024-01-21','ok',1,7),
(3,'fff','2024-01-31','pending',1,7),
(4,'hhhh','2024-01-31','pending',1,7);

/*Table structure for table `sapp_driver_table` */

DROP TABLE IF EXISTS `sapp_driver_table`;

CREATE TABLE `sapp_driver_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `place` varchar(100) NOT NULL,
  `address` varchar(100) NOT NULL,
  `pin` int NOT NULL,
  `phone` bigint NOT NULL,
  `photo` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `regno` int NOT NULL,
  `LOGIN_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `sapp_driver_table_LOGIN_id_80dc3f4f_fk_sapp_login_table_id` (`LOGIN_id`),
  CONSTRAINT `sapp_driver_table_LOGIN_id_80dc3f4f_fk_sapp_login_table_id` FOREIGN KEY (`LOGIN_id`) REFERENCES `sapp_login_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `sapp_driver_table` */

insert  into `sapp_driver_table`(`id`,`name`,`place`,`address`,`pin`,`phone`,`photo`,`email`,`regno`,`LOGIN_id`) values 
(1,'nihal','vly','hjiu',567,4567,'dfg','sdfgh',34,4);

/*Table structure for table `sapp_emargency_table` */

DROP TABLE IF EXISTS `sapp_emargency_table`;

CREATE TABLE `sapp_emargency_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `status` varchar(100) NOT NULL,
  `ACCIDENTREPORT_id` bigint NOT NULL,
  `AMBULANCE_id` bigint NOT NULL,
  `HOSPITAL_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `sapp_emargency_table_ACCIDENTREPORT_id_2869e692_fk_sapp_acci` (`ACCIDENTREPORT_id`),
  KEY `sapp_emargency_table_AMBULANCE_id_a66b9453_fk_sapp_ambu` (`AMBULANCE_id`),
  KEY `sapp_emargency_table_HOSPITAL_id_12934348_fk_sapp_hosp` (`HOSPITAL_id`),
  CONSTRAINT `sapp_emargency_table_ACCIDENTREPORT_id_2869e692_fk_sapp_acci` FOREIGN KEY (`ACCIDENTREPORT_id`) REFERENCES `sapp_accidentreport_table` (`id`),
  CONSTRAINT `sapp_emargency_table_AMBULANCE_id_a66b9453_fk_sapp_ambu` FOREIGN KEY (`AMBULANCE_id`) REFERENCES `sapp_ambulance_table` (`id`),
  CONSTRAINT `sapp_emargency_table_HOSPITAL_id_12934348_fk_sapp_hosp` FOREIGN KEY (`HOSPITAL_id`) REFERENCES `sapp_hospital_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `sapp_emargency_table` */

/*Table structure for table `sapp_emergency_number` */

DROP TABLE IF EXISTS `sapp_emergency_number`;

CREATE TABLE `sapp_emergency_number` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `number` bigint NOT NULL,
  `DRIVER_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `sapp_emergency_number_DRIVER_id_86edfc66_fk_sapp_driver_table_id` (`DRIVER_id`),
  CONSTRAINT `sapp_emergency_number_DRIVER_id_86edfc66_fk_sapp_driver_table_id` FOREIGN KEY (`DRIVER_id`) REFERENCES `sapp_driver_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `sapp_emergency_number` */

insert  into `sapp_emergency_number`(`id`,`number`,`DRIVER_id`) values 
(1,8753224689,1),
(2,87888,1);

/*Table structure for table `sapp_hospital_table` */

DROP TABLE IF EXISTS `sapp_hospital_table`;

CREATE TABLE `sapp_hospital_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `details` varchar(1000) NOT NULL,
  `phone` bigint NOT NULL,
  `email` varchar(100) NOT NULL,
  `latitude` double NOT NULL,
  `longitude` double NOT NULL,
  `image` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `sapp_hospital_table` */

insert  into `sapp_hospital_table`(`id`,`name`,`details`,`phone`,`email`,`latitude`,`longitude`,`image`) values 
(1,'mims','pmna',987654,'sdfghj',234567,2345678,'vlcsnap-2022-05-31-13h48m06s745.png'),
(3,'nadakkavil hsptl','valanchery',9327737388,'nsajdn@sdid.com',56.56,345.45,'download (2)_2biPy5U.jpg');

/*Table structure for table `sapp_location_table` */

DROP TABLE IF EXISTS `sapp_location_table`;

CREATE TABLE `sapp_location_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `latitude` double NOT NULL,
  `longitude` double NOT NULL,
  `LOGIN_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `sapp_location_table_LOGIN_id_5d6adf80_fk_sapp_login_table_id` (`LOGIN_id`),
  CONSTRAINT `sapp_location_table_LOGIN_id_5d6adf80_fk_sapp_login_table_id` FOREIGN KEY (`LOGIN_id`) REFERENCES `sapp_login_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `sapp_location_table` */

insert  into `sapp_location_table`(`id`,`latitude`,`longitude`,`LOGIN_id`) values 
(1,11.2577976,75.7845425,4);

/*Table structure for table `sapp_login_table` */

DROP TABLE IF EXISTS `sapp_login_table`;

CREATE TABLE `sapp_login_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `type` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `sapp_login_table` */

insert  into `sapp_login_table`(`id`,`username`,`password`,`type`) values 
(1,'admin','admin123','admin'),
(3,'abru','abru','tp'),
(4,'nihal','nihal@123','driver'),
(13,'nhl','Nhl12333','tp'),
(14,'abrar','Abrar123','tp'),
(15,'asdf','#Aaaa4444','tp'),
(16,'nhl','Nhl12345','tp'),
(17,'nhl','Nhl12345','tp'),
(18,'nhl','Nhl12345','tp'),
(19,'hgfhf','dfdfrsDf234','tp');

/*Table structure for table `sapp_trafficpoolice_table` */

DROP TABLE IF EXISTS `sapp_trafficpoolice_table`;

CREATE TABLE `sapp_trafficpoolice_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `place` varchar(100) NOT NULL,
  `address` varchar(100) NOT NULL,
  `pin` int NOT NULL,
  `phone` bigint NOT NULL,
  `email` varchar(100) NOT NULL,
  `photo` varchar(100) NOT NULL,
  `designation` varchar(100) NOT NULL,
  `LOGIN_id` bigint NOT NULL,
  `station` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `sapp_trafficpoolice__LOGIN_id_f6deb537_fk_sapp_logi` (`LOGIN_id`),
  CONSTRAINT `sapp_trafficpoolice__LOGIN_id_f6deb537_fk_sapp_logi` FOREIGN KEY (`LOGIN_id`) REFERENCES `sapp_login_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `sapp_trafficpoolice_table` */

insert  into `sapp_trafficpoolice_table`(`id`,`name`,`place`,`address`,`pin`,`phone`,`email`,`photo`,`designation`,`LOGIN_id`,`station`) values 
(7,'jsdfhu','valanchery','valanchery',234354,7465346357,'nduhui@gkls.com','pexels-pixabay-315934.jpg','si',18,'oooo');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
