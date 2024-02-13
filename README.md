# movement-arduino-pc
Proyecto de dispositivo arduino con receptor bluetooth para pc a python

8/02/2024
Emiliano Sanchez Godinez . Todos Los Derechos Reservados.
 ----------------------------------------------------------------------
Documentación del Proyecto

Descripción General:
Este proyecto consiste en un sensor de movimiento programable que utiliza un módulo óptico y una tarjeta Arduino para detectar movimiento. Los datos detectados se transmiten a través de un módulo Bluetooth HC05 a una computadora, donde se ejecuta una acción específica mediante un archivo init.bat que hace referencia a un código Python.
Objetivo del producto:
Este sensor puede ser muy útil para automatizar tareas en una computadora. Al detectar movimiento, el sensor puede enviar una señal al Arduino, que a su vez puede comunicarse con la PC a través del módulo Bluetooth HC05 para ejecutar la combinación de teclas Alt+Tab. Esto puede ser especialmente útil para cambiar rápidamente entre aplicaciones sin tener que usar el teclado o el mouse, lo que puede aumentar la eficiencia y la comodidad del usuario.
Asimismo, para encubrir tareas acciones en la computadora que requieren de privacidad como el trabajo en proyectos confidenciales en zonas abiertas o el uso de herramientas de entretenimiento variadas en horarios no recreativos.

Componentes:
1.	Módulo Óptico TCRT5000: Este módulo es el encargado de detectar el movimiento.
2.	Arduino: Se utiliza para procesar la señal del módulo óptico y transmitirla al módulo Bluetooth.
3.	Módulo Bluetooth HC05: Este módulo recibe la señal del Arduino y la transmite a la computadora.
4.	Computadora: Recibe la señal del módulo Bluetooth y ejecuta una acción específica mediante un archivo init.bat.

Establecimiento del precio:
•	Módulo Bluetooth HC05: $95
•	Sensor óptico TCMT5000: $8
•	Arduino Nano: $229
•	Pila de 9V: $179
Esto da un total de $511 para los componentes. Si se añade un costo de mano de obra de $200, el costo total de fabricación sería de $711. Si se desea un margen de ganancia del 60%, el precio de venta sería de $711 * 1.60 = $1137.6.

Comunicación:
La comunicación entre el módulo Bluetooth y la computadora se realiza a través del puerto COM6 a una velocidad de 9600 baudios.

Código Python:
El código Python se encarga de establecer la conexión Bluetooth y de recibir los datos del sensor de movimiento. Este código es referenciado por el archivo init.bat.
El código monitorea el puerto de trasmisión de entrada de datos Bluetooth COM6 a la espera de recibir el pulso, si se recibe el mensaje esperado, se ejecuta una acción en la computadora.

Archivo init.bat:
Este archivo es el encargado de ejecutar el código Python cuando se detecta movimiento.

Ejecución:
1.	Encienda el dispositivo Arduino: Asegúrese de que el Arduino esté correctamente conectado y encendido.
2.	Establezca el enlace Bluetooth: Establezca la conexión Bluetooth con la computadora mediante el código proporcionado. (Default: 1234)
3.	Ejecute el programa init.bat: Descargue la carpeta zip de la aplicación del proyecto y extraiga los archivos. Ubique el archivo init.bat, edítelo y ejecútelo.
4.	La ventana CMD sirve como controlador activo no-interactuable del programa, al cerrarla se apaga la aplicación. Para aprovechar la función del sensor, simplemente se deja ejecutando como proceso en segundo plano.

Consideraciones de Seguridad:
Es importante tener en cuenta las precauciones de seguridad al trabajar con componentes electrónicos. Asegúrese de manejar correctamente todos los componentes y de seguir las instrucciones del fabricante para evitar daños a los dispositivos.
Mantenimiento y Soporte:
Para el mantenimiento del sistema, se recomienda revisar periódicamente las conexiones y el funcionamiento de los componentes. 

Licencia y Garantía:
Este proyecto es de código abierto, lo que significa que puede ser modificado y utilizado libremente. Se recomienda que cualquier modificación se realice con cuidado y con un entendimiento completo del código y del hardware.

Conclusión:
Este proyecto de sensor de movimiento programable es una excelente manera de aprender sobre la programación de Arduino, la comunicación Bluetooth y la interacción entre hardware y software. Asimismo de cumplir su función principal como un gadget de uso práctico.
 ---------------------------------------------------------------------------------
Pasos:
Encender modulo de deteccion Arduino.
Establecer conexion bluetooth a la computadora.
Editar el archivo init.bat con la ruta de la carpeta de archivos.
Iniciar init.bat

Para terminar el programa cerrar la ventana de cmd
