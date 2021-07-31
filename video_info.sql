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

 Date: 19/04/2021 15:46:53
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for video_info
-- ----------------------------
DROP TABLE IF EXISTS `video_info`;
CREATE TABLE `video_info`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `video_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `video_size` double NULL DEFAULT NULL,
  `video_url` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `video_author` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 4 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of video_info
-- ----------------------------
INSERT INTO `video_info` VALUES (1, '【可乐鸡翅】这真的是给手残党的新手教程。。。', 21.2, 'www.bilibili.com/video/BV1at411874o', '马壮实Hera');
INSERT INTO `video_info` VALUES (2, '【可乐鸡翅】这真的是给手残党的新手教程。。。', 21.2, 'www.bilibili.com/video/BV1at411874o', '马壮实Hera');
INSERT INTO `video_info` VALUES (3, '【可乐鸡翅】这真的是给手残党的新手教程。。。', 21.2, 'www.bilibili.com/video/BV1at411874o', '马壮实Hera');
INSERT INTO `video_info` VALUES (4, '【可乐鸡翅】这真的是给手残党的新手教程。。。', 21.2, 'www.bilibili.com/video/BV1at411874o', '马壮实Hera');

SET FOREIGN_KEY_CHECKS = 1;
