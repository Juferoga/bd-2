-- Creación de función:
-- Se encarga de crear un encabezado a partir del parametro
--   parametros: (p_kgrupo) => referencia a la primary key del grupo
--   retorna:
--      PERIODO    : 2023-2
--      ASIGNATURA : BDI-GRUPO 82
--      DOCENTE    : Alba Consuelo Nieto

CREATE OR REPLACE FUNCTION  generar_encabezado_k_codgrupo (
    p_kgrupo in GRUPO.k_codgrupo%TYPE
  ) RETURN VARCHAR
AS
  -- Creación de VARIABLES LOCALES para el control de 
  --   funcionalidades dentro del procedimiento

  -- Variable para controlar la consulta del periodo consultado
  l_periodo_grupo varchar(50);
  -- Variable para controlar la consulta del nombre de la asignatura
  l_nombre_asignatura varchar(50);
  -- Variable para controlar el id de la asignatura
  l_kasignatura number;
  -- Variable para controlar el nombre del grupo
  l_ngrupo number;
  -- Variable para controlar el id del docente
  l_knit number;
  -- Variable para controlar el nombre del docente
  l_nnombre_docente varchar(50);
BEGIN
  -- Asignación de variable para el control de la identificación de la asignatura                         
  SELECT K_ASIGNATURA INTO l_kasignatura FROM GRUPO WHERE K_CODGRUPO=p_kgrupo;
  -- Asignación de variable para la impresión del nombre del grupo
  SELECT N_GRUPO INTO l_ngrupo FROM GRUPO WHERE K_CODGRUPO=p_kgrupo;
  -- Asignación de variable para el control del identificador del docente
  SELECT K_NIT INTO l_knit FROM GRUPO WHERE K_CODGRUPO=p_kgrupo;
  
  -- Consulta que retorna el año y periodo del grupo
  SELECT 'PERIODO   : ' || Q_ANIO || '-' || Q_PERIODO INTO l_periodo_grupo FROM GRUPO WHERE K_CODGRUPO=p_kgrupo;
  -- Consulta que retorna la asignatura del grupo
  SELECT 'ASIGNATURA: ' || N_NOMBRE INTO l_nombre_asignatura FROM ASIGNATURA WHERE K_ASIGNATURA = l_kasignatura;
  -- Consulta que retorna el docente de la asignatura del grupo
  SELECT 'DOCENTE   : ' || N_NOMBRE || ' ' || N_APELLIDO INTO l_nnombre_docente FROM DOCENTE WHERE K_NIT = l_knit;

  -- Retorno del encabezado en la función
  RETURN l_periodo_grupo || chr(10) || l_nombre_asignatura || '-Grupo' || l_ngrupo || chr(10) || l_nnombre_docente;

END generar_encabezado_k_codgrupo;
/