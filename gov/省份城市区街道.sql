
CREATE TABLE `province` (
  `province_name` varchar(255) DEFAULT NULL COMMENT '省份名',
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=gbk;

CREATE TABLE `city` (
  `city_name` varchar(255) DEFAULT NULL COMMENT '城市名',
	`province_id` int(11) NOT NULL COMMENT '省id',
	`city_code` varchar(255) DEFAULT NULL COMMENT '城市code',
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=gbk;

CREATE TABLE `county` (
  `county_name` varchar(255) DEFAULT NULL COMMENT '区名称',
  `city_id` int(255) DEFAULT NULL COMMENT '城市id',
  `county_code` varchar(255) DEFAULT NULL COMMENT '区编码',
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=gbk;


# town_name, county_id, town_code
CREATE TABLE `town` (
  `town_name` varchar(255) DEFAULT NULL COMMENT '乡镇街道',
  `county_id` int(255) DEFAULT NULL COMMENT '区id',
  `town_code` varchar(255) DEFAULT NULL COMMENT '乡镇街道编码',
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=gbk;