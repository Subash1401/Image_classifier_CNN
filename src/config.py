"""Central place for all settings, so nothing is hard-coded elsewhere."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MODEL_PATH = ROOT / "models" / "best_model.keras"
OUTPUT_DIR = ROOT / "outputs"

CLASS_NAMES = [
    "airplane", "automobile", "bird", "cat", "deer",
    "dog", "frog", "horse", "ship", "truck",
]

IMG_SIZE = 32          # CIFAR-10 images are 32x32 RGB
NUM_CLASSES = 10
BATCH_SIZE = 64
EPOCHS = 30
VAL_SIZE = 5000        # images taken from training set for validation
SEED = 42
