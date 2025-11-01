import os
import shutil
import docx
import pytesseract
from PIL import Image
from PyPDF2 import PdfReader

# ==== CONFIGURATION ====
base_folder = r"E:\coa"
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"  # Update path if needed

# === Chemical groups (merged variants) ===
chemical_groups = {
    "Alpha Arbutin": ["A-Arbutin", "Alpha Arbutin"],
    "Almond Oil": ["Almond Oil"],
    "Citric Acid": ["Citric Acid"],
    "Acrypol 980": ["Acrypol 980"],
    "Imidazolidinyl Urea": ["Imidazolidinyl Urea", "Imdiazolidinyl Urea"],
    "Polysorbate 20": ["Polysorbate 20", "Tween 20", "Sorbiline L.EP", "T 20"],
    "Salicylic Acid": ["Salicylic Acid", "SE820"],
    "EDTA Disodium": ["EDTA Disodium", "EDTA NA2"],
    "Hyaluronic Acid": ["Hyaluronic Acid"],
    "Tilamar PDO": ["Tilamar PDO", "Propanediol PDO"],
    "Propanediol": ["Propanediol"],
    "Deionized Water": ["DI Water"],
    "Sharomix EG10": ["Sharomix EG10"],
    "D-Panthenol": ["D-Panthenol", "Panthenol"],
    "Flaxseed": ["Flax", "Flaxseed"],
    "Glycerin": ["Glycerin", "Glycerine"],
    "GMS SE 40": ["GMS SE 40"],
    "Kojic Acid": ["Kojic Acid"],
    "Niacinamide": ["Niacinamide"],
    "Saliguard HDC": ["Saliguard HDC", "SALIGUARD HDC"],
    "Stearic Acid": ["Stearic", "Stearic Acid"],
    "Rosehip Oil": ["Rosehip"],
    "Coriander": ["Coriander"],
    "TCFF Fragrance": ["TCFF Fragrance", "Fragrance"],
    "Ultrez 30": ["Ultrez 30"]
}

# === Helper functions ===
def read_pdf(file_path):
    try:
        text = ""
        reader = PdfReader(file_path)
        for page in reader.pages:
            text += page.extract_text() or ""
        return text
    except Exception as e:
        print(f"PDF read error {file_path}: {e}")
        return ""

def read_docx(file_path):
    try:
        doc = docx.Document(file_path)
        return "\n".join([p.text for p in doc.paragraphs])
    except Exception as e:
        print(f"DOCX read error {file_path}: {e}")
        return ""

def read_image(file_path):
    try:
        img = Image.open(file_path)
        return pytesseract.image_to_string(img)
    except Exception as e:
        print(f"Image read error {file_path}: {e}")
        return ""

def move_to_folder(file_path, folder_name):
    target_folder = os.path.join(base_folder, folder_name)
    os.makedirs(target_folder, exist_ok=True)
    shutil.move(file_path, os.path.join(target_folder, os.path.basename(file_path)))
    print(f"Moved: {os.path.basename(file_path)} → {folder_name}/")


# === Main process ===
for filename in os.listdir(base_folder):
    file_path = os.path.join(base_folder, filename)

    if not os.path.isfile(file_path):
        continue

    moved = False
    lower_name = filename.lower()

    # --- Step 1: Match by filename ---
    for folder_name, aliases in chemical_groups.items():
        for alias in aliases:
            if alias.lower().replace(" ", "") in lower_name.replace(" ", ""):
                move_to_folder(file_path, folder_name)
                moved = True
                break
        if moved:
            break

    # --- Step 2: If not matched, read content and match ---
    if not moved:
        ext = os.path.splitext(filename)[1].lower()
        text_content = ""

        if ext in [".pdf"]:
            text_content = read_pdf(file_path)
        elif ext in [".docx"]:
            text_content = read_docx(file_path)
        elif ext in [".jpg", ".jpeg", ".png"]:
            text_content = read_image(file_path)

        if text_content:
            text_lower = text_content.lower()
            for folder_name, aliases in chemical_groups.items():
                for alias in aliases:
                    if alias.lower() in text_lower:
                        move_to_folder(file_path, folder_name)
                        moved = True
                        break
                if moved:
                    break

    # --- Step 3: If still not matched, move to _Unsorted ---
    if not moved:
 #       other_folder = os.path.join(base_folder, "_Unsorted")
  #      os.makedirs(other_folder, exist_ok=True)
   #     shutil.move(file_path, os.path.join(other_folder, filename))
        print(f"Unsorted: {filename}")

print("\n✅ Smart file organization completed.")
