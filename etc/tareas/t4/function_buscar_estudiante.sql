CREATE OR REPLACE FUNCTION fu_buscar_estudiante(
	p_kcodest IN estudiante.k_codest%TYPE
) RETURN VARCHAR2
AS
	l_nombre VARCHAR2(50);
BEGIN	

	SELECT n_nombre || ' ' || n_apellido 
	INTO l_nombre 
	FROM estudiante 
	WHERE k_codest = p_kcodest;

	RETURN l_nombre;
END fu_buscar_estudiante;
/