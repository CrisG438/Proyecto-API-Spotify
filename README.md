🎧 Proyecto API Spotify + Base de Datos
📌 Descripción

Este proyecto consiste en consumir la API REST de Spotify para obtener datos reales del usuario (canciones más escuchadas), y almacenarlos en una base de datos relacional SQLite para su posterior consulta.

🎯 Objetivos
Consumir una API REST pública (Spotify)
Implementar autenticación mediante OAuth 2.0
Obtener datos en formato JSON
Guardar los datos en una base de datos relacional
Consultar los datos mediante SQL
🛠️ Tecnologías utilizadas
Python 🐍
Spotipy (cliente para API de Spotify)
SQLite 🗄️
Git & GitHub 🌐
🔐 Autenticación

Se utilizó el flujo:

👉 Authorization Code Flow (OAuth 2.0)

Esto permite:

Login del usuario en Spotify
Acceso a datos personales (top canciones)
Uso de tokens de acceso
📦 Instalación
Clonar el repositorio:
git clone https://github.com/CrisG438/Proyecto-API-Spotify.git
cd Proyecto-API-Spotify
Instalar dependencias:
pip install spotipy
⚙️ Configuración

Debes crear una aplicación en:

👉 https://developer.spotify.com/dashboard

Y obtener:

Client ID
Client Secret

Luego configurar en el código:

CLIENT_ID = "TU_CLIENT_ID"
CLIENT_SECRET = "TU_CLIENT_SECRET"
REDIRECT_URI = "http://127.0.0.1:8888/callback"

También debes agregar esa misma URI en el dashboard de Spotify.

▶️ Ejecución
python spotify_app_data.py

🔄 Funcionamiento
El usuario inicia sesión en Spotify
Se obtienen sus canciones más escuchadas
Los datos se procesan en formato JSON
Se almacenan en una base de datos SQLite
Se pueden consultar mediante SQL
🗄️ Base de datos

Base de datos: spotify.db

Tabla: top_tracks

Campo	Tipo
id	TEXT (PK)
name	TEXT
artist	TEXT
🔍 Consulta de datos

Ejemplo de consulta SQL:

SELECT * FROM top_tracks;
📊 Ejemplo de salida
Canción - Artista
Blinding Lights - The Weeknd
Shape of You - Ed Sheeran
...
🚀 Resultados
✔ Conexión exitosa con API de Spotify
✔ Autenticación mediante OAuth
✔ Obtención de datos reales del usuario
✔ Almacenamiento en base de datos
✔ Consulta mediante SQL
📚 Conclusión

Este proyecto demuestra cómo integrar una API REST externa con una base de datos relacional, utilizando autenticación segura y procesamiento de datos en tiempo real.

👤 Autor

Cristian Gonzalez
GitHub: https://github.com/CrisG438
