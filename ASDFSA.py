import os
import zipfile
import xml.etree.ElementTree as ET

# --- CONFIGURATION ---
BASE_DIR = os.getcwd()
CONTENT_DIR = os.path.join(BASE_DIR, "content")
TARGET_FOLDERS = [
    os.path.join(CONTENT_DIR, "01-Master-Papers"),
    os.path.join(CONTENT_DIR, "00-ARCHIVE"),
    os.path.join(CONTENT_DIR, "appendices")
]

def extract_text_from_docx(docx_path):
    """
    Extracts text from DOCX using standard Python libraries (zipfile + xml).
    No external dependencies required.
    """
    try:
        with zipfile.ZipFile(docx_path) as docx:
            xml_content = docx.read('word/document.xml')
            tree = ET.fromstring(xml_content)
            
            # XML namespace for Word
            namespaces = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
            
            text_parts = []
            # Find all <w:p> (paragraphs)
            for paragraph in tree.findall('.//w:p', namespaces):
                texts = [node.text for node in paragraph.findall('.//w:t', namespaces) if node.text]
                if texts:
                    text_parts.append(''.join(texts))
            
            return '\n\n'.join(text_parts)
    except Exception as e:
        print(f"Error reading {docx_path}: {e}")
        return None

def run_conversion():
    print("🔄 STARTING NO-INSTALL CONVERSION...")
    converted_count = 0
    
    for folder in TARGET_FOLDERS:
        if not os.path.exists(folder):
            continue
            
        print(f"📂 Scanning: {folder}")
        files = os.listdir(folder)
        
        for f in files:
            filepath = os.path.join(folder, f)
            filename, ext = os.path.splitext(f)
            
            # Check for DOCX
            if ext.lower() == '.docx':
                md_path = os.path.join(folder, filename + ".md")
                
                # Only convert if MD doesn't exist
                if not os.path.exists(md_path):
                    print(f"📄 Converting: {f}")
                    text = extract_text_from_docx(filepath)
                    
                    if text:
                        with open(md_path, 'w', encoding='utf-8') as md_file:
                            md_file.write(text)
                        print(f"✅ Created: {filename}.md")
                        converted_count += 1
            
            # (Note: PDF conversion without libraries is not reliably possible in pure Python.
            # This script focuses on DOCX to solve the majority of your issues.)

    print(f"\n🎉 DONE. Converted {converted_count} files.")

if __name__ == "__main__":
    run_conversion()
