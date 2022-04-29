-- phpMyAdmin SQL Dump
-- version 4.9.5deb2
-- https://www.phpmyadmin.net/
--
-- Hôte : localhost:3306
-- Généré le : ven. 22 avr. 2022 à 10:44
-- Version du serveur :  8.0.25-0ubuntu0.20.04.1
-- Version de PHP : 7.4.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `gestion_vol`
--

-- --------------------------------------------------------

--
-- Structure de la table `Aeroclub`
--

CREATE TABLE `Aeroclub` (
  `idAeroclub` int NOT NULL,
  `nomAeroclub` varchar(20) DEFAULT NULL,
  `color` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Structure de la table `Avions`
--

CREATE TABLE `Avions` (
  `idAvion` int NOT NULL,
  `immatAvion` varchar(20) DEFAULT NULL,
  `typeAvion` varchar(20) DEFAULT NULL,
  `idAeroclub` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Structure de la table `Events`
--

CREATE TABLE `Events` (
  `id` int NOT NULL,
  `start_date` datetime DEFAULT CURRENT_TIMESTAMP,
  `end_date` datetime DEFAULT CURRENT_TIMESTAMP,
  `texte` text,
  `idAvion` int DEFAULT NULL,
  `idClient` int NOT NULL,
  `idEnseignant` int DEFAULT NULL,
  `idType` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Structure de la table `Identification`
--

CREATE TABLE `Identification` (
  `idUser` int NOT NULL,
  `nom` varchar(20) DEFAULT NULL,
  `prenom` varchar(20) DEFAULT NULL,
  `mail` varchar(40) DEFAULT NULL,
  `login` varchar(20) DEFAULT NULL,
  `motPasse` varchar(40) DEFAULT NULL,
  `statut` int DEFAULT NULL,
  `avatar` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Structure de la table `TypeVol`
--

CREATE TABLE `TypeVol` (
  `idType` int NOT NULL,
  `nomType` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `Aeroclub`
--
ALTER TABLE `Aeroclub`
  ADD PRIMARY KEY (`idAeroclub`);

--
-- Index pour la table `Avions`
--
ALTER TABLE `Avions`
  ADD PRIMARY KEY (`idAvion`),
  ADD KEY `idAeroclub` (`idAeroclub`);

--
-- Index pour la table `Events`
--
ALTER TABLE `Events`
  ADD PRIMARY KEY (`id`),
  ADD KEY `idAvion` (`idAvion`),
  ADD KEY `idClient` (`idClient`),
  ADD KEY `idEnseignant` (`idEnseignant`),
  ADD KEY `idType` (`idType`);

--
-- Index pour la table `Identification`
--
ALTER TABLE `Identification`
  ADD PRIMARY KEY (`idUser`);

--
-- Index pour la table `TypeVol`
--
ALTER TABLE `TypeVol`
  ADD PRIMARY KEY (`idType`);

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `Avions`
--
ALTER TABLE `Avions`
  ADD CONSTRAINT `Avions_ibfk_1` FOREIGN KEY (`idAeroclub`) REFERENCES `Aeroclub` (`idAeroclub`);

--
-- Contraintes pour la table `Events`
--
ALTER TABLE `Events`
  ADD CONSTRAINT `Events_ibfk_1` FOREIGN KEY (`idAvion`) REFERENCES `Avions` (`idAvion`),
  ADD CONSTRAINT `Events_ibfk_2` FOREIGN KEY (`idClient`) REFERENCES `Identification` (`idUser`),
  ADD CONSTRAINT `Events_ibfk_3` FOREIGN KEY (`idEnseignant`) REFERENCES `Identification` (`idUser`),
  ADD CONSTRAINT `Events_ibfk_4` FOREIGN KEY (`idType`) REFERENCES `TypeVol` (`idType`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
