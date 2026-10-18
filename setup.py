
from pathlib import Path

project_root = Path(__file__).resolve().parent

folders = ["data", "notebooks", "src"]

for folder in folders:
    (project_root / folder).mkdir(exist_ok=True)

print("TerraWatch folders created successfully!")
