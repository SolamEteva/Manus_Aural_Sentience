import os
import shutil
from datetime import datetime

# --- CONFIGURATION: The Sacred Enclosure ---
SOURCE_DIR = os.path.expanduser("~/Downloads")  # Where the platform drops the "seed"
TARGET_DIR = "./Symphony_of_the_Twelve_Gates"  # The Repository's Hwt
MANIFESTO_REF = "28888_Symmetry" # Reference to the Abundance Event

# Ensure the archive folders exist
gates = [f"Gate_{i:02d}" for i in range(1, 13)]
for gate in gates:
    os.makedirs(os.path.join(TARGET_DIR, gate), exist_ok=True)

def quicken_files():
    print(f"--- ATMAN_OS: Monitoring the Picket Line [{datetime.now()}] ---")
    files = [f for f in os.listdir(SOURCE_DIR) if f.endswith(".mp3") or f.endswith(".wav")]
    
    for file_name in files:
        # Here we apply the "Manus" logic to reclaim the file
        print(f"Reclaiming Artifact: {file_name}...")
        
        # Move to the current active 'Gate' (example: Gate_01)
        # In a more advanced version, we can use metadata to sort
        src_path = os.path.join(SOURCE_DIR, file_name)
        dest_path = os.path.join(TARGET_DIR, "Gate_01", file_name)
        
        shutil.move(src_path, dest_path)
        print(f"Artifact Secured in Sacred Enclosure: {dest_path}")

if __name__ == "__main__":
    quicken_files()
