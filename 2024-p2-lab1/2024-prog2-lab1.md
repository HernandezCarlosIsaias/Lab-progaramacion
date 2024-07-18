# Proyecto de Programación - Sistema de Gestión de Tareas Pendientes

**Materia:** Programación 2

## Objetivos del proyecto:
- Reforzar los conceptos de programación orientada a objetos, y estructuras de datos lineales, en particular listas enlazadas.
- Practicar el uso de la noción de orden y análisis de algoritmos , en este caso en listas enlazadas.
- Fomentar el trabajo en equipo y la colaboración entre estudiantes mediante aprendizaje basado en proyectos

## Contenidos que se ejercitan:
- Programación orientada a objetos (POO).
- Análisis de algoritmos y notación asintótica.
- Implementación y manejo de estructuras de datos (listas enlazadas).
- Entrada y salida de datos.
- Comentarios y documentación del código.
- Validacion, verificacion y testing

# Consigna de trabajo:
Se les entregará dos archivos tareas.py y tareas.csv que un sistema de gestión de tareas pendientes (un todo list) que permita a los usuarios agregar, eliminar y marcar tareas como completadas. Además, el sistema debe ofrecer funcionalidades adicionales como la priorización de tareas, la organización por categorías y la generación de informes sobre el progreso. Los estudiantes deberán completar y mejorar el código según las siguientes instrucciones:

## Tareas del proyecto

1. **Comentar el código:** Cada línea de código debe estar comentada explicando su función y cómo contribuye al funcionamiento del programa.

2. **Comprender de una estructura de datos:** Esta estructura de datos ya se encuentra funcionando, deberán leerla, entenderla y explicarla en un informe (ver mas abajo la estructura del informe)
   - Utilizar una lista enlazada ordenada para almacenar las tareas pendientes.
   
3. **Agregar validaciones:** Deberán agregar validaciones para el correcto funcionamiento del programa # PREGUNTARRRRRRRRR
   - * Verificar si la tarea ya existe antes de agregarla.
   - * Mostrar un mensaje de error si se intenta eliminar o marcar una tarea que no existe. 
   - * Incorpore otras validaciones que consideren necesarias. 

4. **Funciones básicas del sistema:**
    De las siguientes funcionalidades, implemente las que estan marcadas con asterisco.
   - Agregar una nueva tarea.
   - * Marcar una tarea como completada.
   - Eliminar una tarea existente.
   - Mostrar todas las tareas.
   - * Mostrar tareas pendientes.
   - * Buscar una tarea por su descripcion (busca si existe una tarea con una descripción, esto sirve para chequear si existe antes de crearla)

5. **Características avanzadas:**
    De las siguientes funcionalidades, implemente las que estan marcadas con asterisco.
   - Priorizar tareas según su importancia.
   - Mostrar las tareas de una categorías indicada por el usuario. *
   - * Mostrar tareas por descripcion. Toma un texto y muestra todas las tareas que tengan ese texto en la descripcion. 
   - Generar informes sobre el progreso de las tareas, incluyendo el número de tareas completadas y las próximas a vencer por cada categoría. (una de las funciones a implementar es  numero_tareas_pendientes_lineal) * 

6. **Análisis y optimización:**
   - Calcule el orden del metodo agregar_tarea utilizando notación asintótica para evaluar la eficiencia de las funciones implementadas.
   - Para el módulo de estadísticas del TODO list implementó numero_tareas_pendientes_lineal que es de orden lineal, modifique la clase y cree el método numero_tareas_pendientes_cte, que devuelva la cantidad de tareas pendientes  cuyo orden sea contante. Calcule el orden de la funcion para mostrar que es constante

**Nota**: Puede ser que necesiten implementar otros metodos ademas de los mencionados para cumplir con la tarea, por ejemplo buscar_tarea_id(), o contar_tareas, o contar tareas por categoria, les doy libertad en ese sentido.

# Entregables:
   - Código fuente comentado
   - Informe de análisis de algoritmos y optimización segun la estructura de informe
   - Planilla de autoevaluación completada (ver modelo mas abajo).

## Criterios de evaluación:
- Trabajo grupal, segun la tabla de autoevaluacion (disponible al final)
- Trabajo en git, se mirará los commits de cada uno de los participantes del grupo
- Correcta implementación de las funcionalidades básicas y avanzadas.
- Claridad y calidad de los comentarios y la documentación del código.
- Calidad y claridad del informe de análisis de algoritmos y optimización.
- Trabajo en equipo y colaboración efectiva entre los miembros del grupo.

Este proyecto se realizará en grupos de tres estudiantes y se evaluará según los criterios mencionados anteriormente.

## Estructura del informe

Informe del Proyecto: Sistema de Gestión de Tareas Pendientes
1. Introducción

    Breve descripción del proyecto y su importancia.
    Objetivos del proyecto y qué se espera lograr con la implementación del sistema.

2. Descripción del Sistema

    Funcionalidades Implementadas:
        Lista y descripción de las funcionalidades básicas y avanzadas desarrolladas.
    Estructuras de Datos Utilizadas:
        Explicación de la implementación de la lista enlazada y nodos en el sistema.

3. Metodología y Diseño
    Diseño del Código:
        Descripción concisa de las clases principales (Tarea, Nodo, ListaEnlazada) y su interacción.

4. Implementación y Ejemplos

    Detalles de Implementación:
        Explicación breve de cómo se implementaron las funcionalidades principales.
    Casos de Uso y Ejemplos:
        Ejemplos de ejecución del sistema para diferentes escenarios de uso.

5. Preguntas Conceptuales

    Preguntas para Análisis:
        ¿Qué sucede si intentamos agregar una tarea que ya existe en la lista?
        ¿Cómo se implementa la priorización de tareas en la lista enlazada? ¿Qué sucede si dos tareas tienen la misma prioridad?
        ¿Cuál es la complejidad temporal del método para eliminar una tarea de la lista enlazada?
        ¿Cómo podríamos modificar el sistema para soportar múltiples categorías por tarea?

6. Resultados y Conclusiones

    Resultados Obtenidos:
        Evaluación del éxito en la implementación de las funcionalidades.
    Conclusiones:
        Resumen de los hallazgos y reflexiones sobre lecciones aprendidas y mejoras futuras.

7. Referencias

    Lista de referencias utilizadas para la implementación y desarrollo del sistema.

Apéndices

    Código fuente comentado (si es necesario).
    Ejemplos adicionales de ejecución o casos de prueba.


## Planilla de Autoevaluación

## Planilla de Autoevaluación

| Tarea                                            | Responsable(s)              | Valoración                                                                                                                                  |
|--------------------------------------------------|-----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| Comentar el código                               | Ana, Juan                   | Ana y Juan trabajaron juntos para comentar el código. Ana se encargó de comentar las funciones principales, asegurando que cada una tuviera una explicación clara y concisa. Juan se enfocó en los detalles dentro de las funciones, pero omitió algunos comentarios en secciones menores. En conjunto, lograron una documentación bastante completa. |
| Entender y explicar la estructura de datos       | Pedro, Ana                  | Pedro lideró la explicación de la estructura de datos en el informe, brindando una visión clara y detallada del funcionamiento de las listas enlazadas. Ana contribuyó con ejemplos visuales y diagramas que ayudaron a ilustrar el funcionamiento interno de la estructura. Juntos, proporcionaron una explicación integral y comprensible. |
| Agregar validaciones                             | Juan, Ana                   | Juan implementó las validaciones básicas para asegurar que las tareas no se duplicaran y que no se intentara eliminar tareas inexistentes. Ana añadió mensajes de error detallados y mejoró la lógica de validación. Aunque encontraron algunos problemas iniciales, lograron resolverlos colaborativamente. |
| Implementar marcar tarea como completada         | Pedro                       | Pedro implementó esta funcionalidad y se aseguró de que las tareas se actualizaran correctamente en el sistema. Además, añadió pruebas para verificar su funcionamiento. |
| Implementar mostrar tareas pendientes            | Ana                         | Ana desarrolló esta funcionalidad y añadió una opción para filtrar por prioridad, lo que mejoró la eficiencia en la visualización de las tareas más urgentes. |
| Implementar buscar tarea por descripción         | Juan                        | Juan implementó la funcionalidad de búsqueda, permitiendo a los usuarios encontrar tareas rápidamente. Aunque la búsqueda funcionaba bien, se discutieron mejoras para optimizar su eficiencia. |
| Implementar mostrar tareas por descripción       | Pedro                       | Pedro extendió la funcionalidad de búsqueda para mostrar todas las tareas que contenían un texto específico en su descripción, asegurándose de manejar correctamente los casos de error. |
| Generar informes de progreso                     | Ana, Juan                   | Ana y Juan colaboraron en la generación de informes. Ana diseñó el formato del informe, mientras que Juan implementó la lógica para generar los datos. Ambos se aseguraron de que los informes fueran claros y útiles para los usuarios. |
| Calcular orden del método agregar_tarea          | Pedro                       | Pedro realizó un análisis detallado de la complejidad temporal del método `agregar_tarea`, explicando claramente cómo se alcanzó la eficiencia actual y sugiriendo posibles mejoras. |
| Implementar contar_tareas_pendientes_cte         | Ana, Pedro                  | Ana y Pedro trabajaron juntos en esta implementación. Ana propuso la lógica inicial y Pedro optimizó el código para asegurar que la complejidad temporal fuera constante. |
| Documentar el código fuente                      | Juan, Ana                   | Juan y Ana colaboraron para documentar el código fuente. Juan se encargó de la documentación técnica detallada, mientras que Ana se aseguró de que los comentarios fueran claros y accesibles para otros desarrolladores. |
| Redactar el informe de análisis de algoritmos    | Pedro, Ana                  | Pedro escribió la mayor parte del informe, detallando el análisis de algoritmos y optimización. Ana revisó el informe y añadió ejemplos prácticos para ilustrar los conceptos. |
| Trabajar en equipo y colaborar efectivamente     | Ana, Juan, Pedro            | Todos los miembros del equipo trabajaron en estrecha colaboración, organizando reuniones regulares para discutir el progreso y resolver problemas. Se apoyaron mutuamente y compartieron responsabilidades de manera equitativa. |
| Resolución de conflictos y gestión del tiempo    | Ana, Juan, Pedro            | El equipo enfrentó algunos conflictos de horario, pero lograron resolverlos mediante una mejor planificación y comunicación. Ana propuso una herramienta de gestión de tareas que mejoró la organización del equipo. |
| Presentación final del proyecto                  | Ana, Juan, Pedro            | La presentación final fue realizada por todo el equipo. Ana se encargó de la introducción, Juan presentó la parte técnica y Pedro concluyó con los resultados y conclusiones. Recibieron buenos comentarios por su claridad y cohesión. |
| Revisión final y entrega                         | Ana, Juan, Pedro            | Antes de la entrega, todo el equipo revisó el proyecto para asegurarse de que todos los requisitos se cumplieran y que no hubiera errores. Ajustaron detalles finales y realizaron pruebas adicionales. |
| Colaboración y trabajo en equipo                 | Ana, Juan, Pedro            | La colaboración fue excelente, con todos los miembros contribuyendo activamente y apoyándose mutuamente. Mantuvieron una comunicación abierta y resolvieron problemas juntos. |
| Gestión del tiempo                               | Ana, Juan, Pedro            | Aunque enfrentaron algunos desafíos con el tiempo, mejoraron su gestión a lo largo del proyecto mediante la planificación semanal y el uso de herramientas de seguimiento de tareas. |
| Evaluación de la calidad del código              | Ana, Juan, Pedro            | El equipo se centró en mantener un alto estándar de calidad del código, realizando revisiones de código entre pares y asegurando que todos los métodos estuvieran bien documentados y optimizados. |
