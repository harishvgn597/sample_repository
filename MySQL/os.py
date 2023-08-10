import shutil
import os

new_directory = 'new_directory'
os.mkdir(new_directory)
print(f"Directory '{new_directory}' created successfully.")

source_directory = 'new_directory'
destination_directory = 'destination_directory'
os.rename(source_directory, destination_directory)
print(f"Directory '{source_directory}' moved to '{destination_directory}'.")


source_directory = 'source_directory'
os.mkdir(source_directory)
destination_directory = 'destination_directory'
shutil.copytree(source_directory, destination_directory)
print(f"Directory '{source_directory}' copied to '{destination_directory}'.")

old_directory_name = 'source_directory'
new_directory_name = 'destination_directory'
os.rename(old_directory_name, new_directory_name)
print(f"Directory '{old_directory_name}' renamed to '{new_directory_name}'.")

directory_to_delete = 'source_directory'
shutil.rmtree(directory_to_delete)
print(f"Directory '{directory_to_delete}' deleted successfully.")