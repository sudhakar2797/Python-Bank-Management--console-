-- phpMyAdmin SQL Dump
-- version 4.7.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 02, 2018 at 08:21 AM
-- Server version: 10.1.26-MariaDB
-- PHP Version: 7.1.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `pydb`
--

-- --------------------------------------------------------

--
-- Table structure for table `customer`
--

CREATE TABLE `customer` (
  `AccountNo` varchar(255) NOT NULL,
  `CustomerName` varchar(255) NOT NULL,
  `AddressLine` varchar(255) NOT NULL,
  `City` varchar(255) NOT NULL,
  `Zip` int(255) NOT NULL,
  `State` varchar(255) NOT NULL,
  `PhoneNo` varchar(255) NOT NULL,
  `AdharNo` varchar(255) NOT NULL,
  `Balance` varchar(255) NOT NULL,
  `AccountType` varchar(255) NOT NULL,
  `Status` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `customer`
--

INSERT INTO `customer` (`AccountNo`, `CustomerName`, `AddressLine`, `City`, `Zip`, `State`, `PhoneNo`, `AdharNo`, `Balance`, `AccountType`, `Status`) VALUES
('4153325853437899', '242134', '32412341', '41234', 234141, '23142', '324124', '324124', '0', '1', '2017-11-29Opened'),
('5894471389874113', '312122', '12312312', '213231', 1333223, '231231', '1231231', '1231231', '674', '0', '2017-11-29Closed'),
('7032746103609444', '341341324', '12342421', '234123', 341234, '2341243', '234123412', '23412341', '200', '0', '2017-11-29Closed'),
('8016174640924308', '412131', '231241234', '2134123412', 12314, '3241234', '3241234', '1243124', '1', '0', '2017-11-29Opened');

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

CREATE TABLE `login` (
  `username` varchar(30) NOT NULL,
  `password` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `login`
--

INSERT INTO `login` (`username`, `password`) VALUES
('5894471389874113', 'raj'),
('7032746103609444', '7032746103609444'),
('8016174640924308', '8016174640924308'),
('Admin', 'Admin'),
('4153325853437899', '4153325853437899');

-- --------------------------------------------------------

--
-- Table structure for table `transaction`
--

CREATE TABLE `transaction` (
  `AccountNo` varchar(255) NOT NULL,
  `TransactionType` varchar(255) NOT NULL,
  `TransactionID` varchar(255) NOT NULL,
  `Balance` varchar(255) NOT NULL,
  `TransDate` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `transaction`
--

INSERT INTO `transaction` (`AccountNo`, `TransactionType`, `TransactionID`, `Balance`, `TransDate`) VALUES
('329736912873612', 'Deposite', '1', '2000', '0000-00-00'),
('329736912873612', 'Withdraw', '2', '200', '0000-00-00'),
('5894471389874113', 'Deposite', '20171129201727', '669', '2017-11-29'),
('5894471389874113', 'Deposite', '20171129201832', '672', '2017-11-29'),
('5894471389874113', 'Deposite', '20171129201840', '675', '2017-11-29'),
('5894471389874113', 'Deposite', '20171129202838', '674', '2017-11-29'),
('7032746103609444', 'Deposite', '20171129215319', '200', '2017-11-29'),
('8016174640924308', 'Deposite', '20171129222211', '2000', '2017-11-29'),
('8016174640924308', 'Deposite', '20171129222650', '1', '2017-11-29'),
('329736912873612', 'Withdraw', '3', '200', '0000-00-00'),
('329736912873612', 'Withdraw', '5', '200', '0000-00-00'),
('329736912873612', 'Withdraw', '6', '200', '0000-00-00');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `customer`
--
ALTER TABLE `customer`
  ADD PRIMARY KEY (`AccountNo`);

--
-- Indexes for table `transaction`
--
ALTER TABLE `transaction`
  ADD UNIQUE KEY `TransactionID` (`TransactionID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
