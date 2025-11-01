import os
import shutil

# === Set your folder path ===
base_folder = r"E:\coa"

# === Map similar chemical names to unified folder names ===
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
    "Saliguard HDC": ["Saliguard HDC"],
    "Stearic Acid": ["Stearic", "Stearic Acid"],
    "Rosehip Oil": ["Rosehip"],
    "Coriander": ["Coriander"],
    "TCFF Fragrance": ["TCFF Fragrance", "Fragrance"],
    "Ultrez 30": ["Ultrez 30"]
}

# === Move files ===
for filename in os.listdir(base_folder):
    file_path = os.path.join(base_folder, filename)

    if not os.path.isfile(file_path):
        continue

    moved = False
    lower_name = filename.lower()

    for folder_name, aliases in chemical_groups.items():
        for alias in aliases:
            if alias.lower().replace(" ", "") in lower_name.replace(" ", ""):
                target_folder = os.path.join(base_folder, folder_name)
                os.makedirs(target_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(target_folder, filename))
                print(f"Moved: {filename} → {folder_name}/")
                moved = True
                break
        if moved:
            break

    if not moved:
      #  other_folder = os.path.join(base_folder, "_Unsorted")
       # os.makedirs(other_folder, exist_ok=True)
        #shutil.move(file_path, os.path.join(other_folder, filename))
        print(f"Unsorted: {filename}")

print("\n✅ Files grouped successfully by chemical names.")
