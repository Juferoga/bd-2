CREATE OR REPLACE FUNCTION fu_buscar_estudiante(
	p_kcodest IN estudiante.k_codest%TYPE,
	pc_error OUT NUMBER,
	pm_error OUT VARCHAR2
) RETURN VARCHAR2
AS
	l_nombre VARCHAR2(50);
BEGIN
	dbms_output.put_line('Ejecutando funcion');
	pc_error := 0;
	pm_error := '';
	
	SELECT n_nombre || ' ' || n_apellido INTO l_nombre FROM estudiante WHERE k_codest = p_kcodest;
	
	RETURN l_nombre;
	
EXCEPTION
	WHEN OTHERS THEN
		pc_error := 1;
		pm_error := 'Ocurrio un error: ' || SQLERRM;
		RETURN 'ERROR';
END fu_buscar_estudiante;
/