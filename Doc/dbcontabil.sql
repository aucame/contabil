-- --------------------------------------------------------
-- Servidor:                     127.0.0.1
-- Versão do servidor:           5.7.17 - MySQL Community Server (GPL)
-- OS do Servidor:               Linux
-- HeidiSQL Versão:              9.4.0.5125
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- Copiando estrutura do banco de dados para dbContabil
DROP DATABASE IF EXISTS `dbContabil`;
CREATE DATABASE IF NOT EXISTS `dbContabil` /*!40100 DEFAULT CHARACTER SET latin1 COLLATE latin1_bin */;
USE `dbContabil`;

-- Copiando estrutura para tabela dbContabil.cadclientes
DROP TABLE IF EXISTS `cadclientes`;
CREATE TABLE IF NOT EXISTS `cadclientes` (
  `idcliente` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(100) COLLATE latin1_bin DEFAULT NULL,
  `endereco` varchar(50) COLLATE latin1_bin DEFAULT NULL,
  `fonecomercial` varchar(20) COLLATE latin1_bin DEFAULT NULL,
  `foneresidencial` varchar(20) COLLATE latin1_bin DEFAULT NULL,
  PRIMARY KEY (`idcliente`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1 COLLATE=latin1_bin;

-- Exportação de dados foi desmarcado.
-- Copiando estrutura para tabela dbContabil.cadempresa
DROP TABLE IF EXISTS `cadempresa`;
CREATE TABLE IF NOT EXISTS `cadempresa` (
  `idempresa` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(100) COLLATE latin1_bin DEFAULT NULL,
  `endereco` varchar(50) COLLATE latin1_bin DEFAULT NULL,
  `fonecomercial` varchar(20) COLLATE latin1_bin DEFAULT NULL,
  PRIMARY KEY (`idempresa`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1 COLLATE=latin1_bin;

-- Exportação de dados foi desmarcado.
-- Copiando estrutura para tabela dbContabil.cadlancamento
DROP TABLE IF EXISTS `cadlancamento`;
CREATE TABLE IF NOT EXISTS `cadlancamento` (
  `idlancamento` int(11) NOT NULL AUTO_INCREMENT,
  `ano` int(11) DEFAULT NULL,
  `mes` int(11) DEFAULT NULL,
  `idplano` varchar(20) COLLATE latin1_bin DEFAULT NULL,
  `valor` decimal(10,2) DEFAULT NULL,
  `idcliente` int(11) DEFAULT NULL,
  PRIMARY KEY (`idlancamento`)
) ENGINE=InnoDB AUTO_INCREMENT=7177 DEFAULT CHARSET=latin1 COLLATE=latin1_bin;

-- Exportação de dados foi desmarcado.
-- Copiando estrutura para tabela dbContabil.cadparam
DROP TABLE IF EXISTS `cadparam`;
CREATE TABLE IF NOT EXISTS `cadparam` (
  `idparam` int(11) NOT NULL AUTO_INCREMENT,
  `mes` int(11) DEFAULT NULL,
  `ano` int(11) DEFAULT NULL,
  `idempresa` int(11) DEFAULT NULL,
  `diasuteis` int(11) DEFAULT NULL,
  `meddiafat` int(11) DEFAULT NULL,
  `paramostra` int(11) DEFAULT NULL,
  `fatamostra` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`idparam`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=latin1 COLLATE=latin1_bin;

-- Exportação de dados foi desmarcado.
-- Copiando estrutura para tabela dbContabil.cadplano
DROP TABLE IF EXISTS `cadplano`;
CREATE TABLE IF NOT EXISTS `cadplano` (
  `idplano` int(11) NOT NULL AUTO_INCREMENT,
  `codigo` varchar(20) COLLATE latin1_bin DEFAULT NULL,
  `descricao` varchar(100) COLLATE latin1_bin DEFAULT NULL,
  `tipocd` varchar(1) COLLATE latin1_bin DEFAULT NULL,
  `tipo` decimal(2,0) DEFAULT NULL,
  `grupo` decimal(2,0) DEFAULT NULL,
  `subgrupo` decimal(2,0) DEFAULT NULL,
  `subgrp` decimal(3,0) DEFAULT NULL,
  `numero` decimal(5,0) DEFAULT NULL,
  `grupoplano` varchar(50) COLLATE latin1_bin DEFAULT NULL,
  PRIMARY KEY (`idplano`)
) ENGINE=InnoDB AUTO_INCREMENT=300 DEFAULT CHARSET=latin1 COLLATE=latin1_bin;

-- Exportação de dados foi desmarcado.
-- Copiando estrutura para tabela dbContabil.cadusuarios
DROP TABLE IF EXISTS `cadusuarios`;
CREATE TABLE IF NOT EXISTS `cadusuarios` (
  `idusuarios` int(11) NOT NULL,
  `nome` varchar(100) DEFAULT NULL,
  `senha` varchar(20) DEFAULT NULL,
  `ativo` varchar(3) DEFAULT NULL,
  `login` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`idusuarios`),
  KEY `idxnome` (`nome`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Exportação de dados foi desmarcado.
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
