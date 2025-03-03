import os

def bulk_rename_files(directory, prefix, new_extension):
    try:
        file_list = os.listdir(directory)

# enumerate()= allows to loop over iterable (such as list, tuple, string) & get index and the value of each item during iteration
        for index, file_name in enumerate(file_list):
            old_file_path = os.path.join(directory, file_name)
            new_file_name = f'{prefix}_{index + 1}.{new_extension}'

            new_file_path = os.join(directory, new_file_name)

            os.rename(old_file_path, new_file_path)
            print(f"Renamed: {file_name} --> {new_file_name}")
            
        print("Bulk renaming successful")

    except FileNotFoundError as e:
        print(f'Folder not found: {e}')


directory = 'folder/to/rename'
prefix = 'video'
new_extension = '.mp4'

bulk_rename_files(directory, prefix, new_extension)