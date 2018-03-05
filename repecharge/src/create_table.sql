-- create table complete_data to store the training data
DROP TABLE IF EXISTS `complete_data`;
CREATE TABLE `complete_data` (
  `rank` int(10) DEFAULT NULL,
  `dt` varchar(8) DEFAULT NULL,
  `cookie` varchar(32) DEFAULT NULL,
  `ip` varchar(15) DEFAULT NULL,
  `mobile_idfa` varchar(32) DEFAULT NULL,
  `mobile_imei` varchar(32) DEFAULT NULL,
  `mobile_android_id` varchar(32) DEFAULT NULL,
  `mobile_openudid` varchar(32) DEFAULT NULL,
  `mobile_mac` varchar(32) DEFAULT NULL,
  `timestamps` int(11) DEFAULT NULL,
  `camp_id` varchar(10) DEFAULT NULL,
  `creativeid` varchar(32) DEFAULT NULL,
  `mobile_os` varchar(200) DEFAULT NULL,
  `mobile_type` varchar(2000) DEFAULT NULL,
  `app_key_key` varchar(32) DEFAULT NULL,
  `app_name_name` varchar(32) DEFAULT NULL,
  `placement_id` varchar(32) DEFAULT NULL,
  `user_agent` varchar(8000) DEFAULT NULL,
  `media_id` varchar(10) DEFAULT NULL,
  `os_type` varchar(100) DEFAULT NULL,
  `born_time` varchar(32) DEFAULT NULL,
  `flag` varchar(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- create table final_test to store the test data
DROP TABLE IF EXISTS `final_test`;
CREATE TABLE `final_test` (
  `rank` int(10) DEFAULT NULL,
  `dt` varchar(8) DEFAULT NULL,
  `cookie` varchar(32) DEFAULT NULL,
  `ip` varchar(15) DEFAULT NULL,
  `mobile_idfa` varchar(32) DEFAULT NULL,
  `mobile_imei` varchar(32) DEFAULT NULL,
  `mobile_android_id` varchar(32) DEFAULT NULL,
  `mobile_openudid` varchar(32) DEFAULT NULL,
  `mobile_mac` varchar(32) DEFAULT NULL,
  `timestamps` int(11) DEFAULT NULL,
  `camp_id` varchar(10) DEFAULT NULL,
  `creativeid` varchar(32) DEFAULT NULL,
  `mobile_os` varchar(200) DEFAULT NULL,
  `mobile_type` varchar(2000) DEFAULT NULL,
  `app_key_key` varchar(32) DEFAULT NULL,
  `app_name_name` varchar(32) DEFAULT NULL,
  `placement_id` varchar(32) DEFAULT NULL,
  `user_agent` varchar(8000) DEFAULT NULL,
  `media_id` varchar(10) DEFAULT NULL,
  `os_type` varchar(100) DEFAULT NULL,
  `born_time` varchar(32) DEFAULT NULL,
  `flag` varchar(1) DEFAULT NULL
  KEY `ip` (`ip`) USING HASH,
  KEY `dt` (`dt`) USING HASH
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- create table media to store the media data
DROP TABLE IF EXISTS `media`;
CREATE TABLE `media` (
  `mid` int(11) NOT NULL DEFAULT '0',
  `category` varchar(10) DEFAULT NULL,
  `firstType` varchar(10) DEFAULT NULL,
  `secondType` varchar(10) DEFAULT NULL,
  `tag` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`mid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;