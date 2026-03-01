import json
import os
from datetime import datetime
from pathlib import Path
import uuid

DATA_DIR = Path(__file__).parent.parent / "data" / "plans"

def ensure_data_dir():
    DATA_DIR.mkdir(parents=True, exist_ok=True)

def create_project(project_name):
    ensure_data_dir()
    project_id = str(uuid.uuid4())
    project_data = {
        "project_id": project_id,
        "project_name": project_name,
        "created_at": datetime.now().isoformat(),
        "last_modified": datetime.now().isoformat(),
        "modules": {
            "snapshot": {},
            "problem": {},
            "market": {},
            "revenue": {},
            "operations": {},
            "risk": {}
        },
        "structured_draft": ""
    }
    
    file_path = DATA_DIR / f"{project_id}.json"
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(project_data, f, indent=2, ensure_ascii=False)
    
    return project_id

def save_module_data(project_id, module_name, data):
    ensure_data_dir()
    file_path = DATA_DIR / f"{project_id}.json"
    
    if not file_path.exists():
        raise FileNotFoundError(f"Project {project_id} not found")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        project_data = json.load(f)
    
    project_data["modules"][module_name] = data
    project_data["last_modified"] = datetime.now().isoformat()
    
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(project_data, f, indent=2, ensure_ascii=False)

def load_project(project_id):
    ensure_data_dir()
    file_path = DATA_DIR / f"{project_id}.json"
    
    if not file_path.exists():
        raise FileNotFoundError(f"Project {project_id} not found")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def update_structured_draft(project_id, draft_text):
    ensure_data_dir()
    file_path = DATA_DIR / f"{project_id}.json"
    
    if not file_path.exists():
        raise FileNotFoundError(f"Project {project_id} not found")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        project_data = json.load(f)
    
    project_data["structured_draft"] = draft_text
    project_data["last_modified"] = datetime.now().isoformat()
    
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(project_data, f, indent=2, ensure_ascii=False)

def list_existing_projects():
    ensure_data_dir()
    projects = []
    
    for file_path in DATA_DIR.glob("*.json"):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                projects.append({
                    "project_id": data["project_id"],
                    "project_name": data["project_name"],
                    "created_at": data["created_at"],
                    "last_modified": data["last_modified"]
                })
        except Exception:
            continue
    
    return sorted(projects, key=lambda x: x["last_modified"], reverse=True)
