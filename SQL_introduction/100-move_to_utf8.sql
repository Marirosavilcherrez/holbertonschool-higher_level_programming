-- Script that converts hbtn_0c_0 database to UTF8 

CREATE TABLE `first_table` (
  `id` int(11) DEFAULT NULL,
  `name` varchar(256) COLLATE utf8mb4_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
