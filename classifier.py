import os
import shutil
import zipfile
import xml.etree.ElementTree as ET

# --- CONFIGURATION ---
BASE_DIR = os.getcwd()
ARCHIVE_DIR = os.path.join(BASE_DIR, "content", "00-ARCHIVE")
PROTOCOLS_ROOT = os.path.join(BASE_DIR, "content", "protocols")

# TARGET FOLDERS & KEYWORDS
TAXONOMY = {
    "Physics": [
        "thermodynamic", "electron", "charge", "quantum", "gravity", "voltage", 
        "entropy", "time", "1/32", "mismatch", "dimensional", "biophysics", "zeno"
    ],
    "Evolution": [
        "placozoan", "merger", "algae", "symbiosis", "sexual dimorphism", 
        "origin", "darwin", "selection", "evolutionary", "history", "ancient"
    ],
    "Biochemistry": [
        "krebs", "tca", "glycolysis", "glutamate", "gaba", "acetyl", "enzyme", 
        "molecular", "protein", "synthesis", "metabolic", "chemistry", "calcium", "plp"
    ],
    "Medicine": [
        "cancer", "oncology", "diabetes", "autoimmunity", "disease", "pathology", 
        "treatment", "protocol", "clinical", "heart", "liver", "organ", "sclerosis", 
        "syndrome", "disorder", "als", "lupus"
    ],
    "Psychiatry": [
        "depression", "anxiety", "schizophrenia", "autism", "adhd", "bipolar", 
        "dopamine", "serotonin", "brain", "neuron", "mental", "psychology", 
        "neurotransmitter", "ocd", "suicide"
    ],
    "Ecology": [
        "soil", "root", "plant", "climate", "environment", "earth", "gaia", 
        "atmosphere", "nature", "rhizosphere", "desalination", "agriculture"
    ]
}

def extract_text_safe(filepath):
    """Reads text from MD, TXT, or DOCX without crashing."""
    ext = os.path.splitext(filepath)[1].lower()
    content = ""
    try:
        if ext in ['.md', '.txt', '.py', '.html']:
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
        elif ext == '.docx':
            with zipfile.ZipFile(filepath) as docx:
                xml_content = docx.read('word/document.xml')
                tree = ET.fromstring(xml_content)
                namespaces = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
                texts = [node.text for node in tree.findall('.//w:t', namespaces) if node.text]
                content = " ".join(texts)
    except:
        pass # If fail, we rely on filename
    return content.lower()

def run_sorting():
    print("🧬 INITIALIZING PROTOCOL SORTING...")

    if not os.path.exists(ARCHIVE_DIR):
        print(f"ERROR: Archive folder not found at {ARCHIVE_DIR}")
        return

    # Create the folder structure
    for folder in TAXONOMY.keys():
        path = os.path.join(PROTOCOLS_ROOT, folder)
        os.makedirs(path, exist_ok=True)

    files = [f for f in os.listdir(ARCHIVE_DIR) if os.path.isfile(os.path.join(ARCHIVE_DIR, f))]
    count = 0

    for f in files:
        filepath = os.path.join(ARCHIVE_DIR, f)
        
        # 1. READ DATA
        filename_clean = f.lower().replace("-", " ").replace("_", " ")
        file_content = extract_text_safe(filepath)
        combined_text = filename_clean + " " + file_content

        # 2. SCORE CATEGORIES
        scores = {cat: 0 for cat in TAXONOMY}
        
        for cat, keywords in TAXONOMY.items():
            for k in keywords:
                if k in combined_text:
                    scores[cat] += 1
                    if k in filename_clean:
                        scores[cat] += 5  # Filename matches are worth more

        # 3. PICK WINNER
        best_cat = max(scores, key=scores.get)
        
        if scores[best_cat] > 0:
            dest = os.path.join(PROTOCOLS_ROOT, best_cat, f)
            shutil.move(filepath, dest)
            print(f"✅ [{best_cat.upper()}] {f}")
            count += 1
        else:
            print(f"⚠️  UNCLASSIFIED: {f} (Leaving in Archive)")

    print(f"\n------------------------------------------------")
    print(f"SORT COMPLETE. {count} files organized into Protocols.")
    print(f"------------------------------------------------")

if __name__ == "__main__":
    run_sorting()
