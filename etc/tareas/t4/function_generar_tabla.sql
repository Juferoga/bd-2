-- Creación de función:
-- Se encarga de crear una tabla a partir del parametro
--   parametros: (p_kgrupo) => referencia a la primary key del grupo
--   retorna:
--      +----------------------------------+---------+--------+-------+-------+
--      |      Tabla calificaciones        |  Nota1  | Nota2  | Nota3 |   EF  | 
--      +----------------------------------+---------+--------+-------+-------+
--      |              Nombre              |   20%   |   20%  |  20%  |  40%  |
--      +----------------------------------+---------+------------------------+
--      | Nauj Epilef                      |   3.5   |   4.5  |  5.0  |  4.3  |
--      | Nauj Epilef                      |   3.5   |   4.5  |  5.0  |  4.3  |
--      | Nauj Epilef                      |   3.5   |   4.5  |  5.0  |  4.3  |
--      +----------------------------------+---------+------------------------+
-- SHOW ERRORS FUNCTION  generar_tabla_k_codgrupo_k_codest;
CREATE OR REPLACE FUNCTION  generar_tabla_k_codgrupo_k_codest (
    p_kgrupo in GRUPO.k_codgrupo%TYPE
  ) RETURN VARCHAR
AS
  l_encabezado_tabla varchar(300);
  CURSOR c_notas IS 
    SELECT DISTINCT n.K_NOTA, n.V_PORCENTAJE
    FROM GRUPO g, ESTUDIANTE_GRUPO eg, ESTUDIANTE_NOTA en, NOTA n
    WHERE g.K_CODGRUPO = eg.K_CODGRUPO
    AND eg.K_CODEST = en.K_CODEST
    AND en.K_NOTA = n.K_NOTA
    AND g.K_CODGRUPO = p_kgrupo
    AND n.K_CODGRUPO = p_kgrupo
    ORDER BY n.V_PORCENTAJE;
  lc_nota c_notas%ROWTYPE;

  CURSOR c_cod_ests IS
    SELECT eg.K_CODEST  
    FROM ESTUDIANTE_GRUPO eg , GRUPO g, ESTUDIANTE e  
    WHERE g.K_CODGRUPO = eg.K_CODGRUPO 
    AND g.K_CODGRUPO = p_kgrupo
    AND e.K_CODEST = eg.K_CODEST 
    ORDER BY e.N_NOMBRE ;
  lc_cod_est c_cod_ests%ROWTYPE;

  l_linea varchar(300);
  l_fila_notas varchar(300);
  l_fila_porcentajes varchar(300);
  l_fila_notas_estudiante varchar(300);
BEGIN
  l_linea :=            '+----------------+------+------+------+------+';
  l_fila_notas       := '| Calificaciones | ';
  l_fila_porcentajes := '|    Nombre      |';
  OPEN c_notas;
  LOOP
    FETCH c_notas INTO lc_nota;
    EXIT WHEN c_notas%NOTFOUND;
    l_fila_notas := l_fila_notas ||'    '|| lc_nota.k_nota ||'  |';
    l_fila_porcentajes := l_fila_porcentajes ||'   '|| (lc_nota.V_PORCENTAJE*100) ||'%  |';
  END LOOP;
  CLOSE c_notas;

  OPEN c_cod_ests;
  LOOP
    FETCH c_cod_ests INTO lc_cod_est;
    EXIT WHEN c_cod_ests%NOTFOUND;
    -- construir filas por estudiante
    l_fila_notas_estudiante := l_fila_notas_estudiante || fu_buscar_estudiante(lc_cod_est.k_codest) || ' - ' || fu_buscar_notas_estudiante(lc_cod_est.k_codest, p_kgrupo);
    l_fila_notas_estudiante := l_fila_notas_estudiante || chr(10);
  END LOOP;
  CLOSE c_cod_ests;

  -- Retorno de la tabla en la función
  RETURN l_linea || chr(10) || l_fila_notas || chr(10) || l_fila_porcentajes || chr(10) || l_linea || chr(10) || l_fila_notas_estudiante || chr(10);
END generar_tabla_k_codgrupo_k_codest;
/