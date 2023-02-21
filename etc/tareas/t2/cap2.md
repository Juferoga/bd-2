## Capitulo 2

Modos tradicionales de expresar funcionalidad:
-	Especificaciones de Requerimientos
-	Descomposiciones Funcionales
-	Diagramas de Flujo de Datos (DFD)
-	Diagramas de Entidad-Relación (ERD)

El enfoque de descomposición funcional está basado en "dividir y conquistar", pero no es lo más recomendable ya que está estrechamente relacionado al desarrollo de sistemas estructurados, por lo que no es utilizable para una aplicación web u orientada a objetos; y además porque se puede perder la conexión con las clases u objetos que previamente fueron entidades; y también porque no es capaz de manejar la complejidad contemporánea de los SI actuales.

Los DFD representan la visión dinámica del sistema. Estos diagramas son usados por personas técnicas, ya que contienen detalles que los usuarios muchas veces no entienden. Además, estos diagramas se pueden usar en diseño para sistemas que no sean orientados a objetos. Estos diagramas se pueden sustituir por casos de uso y diagramas de clases, secuencias, estados y actividades. 

Los ERD muestran cómo se almacenan los datos en una aplicación. También se puede utilizar para representar un modelo lógico de datos y la estructura de una BD relacional. Estos diagramas no muestran la interacción dinámica, por lo que siempre deben utilizarse junto con los DFD para mostrar la imagen completa a los usuarios. Estos diagramas no aportan mucho significado a los usuarios, por lo que pueden ser necesarios si se desea crear un modelo lógico una vez recopilado los requisitos del sistema.

Los prototipos ofrecen a los usuarios una demostración realista de lo que un sistema será capaz de hacer cuando esté terminado. Se centran en la UI y omiten la codificación de fondo. Algunos problemas son el entusiasmo y la impaciencia de algunos usuarios, y la codificación rápida y sucia que puede haber en un equipo de trabajo. Los prototipos deberían usarse para respaldar los casos de uso y el catálogo de reglas de negocio.

Hace falta un nuevo medio entre usuarios y diseñadores de sistemas.


### 2.1
Los diagramas deben concentrarse en los requisitos del sistema desde la perspectiva de los usuarios.
La perspectiva de la aplicación debería ocuparse únicamente de lo que entra y lo que sale, por lo que esto tiene más relevancia para los usuarios que la estudian.
Las interacciones entre los usuarios y el sistema informático son lo que realmente importa en la recopilación de requisitos.
Hay tendencia en entrar primero al cómo antes de definir el qué.
Los casos de uso son una herramienta que puede mostrar exclusivamente el qué.
Ivar Jacobson (1992) y su equipo de Ericsson (Suecia) introdujeron los casos de uso en el mundo de la informática.

### 2.2
Los casos de uso forman parte de UML, que nació en enero de 1997.
UML no es una metodología, si no un lenguaje. 
Proporciona la nomenclatura de los diagramas y especificaciones que se producen. 
Una metodología, por el contrario, consiste en una guía paso a paso para construir un sistema. 
UML no depende de una metodología, ni la metodología tiene por qué depender del UML. UML nació de la colaboración de Grady Booch, James Rumbaugh e Ivar Jacobson (1999). Gracias a sus esfuerzos, la industria informática dispone de un lenguaje común, o notación, con el que especificar los sistemas orientados a objetos.
#### UML está compuesto por 9 diagramas:
-	Diagramas de Casos de Uso
-	Diagramas de Secuencia
-	Diagramas de Colaboración
-	Diagramas de Estados
-	Diagramas de Actividades
-	Diagramas de Clases
-	Diagramas de Objetos
-	Diagramas de Componentes
-	Diagramas de Despliegue

Estos diagramas pueden transmitir todas las vistas necesarias de un sistema informático y pueden servir de base para construir, configurar e implantar el sistema. UML ofrece muchas posibilidades para generar código a partir de la documentación de diseño y para la ingeniería inversa.

- **Casos de Uso:** Constituyen la base de cómo interactúa el sistema con las fuerzas externas que lo rodean. Usuarios/Actores, otros sistemas y otros factores. Representaciones gráficas de las relaciones entre actores y casos de uso, y un caso de uso con otros casos de uso. Impulsan todo el ciclo de desarrollo de software.

- Secuencia y Colaboración: Muestran el funcionamiento interno de un escenario de caso de uso. Visión dinámica del sistema. Los diagramas de secuencia están orientados a interacciones simples y lineales, mientras que los diagramas de colaboración están orientados a interacciones más complejas, como la mensajería multihilo o condicional.

- **Clases:** Visión estática. Muestra cómo se construyen las clases y sus relaciones. El diagrama de objetos se centra en las ejemplificaciones de las clases en tiempo de ejecución.

- **Componentes:** Ayudan a que el sistema pase de ser una colección de objetos de grano fino a una colección de componentes de grano grueso, y muestran sus relaciones.

- **Despliegue:** Muestra cómo se van a desplegar los componentes del sistema en nodos físicos o máquinas, del entorno de producción.

- **Paquetes:** Ocultan la complejidad del sistema.

Los estereotipos permiten ampliar el UML para representar nuevos tipos de abstracciones o conceptos. Personalización.

### 2.3
Vista clásica (subsistemas que la componen) y romántica (las cosas que una persona puede hacer con ella).
Los casos de uso ven el sistema desde el punto de vista romántico. Solo se preocupan por lo que el sistema puede hacer por los usuarios. Esto los hace extremadamente eficaces para transmitir información a los usuarios, ya que eliminan todos los puntos de vista clásicos y reducen los requisitos a lo esencial.

	- Los casos de uso pretenden mostrar las interacciones entre el sistema y las entidades externas al sistema (actores).
	- Los casos de uso son representaciones de caja negra, por lo que no incluyen ningún lenguaje específico de implementación. Hay que tener cuidado de no definir personas o departamentos concretos, widgets de UI, pseudocódigo, etc. Los casos de uso libres de contexto son los que no tienen referencia de implementación.
	- Los casos de uso, a medida que se avanza en la recopilación de requisitos, pasan de ser generales a ser detallados.
	Debbie Ard ha decidido que cada aplicación razonablemente grande parece tener 28 casos de uso. Es indispensable reducir el número de casos de uso al mínimo. Los escenarios son instancias individuales de casos de uso que recorren un camino específico utilizando datos específicos.

Los casos de uso inician por las interacciones con el actor.
Se deben mostrar los actores secundarios en los diagramas de casos de uso cuando las acciones específicas del actor secundario tengan un efecto en las respuestas que proporciona la aplicación.
Los nombres de rol son útiles cuando la asociación entre un actor y un caso de uso necesita información más allá del hecho de que interactúan.

#### Asociaciones:
	- **Generalización**
	- **Extiende:** Amplía un caso de uso original.
	- **Incluye:** Evitar la duplicación de pasos en múltiples casos de uso. Reutilización.

Los escenarios son instancias de casos de uso (con datos de producción) que prueban de forma efectiva una ruta a través de un caso de uso.
Un escenario se puede utilizar en:
	- Durante la actividad de requisitos para proporcionar información inmediata a los usuarios y analistas sobre si los casos de uso reflejan fielmente las necesidades de los usuarios.
	- Durante la actividad de prueba para comprobar si el SI refleja los requisitos.

### 2.4
Aplicaciones
  -	Sistemas Transaccionales
  -	Sistemas de Consulta
  -	Solicitudes de Respuesta (Request for Proposals)
  -	Software Package Evolution
  -	Sistemas no Orientados a Objetos