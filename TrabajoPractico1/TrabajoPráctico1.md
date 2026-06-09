## Fundamentos de Informática - Informática I  FRCon Año 2026 

## Trabajo Práctico Nº 1 

## Programación en Python 

**Parte 1:** _Aplicación en problemas matemáticos._ 

## **Ejercicio 1.1:** Dado el conjunto: _**A= ( 0,1 ) U ( 2,3 )**_ 

Diseñar un script que: 

- Solicite al usuario un número real _x_ . 

- Determine si dicho valor pertenece al conjunto _A_ . 

- Muestre un mensaje indicando si pertenece o no al conjunto. 

## **Ejercicio 1.2:** Dado el conjunto: _**A= ( 0,1 ) U ( 2,3 )**_ 

Diseñar un script que: 

- Solicite al usuario que ingrese siete valores de un número real _x_ . 

- Determine para cada valor si pertenece al conjunto _A_ . 

- Muestre un mensaje indicando si pertenece o no al conjunto. 

- Cuente cuántos valores de _x_ pertenecen al conjunto _A_ y cuántos no. 

- Calcule el promedio de los valores de _x_ que pertenecen al conjunto _A_ . 

- Calcule el promedio de los valores de _x_ que no pertenecen al conjunto _A_ . 

- Calcule el promedio de los valores de _x_ ingresados. 

## **Ejercicio 1.3:** Dado el conjunto: _**A= ( 0,1 ) U ( 2,3 )**_ 

Diseñar un script que: 

- Solicite al usuario que ingrese valores de un número real _x_ . 

- Finalizar el ingreso de valores de _x_ cuando el usuario escriba -1. 

- Determine para cada valor si pertenece al conjunto _A_ . 

- Muestre un mensaje indicando si pertenece o no al conjunto. 

- Cuente valores de _x_ pertenecen al conjunto _A_ y cuántos no. 

- Calcule el promedio de los valores de _x_ que pertenecen al conjunto _A_ . 

- Calcule el promedio de los valores de _x_ que no pertenecen al conjunto _A_ . 

- Calcule el promedio de los valores de _x_ ingresados. 

**Ejercicio 1.4:** Dado el conjunto: _**A = (0,4) U {7}**_ Diseñar un script para: 

- Ingresar un valor real _x_ . 

- Determinar si _x_ pertenece al conjunto _A_ . 

- Determinar si _x_ es punto de acumulación de _A_ . 

- Mostrar el resultado como salida. 

## **Ejercicio 1.5:** Dado el conjunto: _**A= (0, 3)**_ 

## Diseñar un script para: 

- Evaluar valores desde -1 hasta 4. 

- Para cada valor, indicar si pertenece al conjunto. 

- Mostrar en pantalla los valores pertenecientes al conjunto. 



## **Ejercicio 1.6:** Diseñar un script para: 

- Solicitar al usuario que ingrese los extremos inferior y superior de un intervalo. 

- Construir el conjunto: _A_ =( _a,b_ ) donde: _a_ es el extremo inferior y _b_ es el extremo superior. 

- Solicitar al usuario un valor inicial y un valor final para la evaluación de los valores de _x ._ 

- Evaluar los valores comprendidos entre un valor inicial y un valor final ingresados por el usuario. 

- Para cada valor, indicar si pertenece al conjunto. 

- Mostrar en pantalla los valores pertenecientes al conjunto. 

## **Ejercicio 1.7:** Diseñar un script para: 

- Solicitar al usuario que ingrese los extremos inferior y superior de un intervalo. 

- Construir el conjunto: _A_ =( _a,b_ ) donde: _a_ es el extremo inferior y _b_ es el extremo superior. 

- Validar el ingreso de datos, asegurando que: 

   - _a_ y _b_ sean números reales. 

   - _a_ < _b_ , en caso contrario, volver a solicitar los valores. 

- Solicitar al usuario un valor inicial y un valor final para la evaluación de los valores de _x_ 

- Validar el ingreso de los límites de evaluación, asegurando que: 

   - sean números enteros, 

 el valor inicial sea menor o igual al valor final. 

- Evaluar los valores comprendidos entre el valor inicial y un valor final ingresados por el usuario. 

- Para cada valor, indicar si pertenece al conjunto. 

- Mostrar en pantalla los valores pertenecientes al conjunto. 





## **Parte 2:** _Aplicación en problema de ingeniería_ . 

## **Tema:** Evaluación del desempeño global de un sistema ingenieril. 

## **Marco conceptual:** 

Un sistema ingenieril es un conjunto de elementos que trabajan juntos para cumplir un objetivo específico dentro de un contexto de ingeniería. 

Ese sistema puede ser físico, matemático o computacional, pero siempre tiene: 

- **Entradas** (lo que recibe). 

- **Procesos** (lo que transforma). 

- **Salidas** (lo que produce). 

En distintas disciplinas de la ingeniería es necesario evaluar el comportamiento global de un sistema compuesto por múltiples etapas o componentes. 

Estos sistemas se caracterizan por integrar rendimientos, pérdidas y consumos en cada una de las etapas del proceso. Para su mejor comprensión, se presenta el siguiente ejemplo aplicado a un sistema de producción de piezas metálicas. 

Una fábrica produce piezas metálicas pasando por tres etapas: 

1. Corte del material . 

2. Moldeado. 

3. Pulido final. 

En cada etapa se observa: 

- Rendimiento: lo que realmente se aprovecha del proceso. 

- Pérdidas: material o energía desperdiciada. 

- Consumo: recursos usados (energía, tiempo o materiales). 

El comportamiento global de un sistema puede evaluarse mediante un modelo simplificado. Bajo este enfoque, se propone el siguiente índice matemático de desempeño. 


$$
I = \frac{\sum_{i=1}^{n} \big((e - p)_i\big)}{\sum_{i=1}^{n} \big(1 + c_i\big)}
$$



- _I_ : índice de desempeño del sistema 

- _n_ : número de etapas, niveles o ciclos del sistema 

- _e_ : eficiencia promedio del sistema (producción, energía o resistencia útil) 

- _p_ : pérdidas del sistema (energía, material o tiempo) 

- _ci_ : costo, carga o consumo en la etapa _i_ 

**Problema 2.1:** Una empresa de ingeniería desea analizar el desempeño global de un sistema compuesto por varias etapas operativas. Cada etapa presenta un consumo asociado, mientras que el sistema en su conjunto tiene un nivel de eficiencia y pérdidas promedio. 

Se solicita desarrollar un script en Python que permita: 

1. Ingresar la cantidad de etapas del sistema _n_ . 

2. Ingresar los valores de eficiencia _e_ y pérdidas _p_ 

3. Ingresar los valores de carga _ci_ para cada etapa. 

4. Determinar el índice global de desempeño _I_ . 

5. Mostrar el resultado final por pantalla. 

6. Graficar _I_ vs _n_ . 

**Problema 2.2:** Modificar el script del problema 2.1 utilizando la estructura de datos tipo lista. Los valores de carga _ci_ deberán ser ingresados y almacenados en una lista para su posterior procesamiento. 

## **Problema 2.3:** _Aplicación del problema de la parte 2 por carreras_ . 

El modelo matemático presentado conceptualmente debe ser aplicado por especialidad. A continuación, se presenta su aplicación en las tres disciplinas de las ingenierías del curso: 

**Ingeniería Civil:** análisis de estabilidad de edificios por niveles. 

En ingeniería civil, el modelo permite evaluar la estabilidad de una estructura compuesta por varios niveles, considerando el comportamiento de carga y resistencia del material. Variables del modelo: 

- _e_ : resistencia efectiva del material 

- _p_ : pérdidas por deformación o fisuras 

- _ci_ : carga por nivel estructural 

Como aplicación, se analiza el desempeño global de edificaciones o estructuras sometidas a cargas progresivas 

**Ingeniería Eléctrica:** evaluación de la eficiencia de un sistema eléctrico. 

Se utiliza para evaluar la eficiencia global de un sistema de transmisión o distribución de energía, considerando las pérdidas asociadas al transporte eléctrico. 

Variables del modelo: 

- _e_ : energía útil entregada 

- _p_ : pérdidas por resistencia eléctrica 

- _ci_ : consumo por etapa o circuito 

Como aplicación, se estima el rendimiento energético del sistema bajo distintas condiciones de operación. 

**Ingeniería Industrial:** medición del rendimiento global de una línea de producción. 

Se aplica al análisis del rendimiento global de una línea de producción compuesta por varias estaciones de trabajo. 

- _e_ : producción efectiva del sistema. 

- _p_ : desperdicio o nivel de defectos. 

- _ci_ : carga operativa o costo asociado a cada estación, 

Como aplicación, se evalúa la eficiencia del proceso productivo y la distribución de recursos en la línea de trabajo. 

Cada estudiante deberá desarrollar un script de programación que permita calcular el índice de desempeño del sistema, de acuerdo con la carrera que esté cursando, considerando la interpretación correspondiente de las variables del modelo. 

El programa debe: 

- Solicitar los datos de entrada correspondientes ( _n_ , _e_ , _p_ y _ci_ ). 

- Realizar el cálculo del índice de desempeño. 

- Mostrar el resultado final 

- Diseñar distintas salidas gráficas. 

Realizar el análisis e interpretación del dato resultante y las gráficas obtenidas. 



