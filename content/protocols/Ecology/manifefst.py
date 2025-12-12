import os
import docx  # Needs: pip install python-docx
import PyPDF2 # Needs: pip install PyPDF2

def extract_text_from_docx(path):
    try:
        doc = docx.Document(path)
        return "\n".join([para.text for para in doc.paragraphs])
    except:
        return "[Error reading DOCX file]"

def extract_text_from_pdf(path):
    try:
        text = ""
        with open(path, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            for page in reader.pages:
                text += page.extract_text() + "\n"
        return text
    except:
        return "[Error reading PDF file]"

def harvest_all_content():
    output_filename = "FULL_LIBRARY_CONTENT_DUMP.txt"
    current_folder = os.getcwd()
    
    print(f"Starting Harvest in: {current_folder}")
    print("This might take a moment if files are large...")
    
    with open(output_filename, "w", encoding="utf-8") as outfile:
        outfile.write(f"--- CODEX MASSIVE CONTENT DUMP ---\n")
        outfile.write(f"--- COLLECTED FROM: {current_folder} ---\n\n")
        
        file_count = 0
        
        # Walk through all subfolders
        for root, dirs, files in os.walk(current_folder):
            for file in sorted(files):
                path = os.path.join(root, file)
                filename = file.lower()
                content = ""
                
                # Filter for valid document types
                if filename.endswith(".docx") and "~$" not in filename: # Skip temp files
                    print(f"Processing DOCX: {file}")
                    content = extract_text_from_docx(path)
                elif filename.endswith(".pdf"):
                    print(f"Processing PDF: {file}")
                    content = extract_text_from_pdf(path)
                elif filename.endswith((".txt", ".md", ".py")):
                    if "FULL_LIBRARY_CONTENT_DUMP" in filename: continue # Skip the output file itself
                    print(f"Processing TEXT: {file}")
                    try:
                        with open(path, "r", encoding="utf-8", errors='ignore') as f:
                            content = f.read()
                    except:
                        content = "[Error reading text file]"
                else:
                    continue # Skip images, zips, etc.

                # Write content to the master dump file
                outfile.write("\n" + "#"*60 + "\n")
                outfile.write(f"FILENAME: {file}\n")
                outfile.write(f"PATH: {path}\n")
                outfile.write("#"*60 + "\n\n")
                outfile.write(content)
                outfile.write("\n\n")
                
                file_count += 1

    print("\n" + "="*50)
    print("HARVEST COMPLETE!")
    print(f"Processed {file_count} files.")
    print(f"All content saved to: {output_filename}")
    print("="*50)

if __name__ == "__main__":
    harvest_all_content()
