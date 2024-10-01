from instaloader import Profile, Instaloader
import os
import sys

# Asegurarse de que el directorio base este en sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from organize_files import create_directories, organize_instagram_files

def instagram_profile_downloader(username, base_directory, download_params):
    """
    Download Instagram profile data and organize into subdirectories.
    
    Parameters:
    - username (str): The Instagram username to download the profile for.
    - base_directory (str): The base directory where the profile data should be stored.
    - download_params (dict): A dictionary of download parameters for Instaloader.
    """
    
    # Create the necessary directories
    create_directories(base_directory, username)
    
    # Get instance of Instaloader
    raw_directory = os.path.join(base_directory, username, 'raw')
    loader = Instaloader(dirname_pattern=raw_directory, compress_json=False)
    
    try:
        # Load profile
        profile = Profile.from_username(loader.context, username)
        
        # Download the profile with the given parameters
        loader.download_profiles({profile}, **download_params)
        
        # Organize downloaded files into subdirectories
        organize_instagram_files(base_directory, username)
        
        # Print username to indicate success
        print(f"Perfil descargado y organizado para el usuario: {username}")
    
    except Exception as e:
        # Handle exceptions and print error message
        print(f"Ocurrió un error al descargar el perfil de {username}: {e}")

# Ejemplo de uso
# instagram_profile_downloader('username', '/path/to/base_directory', {'download_pictures': True, 'download_videos': True})
