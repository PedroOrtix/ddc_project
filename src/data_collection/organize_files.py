import os
import shutil

def create_directories(base_directory, username):
    """
    Create the required directory structure if it doesn't exist.
    
    Parameters:
    - base_directory (str): The base directory where the profile data is stored.
    - username (str): The username of the person whose data is being organized.
    """
    user_directory = os.path.join(base_directory, username)
    
    raw_dir = os.path.join(user_directory, 'raw')
    
    instagram_image_dir = os.path.join(raw_dir, 'photos')
    instagram_video_dir = os.path.join(raw_dir, 'videos')
    instagram_metadata_dir = os.path.join(raw_dir, 'metadata')
    
    directories = [
        raw_dir, instagram_image_dir, instagram_video_dir, instagram_metadata_dir
    ]
    
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)

def organize_instagram_files(base_directory, username):
    """
    Organize Instagram files into specified subdirectories.
    
    Parameters:
    - base_directory (str): The base directory where the profile data is stored.
    - username (str): The username of the person whose data is being organized.
    """
    user_directory = os.path.join(base_directory, username)
    raw_dir = os.path.join(user_directory, 'raw')
    
    instagram_image_dir = os.path.join(raw_dir, 'photos')
    instagram_video_dir = os.path.join(raw_dir, 'videos')
    instagram_metadata_dir = os.path.join(raw_dir, 'metadata')

    for filename in os.listdir(raw_dir):
        file_path = os.path.join(raw_dir, filename)
        
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            shutil.move(file_path, instagram_image_dir)
        elif filename.lower().endswith('.mp4'):
            shutil.move(file_path, instagram_video_dir)
        elif filename.endswith('.json') or filename.endswith('.txt'):
            shutil.move(file_path, instagram_metadata_dir)

