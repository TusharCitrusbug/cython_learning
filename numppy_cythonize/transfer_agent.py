import os
import shutil

def create_cython_files(src_folder, dest_folder):
    # Create the destination folder if it doesn't exist
    os.makedirs(dest_folder, exist_ok=True)
    print(os.walk(src_folder))
    # Traverse the source folder and process each file
    for root, dirs, files in os.walk(src_folder):
        print(root,"rooooooooooooo")
        # Create the relative path for the destination folder
        relative_path = os.path.relpath(root, src_folder)
        dest_folder_path = os.path.join(dest_folder, relative_path)

        # Create the destination folder
        os.makedirs(dest_folder_path, exist_ok=True)

        for file in files:
            if file.endswith(".py"):
                # Create the full path of the source file
                src_file_path = os.path.join(root, file)

                # Create the relative path for the destination file
                relative_file_path = os.path.relpath(src_file_path, src_folder)
                dest_file_path = os.path.join(dest_folder_path, os.path.splitext(relative_file_path)[0] + ".pyx")

                # Read the content of the source file
                with open(src_file_path, "r") as src_file:
                    file_content = src_file.read()

                # Write the content to the destination .pyx file
                with open(dest_file_path, "w") as dest_file:
                    dest_file.write(file_content)

if __name__ == "__main__":
    # Specify the virtual environment path and numpy module folder
    venv_path = "/home/xoro/c_with_python/env/lib/python3.10/site-packages/numpy"
    numpy_module_folder = os.path.join(venv_path, "lib", "pythonX.X", "site-packages", "numpy")

    # Specify the destination folder for .pyx files
    destination_folder = "cythonized_numpy"

    # Create Cython files and copy the entire folder structure
    create_cython_files(numpy_module_folder, destination_folder)

    print(f"Cython files created and folder structure copied to: {destination_folder}")
