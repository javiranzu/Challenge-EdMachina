SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
CREATE TABLE IF NOT EXISTS `leads` (
  `id_registro` int(11) NOT NULL,
  `nombre` varchar(200) NOT NULL,
  `email` varchar(200) NOT NULL,
  `direccion` varchar(200) NOT NULL,
  `telefono` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
CREATE TABLE IF NOT EXISTS `materias` (
  `id_materia` int(11) NOT NULL,
  `id_registro` int(11) NOT NULL,
  `materia` varchar(80) NOT NULL,
  `tiempo_cursado` int(11) NOT NULL,
  `carrera` varchar(80) NOT NULL,
  `anio_inscripcion` varchar(4) NOT NULL,
  `veces_cursado` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
ALTER TABLE `leads`
  ADD PRIMARY KEY (`id_registro`);
ALTER TABLE `materias`
  ADD PRIMARY KEY (`id_materia`),
  ADD KEY `FK_id_registro` (`id_registro`) USING BTREE;
ALTER TABLE `leads`
  MODIFY `id_registro` int(11) NOT NULL AUTO_INCREMENT;
ALTER TABLE `materias`
  MODIFY `id_materia` int(11) NOT NULL AUTO_INCREMENT;
ALTER TABLE `materias`
  ADD CONSTRAINT `materias_ibfk_1` FOREIGN KEY (`id_registro`) REFERENCES `leads` (`id_registro`) ON UPDATE CASCADE;
COMMIT;
