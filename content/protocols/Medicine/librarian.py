import os

# --- THE CLASSIFICATION LOGIC ---
# Adjust these keywords if you have specific terms for your papers.
BRANCHES = {
    "CORE_THEORY": {
        "title": "BRANCH 1: THE CORE THEORY",
        "desc": "Foundational Physics, Codex, and Bioenergetics.",
        "keywords": ["origin", "codex", "appendum", "bioenergetic", "metabol", "physic", "dimension", "geometry", "thermodynamic", "entropy", "final"],
        "files": []
    },
    "MEDICAL_PROTOCOLS": {
        "title": "BRANCH 2: THE MEDICAL PROTOCOLS",
        "desc": "Specific Diseases, Cures, and Triad Solutions.",
        "keywords": ["protocol", "triad", "cancer", "autoimmune", "rheumatoid", "schizophrenia", "parkinson", "als", "lou", "scoliosis", "sciatica", "tinnitus", "sjogren", "hair", "vertex", "snoring", "apnea", "sibo", "gut", "colon", "liver", "kidney", "restoring", "aging", "rejuvenation", "telomere", "mitochondria", "choline", "acid", "shield", "warburg"],
        "files": []
    },
    "COSMIC_IMPERATIVE": {
        "title": "BRANCH 3: THE COSMIC IMPERATIVE",
        "desc": "Artificial Sun, Space, and Dark Matter.",
        "keywords": ["sun", "fusion", "dark", "matter", "hubble", "tensor", "void", "starless", "infrared", "galaxy", "cosmic", "black", "hole", "electron", "11th", "neural-arc", "viscosity"],
        "files": []
    },
    "SOCIAL_CAREER": {
        "title": "BRANCH 4: SOCIAL & CAREER",
        "desc": "Archetypes, Psychology, and Society.",
        "keywords": ["career", "social", "archetype", "phenotype", "psychology", "plea", "truth", "society", "city", "androgen", "estrogen", "dominance", "predictive", "model"],
        "files": []
    },
    "UNCATEGORIZED": {
        "title": "UNCATEGORIZED PAPERS",
        "desc": "Files that didn't match specific keywords. Check these manually.",
        "keywords": [], 
        "files": []
    }
}

def categorize_file(filename):
    """Sorts a file into a branch based on keywords in the filename."""
    name_lower = filename.lower()
    
    # Check each branch for matching keywords
    for branch_key, data in BRANCHES.items():
        if branch_key == "UNCATEGORIZED": continue
        for keyword in data["keywords"]:
            if keyword in name_lower:
                return branch_key
    
    # If no match found, it goes to Uncategorized
    return "UNCATEGORIZED"

def generate_index():
    # 1. Get all files in the current directory
    # (Filters for document types only)
    files = [f for f in os.listdir('.') if os.path.isfile(f) and f.lower().endswith(('.docx', '.pdf', '.txt', '.md'))]
    
    # Remove the script itself and the output file from the list
    if "librarian.py" in files: files.remove("librarian.py")
    if "CODEX_INDEX.html" in files: files.remove("CODEX_INDEX.html")

    # 2. Sort files into branches
    count = 0
    for f in files:
        branch = categorize_file(f)
        BRANCHES[branch]["files"].append(f)
        count += 1

    # 3. Generate HTML
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>CODEX LIBRARY INDEX</title>
        <style>
            body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #1a1a1a; color: #e0e0e0; max-width: 1200px; margin: 0 auto; padding: 40px; }
            h1 { text-align: center; color: #d4af37; border-bottom: 2px solid #444; padding-bottom: 20px; }
            .stats { text-align: center; color: #888; margin-bottom: 40px; }
            .branch { background: #252525; margin-bottom: 30px; padding: 25px; border-radius: 8px; border: 1px solid #333; box-shadow: 0 4px 6px rgba(0,0,0,0.3); }
            .branch-header { border-bottom: 1px solid #444; padding-bottom: 10px; margin-bottom: 20px; }
            .branch-title { font-size: 1.5em; font-weight: bold; color: #fff; }
            .branch-desc { color: #aaa; margin-top: 5px; }
            .file-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(350px, 1fr)); gap: 15px; }
            .file-card { background: #2d2d2d; padding: 15px; border-radius: 4px; border-left: 3px solid #d4af37; transition: transform 0.2s, background 0.2s; }
            .file-card:hover { transform: translateY(-2px); background: #333; }
            .file-link { text-decoration: none; color: #e0e0e0; font-size: 0.95em; word-break: break-word; display: block; }
            .uncategorized { border-left-color: #ff4444; }
        </style>
    </head>
    <body>
        <h1>THE CODEX LIBRARY</h1>
        <div class="stats">System Scan Complete. Total Files Indexed: """ + str(count) + """</div>
    """

    # Branch Order
    order = ["CORE_THEORY", "MEDICAL_PROTOCOLS", "COSMIC_IMPERATIVE", "SOCIAL_CAREER", "UNCATEGORIZED"]

    for key in order:
        data = BRANCHES[key]
        if not data["files"]: continue # Hide empty branches
        
        card_class = "file-card uncategorized" if key == "UNCATEGORIZED" else "file-card"
        
        html += f"""
        <div class="branch">
            <div class="branch-header">
                <div class="branch-title">{data['title']}</div>
                <div class="branch-desc">{data['desc']} ({len(data['files'])} files)</div>
            </div>
            <div class="file-grid">
        """
        
        for filename in sorted(data["files"]):
            html += f"""
                <div class="{card_class}">
                    <a href="{filename}" class="file-link" target="_blank">{filename}</a>
                </div>
            """
            
        html += """
            </div>
        </div>
        """

    html += """
    </body>
    </html>
    """

    # 4. Write to file
    with open("CODEX_INDEX.html", "w", encoding="utf-8") as f:
        f.write(html)
    
    print(f"SUCCESS: Indexed {count} files. Open 'CODEX_INDEX.html' to see your library.")

if __name__ == "__main__":
    generate_index()

