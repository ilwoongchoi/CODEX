import os
import docx

SOURCE_DIR = "content/appendices"

def convert_docx_to_md():
    print(f"Scanning {SOURCE_DIR} for .docx files...")
    
    for root, dirs, files in os.walk(SOURCE_DIR):
        for f in files:
            if f.endswith(".docx") and not f.startswith("~$"):
                full_path = os.path.join(root, f)
                md_path = full_path.replace(".docx", ".md")
                
                try:
                    doc = docx.Document(full_path)
                    text = f"# {f.replace('.docx', '')}\n\n"
                    for para in doc.paragraphs:
                        text += para.text + "\n\n"
                    
                    with open(md_path, "w", encoding="utf-8") as md_file:
                        md_file.write(text)
                    print(f"Converted: {f} -> {md_path}")
                except Exception as e:
                    print(f"Error converting {f}: {e}")

if __name__ == "__main__":
    convert_docx_to_md()
