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

 Date: 25/05/2021 12:04:45
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for download_info
-- ----------------------------
DROP TABLE IF EXISTS `download_info`;
CREATE TABLE `download_info`  (
  `id` int NOT NULL,
  `download_url` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `download_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `download_size` double NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
