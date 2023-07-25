-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 17, 2023 at 06:51 AM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `hms_py`
--

-- --------------------------------------------------------

--
-- Table structure for table `hospital`
--

CREATE TABLE `hospital` (
  `Reference_NO` int(11) NOT NULL,
  `NameOfTablet` varchar(45) DEFAULT NULL,
  `Dose` varchar(45) DEFAULT NULL,
  `NumbersOfTablets` varchar(45) DEFAULT NULL,
  `LOT` varchar(45) DEFAULT NULL,
  `IssueDate` varchar(45) DEFAULT NULL,
  `ExpDate` varchar(45) DEFAULT NULL,
  `DailyDose` varchar(45) DEFAULT NULL,
  `Storage` varchar(45) DEFAULT NULL,
  `NHSNumber` varchar(45) DEFAULT NULL,
  `PatientName` varchar(45) DEFAULT NULL,
  `DOB` varchar(45) DEFAULT NULL,
  `PatientAdress` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `hospital`
--

INSERT INTO `hospital` (`Reference_NO`, `NameOfTablet`, `Dose`, `NumbersOfTablets`, `LOT`, `IssueDate`, `ExpDate`, `DailyDose`, `Storage`, `NHSNumber`, `PatientName`, `DOB`, `PatientAdress`) VALUES
(1, 'Panadol extra', '2', '12', 'null', '12-12-12', '13-12-17', '1 tab ', 'refrigetor optional', '11111111', 'Saqlain haider', '27-11-1997', 'lahore'),
(2, 'Panadol extra', '2', '12', 'null', '12-12-12', '13-12-17', '1 tab ', 'refrigetor optional', '11111111', 'Saqlain haider', '27-11-1997', 'lahore'),
(4, 'Brufen', '2', '12', 'null', '12-12-12', '13-12-17', '1 tab ', 'refrigetor optional', '11111111', 'Saqlain haider', '27-11-1997', 'lahore'),
(7, 'Panadol extra', '1', '12', 'not required', '12/12/2000', '12/12/2010', '2', 'room temperature', '77889900', 'Saqlain haider', '12/12/1899', 'lahore');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `hospital`
--
ALTER TABLE `hospital`
  ADD PRIMARY KEY (`Reference_NO`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
