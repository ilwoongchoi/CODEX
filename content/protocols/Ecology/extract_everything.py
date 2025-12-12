import os
import docx  # Requires: pip install python-docx
import PyPDF2 # Requires: pip install PyPDF2

# --- CONFIGURATION ---
SOURCE_FOLDER = os.path.dirname(os.path.abspath(__file__))
OUTPUT_FILE = os.path.join(SOURCE_FOLDER, "ALL_RAW_CONTENT_MASTER_FILE_FULL.txt")
THIS_SCRIPT = os.path.basename(__file__)

def read_docx(file_path):
    try:
        doc = docx.Document(file_path)
        full_text = []
        for para in doc.paragraphs:
            full_text.append(para.text)
        return '\n'.join(full_text)
    except Exception as e:
        return f"[ERROR READING DOCX: {e}]"

def read_pdf(file_path):
    try:
        text = ""
        with open(file_path, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            for page in reader.pages:
                text += page.extract_text() + "\n"
        return text
    except Exception as e:
        return f"[ERROR READING PDF: {e}]"

def main():
    print(f"Starting Deep Extraction in: {SOURCE_FOLDER}")
    
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as outfile:
        for root, dirs, files in os.walk(SOURCE_FOLDER):
            for filename in files:
                if filename == THIS_SCRIPT or filename.startswith("ALL_RAW"):
                    continue
                
                file_path = os.path.join(root, filename)
                content = ""
                
                # DETECT FILE TYPE
                if filename.lower().endswith('.docx'):
                    print(f"Extracting DOCX: {filename}...")
                    content = read_docx(file_path)
                
                elif filename.lower().endswith('.pdf'):
                    print(f"Extracting PDF: {filename}...")
                    content = read_pdf(file_path)
                
                elif filename.lower().endswith(('.txt', '.md', '.markdown')):
                    print(f"Reading TEXT: {filename}...")
                    try:
                        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                            content = f.read()
                    except:
                        content = "[Encoding Error]"
                
                else:
                    continue # Skip other files

                # WRITE TO MASTER FILE
                if content:
                    outfile.write("\n" + "="*50 + "\n")
                    outfile.write(f"FILENAME: {filename}\n")
                    outfile.write("="*50 + "\n")
                    outfile.write(content)
                    outfile.write("\n\n")

    print(f"\nDONE. Saved to: {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
