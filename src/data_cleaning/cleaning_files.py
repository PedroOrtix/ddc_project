import json
import os
import shutil
from typing import Dict, Any
from pathlib import Path
from datetime import datetime

def extract_post_metadata(raw_post_data: Dict) -> Dict:
    """
    Extrae y limpia la metadata relevante de un post de Instagram.
    
    Args:
        raw_post_data (Dict): Datos crudos del post de Instagram
    
    Returns:
        Dict: Metadata limpia y estructurada del post
    """
    post = raw_post_data['node']
    caption = post['edge_media_to_caption']['edges'][0]['node']['text'] if post['edge_media_to_caption']['edges'] else ""
    
    location = {
        "name": post['location']['name'] if post.get('location') else None,
        "has_public_page": post['location'].get('has_public_page') if post.get('location') else None,
        "id": post['location'].get('id') if post.get('location') else None
    }
    
    media_info = []
    if 'edge_sidecar_to_children' in post:
        for media in post['edge_sidecar_to_children']['edges']:
            media_node = media['node']
            media_info.append({
                "is_video": media_node.get('is_video', False),
                "display_url": media_node.get('display_url'),
                "accessibility_caption": media_node.get('accessibility_caption')
            })
    else:
        media_info.append({
            "is_video": post.get('is_video', False),
            "display_url": post.get('display_url'),
            "accessibility_caption": post.get('accessibility_caption')
        })
    
    return {
        "caption": caption,
        "likes": post.get('edge_liked_by', {}).get('count', -1),
        "comments_count": post.get('edge_media_to_comment', {}).get('count', 0),
        "location": location,
        "media_count": len(media_info),
        "media": media_info
    }

def extract_user_metadata(raw_user_data: Dict) -> Dict:
    """
    Extrae y limpia la metadata relevante del perfil de usuario.
    
    Args:
        raw_user_data (Dict): Datos crudos del perfil de usuario
    
    Returns:
        Dict: Metadata limpia y estructurada del usuario
    """
    return {
        "username": raw_user_data.get('username'),
        "full_name": raw_user_data.get('full_name'),
        "biography": raw_user_data.get('biography'),
        "external_url": raw_user_data.get('external_url'),
        "followers": raw_user_data.get('followers'),
        "followees": raw_user_data.get('followees'),
        "mediacount": raw_user_data.get('mediacount'),
        "is_verified": raw_user_data.get('is_verified'),
        "is_private": raw_user_data.get('is_private'),
        "is_business_account": raw_user_data.get('is_business_account'),
        "profile_pic_url": raw_user_data.get('profile_pic_url')
    }

def clean_instagram_data(username: str) -> Dict:
    """
    Limpia y estructura los datos de un perfil de Instagram.
    
    Args:
        username (str): Nombre de usuario de Instagram
    
    Returns:
        Dict: Datos limpios y estructurados del perfil y sus posts
    
    Raises:
        ValueError: Si no se encuentra el directorio raw del usuario
    """
    # Definir rutas
    user_path = Path('data') / username
    raw_path = user_path / 'raw'
    processed_path = user_path / 'processed'
    processed_photos_path = processed_path / 'photos'
    
    # Verificar existencia del directorio raw
    if not raw_path.exists():
        raise ValueError(f"No se encontró el directorio raw para el usuario {username}")
    
    # Crear directorios de procesamiento
    processed_path.mkdir(exist_ok=True)
    processed_photos_path.mkdir(exist_ok=True)
    
    # Leer y limpiar metadata del usuario
    with open(raw_path / f'{username}_metadata.json', 'r', encoding='utf-8') as f:
        raw_user_data = json.load(f)
    
    cleaned_data = {
        "metadata_usuario": extract_user_metadata(raw_user_data),
        "posts": {}
    }
    
    # Procesar posts
    posts_path = raw_path / 'metadata'
    for filename in os.listdir(posts_path):
        try:
            # Verificar formato de fecha en nombre del archivo
            date_str = filename.split('.')[0]
            datetime.strptime(date_str, '%Y-%m-%d_%H-%M-%S_UTC')
            
            # Leer y limpiar datos del post
            with open(posts_path / filename, 'r', encoding='utf-8') as f:
                raw_post_data = json.load(f)
                iso_date = datetime.strptime(date_str, '%Y-%m-%d_%H-%M-%S_UTC').strftime('%Y-%m-%dT%H:%M:%S')
                cleaned_data['posts'][iso_date] = extract_post_metadata(raw_post_data)
        
        except ValueError:
            continue
    
    # Guardar datos limpios
    with open(processed_path / 'datos_perfil_procesados.json', 'w', encoding='utf-8') as f:
        json.dump(cleaned_data, f, indent=4, ensure_ascii=False)
    
    # Copiar fotos
    photos_path = raw_path / 'photos'
    if photos_path.exists():
        for photo in os.listdir(photos_path):
            if photo.endswith(('.jpg', '.jpeg', '.png')):
                shutil.copy2(photos_path / photo, processed_photos_path / photo)
    
    return cleaned_data

if __name__ == "__main__":
    try:
        username = input("Por favor, introduce el nombre de usuario de Instagram: ")
        clean_instagram_data(username)
        print(f"Procesado exitoso para: {username}")
    except Exception as e:
        print(f"Error procesando {username}: {str(e)}")
