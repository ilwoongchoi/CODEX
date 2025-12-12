import os
import shutil

# --- CONFIGURATION ---
BASE_DIR = os.getcwd()
CONTENT_DIR = os.path.join(BASE_DIR, "content")

# TARGET FOLDERS
SOURCE_DIR = os.path.join(CONTENT_DIR, "appendices")  # SOURCE: The Mess
ARCHIVE_DIR = os.path.join(CONTENT_DIR, "00-ARCHIVE") # DEST: The Junk
MASTER_DIR = os.path.join(CONTENT_DIR, "01-Master-Papers") # DEST: The Gems

# --- THE LOGIC ---
# 1. We look for these keywords inside the file.
# 2. If we can't read the file, we look for these strings in the FILENAME.
DEFINITIONS = {
    "01-Volume-1-The-Physics": {
        "keywords": ["210 joules", "1.32%", "1/32 charge", "thermodynamic debt", "placozoan", "11th electron"],
        "filename_match": ["history", "physics", "thermodynamic", "circuit"]
    },
    "02-Volume-2-The-Archetypes": {
        "keywords": ["solar archetype", "scalar archetype", "big man", "small woman", "hierarchy of deceit", "oxytocin"],
        "filename_match": ["codex", "appendum", "archetype", "deceit"]
    },
    "03-Volume-3-The-Pathology": {
        "keywords": ["vertex overload", "neural burnout", "warburg", "self-harm", "autoimmunity", "depression"],
        "filename_match": ["pathology", "harm", "notes", "collapse"]
    },
    "04-Volume-4-The-Origin": {
        "keywords": ["electrochemical origin", "origin of life", "vent", "alkaline"],
        "filename_match": ["origin", "electrochemical"]
    }
}

def read_file_content(filepath):
    """Attempts to read text. Returns empty string if failed."""
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            return f.read().lower()
    except:
        try:
            # Fallback for binary/docx - just read raw bytes as string
            with open(filepath, 'rb') as f:
                return str(f.read()).lower()
        except:
            return ""

def classify_file(filepath, filename):
    """Checks content FIRST. If that fails/is unsure, checks FILENAME."""
    text = read_file_content(filepath)
    filename_lower = filename.lower()
    
    best_category = None
    highest_score = 0

    for category, logic in DEFINITIONS.items():
        score = 0
        
        # 1. Check Content Keywords
        for word in logic["keywords"]:
            if word in text:
                score += 2  # Content match is worth more
        
        # 2. Check Filename (Backup)
        for name_part in logic["filename_match"]:
            if name_part in filename_lower:
                score += 5  # Strong signal if filename matches explicit topics
        
        if score > highest_score:
            highest_score = score
            best_category = category
            
    # Threshold: Must have at least a decent match (score > 2)
    if highest_score >= 2:
        return best_category
    return None

def run_librarian():
    print("🔴 EXECUTING FINAL SORTING PROTOCOL...")

    # Check Paths
    if not os.path.exists(SOURCE_DIR):
        print(f"CRITICAL ERROR: Could not find folder: {SOURCE_DIR}")
        return

    os.makedirs(ARCHIVE_DIR, exist_ok=True)
    os.makedirs(MASTER_DIR, exist_ok=True)

    files = [f for f in os.listdir(SOURCE_DIR) if os.path.isfile(os.path.join(SOURCE_DIR, f))]
    
    if not files:
        print("Folder is empty. Nothing to do.")
        return

    count_moved = 0
    count_archived = 0

    for filename in files:
        filepath = os.path.join(SOURCE_DIR, filename)
        
        # Skip system files
        if filename.startswith("."): 
            continue

        category = classify_file(filepath, filename)

        if category:
            # IT IS A MASTER PAPER
            new_name = f"{category}.md"
            dest_path = os.path.join(MASTER_DIR, new_name)
            
            # Copy and Rename
            shutil.copy2(filepath, dest_path)
            # Move original to Archive
            shutil.move(filepath, os.path.join(ARCHIVE_DIR, filename))
            
            print(f"✅ SORTED: {filename} -> {new_name}")
            count_moved += 1
        else:
            # IT IS NOISE
            shutil.move(filepath, os.path.join(ARCHIVE_DIR, filename))
            print(f"🗑️  ARCHIVED: {filename}")
            count_archived += 1

    print("\n------------------------------------------------")
    print(f"DONE. {count_moved} Master Papers created.")
    print(f"{count_archived} files moved to Archive.")
    print("------------------------------------------------")

if __name__ == "__main__":
    run_librarian()


