-- change to utf-8
USE `hbtn_0c_0`
ALTER TABLE `first_table`
CONVERT TO CHARACTER SET tf8mb4 collate utf8mb4_unicode_ci;
ALTER TABLE `first_table` MODIFY name CHARACTER SET tf8mb4 collate utf8mb4_unicode_ci;
