import os

folder = "/Users/boozer/my_devops_journey/projects"

file_types = {
    "images": [".jpg", ".jpeg", ".png", ".gif"],
    "documents": [".pdf", ".doc", ".txt"],
    "music": [".mp3", ".wav"],
    "videos": [".mp4", ".mov"]
}

files = os.listdir(folder)

for file in files:
    extension = os.path.splitext(file)[1]
    
    for category, extensions in file_types.items():
        if extension in extensions:
            # Создать папку если её нет
            category_folder = os.path.join(folder, category)
            if not os.path.exists(category_folder):
                os.makedirs(category_folder)
            
            # Переместить файл
            old_path = os.path.join(folder, file)
            new_path = os.path.join(category_folder, file)
            os.rename(old_path, new_path)
            print(f"Переместил: {file} → {category}/")