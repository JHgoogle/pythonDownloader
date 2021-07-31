/*
 Navicat Premium Data Transfer

 Source Server         : windo124
 Source Server Type    : MySQL
 Source Server Version : 80023
 Source Host           : localhost:3306
 Source Schema         : django

 Target Server Type    : MySQL
 Target Server Version : 80023
 File Encoding         : 65001

 Date: 19/04/2021 15:46:38
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for pic_info
-- ----------------------------
DROP TABLE IF EXISTS `pic_info`;
CREATE TABLE `pic_info`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `pic_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `pic_size` double NULL DEFAULT NULL,
  `pic_md5` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 30 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of pic_info
-- ----------------------------
INSERT INTO `pic_info` VALUES (22, '可乐1', 0.03, '9aeff98e368f2c0c4552a012f28d85a3');
INSERT INTO `pic_info` VALUES (23, '可乐2', 0.85, '950b9a5e5f5b065aae569d99806ae23c');
INSERT INTO `pic_info` VALUES (24, '可乐3', 0.03, '00d343eb8cfc7efb81e2d7fefba70d5d');
INSERT INTO `pic_info` VALUES (25, '橘猫1', 2.22, 'f6bab0df4d35a170a5877cdcdc59010d');
INSERT INTO `pic_info` VALUES (26, '橘猫2', 0.09, '94b835703e4df155aa0db4e77ebcfb81');
INSERT INTO `pic_info` VALUES (27, '橘猫3', 0.09, '506f0c7f34457d6123045ad48b8d58c3');
INSERT INTO `pic_info` VALUES (28, '咖啡1', 0.1, '0fa3748daf179d61abc9446290377b62');
INSERT INTO `pic_info` VALUES (29, '咖啡2', 0.07, 'd38c1bdeb554a5e258132f4b71d3dd09');
INSERT INTO `pic_info` VALUES (30, '咖啡3', 0.05, '4ce74d886754ec670ff81148611a4cf3');

SET FOREIGN_KEY_CHECKS = 1;
