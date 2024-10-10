from instaloader import Instaloader, Profile, FrozenNodeIterator, resumable_iteration, Post
import os
import sys
import json
from datetime import datetime

# Asegurarse de que el directorio base esté en sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from data_collection.organize_files import create_directories, organize_instagram_files

def save_post_metadata(post, metadata_path):
    """
    Guarda los metadatos del post en un archivo JSON.
    
    Parameters:
    - post (Post): La instancia de Post que contiene la información.
    - metadata_path (str): Ruta donde se guardará el archivo JSON.
    """
    metadata = {
        "shortcode": post.shortcode,
        "caption": post.caption,
        "hashtags": post.caption_hashtags,
        "mentions": post.caption_mentions,
        "likes": post.likes,
        "comments_count": post.comments,
        "location": {
            "name": post.location.name if post.location else None,
            "lat": post.location.lat if post.location else None,
            "lng": post.location.lng if post.location else None
        },
        "is_video": post.is_video,
        "video_duration": post.video_duration,
        "media_count": post.mediacount,
        "owner_username": post.owner_username,
        "post_url": f"https://www.instagram.com/p/{post.shortcode}/",
        "date_utc": post.date_utc.isoformat(),
        "tagged_users": post.tagged_users
    }
    
    with open(metadata_path, 'w', encoding="utf-8") as f:
        json.dump(metadata, f, indent=4, ensure_ascii=False)
    
    print(f"Metadatos guardados en {metadata_path}")


def download_instagram_posts(username, base_directory):
    """
    Descarga todos los posts de un perfil de Instagram de forma resumible, incluyendo los metadatos.
    
    Parameters:
    - username (str): Nombre de usuario de Instagram.
    - base_directory (str): El directorio base donde se almacenarán los datos del perfil.
    """
    
    # Crear los directorios necesarios
    create_directories(base_directory, username)
    
    # Crear instancia de Instaloader
    raw_directory = os.path.join(base_directory, username, 'raw')
    loader = Instaloader(dirname_pattern=raw_directory, compress_json=False, download_videos=False, max_connection_attempts=5)
    
    # Iniciar sesión si se proporciona el nombre de usuario y contraseña
    if 'INSTA_USERNAME' in os.environ and 'INSTA_PASSWORD' in os.environ:
        scrape_profile = os.getenv('INSTA_USERNAME')
        loader.login(user=scrape_profile, passwd=os.getenv('INSTA_PASSWORD'))
        print("Logged in successfully!")
    else:
        print("Las variables de entorno INSTA_USERNAME e INSTA_PASSWORD no están disponibles.")

    try:
        # Obtener el perfil utilizando el nombre de usuario
        profile = Profile.from_username(loader.context, username)
        
        # Obtener el iterador de los posts del perfil
        post_iterator = profile.get_posts()

        # Funciones para cargar y guardar el estado del iterador
        resume_file = os.path.join(base_directory, username, "resume_info_{}.json".format(username))
        
        def load_resumable(_, path):
            with open(path, 'r') as f:
                return FrozenNodeIterator(**json.load(f))
        
        def save_resumable(fni, path):
            with open(path, 'w') as f:
                json.dump(fni._asdict(), f)
        
        # Usar resumable_iteration para gestionar la interrupción y reanudación de la descarga
        with resumable_iteration(
            context=loader.context,
            iterator=post_iterator,
            load=load_resumable,
            save=save_resumable,
            format_path=lambda _: resume_file
        ) as (is_resuming, start_index):
            print(f"Resuming: {is_resuming}, starting from post index: {start_index}")
            
            # Descargar los posts iterando sobre el iterador
            for post in post_iterator:
                print(f"Descargando post {post.shortcode} de {username}")
                
                # Descargar el post
                loader.download_post(post, target=username)
                
                # Guardar metadatos del post
                metadata_path = os.path.join(raw_directory, f"{post.shortcode}_metadata.json")
                save_post_metadata(post, metadata_path)
        
        # Organizar los archivos descargados en subdirectorios
        organize_instagram_files(base_directory, username)

        # Borrar archivo de resumable si se completó correctamente
        if os.path.exists(resume_file):
            os.remove(resume_file)
        
        print(f"Todos los posts han sido descargados y organizados para el usuario: {username}")
    
    except Exception as e:
        # Manejar excepciones y mostrar mensaje de error
        print(f"Ocurrió un error al descargar el perfil de {username}: {e}")


# Ejemplo de uso
# download_instagram_posts('username', '/path/to/base_directory')
