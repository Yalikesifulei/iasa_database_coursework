-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema kursach
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `kursach` ;

-- -----------------------------------------------------
-- Schema kursach
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `kursach` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `kursach` ;

-- -----------------------------------------------------
-- Table `kursach`.`faculties`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `kursach`.`faculties` ;

CREATE TABLE IF NOT EXISTS `kursach`.`faculties` (
  `faculty_id` INT NOT NULL,
  `faculty_name` VARCHAR(256) NOT NULL,
  `headmaster_id` INT NOT NULL,
  PRIMARY KEY (`faculty_id`),
  UNIQUE INDEX `faculty_ID_UNIQUE` (`faculty_id` ASC) VISIBLE,
  UNIQUE INDEX `faculty_Name_UNIQUE` (`faculty_name` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `kursach`.`chairs`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `kursach`.`chairs` ;

CREATE TABLE IF NOT EXISTS `kursach`.`chairs` (
  `chair_id` INT NOT NULL,
  `faculty_id` INT NOT NULL,
  `chair_name` VARCHAR(256) NOT NULL,
  PRIMARY KEY (`chair_id`),
  UNIQUE INDEX `teacher_id_UNIQUE` (`chair_id` ASC) VISIBLE,
  INDEX `faculty_id_idx` (`faculty_id` ASC) VISIBLE,
  CONSTRAINT `faculty_id`
    FOREIGN KEY (`faculty_id`)
    REFERENCES `kursach`.`faculties` (`faculty_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `kursach`.`groups`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `kursach`.`groups` ;

CREATE TABLE IF NOT EXISTS `kursach`.`groups` (
  `group_code` VARCHAR(10) NOT NULL,
  `chair_id` INT NOT NULL,
  `study_year` INT NOT NULL,
  `type` VARCHAR(1) NOT NULL DEFAULT 'b',
  PRIMARY KEY (`group_code`),
  UNIQUE INDEX `group_code_UNIQUE` (`group_code` ASC) VISIBLE,
  INDEX `chair_id_idx` (`chair_id` ASC) VISIBLE,
  CONSTRAINT `chair_id_group`
    FOREIGN KEY (`chair_id`)
    REFERENCES `kursach`.`chairs` (`chair_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `kursach`.`teachers`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `kursach`.`teachers` ;

CREATE TABLE IF NOT EXISTS `kursach`.`teachers` (
  `teacher_id` INT NOT NULL,
  `chair_id` INT NOT NULL,
  `name` VARCHAR(128) NOT NULL,
  `title` VARCHAR(45) NOT NULL,
  `sex` VARCHAR(1) NOT NULL,
  `birthday` DATE NULL DEFAULT NULL,
  `child_count` INT NULL DEFAULT NULL,
  `is_studying` TINYINT NULL DEFAULT NULL,
  `phd_date` DATE NULL DEFAULT NULL,
  `phd_topic` VARCHAR(256) NULL DEFAULT NULL,
  `prof_date` DATE NULL DEFAULT NULL,
  `prof_topic` VARCHAR(256) NULL DEFAULT NULL,
  `salary` INT NULL DEFAULT NULL,
  `sc_topic` VARCHAR(128) NULL DEFAULT NULL,
  `sc_field` VARCHAR(128) NULL DEFAULT NULL,
  PRIMARY KEY (`teacher_id`),
  UNIQUE INDEX `teacher_id_UNIQUE` (`teacher_id` ASC) VISIBLE,
  INDEX `chair_id_idx` (`chair_id` ASC) VISIBLE,
  CONSTRAINT `chair_id_teacher`
    FOREIGN KEY (`chair_id`)
    REFERENCES `kursach`.`chairs` (`chair_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `kursach`.`students`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `kursach`.`students` ;

CREATE TABLE IF NOT EXISTS `kursach`.`students` (
  `student_id` INT NOT NULL,
  `group_code` VARCHAR(10) NOT NULL,
  `name` VARCHAR(128) NOT NULL,
  `sex` VARCHAR(1) NOT NULL,
  `birthday` DATE NULL DEFAULT NULL,
  `has_children` TINYINT NULL DEFAULT NULL,
  `diploma_teacher_id` INT NULL DEFAULT NULL,
  `diploma_topic` VARCHAR(256) NULL DEFAULT NULL,
  `scholarship` INT NULL DEFAULT NULL,
  PRIMARY KEY (`student_id`),
  INDEX `student_group_idx` (`group_code` ASC) VISIBLE,
  INDEX `diploma_teacher_id_idx` (`diploma_teacher_id` ASC) VISIBLE,
  CONSTRAINT `diploma_teacher_id`
    FOREIGN KEY (`diploma_teacher_id`)
    REFERENCES `kursach`.`teachers` (`teacher_id`),
  CONSTRAINT `student_group`
    FOREIGN KEY (`group_code`)
    REFERENCES `kursach`.`groups` (`group_code`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `kursach`.`subjects`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `kursach`.`subjects` ;

CREATE TABLE IF NOT EXISTS `kursach`.`subjects` (
  `subject_id` INT NOT NULL,
  `chair_id` INT NOT NULL,
  `subject_name` VARCHAR(128) NOT NULL,
  `subject_year` INT NOT NULL,
  `subject_semester` INT NOT NULL,
  `subject_lec_hours` INT NULL DEFAULT NULL,
  `subject_prac_hours` INT NULL DEFAULT NULL,
  `subject_lab_hours` INT NULL DEFAULT NULL,
  `subject_course_work_hours` INT NULL DEFAULT NULL,
  `subject_control` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`subject_id`),
  INDEX `chair_id_idx` (`chair_id` ASC) VISIBLE,
  CONSTRAINT `chair_id`
    FOREIGN KEY (`chair_id`)
    REFERENCES `kursach`.`chairs` (`chair_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `kursach`.`session`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `kursach`.`session` ;

CREATE TABLE IF NOT EXISTS `kursach`.`session` (
  `session_id` INT NOT NULL,
  `student_id` INT NOT NULL,
  `subject_id` INT NOT NULL,
  `teacher_id` INT NOT NULL,
  INDEX `student_idx` (`student_id` ASC) VISIBLE,
  INDEX `subject_idx` (`subject_id` ASC) VISIBLE,
  INDEX `teacher_idx` (`teacher_id` ASC) VISIBLE,
  CONSTRAINT `student`
    FOREIGN KEY (`student_id`)
    REFERENCES `kursach`.`students` (`student_id`),
  CONSTRAINT `subject`
    FOREIGN KEY (`subject_id`)
    REFERENCES `kursach`.`subjects` (`subject_id`),
  CONSTRAINT `teacher`
    FOREIGN KEY (`teacher_id`)
    REFERENCES `kursach`.`teachers` (`teacher_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `kursach`.`schedule`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `kursach`.`schedule` ;

CREATE TABLE IF NOT EXISTS `kursach`.`schedule` (
  `subject_id` INT NOT NULL,
  `teacher_id` INT NOT NULL,
  `group_code` VARCHAR(10) NULL,
  `lesson_type` VARCHAR(4) NULL,
  INDEX `teacher_id_idx` (`teacher_id` ASC) VISIBLE,
  INDEX `subject_id_idx` (`subject_id` ASC) VISIBLE,
  INDEX `group_code_idx` (`group_code` ASC) VISIBLE,
  CONSTRAINT `subject_id`
    FOREIGN KEY (`subject_id`)
    REFERENCES `kursach`.`subjects` (`subject_id`),
  CONSTRAINT `teacher_id`
    FOREIGN KEY (`teacher_id`)
    REFERENCES `kursach`.`teachers` (`teacher_id`),
  CONSTRAINT `group_code`
    FOREIGN KEY (`group_code`)
    REFERENCES `kursach`.`groups` (`group_code`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
