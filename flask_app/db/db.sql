-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema canciones
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema canciones
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `canciones` DEFAULT CHARACTER SET utf8 ;
USE `canciones` ;

-- -----------------------------------------------------
-- Table `canciones`.`usuarios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `canciones`.`usuarios` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(255) NULL,
  `email` VARCHAR(255) NULL,
  `password` VARCHAR(255) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `canciones`.`canciones`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `canciones`.`canciones` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `titulo` VARCHAR(255) NULL,
  `artista` VARCHAR(255) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `canciones`.`canciones_has_usuarios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `canciones`.`canciones_has_usuarios` (
  `canciones_id` INT NOT NULL,
  `usuarios_id` INT NOT NULL,
  PRIMARY KEY (`canciones_id`, `usuarios_id`),
  INDEX `fk_canciones_has_usuarios_usuarios1_idx` (`usuarios_id` ASC) VISIBLE,
  INDEX `fk_canciones_has_usuarios_canciones_idx` (`canciones_id` ASC) VISIBLE,
  CONSTRAINT `fk_canciones_has_usuarios_canciones`
    FOREIGN KEY (`canciones_id`)
    REFERENCES `canciones`.`canciones` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_canciones_has_usuarios_usuarios1`
    FOREIGN KEY (`usuarios_id`)
    REFERENCES `canciones`.`usuarios` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
