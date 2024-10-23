import os
import json
import time
from instaloader import Instaloader, Profile, InstaloaderException

def download_instagram_highlights(username, base_directory):
    # Crear el directorio 'raw' donde se guardará la descarga
    raw_directory = os.path.join(base_directory, username, 'raw')
    
    # Crear instancia de Instaloader con configuración específica
    loader = Instaloader(
        dirname_pattern=raw_directory, 
        compress_json=False, 
        download_videos=False, 
        max_connection_attempts=5
    )

    # Iniciar sesión si se proporciona el nombre de usuario y contraseña en las variables de entorno
    if 'INSTA_USERNAME' in os.environ and 'INSTA_PASSWORD' in os.environ:
        scrape_profile = os.getenv('INSTA_USERNAME')
        loader.login(user=scrape_profile, passwd=os.getenv('INSTA_PASSWORD'))
        print("Logged in successfully!")
    else:
        print("Las variables de entorno INSTA_USERNAME e INSTA_PASSWORD no están disponibles.")
        # Salir si no hay credenciales
    
    # Crear instancia del perfil a partir del nombre de usuario
    # Obtener el perfil
    try:
        profile = Profile.from_username(loader.context, username)
    except InstaloaderException as e:
        print(f"Error al obtener el perfil: {e}")
        return
    
    # Crear un directorio para guardar los highlights
    highlights_directory = os.path.join(base_directory, username, "highlights")
    if not os.path.exists(highlights_directory):
        os.makedirs(highlights_directory)
    
    # Obtener los highlights del perfil
    highlights = loader.get_highlights(profile)
    
    for highlight in highlights:
        # Crear un directorio para cada highlight
        highlight_title = highlight.title.replace(' ', '_')
        highlight_directory = os.path.join(highlights_directory, highlight_title)
        if not os.path.exists(highlight_directory):
            os.makedirs(highlight_directory)

        # Descargar los metadatos del highlight
        highlight_metadata = {
            "title": highlight.title,
            "owner_username": highlight.owner_username,
            "owner_id": highlight.owner_id,
            "unique_id": highlight.unique_id,
            "item_count": highlight.itemcount,
            "cover_url": highlight.cover_url,
            "cover_cropped_url": highlight.cover_cropped_url,
            "last_seen_utc": highlight.last_seen_utc.isoformat() if highlight.last_seen_utc else None
        }

        # Guardar los metadatos en un archivo JSON
        metadata_path = os.path.join(highlight_directory, f"{highlight_title}_metadata.json")
        with open(metadata_path, 'w', encoding='utf-8') as f:
            json.dump(highlight_metadata, f, indent=4, ensure_ascii=False)
        
        # lets sleep for one sec
        time.sleep(1)

        # Descargar los items (story items) del highlight
        for item in highlight.get_items():
            loader.download_storyitem(item, highlight_directory)

    print(f"Highlights de {username} descargados correctamente en {highlights_directory}")
