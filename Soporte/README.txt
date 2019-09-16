PROYECTO - FOTOMOSAICOS.
PROCESO DIGITAL DE IMÁGENES.

Alumno: Jonathan Suárez López.
# CUENTA: 313259595.

* Requerimientos para ejecutar el programa *

- Tener Python 3.x.x instalado.
- Tener Pillow instalado. Más información en https://pypi.org/project/Pillow/ 
- Tener PyQt5 instalado.

Para utilizar el filtro de Fotomosaicos, primero se debe crear un archivo .txt en el que se cargue una biblioteca de imágenes predefinida, para esto hacer lo siguiente:
- Ejecutar Info_imgs.py con el siguiente comando.
$ python3 Info_imgs.py
Aparecerá una ventana, introducir el nombre del .TXT a generar, y darle al botón de Cargar, escoger la carpeta en la que se encuentre el paquete de imágenes a querer usar para generar el fotomosaico, darle aceptar y esperar. 

			********(¡IMPORTANTE!)*******
ASEGURARSE DE QUE LA CARPETA ESCOGIDA CONTENGA SÓLO IMÁGENES, SI NO, HABRÁN ERRORES.

Este proceso puede tardar dependiendo la velocidad del procesador y de la cantidad de imágenes (aprox. 1 minuto por 5000 imágenes).

Cerrar este programa, y ejecutar ahora:
$ python3 Filtros.py
Al abrir el programa, escoger una imagen a procesar, escoger el filtro de Fotomosaico, y darle al botón de cargar conjunto de imágenes, de ahí escoger el .TXT generado por el programa anterior, darle aceptar y finalmente darle en "Aplica fotomosaico". Empezará el proceso, éste puede llevar 3 o más minutos, dependiendo el número de imágenes a contemplar.

Como resultado se tendrá el fotomosaico.