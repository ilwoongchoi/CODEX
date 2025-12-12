import os
import shutil
import re

# --- CONFIGURATION ---
BASE_DIR = os.getcwd()
ARCHIVE_DIR = os.path.join(BASE_DIR, "content", "00-ARCHIVE")
PROTOCOLS_ROOT = os.path.join(BASE_DIR, "content", "protocols")

TAXONOMY = {
    "Physics": ["thermodynamic", "electron", "charge", "quantum", "gravity", "voltage", "entropy", "dimensional", "biophysics"],
    "Evolution": ["placozoan", "merger", "algae", "symbiosis", "sexual dimorphism", "origin", "evolutionary"],
    "Biochemistry": ["krebs", "tca", "glycolysis", "glutamate", "gaba", "acetyl", "enzyme", "molecular", "metabolic"],
    "Medicine": ["cancer", "oncology", "diabetes", "autoimmunity", "disease", "pathology", "treatment", "protocol", "sclerosis", "syndrome", "disorder", "als", "lupus"],
    "Psychiatry": ["depression", "anxiety", "schizophrenia", "autism", "adhd", "bipolar", "dopamine", "serotonin", "brain", "mental", "neurotransmitter"],
    "Ecology": ["soil", "root", "plant", "climate", "environment", "earth", "gaia", "nature"]
}

def sanitize_filename(filename):
    """Removes illegal characters and trims length."""
    # Remove ^J, newlines, and other weird chars
    clean_name = re.sub(r'[\^J\n\r\t]', '', filename)
    clean_name = re.sub(r'[<>:"/\\|?*]', '', clean_name) # Standard Windows illegal chars
    
    # Trim content to 150 chars max to avoid path limit errors
    name, ext = os.path.splitext(clean_name)
    if len(name) > 150:
        name = name[:150]
    
    return name.strip() + ext

def run_sorting():
    print("🧹 SANITIZING AND SORTING FILES...")

    if not os.path.exists(ARCHIVE_DIR):
        print(f"Archive not found: {ARCHIVE_DIR}")
        return

    # Create destination folders
    for folder in TAXONOMY.keys():
        os.makedirs(os.path.join(PROTOCOLS_ROOT, folder), exist_ok=True)

    files = os.listdir(ARCHIVE_DIR)
    
    for f in files:
        src_path = os.path.join(ARCHIVE_DIR, f)
        
        # 1. SANITIZE NAME
        safe_name = sanitize_filename(f)
        if safe_name != f:
            # Rename the file physically first
            new_src_path = os.path.join(ARCHIVE_DIR, safe_name)
            try:
                os.rename(src_path, new_src_path)
                print(f"🔧 Renamed bad file: {f} -> {safe_name}")
                src_path = new_src_path # Update path for moving step
                f = safe_name
            except Exception as e:
                print(f"❌ Could not rename {f}: {e}")
                continue

        # 2. SORT
        filename_lower = f.lower()
        best_cat = "Unsorted" # Default if no keyword matches
        
        for cat, keywords in TAXONOMY.items():
            if any(k in filename_lower for k in keywords):
                best_cat = cat
                break
        
        if best_cat != "Unsorted":
            dest = os.path.join(PROTOCOLS_ROOT, best_cat, f)
            try:
                shutil.move(src_path, dest)
                print(f"✅ [{best_cat}] {f}")
            except Exception as e:
                print(f"❌ Move Failed for {f}: {e}")

    print("\nDONE.")

if __name__ == "__main__":
    run_sorting()
