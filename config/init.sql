-- release format = yyyy-MM-dd
CREATE TABLE `moontomi`.`album` (
  `album_id`  int          NOT NULL AUTO_INCREMENT,
  `title`     varchar(250) NOT NULL,
  `artist_id` int          NOT NULL,
  `image_id`  varchar(32)  NOT NULL,
  `tracks`    json         NOT NULL,
  `release`   char(10)     NOT NULL,
  PRIMARY KEY (`album_id`)
) ENGINE=InnoDB
  DEFAULT CHARSET=utf8mb4
  COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `moontomi`.`album_genre` (
  `album_id` int NOT NULL,
  `genre_id` int NOT NULL,
  PRIMARY KEY (`album_id`, `genre_id`)
) ENGINE=InnoDB
  DEFAULT CHARSET=utf8mb4
  COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `moontomi`.`genre` (
  `genre_id` int         NOT NULL AUTO_INCREMENT,
  `category` varchar(20) NOT NULL,
  `name`     varchar(50) NOT NULL,
  PRIMARY KEY (`genre_id`)
) ENGINE=InnoDB
  DEFAULT CHARSET=utf8mb4
  COLLATE=utf8mb4_0900_ai_ci;

-- pronounce: 한글 발음, name이 한글이면 NULL
-- name_en: 영어 표기, name이 영어면 NULL
CREATE TABLE `moontomi`.`artist` (
  `artist_id` int          NOT NULL AUTO_INCREMENT,
  `name`      varchar(100) NOT NULL,
  `name_en`   varchar(100) DEFAULT NULL,
  `pronounce` varchar(100) DEFAULT NULL,
  `nation`    varchar(20)  NOT NULL,
  PRIMARY KEY (`artist_id`)
) ENGINE=InnoDB
  DEFAULT CHARSET=utf8mb4
  COLLATE=utf8mb4_0900_ai_ci;

-- date format = yyyy-MM-dd
-- open 하기 전에는 rating = NULL
-- migration 이전에는 date = NULL
CREATE TABLE `moontomi`.`lecture` (
  `lecture_id` int      NOT NULL AUTO_INCREMENT,
  `album_id`   int      NOT NULL,
  `rating`     int      DEFAULT NULL,
  `date`       char(10) DEFAULT NULL,
  `season_id`  int      NOT NULL,
  PRIMARY KEY (`lecture_id`)
) ENGINE=InnoDB
  DEFAULT CHARSET=utf8mb4
  COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `moontomi`.`comment` (
  `lecture_id`  int          NOT NULL,
  `writer`      varchar(50)  NOT NULL,
  `password`    varchar(50)  NOT NULL,
  `picks`       json         NOT NULL,
  `text`        varchar(500) NOT NULL,
  `created_at`  datetime     DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`lecture_id`, `writer`)
) ENGINE=InnoDB
  DEFAULT CHARSET=utf8mb4
  COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `moontomi`.`season` (
  `season_id` int         NOT NULL,
  `name`      varchar(50) NOT NULL,
  `image_id`  varchar(32) NOT NULL,
  PRIMARY KEY (`season_id`)
) ENGINE=InnoDB
  DEFAULT CHARSET=utf8mb4
  COLLATE=utf8mb4_0900_ai_ci;
