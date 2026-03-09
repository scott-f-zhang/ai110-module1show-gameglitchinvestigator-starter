from pathlib import Path
import sys


PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    # FIX: After your pytest import error report, AI added project root for stable test imports.
    sys.path.insert(0, str(PROJECT_ROOT))
