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

 Date: 19/04/2021 15:46:44
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for song_info
-- ----------------------------
DROP TABLE IF EXISTS `song_info`;
CREATE TABLE `song_info`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `song_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `singer` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 175 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of song_info
-- ----------------------------
INSERT INTO `song_info` VALUES (1, '白噪音婴儿睡眠', '深呼吸');
INSERT INTO `song_info` VALUES (2, '白噪音', '银临');
INSERT INTO `song_info` VALUES (3, '白噪音大全', '白噪音');
INSERT INTO `song_info` VALUES (4, '白噪音 - (White Noise)', '话梅鹿PruneDeer');
INSERT INTO `song_info` VALUES (5, '白噪音', '安静');
INSERT INTO `song_info` VALUES (6, '深度催眠', '深呼吸');
INSERT INTO `song_info` VALUES (7, 'Summer - (电影《菊次郎的夏天》主题曲)', '久石譲');
INSERT INTO `song_info` VALUES (8, '提升睡眠质量的雨声 - (Improve Sleep Quality)', '贵族音乐ASMR');
INSERT INTO `song_info` VALUES (145, '孤独的夜哨', '张震岳');
INSERT INTO `song_info` VALUES (146, '白噪音婴儿睡眠', '深呼吸');
INSERT INTO `song_info` VALUES (147, '白噪音', '银临');
INSERT INTO `song_info` VALUES (148, '白噪音大全', '白噪音');
INSERT INTO `song_info` VALUES (149, '深度催眠', '深呼吸');
INSERT INTO `song_info` VALUES (150, '白噪音 - (White Noise)', '话梅鹿PruneDeer');
INSERT INTO `song_info` VALUES (151, '白噪音', '安静');
INSERT INTO `song_info` VALUES (152, '提升睡眠质量的雨声 - (Improve Sleep Quality)', '贵族音乐ASMR');
INSERT INTO `song_info` VALUES (153, 'Summer - (电影《菊次郎的夏天》主题曲)', '久石譲');
INSERT INTO `song_info` VALUES (154, '婴儿白噪音', 'Acerting Art');
INSERT INTO `song_info` VALUES (155, '流水声', '白噪音');
INSERT INTO `song_info` VALUES (156, '白噪音婴儿睡眠', '背景音');
INSERT INTO `song_info` VALUES (157, '白噪音', 'Jaz');
INSERT INTO `song_info` VALUES (158, '舒适的林荫溪谷．ASMR环境白噪音', '贵族音乐ASMR');
INSERT INTO `song_info` VALUES (159, '晚上冥想火声', 'Truesound Village');
INSERT INTO `song_info` VALUES (160, '大自然纾压鸟鸣．ASMR环境白噪音', '贵族音乐ASMR');
INSERT INTO `song_info` VALUES (161, '舒伯特摇篮曲 (水晶版)', '');
INSERT INTO `song_info` VALUES (162, '夜晚虫鸣之歌', '贵族音乐ASMR');
INSERT INTO `song_info` VALUES (163, '爱尔兰小篝火', 'Truesound Village');
INSERT INTO `song_info` VALUES (164, '宝宝哄睡白噪音: 夏夜流水', '贵族音乐宝宝');
INSERT INTO `song_info` VALUES (165, '终极空调 (白噪声循环)', '科学的声音');
INSERT INTO `song_info` VALUES (166, '细界', '阿细');
INSERT INTO `song_info` VALUES (167, '天后（国粤版）（Cover 陈势安）', '阿细');
INSERT INTO `song_info` VALUES (168, '细界', '钢铁暗黑真经');
INSERT INTO `song_info` VALUES (169, '细界', '宇心');
INSERT INTO `song_info` VALUES (170, '细界', '阿V');
INSERT INTO `song_info` VALUES (171, '细界', 'Xun寻');
INSERT INTO `song_info` VALUES (172, '细界', '卡羅琳');
INSERT INTO `song_info` VALUES (173, '细界', '茉凌');
INSERT INTO `song_info` VALUES (174, '野孩子', '阿细');
INSERT INTO `song_info` VALUES (175, '爱太远的人-Fan’s version（翻自 阿细） ', '小明。');

SET FOREIGN_KEY_CHECKS = 1;
