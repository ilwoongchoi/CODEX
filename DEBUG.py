import os

# --- CONFIG ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONTENT_DIR = os.path.join(BASE_DIR, "content")

print("="*60)
print(" DIAGNOSTIC REPORT: FOLDER STRUCTURE VERIFICATION")
print("="*60)
print(f"Script location: {BASE_DIR}")
print(f"Scanning target: {CONTENT_DIR}")
print("-" * 60)

if not os.path.exists(CONTENT_DIR):
    print("CRITICAL ERROR: 'content' folder NOT FOUND.")
    print("The script cannot see your files.")
    exit()

found_files = 0
found_folders = []

# Walk through the directory and print the structure
for root, dirs, files in os.walk(CONTENT_DIR):
    # Calculate depth to indent output
    level = root.replace(CONTENT_DIR, '').count(os.sep)
    indent = ' ' * 4 * (level)
    folder_name = os.path.basename(root)
    
    if folder_name == "content": folder_name = "[CONTENT ROOT]"
    
    print(f"{indent}📂 {folder_name}/")
    found_folders.append(folder_name)
    
    subindent = ' ' * 4 * (level + 1)
    for f in files:
        if f.startswith('.'): continue # Skip hidden system files
        found_files += 1
        # specific check for the archive files you mentioned
        if level < 2: # Only show files at top levels to avoid spamming
            print(f"{subindent}📄 {f}")
        elif len(files) > 0 and files.index(f) == 0:
             print(f"{subindent}📄 ... {len(files)} files found in this folder ...")

print("="*60)
print(f"TOTAL FILES FOUND: {found_files}")
print("="*60)

# --- SPECIFIC CHECKS ---
if "00-archive" not in found_folders:
    print("❌ ALERT: '00-archive' folder is MISSING from the scan!")
else:
    print("✅ '00-archive' folder was found.")

if found_files == 0:
    print("❌ ALERT: The 'content' folder is EMPTY.")
