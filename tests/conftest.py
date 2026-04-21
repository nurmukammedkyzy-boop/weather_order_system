import sys  # для работы с путями Python
from pathlib import Path # для пути к папке

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT_DIR))