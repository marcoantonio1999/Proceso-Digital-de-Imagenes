Para empezar;
Cabe recalcar que todas las imagenes del data set no pueden ser archivos de tipo png, por alguna razon pillow no permite hacer el cambio de pgn a jpg, mientras que con cualquier otra deberia funcionar correctamente.

Otra aclararacion es que el data set de imagenes fue de medio millon de fotos, por lo que para poder procesar la imagen tardo cerca de 17 horas, mi computadora es muy potente por lo que podria ser un tiempo mas alto en otros casos.

El codigo se pudo optimizar con hilos pero como dice el profesor, primero se hace para que jale

Para ejecutar la tarea solo es necesario descargar primero los paquetes con el comando




```bash

pip3 install -r requeriments.txt
```


Despues se deben ejecutar los siguientes archivos en el siguiente orden

```bash

python3 main.py

```
```bash

python3 creaBase.py

```
```bash

python3 final.py

```

