import os
import shutil
import markdown
import json
import re
import time
import glob
import stat

# --- LIBRARIES ---
HAS_DOCX = False
try:
    from docx import Document
    HAS_DOCX = True
except ImportError: pass

# --- CONFIG ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONTENT_DIR = os.path.join(BASE_DIR, "content")
# RESTORED TO PUBLIC
OUTPUT_DIR = os.path.join(BASE_DIR, "docs") 

# --- UTILS ---
def on_rm_error(func, path, exc_info):
    try:
        os.chmod(path, stat.S_IWRITE)
        os.unlink(path)
    except: pass

def nuclear_clean():
    if os.path.exists(OUTPUT_DIR):
        shutil.rmtree(OUTPUT_DIR, onerror=on_rm_error)
    # Remove docs folder if it exists (cleanup from previous error)
    if os.path.exists(os.path.join(BASE_DIR, "docs")):
        shutil.rmtree(os.path.join(BASE_DIR, "docs"), onerror=on_rm_error)

def sanitize_name(name):
    return "".join([c if (c.isalnum() or c in "._-") else "-" for c in name])

def make_safe_rel_path(rel_path_from_content):
    parts = rel_path_from_content.split(os.sep)
    safe_parts = [sanitize_name(p) for p in parts]
    base, ext = os.path.splitext(safe_parts[-1])
    safe_parts[-1] = base + ".html"
    return "/".join(safe_parts)

def get_docx_text_safe(path):
    if not HAS_DOCX: return None
    try:
        doc = Document(path)
        return "\n".join([p.text for p in doc.paragraphs])
    except: return None

def clean_text_for_search(text):
    if not text: return ""
    text = re.sub(r'<[^>]+>', '', text)
    return " ".join(text.replace('#', '').replace('*', '').replace('\n', ' ').split())

def clean_title_display(title):
    return title.replace("-", " ").replace("_", " ").replace(".md", "").replace(".txt", "").strip()

BUILD_ID = int(time.time())

# --- COPYRIGHT ---
COPYRIGHT_TEXT = f"""
<div class="footer-warning">
    <hr>
    <strong>⚠ RESTRICTED SYSTEM ACCESS ⚠</strong><br>
    PROPERTY OF CODEX OF COSMOS.<br>
    UNAUTHORIZED REPRODUCTION OR DISTRIBUTION IS STRICTLY PROHIBITED.<br>
    LOGGED IP ADDRESS. SESSION ID: {BUILD_ID}<br>
    ALL RIGHTS RESERVED © 2025
</div>
"""

# --- CSS (WITH COPY PROTECTION) ---
CSS_CONTENT = """
* { box-sizing: border-box; }
/* SECURITY LAYERS */
body { 
    -webkit-user-select: none; /* Safari */
    -ms-user-select: none; /* IE 10 and IE 11 */
    user-select: none; /* Standard syntax */
    margin: 0; padding: 0; background: #fff; color: #111; 
    font-family: 'Courier New', monospace; display: flex; flex-direction: row;
}
/* Allow selection only in search box */
#searchInput { user-select: text; -webkit-user-select: text; }

.sidebar {
    min-width: 350px; max-width: 350px; background: #f4f4f4;
    border-right: 2px solid #000; padding: 20px; height: 100vh; overflow-y: auto;
}
.main-content {
    flex-grow: 1; padding: 50px; height: 100vh; overflow-y: auto;
}
a { text-decoration: none; color: #000; cursor: pointer; }
.sidebar ul li { border-bottom: 1px solid #ddd; }
.sidebar ul li a { display: block; padding: 10px; background: #fff; }
.sidebar ul li a:hover { background: #ffebeb; color: #D00000; font-weight: bold; }
h1 { border-bottom: 4px solid #000; padding-bottom: 15px; margin-top: 0; }
ul { padding-left: 0; list-style: none; }
.submenu-title { margin-top: 20px; font-weight: bold; text-transform: uppercase; border-bottom: 2px solid #000; margin-bottom: 5px; padding-bottom: 5px; }
.footer-warning { margin-top: 50px; padding: 15px; font-size: 0.8em; text-align: center; background: #eee; }
.search-box { margin-bottom: 20px; padding-bottom: 20px; border-bottom: 2px solid #000; }
#searchInput { width: 100%; padding: 10px; border: 2px solid #000; }
#searchResults { display: none; border: 1px solid #000; padding: 10px; margin-top: 5px; background: #fff; }
.file-card { border: 2px solid #000; padding: 20px; background: #f9f9f9; text-align: center; margin-bottom: 20px; }
.zenodo-btn { display: inline-block; background: #000; color: #fff; padding: 12px 25px; font-weight: bold; margin-top: 10px; }
.zenodo-btn:hover { background: #D00000; }
pre { white-space: pre-wrap; background: #fafafa; padding: 15px; border: 1px solid #eee; }
"""

# --- JAVASCRIPT SHIELD (SEARCH + COPY BLOCK) ---
CODEX_SHIELD = f"""
<script src="ROOT_PLACEHOLDER/search_index.js?v={BUILD_ID}"></script>
<script>
// --- SEARCH LOGIC ---
function runSearch() {{
    const query = document.getElementById('searchInput').value.toLowerCase();
    const resultsDiv = document.getElementById('searchResults');
    resultsDiv.style.display = 'block';
    resultsDiv.innerHTML = '';
    
    if (query.length < 2) {{ resultsDiv.style.display = 'none'; return; }}
    if (typeof SEARCH_INDEX === 'undefined') {{ resultsDiv.innerHTML = 'Loading...'; return; }}
    
    const results = SEARCH_INDEX.filter(item => item.title.toLowerCase().includes(query) || item.text.toLowerCase().includes(query));
    if (results.length === 0) {{ resultsDiv.innerHTML = 'No matches.'; return; }}
    
    let html = '<ul>';
    results.forEach(item => {{
        let cleanPath = item.path;
        if (cleanPath.startsWith('/')) cleanPath = cleanPath.substring(1);
        const root = (typeof ROOT_PATH !== 'undefined' ? ROOT_PATH : "");
        html += `<li><a href="${{root}}${{cleanPath}}"><strong>${{item.title}}</strong></a></li>`;
    }});
    html += '</ul>';
    resultsDiv.innerHTML = html;
}}

// --- SECURITY PROTOCOL (BLOCK RIGHT CLICK & COPY) ---
document.addEventListener('contextmenu', event => event.preventDefault());
document.addEventListener('keydown', function(event) {{
    if (event.ctrlKey && (event.key === 'c' || event.key === 'u' || event.key === 's' || event.key === 'p')) {{
        event.preventDefault();
        alert('⚠ SECURITY ALERT: SYSTEM ACCESS RESTRICTED ⚠');
    }}
}});
</script>
"""

def build():
    nuclear_clean()
    os.makedirs(OUTPUT_DIR + "/css", exist_ok=True)
    with open(OUTPUT_DIR + "/css/style.css", "w", encoding="utf-8") as f: f.write(CSS_CONTENT)

    site_structure = {}
    search_index = []
    
    categories = [d for d in os.listdir(CONTENT_DIR) if os.path.isdir(os.path.join(CONTENT_DIR, d)) and not d.startswith('.')]
    categories.sort()

    print("--- RESTORING PUBLIC FOLDER ---")

    for cat in categories:
        site_structure[cat] = {} 
        cat_path = os.path.join(CONTENT_DIR, cat)
        
        for root, dirs, files in os.walk(cat_path):
            if os.path.abspath(OUTPUT_DIR) in os.path.abspath(root): continue
            
            # Filter garbage files
            valid_files = [f for f in files if f.lower().endswith(('.md', '.txt', '.docx', '.pdf')) and not f.startswith('~$')]
            if not valid_files: continue

            rel_subdir = os.path.relpath(root, cat_path)
            sub_name = "ROOT" if rel_subdir == "." else rel_subdir.replace("\\", "/")
            if sub_name not in site_structure[cat]: site_structure[cat][sub_name] = []

            for f in valid_files:
                full_path = os.path.join(root, f)
                ext = os.path.splitext(f)[1].lower()
                title = clean_title_display(os.path.splitext(f)[0])
                raw_text = ""
                html_body = ""
                
                # --- PDF ---
                if ext == '.pdf':
                    rel_from_content = os.path.relpath(full_path, CONTENT_DIR)
                    safe_pdf_rel = sanitize_name(os.path.dirname(rel_from_content)) + "/" + sanitize_name(os.path.basename(f))
                    dest_pdf = os.path.join(OUTPUT_DIR, safe_pdf_rel)
                    os.makedirs(os.path.dirname(dest_pdf), exist_ok=True)
                    shutil.copy2(full_path, dest_pdf)
                    
                    pdf_filename = sanitize_name(os.path.basename(f))
                    html_body = f"""<div class="file-card"><h3>DOCUMENT: {title}</h3><a href="{pdf_filename}" class="zenodo-btn" target="_blank">DOWNLOAD PDF</a></div>"""
                    raw_text = title 

                # --- DOCX ---
                elif ext == '.docx':
                    docx_text = get_docx_text_safe(full_path)
                    
                    if docx_text is None:
                        rel_from_content = os.path.relpath(full_path, CONTENT_DIR)
                        safe_docx_rel = sanitize_name(os.path.dirname(rel_from_content)) + "/" + sanitize_name(os.path.basename(f))
                        dest_docx = os.path.join(OUTPUT_DIR, safe_docx_rel)
                        os.makedirs(os.path.dirname(dest_docx), exist_ok=True)
                        shutil.copy2(full_path, dest_docx)
                        
                        docx_filename = sanitize_name(os.path.basename(f))
                        html_body = f"""<div class="file-card"><h3>DOCUMENT: {title}</h3><p>Preview unavailable. File is a Word Document.</p><a href="{docx_filename}" class="zenodo-btn" target="_blank">DOWNLOAD WORD FILE</a></div>"""
                        raw_text = title
                    else:
                        raw_text = docx_text
                        html_body = f"<pre>{docx_text}</pre>"
                
                # --- MARKDOWN / TEXT ---
                else: 
                    try:
                        with open(full_path, "r", encoding="utf-8", errors='ignore') as file:
                            content = file.read()
                            raw_text = content
                            html_body = markdown.markdown(content)
                            first_line = content.split('\n')[0]
                            if first_line.startswith('# '):
                                title = first_line.replace('# ', '').strip()
                    except: continue

                # PATH GENERATION
                rel_from_content = os.path.relpath(full_path, CONTENT_DIR)
                safe_html_rel_path = make_safe_rel_path(rel_from_content)
                
                parts = safe_html_rel_path.split("/")
                depth = max(0, len(parts) - 1)

                site_structure[cat][sub_name].append({
                    "title": title,
                    "rel_path": safe_html_rel_path,
                    "html_body": html_body,
                    "depth": depth
                })
                search_index.append({"title": title, "text": clean_text_for_search(raw_text), "path": safe_html_rel_path})

    with open(os.path.join(OUTPUT_DIR, "search_index.js"), "w", encoding="utf-8") as f:
        f.write(f"window.SEARCH_INDEX = {json.dumps(search_index)};")

    def get_sidebar(current_depth):
        prefix = "./" if current_depth == 0 else "../" * current_depth
        html = f"""<div class="search-box"><input type="text" id="searchInput" placeholder="SEARCH..." onkeyup="runSearch()"><div id="searchResults"></div></div><h3>SYSTEM INDEX</h3><ul><li><a href='{prefix}index.html'>[ HOME ]</a></li></ul>"""
        
        for cat, subfolders in sorted(site_structure.items()):
            html += f"<br><strong>{cat.upper().replace('-', ' ')}</strong>"
            html += "<ul>"
            sub_keys = sorted(subfolders.keys())
            if "ROOT" in sub_keys: 
                sub_keys.remove("ROOT")
                sub_keys.insert(0, "ROOT")
            
            for sub in sub_keys:
                files = sorted(subfolders[sub], key=lambda x: x['title'])
                if sub != "ROOT":
                    display = sub.split("/")[-1].replace("-", " ").upper()
                    html += f"<div class='submenu-title'>{display}</div>"
                for file in files:
                    link = prefix + file['rel_path']
                    html += f"<li><a href='{link}'>{file['title']}</a></li>"
            html += "</ul>"
        
        html += COPYRIGHT_TEXT
        return html

    for cat, subfolders in site_structure.items():
        for sub, files in subfolders.items():
            for file in files:
                depth = file['depth']
                sidebar = get_sidebar(depth)
                root_prefix = "./" if depth == 0 else "../" * depth
                current_shield = CODEX_SHIELD.replace("ROOT_PLACEHOLDER/", root_prefix)
                script_vars = f"<script>const ROOT_PATH = '{root_prefix}';</script>"
                
                full_html = f"""<!DOCTYPE html><html><head><title>{file['title']}</title><link rel="stylesheet" href="{root_prefix}css/style.css?v={BUILD_ID}">{script_vars}{current_shield}</head><body><div class="sidebar">{sidebar}</div><div class="main-content"><h1>{file['title']}</h1>{file['html_body']}</div></body></html>"""
                
                out_path = os.path.join(OUTPUT_DIR, file['rel_path'])
                os.makedirs(os.path.dirname(out_path), exist_ok=True)
                with open(out_path, "w", encoding="utf-8") as f: f.write(full_html)

    # INDEX
    index_html = f"""<!DOCTYPE html><html><head><title>CODEX OF COSMOS</title><link rel="stylesheet" href="css/style.css?v={BUILD_ID}"><script>const ROOT_PATH = './';</script>{CODEX_SHIELD.replace("ROOT_PLACEHOLDER/", "")}</head><body><div class="sidebar">{get_sidebar(0)}</div><div class="main-content"><h1>CODEX OF COSMOS</h1><p>SYSTEM ONLINE. PUBLIC FOLDER RESTORED.</p></div></body></html>"""
    with open(os.path.join(OUTPUT_DIR, "index.html"), "w", encoding="utf-8") as f: f.write(index_html)
    
    with open(os.path.join(BASE_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write('<meta http-equiv="refresh" content="0; url=./public/index.html">')

    print("\n--- DONE. PUBLIC FOLDER IS BACK. ---")

if __name__ == "__main__":
    build()

