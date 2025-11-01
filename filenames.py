import os

def save_filenames_to_text(folder_path, output_file="filenames.txt"):
    # Check if the folder exists
    if not os.path.exists(folder_path):
        print(f"Folder not found: {folder_path}")
        return

    # List all files (excluding directories)
    file_names = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    # Write file names to text file
    with open(output_file, "w", encoding="utf-8") as f:
        for name in file_names:
            f.write(name + "\n")

    print(f"✅ {len(file_names)} file names saved to {output_file}")


# Example usage:
# Replace this path with your folder path
folder_path = r"E:\coa"
save_filenames_to_text(folder_path)
