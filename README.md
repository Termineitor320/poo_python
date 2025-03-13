# poo en python

- el paradigma de POO esta basado en una abstraccion del mundo real que nos va a permitir desarrollar programas de forma mas cercana como vemos el mundo, pensando en objetos que tenemos delante y en acciones que podemos hacer con ellos. 

## clase 

- una clase es un tipo de dato  cuyas variables se llaman objetos o instancias. 

- la clase es definicion del concepto real y los objetos o instancias son el "propio" objeto del mundo real.  


- las clases estan conformadas por 2 elementos: atributos y metodos.

### atributos 

- informacion que almacena la clase. 

### metodos 

- operaciones que puedan realizar las clases.

## definicion de una clase en python

```python
class NombreClase:
    def_init_(self, variable1, variable2):
        self, atributo1 = valor1
        self, atributo2 = valor2

def nombre metodo(self):
    bloquecodigo
```    

### componentes 

class```:palabra reservada en python para definir una clase.

```NombreClase```:nombre de la clas que quieres crear 

```def```:palabra reservada en python que se utiliza para definir tanto el constructor de la clase (metodo que se ejecuta la primera vez que usas una clase ) como los diferenrtes metodos ue tiene 

```__init__```: palabra reservada en python para definir el metodo constructor de la clase. Es lo primero que se ejecuta cuando crear un objeto de una clase 

```(self, variablex)```:parametro del constructor de la clase. El parametro es obligatorio y despues puedes tener tantos parametros como quieras. la forma de añadir parametros en la misma que en las funciones.

```self, atributox```:forma de utilizacion y acceso a los atributos de la clase.

``Nombremetodo``: nombre del metodo de la clase 

```self```: El parametro es obligatorio y despues puedes tener tantos parametros como quieras. la forma de añadir parametros en la misma que en las funciones.

```bloquecodigo```: instrucciones que ejecutara el metodo.

- cuando defines una clase debes tener en cuenta los siguientes puntos.

    - puedes definir tantos atributos como necesites.
    - puedes definir tantos metodos como necesites  
    - puedes definir tantos parametro en el constructor como necesites  


