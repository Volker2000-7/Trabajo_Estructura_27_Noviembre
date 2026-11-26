# Trabajo_Estructura_27_Noviembre

Se decidió utilizar el algoritmo quick sort para el ordenamiento de pasajeros debido a su eficiencia de O(nlog n), esto permite ordenar grandes cantidades de registros con un número de operaciones considerablemente menor que otros algoritmos como bubble sort o selection sort. Otra opción a considerar fue heap sort, que garantiza el funcionamiento en O(nlog n) incluso en el peor de los casos, pero preferimos usar quick sort por la facilidad de implementación y la reutilización de la misma función para los 3 criterios de ordenamiento.

Para trabajar con nuestra estructura de datos basada en listas enlazadas, se realiza una conversión temporal a una lista de Python, permitiendo aplicar el algoritmo sin modificar el orden original de los registros almacenados.

Ocupamos listas enlazadas porque nos permiten ir agregando registros de las clases (clientes, buses, viajes y pasajes) de manera indefinida sin depender de un límite de tamaño fijo. Además, al cargar los datos en memoria al inicio, podemos recorrer y consultar toda la información mucho más rápido mediante punteros en lugar de tener que estar abriendo y leyendo los archivos .csv.

