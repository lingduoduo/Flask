CREATE DATABASE `movie_cat` DEFAULT CHARACTER SET = `utf8mb4`;


CREATE TABLE `user` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT 'id',
  `nickname` varchar(30) NOT NULL DEFAULT '' COMMENT 'nick name',
  `login_name` varchar(20) NOT NULL DEFAULT '' COMMENT 'login name',
  `login_pwd` varchar(32) NOT NULL DEFAULT '' COMMENT 'login password',
  `login_salt` varchar(32) NOT NULL DEFAULT '' COMMENT 'login salt',
  `status` tinyint(3) NOT NULL DEFAULT '1' COMMENT 'status 0：invalid 1:valid',
  `updated_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'last update time',
  `created_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'create time',
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_login_name` (`login_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='User Database';





CREATE TABLE `movie` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL DEFAULT '' COMMENT 'name',
  `classify` varchar(100) NOT NULL DEFAULT '' COMMENT 'classify',
  `actor` varchar(500) NOT NULL DEFAULT '' COMMENT 'actor',
  `cover_pic` varchar(300) NOT NULL DEFAULT '' COMMENT 'cover_pic',
  `pics` varchar(1000) NOT NULL DEFAULT '' COMMENT 'pic_json',
  `url` varchar(300) NOT NULL DEFAULT '' COMMENT 'url',
  `desc` text NOT NULL COMMENT 'description',
  `magnet_url` varchar(5000) NOT NULL DEFAULT '' COMMENT 'magnet_url',
  `hash` varchar(32) NOT NULL DEFAULT '' COMMENT 'hash',
  `pub_date` datetime NOT NULL COMMENT 'published date',
  `source` varchar(20) NOT NULL DEFAULT '' COMMENT 'source',
  `view_counter` int(11) NOT NULL DEFAULT '0' COMMENT 'view content',
  `updated_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'last update time',
  `created_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'create time',
  PRIMARY KEY (`id`),
  UNIQUE KEY `idx_hash` (`hash`),
  KEY `idx_pu_date` (`pub_date`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4 COMMENT='Movie Database';
