import os
import json
from instaloader import Instaloader, Profile

def download_instagram_profile_metadata(username, base_directory):
    """
    Descarga la metadata de un perfil de Instagram.
    
    Parameters:
    - username (str): Nombre de usuario de Instagram.
    - base_directory (str): El directorio base donde se almacenarán los datos del perfil.
    """
    
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
        
        # Crear un diccionario con la metadata del perfil
        profile_metadata = {
            "username": profile.username,
            "full_name": profile.full_name,
            "biography": profile.biography,
            "external_url": profile.external_url,
            "followers": profile.followers,
            "followees": profile.followees,
            "mediacount": profile.mediacount,
            "is_verified": profile.is_verified,
            "is_private": profile.is_private,
            "is_business_account": profile.is_business_account,
            "business_category_name": profile.business_category_name if profile.is_business_account else None,
            "profile_pic_url": profile.profile_pic_url,
            "biography_hashtags": profile.biography_hashtags,
            "biography_mentions": profile.biography_mentions,
            "blocked_by_viewer": profile.blocked_by_viewer,
            "follows_viewer": profile.follows_viewer,
            "followed_by_viewer": profile.followed_by_viewer,
        }
        
        # Guardar la metadata en un archivo JSON
        metadata_path = os.path.join(raw_directory, f"{username}_metadata.json")
        with open(metadata_path, 'w', encoding="utf-8") as f:
            json.dump(profile_metadata, f, indent=4, ensure_ascii=False)
        
        print(f"Metadata del perfil guardada en {metadata_path}")
    
    except Exception as e:
        print(f"Ocurrió un error al descargar la metadata del perfil de {username}: {e}")