# Tarea 1: DCCasino :school_satchel:

## Consideraciones generales :octocat:
Las probabilidades no suelen ser tan altas con lo pedido en el enunciado, es por eso que modifiqué un poco la fórmula para que haya más chance de ganar/perder en un juego.

### Cosas implementadas y no implementadas :white_check_mark: :x:

#### Programación Orientada a Objetos: 38 pts (28%)
##### ❌  Diagrama
##### ✅ Definición de clases, atributos, métodos y properties
Se crean las clases pedidas, con capas de abstracción (clase Menu, clase Jugador) y properties (getters y setters). Además de las clases pedidas, se crea Menu y derivados.

##### ✅ Relaciones entre clases
Existe una relación de composición entre la clase Casino y el conjunto de clases (Juego, Jugador, Bebestible), y entre Juego y Jugador. También hay una relación de agregación entre Menu y Casino. Por último, hay herencia simple y múltiple en las clases Jugador, Bebestible y Menu (revisar archivos correspondientes).

#### Simulaciones: 10 pts (7%)
##### ✅ Crear partida
Se despliega el menú de inicio con los distintos usuarios a elegir como opción. Luego, se setea al usuario dentro del casino con la opción elegida. Se pasa al menú principal.

#### Acciones: 35 pts (26%)
##### ✅ Jugador
Se crean distintas clases dependiendo del tipo de jugador (Ludopata, Casual, etc), los cuales implementan un mismo método: ```accion_especial``` (se usa polimorfismo). Cada acción actúa según lo pedido en el enunciado.

Además, se cuenta con el método ```apostar```, que realiza una apuesta dentro del juego, y puede doblarse o perderse el monto total dependiendo de una cierta probabilidad.

##### ✅ Juego
Entrega los resultados finales del juego, modificando las características del jugador en cuestión según lo pedido.

##### ✅ Bebestible
Se crean distintas clases dependiendo del tipo de jugador (Ludopata, Casual, etc), los cuales implementan un mismo método: ```consumir``` (se usa polimorfismo). Cada acción actúa según lo pedido en el enunciado, modificando las características del jugador cuando el bebestible es consumido. 

##### ✅ Casino
Al instanciar la clase Casino, se setean todos los juegos, jugadores y bebestibles en atributos de la clase. Al llamar al método ```jugar```, se procede a jugar el juego elegido, interactuando con la clase Juego y Jugador, y los métodos ```entregar_resultados``` y ```apostar```, respectivamente.

Además, se implementa el método ```evento_especial```, que da un bebestible gratis al jugador después de cada apuesta si se cumple cierta probabilidad.

#### Consola: 41 pts (30%)
##### ✅ Menú de Inicio
Se despliega lo pedido correctamente.

##### ✅ Opciones de jugador
Se despliega lo pedido correctamente.

##### ✅ Menú principal
Se despliega lo pedido correctamente.

##### ✅ Opciones de juegos
Se despliega lo pedido correctamente.

##### ✅ Carta de bebestibles
Se despliega lo pedido correctamente.

##### ✅ Ver estado del Jugador
Se despliega lo pedido correctamente.

##### ✅ Robustez
La clase Menu cuenta con un atributo ```opciones```, el cual es un diccionario que guarda las opciones disponibles para elegir. Además cuenta con el método ```validar_opcion```, el cual pide el input y lo busca dentro de las keys de ```opciones```; si no se encuentra, se muestra un mensaje de error, y se pide otro input.

De esta manera, en cada (sub)menú se hace un buen filtro de las opciones a elegir.

#### Manejo de archivos: 13 pts (9%)
##### ✅ Archivos CSV 
En la clase Casino, está el método ```cargar_csv``` que se encarga de manejar los archivos con este formato, y pasarlos a diccionarios.

##### ✅ parametros.py
Se crean los parámetros pedidos en el enunciado.


#### Bonus: 3 décimas máximo
##### ❌ Ver Show
## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```main.py```. Además se debe crear los siguientes archivos y directorios adicionales:
1. ```flujo.py``` en ```./```
2. ```gui``` en ```./```
3. ```csv``` en ```./```
4. ...


## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```random```: ```random(), randint()```
2. . ```abc```: ```ABC```
3. ```tabulate```: ```tabulate()``` (debe instalarse)
### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```Gui```: Contiene a ```Gui```, sirve para mejorar la interfaz gráfica
2. ```Menu```: Contiene a ```Menu, MenuInicio, MenuPrincipal, SubMenu, SubMenuBeb, SubMenuHabJug```, contiene clases para crear loss distintos tipos de menú
3. ```misc_funcs```: Funciones helpers

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. Se asume que le ayudante usará sus propios archivos csv en la carpeta correspondiente (en el enunciado aparece que se deben ignorar al hacer push).


## Referencias de código externo :book:

## Descuentos
La guía de descuentos se encuentra [link](https://github.com/IIC2233/syllabus/blob/main/Tareas/Descuentos.md).
