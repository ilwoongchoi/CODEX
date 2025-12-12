import os

def scan_project():
    print("=== PROJECT STRUCTURE AND CONTENT SCAN ===\n")
    
    # Define what to scan
    target_dir = "content"
    
    if not os.path.exists(target_dir):
        print(f"ERROR: Directory '{target_dir}' not found.")
        return

    # Walk through all files
    for root, dirs, files in os.walk(target_dir):
        for filename in files:
            # Get the full path
            filepath = os.path.join(root, filename)
            
            # Print the File Name clearly
            print(f"\n{'='*60}")
            print(f"FILE: {filepath}")
            print(f"{'='*60}\n")
            
            # Read and Print the Content
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                    print(content)
            except Exception as e:
                print(f"[Error reading file: {e}]")
            
            print("\n" + "-"*60)

if __name__ == "__main__":
    scan_project()
