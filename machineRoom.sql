/*
Navicat MySQL Data Transfer

Source Server         : bnrc
Source Server Version : 50722
Source Host           : 10.108.104.228:3306
Source Database       : machineRoom

Target Server Type    : MYSQL
Target Server Version : 50722
File Encoding         : 65001

Date: 2018-06-20 10:17:50
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for admin
-- ----------------------------
DROP TABLE IF EXISTS `admin`;
CREATE TABLE `admin` (
  `u_id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `u_name` varchar(100) NOT NULL,
  `u_password` varchar(100) NOT NULL,
  `u_tele` varchar(100) NOT NULL,
  `u_email` varchar(100) DEFAULT NULL,
  `u_auth` int(1) NOT NULL DEFAULT '0',
  `register_date` datetime DEFAULT NULL,
  `history` text,
  PRIMARY KEY (`u_id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of admin
-- ----------------------------
INSERT INTO `admin` VALUES ('1', 'Catherine', '123456', '18210623224', 'zhangyaru@bupt.edu.cn', '1', '2018-05-15 00:00:00', 'catherine lolgin in');
INSERT INTO `admin` VALUES ('2', 'Alanrah', '123456', '18210623224', 'zhangyaru@bupt.edu.cn', '1', '2018-05-15 00:00:00', 'Alanrah lolgin in');
INSERT INTO `admin` VALUES ('7', 'test1', 'test1', '1235790', 'bgfbfg', '0', '2018-06-05 15:07:53', null);
INSERT INTO `admin` VALUES ('8', 'tewst2', '231243', '1235790', 'bgfbfg', '0', '2018-06-05 15:09:18', null);
INSERT INTO `admin` VALUES ('9', '雅茹', '123456', '1234567896', 'xji@163. com', '0', '2018-06-05 18:41:35', null);
INSERT INTO `admin` VALUES ('10', 'bnrc', 'bnrc', '62281119', 'bnrc@bupt.edu.cn', '0', '2018-06-07 17:06:52', null);
INSERT INTO `admin` VALUES ('11', 'ing', 'ing', '123', 'xcbn', '0', '2018-06-07 17:29:28', null);
INSERT INTO `admin` VALUES ('12', 'dddd', 'dddd', '369852147', 'yui', '0', '2018-06-07 18:17:03', null);

-- ----------------------------
-- Table structure for cabinet
-- ----------------------------
DROP TABLE IF EXISTS `cabinet`;
CREATE TABLE `cabinet` (
  `r_id` int(11) DEFAULT NULL,
  `c_id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `c_name` varchar(100) NOT NULL,
  `c_un` int(11) DEFAULT NULL,
  `last_modified` datetime DEFAULT NULL,
  `c_status` int(11) NOT NULL,
  PRIMARY KEY (`c_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of cabinet
-- ----------------------------
INSERT INTO `cabinet` VALUES ('1', '1', '机柜1号', '10', '2018-05-15 10:56:02', '1');
INSERT INTO `cabinet` VALUES ('1', '2', '机柜2号', '10', '2018-05-30 14:56:47', '1');
INSERT INTO `cabinet` VALUES ('2', '3', '机柜3号', '10', '2018-05-30 16:43:35', '1');

-- ----------------------------
-- Table structure for deviceDetailInfo
-- ----------------------------
DROP TABLE IF EXISTS `deviceDetailInfo`;
CREATE TABLE `deviceDetailInfo` (
  `d_id` int(11) NOT NULL,
  `d_length` float DEFAULT NULL,
  `d_width` float DEFAULT NULL,
  `d_height` float DEFAULT NULL,
  `d_pic` varchar(100) DEFAULT NULL,
  `pos_pic` varchar(100) DEFAULT NULL,
  `d_producer` varchar(100) DEFAULT NULL,
  `d_seq` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of deviceDetailInfo
-- ----------------------------
INSERT INTO `deviceDetailInfo` VALUES ('2', '0.5', '0.5', '0.02', ' https://img14.360buyimg.com/n0/jfs/t1960/212/953026969/405901/59eacc17/563968eeNb3b2e0df.jpg', 'https://ss0.bdstatic.com/70cFvHSh_Q1PYnxGkpoWK1HF6hhy/it/u=3167998012,2116482000&fm=27&gp=0.jpg', 'TP-LINK', ' TL-SF1005D');
INSERT INTO `deviceDetailInfo` VALUES ('3', '0.2', '0.2', '0.1', 'https://img14.360buyimg.com/n0/jfs/t3427/221/1828863550/93027/757e93ac/5832861fN2566f854.jpg', 'https://ss0.bdstatic.com/70cFvHSh_Q1PYnxGkpoWK1HF6hhy/it/u=3167998012,2116482000&fm=27&gp=0.jpg', 'TP-LINK', 'TL-WDR5620');
INSERT INTO `deviceDetailInfo` VALUES ('4', '1', '1', '2', 'http://bmp.skxox.com/201606/23/xiaowai.153607.jpg', null, 'TP-LINK', 'test');
INSERT INTO `deviceDetailInfo` VALUES ('5', '1', '3', '2', 'http://www.qianqigroup.com/Upload/product/max/SeverCabinet/19Inch19USeverCabinet11-18462028953.jpg', null, 'test', 'test');
INSERT INTO `deviceDetailInfo` VALUES ('22', null, null, null, 'http://10.108.104.228:5000/static/devicePic/switch/1528186600045.jpg', '', null, null);
INSERT INTO `deviceDetailInfo` VALUES ('23', '78', '0', '0', 'http://10.108.104.228:5000/static/devicePic/cabinet/131.jpg', '', '', '');
INSERT INTO `deviceDetailInfo` VALUES ('28', '12', '34', '67', 'http://10.108.104.228:5000/static/devicePic/router/4.jpg', '8', '', '');
INSERT INTO `deviceDetailInfo` VALUES ('30', null, null, null, 'http://10.108.104.228:5000/static/devicePic/rockServer/1528270944488.jpg', '8', null, null);
INSERT INTO `deviceDetailInfo` VALUES ('31', null, null, null, 'http://10.108.104.228:5000/static/devicePic/router/1528280138310.jpg', '-1', null, null);
INSERT INTO `deviceDetailInfo` VALUES ('32', null, null, null, 'http://10.108.104.228:5000/static/devicePic/switch/1528342367405.jpg', '-1', null, null);
INSERT INTO `deviceDetailInfo` VALUES ('33', null, null, null, 'http://10.108.104.228:5000/static/devicePic/router/1528353165761.jpg', '-1', null, null);
INSERT INTO `deviceDetailInfo` VALUES ('35', null, null, null, 'http://10.108.104.228:5000/static/devicePic/cabinet/1528362230219.jpg', '-1', null, null);
INSERT INTO `deviceDetailInfo` VALUES ('36', '1', '1', '2', 'http://10.108.104.228:5000/static/devicePic/router/1528367499976.jpg', '-1', 'Xxxxxxx', 'Xxxxxxxx');

-- ----------------------------
-- Table structure for deviceInfo
-- ----------------------------
DROP TABLE IF EXISTS `deviceInfo`;
CREATE TABLE `deviceInfo` (
  `r_id` int(11) DEFAULT NULL,
  `c_id` int(11) DEFAULT NULL,
  `d_id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `d_class` varchar(255) NOT NULL,
  `d_name` varchar(100) NOT NULL,
  `d_u` int(11) DEFAULT NULL COMMENT '=0，这是机柜，>=1，设备在机柜上,=-1，设备不在机柜上',
  `last_modified` datetime DEFAULT NULL,
  `c_un` int(10) DEFAULT NULL COMMENT 'c_un=0,这是设备,c_un>=1，这是机柜',
  `d_status` int(11) NOT NULL DEFAULT '1',
  PRIMARY KEY (`d_id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of deviceInfo
-- ----------------------------
INSERT INTO `deviceInfo` VALUES ('1', '4', '2', '交换机', '交换机一号', '20', '2018-06-11 15:36:29', '0', '1');
INSERT INTO `deviceInfo` VALUES ('1', '5', '3', '路由器', '路由器', '1', '2018-05-30 15:10:03', '0', '1');
INSERT INTO `deviceInfo` VALUES ('1', '4', '4', '机柜', '机柜1号', '0', '2018-06-06 10:43:05', '10', '1');
INSERT INTO `deviceInfo` VALUES ('1', '5', '5', '机柜', '机柜2号', '0', '2018-06-05 18:37:16', '10', '1');
INSERT INTO `deviceInfo` VALUES ('2', '0', '22', '显示器', '显示器', '0', '2018-06-05 16:17:10', null, '1');
INSERT INTO `deviceInfo` VALUES ('4', '23', '23', '机柜', '机柜', '0', '2018-06-06 11:08:43', null, '1');
INSERT INTO `deviceInfo` VALUES ('4', '23', '28', '塔式服务器', 'ABC的功夫', '8', '2018-06-11 16:17:07', null, '1');
INSERT INTO `deviceInfo` VALUES ('4', '23', '30', '机架式服务器', '机架式服务器', '8', '2018-06-06 15:44:55', null, '1');
INSERT INTO `deviceInfo` VALUES ('2', '31', '31', '塔式服务器', '塔式服务器', '0', '2018-06-06 18:16:54', null, '1');
INSERT INTO `deviceInfo` VALUES ('5', '0', '32', '键盘', '键盘', '0', '2018-06-07 11:33:17', null, '1');
INSERT INTO `deviceInfo` VALUES ('4', '33', '33', 'Test', 'Test', '0', '2018-06-07 14:34:35', null, '1');
INSERT INTO `deviceInfo` VALUES ('5', '0', '35', 'Test', 'B7egzgh', '0', '2018-06-07 17:05:15', null, '1');
INSERT INTO `deviceInfo` VALUES ('8', '36', '36', '机柜', '机柜1', '0', '2018-06-07 18:41:16', null, '1');

-- ----------------------------
-- Table structure for manageRoom
-- ----------------------------
DROP TABLE IF EXISTS `manageRoom`;
CREATE TABLE `manageRoom` (
  `u_id` int(11) DEFAULT NULL,
  `r_id` int(11) DEFAULT NULL,
  `auth` int(11) DEFAULT '1'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of manageRoom
-- ----------------------------
INSERT INTO `manageRoom` VALUES ('1', '1', '1');
INSERT INTO `manageRoom` VALUES ('2', '1', '1');
INSERT INTO `manageRoom` VALUES ('1', '2', '1');
INSERT INTO `manageRoom` VALUES ('1', '4', '1');
INSERT INTO `manageRoom` VALUES ('1', '5', '1');
INSERT INTO `manageRoom` VALUES ('1', '5', '1');
INSERT INTO `manageRoom` VALUES ('12', '8', '1');
INSERT INTO `manageRoom` VALUES ('12', '9', '1');

-- ----------------------------
-- Table structure for roomInfo
-- ----------------------------
DROP TABLE IF EXISTS `roomInfo`;
CREATE TABLE `roomInfo` (
  `r_id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `r_name` varchar(100) NOT NULL,
  `r_owner` varchar(100) NOT NULL,
  `r_pos` varchar(100) DEFAULT NULL,
  `r_length` float DEFAULT NULL,
  `r_width` float DEFAULT NULL,
  `r_height` float DEFAULT NULL,
  `r_pic` text,
  `create_datetime` datetime DEFAULT NULL,
  PRIMARY KEY (`r_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of roomInfo
-- ----------------------------
INSERT INTO `roomInfo` VALUES ('1', '北邮网研七组机房', '未来网实验室', '北邮科研楼410', '20', '20', '20', null, '2018-05-15 11:23:52');
INSERT INTO `roomInfo` VALUES ('2', 'test', 'test', 'test', '20', '20', '20', null, '2018-05-30 16:54:35');
INSERT INTO `roomInfo` VALUES ('4', '1', 'aa', 'cc', '1', '2', '3', null, '2018-06-03 14:31:37');
INSERT INTO `roomInfo` VALUES ('5', 'k', 'k', 'k', '9', '7', '6', null, '2018-06-03 17:49:14');
INSERT INTO `roomInfo` VALUES ('7', 'k', 'k', 'k', '9', '7', '6', null, '2018-06-03 17:52:25');
INSERT INTO `roomInfo` VALUES ('8', 'Dddd', 'Dddd', 'Dddd', '1', '2', '3', null, '2018-06-07 18:19:54');
INSERT INTO `roomInfo` VALUES ('9', 'Dddd的', 'Dddd', 'Dddd的', '0', '0', '0', null, '2018-06-07 18:28:50');
