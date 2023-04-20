-- SHOW ERRORS FUNCTION fu_buscar_notas_estudiante;
CREATE OR REPLACE FUNCTION fu_buscar_notas_estudiante(
	p_kcodest IN estudiante.k_codest%TYPE,
	p_kgrupo IN GRUPO.K_CODGRUPO%TYPE
) RETURN VARCHAR2
AS
	CURSOR c_notas_est IS
    SELECT en.K_NOTA ,en.V_NOTA  
		FROM ESTUDIANTE_NOTA en 
		WHERE K_CODEST = p_kcodest 
		AND K_CODGRUPO = p_kgrupo; 
  	lc_nota_est c_notas_est%ROWTYPE;
	l_fila_notas varchar(300);
BEGIN
	OPEN c_notas_est;
	LOOP
    	FETCH c_notas_est INTO lc_nota_est;
    	EXIT WHEN c_notas_est%NOTFOUND;
    	l_fila_notas := l_fila_notas || lc_nota_est.V_NOTA || '  |   ';
  END LOOP;
  CLOSE c_notas_est;
	RETURN l_fila_notas;
END fu_buscar_notas_estudiante;
/