import os

# --- INTELLIGENT CONFIGURATION ---
# This line finds the exact folder where this script is sitting right now.
SOURCE_FOLDER = os.path.dirname(os.path.abspath(__file__))
OUTPUT_FILE = os.path.join(SOURCE_FOLDER, "ALL_RAW_CONTENT_MASTER_FILE.txt")
THIS_SCRIPT_NAME = os.path.basename(__file__)

def consolidate_files():
    print(f"Scanning current folder: {SOURCE_FOLDER}...")
    
    file_count = 0
    
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as outfile:
        # Walk through this folder and all subfolders
        for root, dirs, files in os.walk(SOURCE_FOLDER):
            for filename in files:
                
                # CRITICAL: Skip the script itself and the output file (no infinite loops)
                if filename == THIS_SCRIPT_NAME or filename == os.path.basename(OUTPUT_FILE):
                    continue
                
                # Check for text files (Add .docx logic later if needed, mostly text/md for now)
                if filename.lower().endswith(('.txt', '.md', '.markdown', '.js', '.json', '.html', '.css', '.py')):
                    file_path = os.path.join(root, filename)
                    
                    try:
                        with open(file_path, 'r', encoding='utf-8', errors='ignore') as infile:
                            content = infile.read()
                            
                            # Write clear headers
                            outfile.write("\n" + "#" * 50 + "\n")
                            outfile.write(f"FILENAME: {filename}\n")
                            outfile.write(f"FULL_PATH: {file_path}\n")
                            outfile.write("#" * 50 + "\n\n")
                            
                            outfile.write(content)
                            outfile.write("\n\n")
                            
                            file_count += 1
                            print(f"Merged: {filename}")
                            
                    except Exception as e:
                        print(f"Skipped {filename}: {e}")

    print(f"\nSUCCESS! {file_count} files merged.")
    print(f"OUTPUT SAVED TO: {OUTPUT_FILE}")

if __name__ == "__main__":
    consolidate_files()

