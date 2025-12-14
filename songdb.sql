-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Dec 14, 2025 at 06:34 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `songdb`
--

-- --------------------------------------------------------

--
-- Table structure for table `Album`
--

CREATE TABLE `Album` (
  `AlbumID` int(11) NOT NULL,
  `Title` varchar(200) NOT NULL,
  `Year` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `Album`
--

INSERT INTO `Album` (`AlbumID`, `Title`, `Year`) VALUES
(1, 'Her Loss', 2022);

-- --------------------------------------------------------

--
-- Table structure for table `Artist`
--

CREATE TABLE `Artist` (
  `ArtistID` int(11) NOT NULL,
  `Name` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `Artist`
--

INSERT INTO `Artist` (`ArtistID`, `Name`) VALUES
(2, 'Drake'),
(1, 'John Rai'),
(3, 'Pritam');

-- --------------------------------------------------------

--
-- Table structure for table `Category`
--

CREATE TABLE `Category` (
  `CategoryID` int(11) NOT NULL,
  `CategoryName` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `Category`
--

INSERT INTO `Category` (`CategoryID`, `CategoryName`) VALUES
(2, 'Classic'),
(1, 'Pop');

-- --------------------------------------------------------

--
-- Table structure for table `IsIn`
--

CREATE TABLE `IsIn` (
  `SongID` int(11) NOT NULL,
  `CategoryID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `IsIn`
--

INSERT INTO `IsIn` (`SongID`, `CategoryID`) VALUES
(1, 1),
(2, 1);

-- --------------------------------------------------------

--
-- Table structure for table `IsOn`
--

CREATE TABLE `IsOn` (
  `SongID` int(11) NOT NULL,
  `AlbumID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `IsOn`
--

INSERT INTO `IsOn` (`SongID`, `AlbumID`) VALUES
(1, 1),
(2, 1);

-- --------------------------------------------------------

--
-- Table structure for table `Plays`
--

CREATE TABLE `Plays` (
  `SongID` int(11) NOT NULL,
  `ArtistID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `Plays`
--

INSERT INTO `Plays` (`SongID`, `ArtistID`) VALUES
(1, 1),
(2, 1);

-- --------------------------------------------------------

--
-- Table structure for table `Song`
--

CREATE TABLE `Song` (
  `SongID` int(11) NOT NULL,
  `Title` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `Song`
--

INSERT INTO `Song` (`SongID`, `Title`) VALUES
(1, 'K Garu'),
(2, 'Jara Se');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Album`
--
ALTER TABLE `Album`
  ADD PRIMARY KEY (`AlbumID`);

--
-- Indexes for table `Artist`
--
ALTER TABLE `Artist`
  ADD PRIMARY KEY (`ArtistID`),
  ADD UNIQUE KEY `Name` (`Name`);

--
-- Indexes for table `Category`
--
ALTER TABLE `Category`
  ADD PRIMARY KEY (`CategoryID`),
  ADD UNIQUE KEY `CategoryName` (`CategoryName`);

--
-- Indexes for table `IsIn`
--
ALTER TABLE `IsIn`
  ADD PRIMARY KEY (`SongID`,`CategoryID`),
  ADD KEY `CategoryID` (`CategoryID`);

--
-- Indexes for table `IsOn`
--
ALTER TABLE `IsOn`
  ADD PRIMARY KEY (`SongID`,`AlbumID`),
  ADD KEY `AlbumID` (`AlbumID`);

--
-- Indexes for table `Plays`
--
ALTER TABLE `Plays`
  ADD PRIMARY KEY (`SongID`,`ArtistID`),
  ADD KEY `ArtistID` (`ArtistID`);

--
-- Indexes for table `Song`
--
ALTER TABLE `Song`
  ADD PRIMARY KEY (`SongID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `Album`
--
ALTER TABLE `Album`
  MODIFY `AlbumID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `Artist`
--
ALTER TABLE `Artist`
  MODIFY `ArtistID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `Category`
--
ALTER TABLE `Category`
  MODIFY `CategoryID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `Song`
--
ALTER TABLE `Song`
  MODIFY `SongID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `IsIn`
--
ALTER TABLE `IsIn`
  ADD CONSTRAINT `isin_ibfk_1` FOREIGN KEY (`SongID`) REFERENCES `Song` (`SongID`),
  ADD CONSTRAINT `isin_ibfk_2` FOREIGN KEY (`CategoryID`) REFERENCES `Category` (`CategoryID`);

--
-- Constraints for table `IsOn`
--
ALTER TABLE `IsOn`
  ADD CONSTRAINT `ison_ibfk_1` FOREIGN KEY (`SongID`) REFERENCES `Song` (`SongID`),
  ADD CONSTRAINT `ison_ibfk_2` FOREIGN KEY (`AlbumID`) REFERENCES `Album` (`AlbumID`);

--
-- Constraints for table `Plays`
--
ALTER TABLE `Plays`
  ADD CONSTRAINT `plays_ibfk_1` FOREIGN KEY (`SongID`) REFERENCES `Song` (`SongID`),
  ADD CONSTRAINT `plays_ibfk_2` FOREIGN KEY (`ArtistID`) REFERENCES `Artist` (`ArtistID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
