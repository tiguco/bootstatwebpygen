import os
import shutil

def delete_directory_contents_recursive(directory_path):
    """
    Recursively deletes all contents of a directory and its subdirectories.
    
    Args:
        directory_path (str): Path to the directory to clean
    """
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

# Example usage
if __name__ == "__main__":
    target_directory = "/path/to/directory/to/clean"
    target_directory = "/tmp/y"
    delete_directory_contents_recursive(target_directory)
    print("Directory contents deletion completed!")
