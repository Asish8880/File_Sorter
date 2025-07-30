import os
import shutil

FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".txt", ".doc", ".pptx", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Scripts": [".py", ".js", ".html", ".css", ".sh"],
    "Others": []  # fallback category
}

def get_category(extension):
    for category, extensions in FILE_TYPES.items():
        if extension.lower() in extensions:
            return category
    return "Others"

def sort_files_by_format(folder_path):
    if not os.path.isdir(folder_path):
        print("Provided path is not a folder.")
        return

    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)

        if os.path.isfile(file_path):
            _, extension = os.path.splitext(file)
            category = get_category(extension)

            category_folder = os.path.join(folder_path, category)
            os.makedirs(category_folder, exist_ok=True)

            dest_path = os.path.join(category_folder, file)
            shutil.move(file_path, dest_path)
            print(f"Moved: {file} → {category}/")

if __name__ == "__main__":
    folder = input("Enter the full path of the folder to sort: ").strip()
    sort_files_by_format(folder)
