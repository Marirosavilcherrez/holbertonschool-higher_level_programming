-- Script that converts hbtn_0c_0 database to UTF8 

<<<<<<< HEAD
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

ALTER TABLE first_table
  CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

ALTER TABLE first_table
  MODIFY COLUMN name varchar(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
=======
CREATE TABLE `first_table` (
  `id` int(11) DEFAULT NULL,
  `name` varchar(256) COLLATE utf8mb4_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
>>>>>>> cbfec39a57025d44fd82aae89d325ebdeb8b5075
