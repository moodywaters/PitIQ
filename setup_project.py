import os

# Define folder structure
folders = [
    "app",
    "app/static",
    "tests"
]

# Define files with optional starter content
files = {
    "app/__init__.py": "",
    "app/main.py": "# FastAPI entry point for PitIQ\n\nif __name__ == '__main__':\n    print('PitIQ app skeleton ready!')\n",
    "app/db.py": "# Database connection helpers will go here\n",
    "app/probes.py": "# Probe reading logic will go here\n",
    "app/models.py": "# Database table creation scripts will go here\n",
    "app/routes.py": "# FastAPI routes will go here\n",
    "tests/test_probes.py": "# Basic probe test placeholder\n",
    "requirements.txt": "fastapi\nuvicorn\nplotly\nsqlite3\n",
    "README.md": "# PitIQ - Raspberry Pi BBQ Temperature Monitoring\n\nPhase 1: Local-first temp monitoring with FastAPI & SQLite\n",
    ".gitignore": "__pycache__/\n*.pyc\n*.db\n.env\n"
}

def create_project_structure(base_path="."):
    print("Creating PitIQ folder structure...")
    
    for folder in folders:
        folder_path = os.path.join(base_path, folder)
        os.makedirs(folder_path, exist_ok=True)
        print(f"Created folder: {folder_path}")

    for file, content in files.items():
        file_path = os.path.join(base_path, file)
        # Avoid overwriting existing files
        if not os.path.exists(file_path):
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Created file: {file_path}")
        else:
            print(f"File already exists: {file_path}")

    print("\n✅ Project structure setup complete!")

if __name__ == "__main__":
    create_project_structure()
