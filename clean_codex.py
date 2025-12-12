import os
import shutil

# --- CONFIGURATION ---
WEBSITE_CONTENT_DIR = "content/Appendices"
BACKUP_DIR = "C:/Users/User/OneDrive/Documents/Codex_Removed_Chats"

# Keywords that indicate a "Chat Log" or "Draft"
BAD_KEYWORDS = [
    "I-need-you",
    "yes-a-bit",
    "Answer",
    "commands",
    "absorb-everything",
    "make-connections",
    "MAKE-CONNECTIONS",
    "codex-appendum",
    "quantumjournal", # Assuming this was a raw PDF dump
    "https", # Web dumps
    "D2-1" # Random images
]

def clean_codex():
    if not os.path.exists(BACKUP_DIR):
        os.makedirs(BACKUP_DIR)
        print(f"Created Backup Folder: {BACKUP_DIR}")

    print(f"Scanning {WEBSITE_CONTENT_DIR} for conversation logs...")
    
    moved_count = 0
    
    for root, dirs, files in os.walk(WEBSITE_CONTENT_DIR):
        for f in files:
            # Check if filename contains any "Bad Keywords"
            is_bad = any(keyword in f for keyword in BAD_KEYWORDS)
            
            # Also catch generic small/weird files if needed
            
            if is_bad:
                src_path = os.path.join(root, f)
                dst_path = os.path.join(BACKUP_DIR, f)
                
                try:
                    shutil.move(src_path, dst_path)
                    print(f"MOVED (Conversational): {f} -> Documents")
                    moved_count += 1
                except Exception as e:
                    print(f"Error moving {f}: {e}")

    print(f"\nCLEANUP COMPLETE.")
    print(f"Moved {moved_count} conversation files to: {BACKUP_DIR}")
    print("Your website folder now contains ONLY the Formal Papers.")

if __name__ == "__main__":
    clean_codex()
