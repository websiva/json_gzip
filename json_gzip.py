import os
import subprocess

# Get the full path to the directory containing this script
exe_file_location = os.getcwd()
#exe_file_location="E:\\001_new_generator - Copy\\test"
# Full path to the 7-Zip executable
seven_zip_path = 'C:/Program Files/7-Zip/7z.exe'  # Replace with the actual path to 7z.exe

print(f"Current directory: {exe_file_location}")
your_directory_path = exe_file_location

def delete_log_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".log"):
                file_path = os.path.join(root, file)
                os.remove(file_path)
                print(f"Deleted: {file_path}")

def compress_and_rename_json_files(directory, seven_zip_path):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".json"):
                json_file_path = os.path.join(root, file)
                gz_file_path = f'{os.path.splitext(json_file_path)[0]}.gz'

                command = f'"{seven_zip_path}" a -tgzip "{gz_file_path}" "{json_file_path}"'

                subprocess.run(command, shell=True)

                print(f"Compressed: {json_file_path} -> {gz_file_path}")

                os.remove(json_file_path)
                print(f"Deleted: {json_file_path}")

                os.rename(gz_file_path, f'{os.path.splitext(json_file_path)[0]}.json')
                print(f"Renamed: {gz_file_path} -> {os.path.splitext(json_file_path)[0]}.json")

def main():
    delete_log_files(your_directory_path)
    compress_and_rename_json_files(your_directory_path, seven_zip_path)

if __name__ == "__main__":
    main()
