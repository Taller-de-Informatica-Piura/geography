# 🌍 Proyecto: Duolingo de Ciudades

¡Hola! Este proyecto es un juego divertido para aprender sobre ciudades del mundo. Vamos a usar Python, mapas y un poco de magia de ChatGPT para crear nuestro propio **Duolingo de Ciudades**.

---

## 📂 Estructura de carpetas

El proyecto tiene esta estructura:


geography/
│
├─ imagen/ # Carpeta con imágenes de varios lugares y ciudades del mundo
│ ├─ cuzco.jpg
│ ├─ paris.jpg
│ └─ tokyo.jpg
│
├─ get_xy_city.py # Script de Python que usa un servicio web para obtener las coordenadas GPS (x, y) de una ciudad
│
├─ map_sample.html # Mapa de ejemplo con algunas ciudades ya marcadas
│
└─ README.md # Este archivo

---

## 🖥️ Cómo funciona `get_xy_city.py`

Este script usa el servicio web de [Nominatim](https://nominatim.openstreetmap.org) para obtener las coordenadas GPS de cualquier ciudad que ingreses. Por ejemplo:

```bash
python get_xy_city.py
Ingrese el nombre de la ciudad: Lima
Coordenadas: x=-12.0464, y=-77.0428
```

🎯 Tareas del proyecto

1. Crear un Duolingo de Ciudades

Usando ChatGPT, vamos a adaptar un script que hicimos antes para un juego estilo Duolingo:

- Mostrar el nombre de la ciudad.
- Mostrar dos imágenes de ciudades.
- El usuario tiene que hacer clic en la imagen correcta que corresponda con el nombre de la ciudad.

2. Crear un listado de ciudades con coordenadas

Partiendo de `get_xy_city.py`:

- Adaptar el script para leer todas las imágenes en la carpeta `imagen/`.
- Obtener las coordenadas GPS (x, y) de cada ciudad usando el webservice.
- Guardar los datos en un archivo `.csv` con las columnas:

nombre_ciudad,x,y
Lima,-12.0464,-77.0428
París,48.8566,2.3522
Tokio,35.6895,139.6917


3. Crear un mapa interactivo con Folium

Usar Python y la librería Folium para crear un mapa interactivo con todas las ciudades de tu .csv.

Cada ciudad se mostrará como un marcador en el mapa.

Guardar el mapa como un archivo HTML que puedas abrir en tu navegador.

# 🎯 Tareas del proyecto

Este proyecto se hace usando **Python**, preferentemente ejecutando los scripts desde **Thonny** (ya instalado en los laptops del colegio). También necesitarás la librería **Folium** para crear mapas interactivos. Puedes instalarla con:

```bash
pip install folium
```



