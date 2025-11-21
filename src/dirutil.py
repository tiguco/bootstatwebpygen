import os
import shutil


def delete_directory_contents_recursive(directory_path):
    # Check if directory exists
    if not os.path.exists(directory_path):
        print(f"Directory '{directory_path}' does not exist.")
        return
    
    # Check if it's actually a directory
    if not os.path.isdir(directory_path):
        print(f"'{directory_path}' is not a directory.")
        return
    
    # Iterate through all items in the directory
    for item in os.listdir(directory_path):
        item_path = os.path.join(directory_path, item)
        
        if os.path.isdir(item_path):
            # If it's a directory, recursively delete its contents
            delete_directory_contents_recursive(item_path)
            
            # After emptying the directory, remove the directory itself
            try:
                os.rmdir(item_path)
                print(f"Removed directory: {item_path}")
            except OSError as e:
                print(f"Error removing directory {item_path}: {e}")
        else:
            # If it's a file, delete it
            try:
                os.remove(item_path)
                print(f"Removed file: {item_path}")
            except OSError as e:
                print(f"Error removing file {item_path}: {e}")


def copy_directory_recursive(source_dir, dest_dir):
    if not os.path.exists(source_dir):
        raise FileNotFoundError(f"Source directory '{source_dir}' does not exist")
    
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    delete_directory_contents_recursive(dest_dir)
    
    for item in os.listdir(source_dir):
        source_path = os.path.join(source_dir, item)
        dest_path = os.path.join(dest_dir, item)
        
        if os.path.isdir(source_path):
            copy_directory_recursive(source_path, dest_path)
        else:
            shutil.copy2(source_path, dest_path)  # copy2 preserves metadata


