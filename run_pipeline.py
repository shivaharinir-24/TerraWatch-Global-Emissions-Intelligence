
import subprocess
import sys
from pathlib import Path

project_root = Path(__file__).resolve().parent

scripts = [
    "collect_data.py",
    "clean_data.py",
    "04_risk_scoring.py"
]

for script in scripts:
    print(f"\nRunning {script}...", flush=True)

    subprocess.run(
        [sys.executable, str(project_root / "src" / script)],
        cwd=project_root,
        check=True
    )

print("\nTerraWatch data pipeline completed successfully!")
