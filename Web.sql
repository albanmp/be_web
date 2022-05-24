-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Hôte : localhost:8889
-- Généré le : mar. 24 mai 2022 à 15:39
-- Version du serveur :  5.7.34
-- Version de PHP : 7.4.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `Web`
--

-- --------------------------------------------------------

--
-- Structure de la table `Aeroclub`
--

CREATE TABLE `Aeroclub` (
  `idAeroclub` int(11) NOT NULL,
  `nomAeroclub` varchar(20) DEFAULT NULL,
  `color` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure de la table `Avions`
--

CREATE TABLE `Avions` (
  `idAvion` int(11) NOT NULL,
  `immatAvion` varchar(20) DEFAULT NULL,
  `typeAvion` varchar(20) DEFAULT NULL,
  `idAeroclub` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure de la table `events`
--

CREATE TABLE `events` (
  `id` int(11) NOT NULL,
  `start_date` datetime NOT NULL,
  `end_date` datetime NOT NULL,
  `text` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `events`
--

INSERT INTO `events` (`id`, `start_date`, `end_date`, `text`) VALUES
(1, '2022-05-19 12:33:53', '2022-05-19 12:33:53', NULL),
(2, '2022-05-23 12:20:00', '2022-05-23 12:20:00', 'test2');

-- --------------------------------------------------------

--
-- Structure de la table `Identification`
--

CREATE TABLE `Identification` (
  `idUser` int(11) NOT NULL,
  `nom` varchar(20) DEFAULT NULL,
  `prenom` varchar(20) DEFAULT NULL,
  `mail` varchar(40) DEFAULT NULL,
  `login` varchar(20) DEFAULT NULL,
  `motPasse` varchar(40) DEFAULT NULL,
  `statut` int(11) DEFAULT NULL,
  `avatar` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `Identification`
--

INSERT INTO `Identification` (`idUser`, `nom`, `prenom`, `mail`, `login`, `motPasse`, `statut`, `avatar`) VALUES
(10, 'Bayon', 'Thomas', 'bayonthms@gmail.com', 'bayonth', 'thomas', 0, '2.png'),
(12, 'Bay', 'Tom', 'baa', 'tombay', 'abc', 1, '3.png'),
(14, 'To', 'to', 'deijw', 'dew', 'dewde', 1, '11.png');

-- --------------------------------------------------------

--
-- Structure de la table `TypeVol`
--

CREATE TABLE `TypeVol` (
  `idType` int(11) NOT NULL,
  `nomType` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

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
-- Index pour la table `events`
--
ALTER TABLE `events`
  ADD PRIMARY KEY (`id`);

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
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `events`
--
ALTER TABLE `events`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT pour la table `Identification`
--
ALTER TABLE `Identification`
  MODIFY `idUser` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `Avions`
--
ALTER TABLE `Avions`
  ADD CONSTRAINT `Avions_ibfk_1` FOREIGN KEY (`idAeroclub`) REFERENCES `Aeroclub` (`idAeroclub`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
