-- step number 1
CREATE DATABASE IF NOT EXISTS InterfaceJobs
  DEFAULT CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;

-- step number 2
USE InterfaceJobs;


-- step number 3
CREATE TABLE `interfacejobs`.`integrator_parameter` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `description` VARCHAR(200) NULL,
  `value` VARCHAR(1) NULL,
  PRIMARY KEY (`id`));

-- step number 4
CREATE TABLE `interfacejobs`.`scheduler_parameter` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `description` VARCHAR(200) NULL,
  `scheduling_type` VARCHAR(45) NULL,
  `value` VARCHAR(45) NULL,
  PRIMARY KEY (`id`));
