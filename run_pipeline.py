
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

    
result = subprocess.run(
    [sys.executable, str(project_root / "src" / script)],
    cwd=project_root,
    capture_output=True,
    text=True
)

print(result.stdout, flush=True)
print(result.stderr, flush=True)

if result.returncode != 0:
    raise RuntimeError(
        f"{script} failed:\n{result.stderr}"
    )


print("\nTerraWatch data pipeline completed successfully!")
