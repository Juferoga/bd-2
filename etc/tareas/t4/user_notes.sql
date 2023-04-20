-- Creación de procedimiento:
-- Se encarga de crear una tabla a partir del parametro
--   parametros: (p_kgrupo) => referencia a la primary key del grupo
--   retorna:
--      ::: [ Encabezado ] :::
--      PERIODO    : 2023-2
--      ASIGNATURA : BDI-GRUPO 82
--      DOCENTE    : Alba Consuelo Nieto
--      ::: [ FIN Encabezado ] :::
--      ::: [ Tabla ] :::
--      +----------------------------------+---------+--------+-------+-------+
--      |      Tabla calificaciones        |  Nota1  | Nota2  | Nota3 |   EF  | 
--      +----------------------------------+---------+--------+-------+-------+
--      |              Nombre              |   20%   |   20%  |  20%  |  40%  |
--      +----------------------------------+---------+------------------------+
--      | Nauj Epilef                      |   3.5   |   4.5  |  5.0  |  4.3  |
--      | Nauj Epilef                      |   3.5   |   4.5  |  5.0  |  4.3  |
--      | Nauj Epilef                      |   3.5   |   4.5  |  5.0  |  4.3  |
--      +----------------------------------+---------+------------------------+
--      ::: [ FIN Tabla ] :::

CREATE OR REPLACE PROCEDURE generar_tabla_con_k_codgrupo (
    p_kgrupo in GRUPO.k_codgrupo%TYPE
  )
AS
  
BEGIN
  -- Generación de encabezado dinámico :)
  dbms_output.put_line(generar_encabezado_k_codgrupo(p_kgrupo));
  -- Creación de tabla
  dbms_output.put_line(generar_tabla_k_codgrupo_k_codest(p_kgrupo));
END generar_tabla_con_k_codgrupo;
/