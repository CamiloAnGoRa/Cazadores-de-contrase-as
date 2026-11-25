# Cazadores-de-contraseñas

´´´

Excepciones
    EntradaNoNumericaError
    LongitudInvalidaError
    ContraseñaInvalidaError

´´´ 

Ninguna excepcion imprime mensajes por pantalla. Lo unico que realizan es el transporte del error y los datos que tienen asociados.
El mensaje que le llega al usuario corresponde a la clase JuegoCazador

---

### ´JuegoCazadorError´

Esta es la clase base para el manejo de las exepciones del juego. Sin atributos solo es heradada de Exception.
Permite la captura de cualquier error propio del juego sin atrapar errores ajenos, como un ´TypeError´que se cause en los fallos de la logica del desarrollo

--- 

### ´EntradaNoNumericaError´

Es ejecutada en el momento en que el jugador registra un valor el cual no corresponde a un digito. Es heredada de ´JuegoCazadorError´

---

### ´LongitudInvalidaError´

Se ejecuta en el momento en que la longitud que el usuario registra se encuentra por fuera del rango establecido como minimo o como maximo 8-80
El minimo y el maximo se reciben como parametros para que la excepcion no dependa de la clase Contraseña y de esta manera evitar una dependencia circular 

--- 

### ContraseñaInvalidaError

Ejecutada en el momento en el que la contraseña no cumpla con los requisitos obligatorios (mayuscula, minuscula, numero, caracter especial, sin caracteres repetidos)





