-- phpMyAdmin SQL Dump
-- version 4.9.5deb2
-- https://www.phpmyadmin.net/
--
-- Hôte : localhost:3306
-- Généré le : mer. 01 juin 2022 à 16:17
-- Version du serveur :  8.0.28-0ubuntu0.20.04.3
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
-- Base de données : `web`
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

--
-- Déchargement des données de la table `Aeroclub`
--

INSERT INTO `Aeroclub` (`idAeroclub`, `nomAeroclub`, `color`) VALUES
(0, 'Admin', 'black'),
(1, 'ENAC Lasbordes', 'blue'),
(2, 'Aéroclub de Luchon', 'purple'),
(3, 'Ailes Anciennes', 'orange'),
(4, 'Air France Toulouse', 'red'),
(5, 'M.Dassault L.Breguet', 'green'),
(6, 'Ailes Toulousaines', 'brown'),
(7, 'MidiPyrénées Voltige', 'pink');

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

--
-- Déchargement des données de la table `Avions`
--

INSERT INTO `Avions` (`idAvion`, `immatAvion`, `typeAvion`, `idAeroclub`) VALUES
(1, 'F-GGXU', 'Robin DR400-120', 1),
(2, 'F-GLVY', 'Robin DR400-120', 1),
(3, 'F-GYRL', 'Robin DR400-140B', 1),
(4, 'F-GUAC', 'TB10 Tobago', 1),
(5, 'F-GOVL', 'Robin DR400-120', 1),
(6, 'F-GHEO', 'CESSNA 182RG', 1),
(7, 'F-WITH', 'AS355 Ecureuil 2', 3),
(8, 'F-SERI', 'Airbus E-Fan', 3),
(9, 'N4887', 'Boeing 33 SGT', 3),
(10, 'F-AVRU', 'Dassault Etendard IV', 3),
(11, 'F-UITR', 'Br 765 Sahara', 3),
(12, 'F-XFPO', 'Dassault Falcon 10', 3),
(13, 'F-GYKI', 'DR400', 4),
(14, 'F-GMKY', 'DR400', 4),
(15, 'F-HOBY', 'Piper 18', 4),
(16, 'F-MOIP', 'DR400', 5),
(17, 'F-KILO', 'DR400', 5),
(18, 'F-KJIU', 'DR400', 5),
(19, 'F-OIPT', 'ULM A22L2', 5),
(20, 'F-GORK', 'Robin DR400/140B', 6),
(21, 'F-GYKC', 'Robin DR400/140B', 6),
(22, 'F-GFMM', 'Robin DR400/140B', 6),
(23, 'F-HJAT', 'Tecnam P2002', 6),
(24, 'F-HZAM', 'Tecnam P2002', 6),
(25, 'F-HLAD', 'WT9 Dynamic', 6),
(26, '85-AFI', 'Nynja', 6),
(27, '74-AGZ', 'Tecnam P92 Ecolight', 6),
(28, '31-VZT', 'Humbert Tétras', 6),
(29, 'F-GMPV', 'CAP10 C', 7),
(30, 'F-GLJG', 'EXTRA200', 7),
(31, 'F-HXAL', 'EXTRA330 SC', 7),
(32, 'F-CJOK', 'A Schleicher GmbH', 2),
(33, 'F-CJBA', 'Centrair SNC Allianc', 2),
(34, 'F-CFYC', 'Grob G103 Twin II', 2),
(35, 'F-CXBD', 'Schempp-Hirt Duo Di', 2),
(36, 'F-CZAR', 'Grob G102 Astir CS', 2),
(37, 'F-CIMA', 'Schempp-Hirt Discus', 2),
(38, 'F-CIMB', 'Schempp-Hirt Discus', 2),
(39, 'F-CLEO', 'Glaser-Dirks DG-300', 2),
(40, 'F-CGZD', 'LS6-18w', 2);

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
  `avatar` varchar(20) DEFAULT NULL,
  `idAeroclub` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Déchargement des données de la table `Identification`
--

INSERT INTO `Identification` (`idUser`, `nom`, `prenom`, `mail`, `login`, `motPasse`, `statut`, `avatar`, `idAeroclub`) VALUES
(1, 'Daddi Addoun', 'Saad', 'saad.daddi-addoun@alumni.enac.fr', 'saadaddi', 'Saad147#', 0, '4.png', 0),
(2, 'Loumeaud', 'Thomas', 'thomas.loumeaud@alumni.enac.fr', 'thomaslmd', 'Thomas458/', 0, '6.png', 0),
(3, 'Bayon', 'Thomas', 'thomas.bayon@alumni.enac.fr', 'bayonth', 'thomas', 0, '8.png', 0),
(4, 'des Pallières', 'Alban', 'alban.despallieres@alumni.enac.fr', 'albandp', 'alban006', 0, '6.png', 0),
(5, 'Lagasse', 'Jean-René', 'enac.lasbordes@aeroclub.fr', 'enaclasbordes', 'rbdyy', 1, '5.png', 1),
(6, 'Malraux', 'André', 'luchon@aeroclub.fr', 'luchonaero', 'dfhg', 1, '1.png', 2),
(7, 'Béteille', 'Roger', 'ailes.anciennes@aeroclub.fr', 'ailesanciennes', 'kiuy', 1, '3.png', 3),
(8, 'Lagasse', 'Jean-Luc', 'air.france@aeroclub.fr', 'airfranceaero', 'hytr', 1, '2.png', 4),
(9, 'Dassault', 'Marcel', 'dassault.breguet@aeroclub.fr', 'dassaultbreguetaero', 'vfrt', 1, '6.png', 5),
(10, 'Lagasse', 'Jean-Michel', 'ailes.toulousaines@aeroclub.fr', 'ailestoulousaines', 'xdre', 1, '8.png', 6),
(11, 'Lagasse', 'Jean-Sylvain', 'midipyr.voltige@aeroclub.fr', 'midipyrvoltige', 'gtra', 1, '9.png', 7);

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
