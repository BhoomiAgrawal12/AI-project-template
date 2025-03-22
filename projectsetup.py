import os
from pathlib import Path

while True:
    project_name = input("Enter the name of your project: ")
    if project_name != '':
        break

list_files = [
    ".github/workflows/.gitkeep",
    "README.md",
    f"{project_name}/__init__.py",
    f"{project_name}/components/data_preprocessing.py",
    f"{project_name}/components/data_ingestion.py",
    f"{project_name}/components/mode_evaluation.py",
    f"{project_name}/components/model_loading.py",
    f"{project_name}/pipeline/inference.py",
    f"{project_name}/pipeline/training.py",
    f"{project_name}/exceptions.py",
    f"{project_name}/logger.py",
    "templates/index.html",
    "static/style.css",
    "notebook/research.ipynb",
    "init_setup.sh",
    "requirements.txt",
    "dockerfile",
    "app.py",
    ".gitignore",
]

for file in list_files:
    filepath = Path(file)
    filedir, filename = os.path.split(filepath)

    if filedir != '':
        os.makedirs(filedir, exist_ok=True)

    if not os.path.exists(filepath):
        with open(filepath, 'w') as f:
            pass
