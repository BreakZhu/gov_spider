/*
 Navicat Premium Data Transfer

 Source Server         : localhost
 Source Server Type    : MySQL
 Source Server Version : 50724
 Source Host           : localhost:3306
 Source Schema         : code_spider

 Target Server Type    : MySQL
 Target Server Version : 50724
 File Encoding         : 65001

 Date: 21/12/2018 10:25:50
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for province
-- ----------------------------
DROP TABLE IF EXISTS `province`;
CREATE TABLE `province`  (
  `province_name` varchar(255) CHARACTER SET gbk COLLATE gbk_chinese_ci NULL DEFAULT NULL COMMENT '省份名',
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 32 CHARACTER SET = gbk COLLATE = gbk_chinese_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of province
-- ----------------------------
INSERT INTO `province` VALUES ('北京市', 1);
INSERT INTO `province` VALUES ('天津市', 2);
INSERT INTO `province` VALUES ('河北省', 3);
INSERT INTO `province` VALUES ('山西省', 4);
INSERT INTO `province` VALUES ('内蒙古自治区', 5);
INSERT INTO `province` VALUES ('辽宁省', 6);
INSERT INTO `province` VALUES ('吉林省', 7);
INSERT INTO `province` VALUES ('黑龙江省', 8);
INSERT INTO `province` VALUES ('上海市', 9);
INSERT INTO `province` VALUES ('江苏省', 10);
INSERT INTO `province` VALUES ('浙江省', 11);
INSERT INTO `province` VALUES ('安徽省', 12);
INSERT INTO `province` VALUES ('福建省', 13);
INSERT INTO `province` VALUES ('江西省', 14);
INSERT INTO `province` VALUES ('山东省', 15);
INSERT INTO `province` VALUES ('河南省', 16);
INSERT INTO `province` VALUES ('湖北省', 17);
INSERT INTO `province` VALUES ('湖南省', 18);
INSERT INTO `province` VALUES ('广东省', 19);
INSERT INTO `province` VALUES ('广西壮族自治区', 20);
INSERT INTO `province` VALUES ('海南省', 21);
INSERT INTO `province` VALUES ('重庆市', 22);
INSERT INTO `province` VALUES ('四川省', 23);
INSERT INTO `province` VALUES ('贵州省', 24);
INSERT INTO `province` VALUES ('云南省', 25);
INSERT INTO `province` VALUES ('西藏自治区', 26);
INSERT INTO `province` VALUES ('陕西省', 27);
INSERT INTO `province` VALUES ('甘肃省', 28);
INSERT INTO `province` VALUES ('青海省', 29);
INSERT INTO `province` VALUES ('宁夏回族自治区', 30);
INSERT INTO `province` VALUES ('新疆维吾尔自治区', 31);

SET FOREIGN_KEY_CHECKS = 1;
