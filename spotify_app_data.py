import spotipy
from spotipy.oauth2 import SpotifyOAuth
import sqlite3

# 🔐 TUS DATOS (pon los tuyos)
CLIENT_ID = "f5fef334de184831bf659f775ea3873b"
CLIENT_SECRET = "d1fc05274a9542838caf622f71b476eb"
REDIRECT_URI = "http://127.0.0.1:8888/callback"

# 🎧 AUTENTICACIÓN (LOGIN)
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope="user-top-read"
))

print("✅ Login exitoso")

# 🎵 OBTENER TOP CANCIONES
results = sp.current_user_top_tracks(limit=10)

print("\n🎧 Tus canciones más escuchadas:\n")

for track in results['items']:
    print(f"{track['name']} - {track['artists'][0]['name']}")

# 🗄️ BASE DE DATOS
conn = sqlite3.connect("spotify.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS top_tracks (
    id TEXT PRIMARY KEY,
    name TEXT,
    artist TEXT
)
""")

# 💾 GUARDAR DATOS
for track in results['items']:
    cursor.execute("""
    INSERT OR REPLACE INTO top_tracks (id, name, artist)
    VALUES (?, ?, ?)
    """, (
        track['id'],
        track['name'],
        track['artists'][0]['name']
    ))

conn.commit()

print("\n✅ Datos guardados en la base de datos")

# 🔍 CONSULTAR DATOS
cursor.execute("SELECT * FROM top_tracks")

rows = cursor.fetchall()

print("\n📊 DATOS EN LA BASE:")
for row in rows:
    print(row)

conn.close()