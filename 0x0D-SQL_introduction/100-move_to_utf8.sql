-- change to utf-8
USE `hbtn_0c_0`
ALTER DATABASE `hbtn_0c_0`CHARACTER SET tf8mb4 collate utf8mb4_unicode_ci;
SELECT * FROM `first_table`
ALTER TABLE `first_table` MODIFY name CHARACTER SET tf8mb4 collate utf8mb4_unicode_ci;
