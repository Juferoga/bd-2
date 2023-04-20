-- Habilitamos la salida por consola de la terminal
set serveroutput on
-- deshabilitamos la verificación
set verify off
-- Creamos nuestro bloque anonimo
SET LINESIZE 200;
DECLARE
  -- Declaramos las variables que vamos a utilizar
  l_kgrupo NUMBER := 5;
BEGIN
  -- Generamos la tabla con el procedimiento
  generar_tabla_con_k_codgrupo(l_kgrupo);
END;
/