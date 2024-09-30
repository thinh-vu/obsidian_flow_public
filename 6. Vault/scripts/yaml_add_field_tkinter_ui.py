import os
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
import yaml

def append_field_to_yaml(file_path, field_name, field_value=None):
    """Reads the YAML frontmatter of a markdown file, appends a field if missing."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        # Identify YAML frontmatter boundaries
        if lines[0].strip() == "---":
            frontmatter_end = lines.index("---\n", 1)
            yaml_content = "".join(lines[1:frontmatter_end])
            frontmatter = yaml.safe_load(yaml_content) or {}

            # Check if the field exists in frontmatter
            if field_name not in frontmatter:
                # Append the new field
                frontmatter[field_name] = field_value if field_value else ""

                # Rebuild the file with updated frontmatter
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write("---\n")
                    yaml.dump(frontmatter, file, default_flow_style=False, sort_keys=False)
                    file.write("---\n")
                    file.writelines(lines[frontmatter_end+1:])

    except Exception as e:
        print(f"Error processing {file_path}: {e}")

def process_directory(directory, field_name, field_value):
    """Loops over all *.md files in a directory, appending the specified field if missing."""
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                print(f"Processing file: {file_path}")
                append_field_to_yaml(file_path, field_name, field_value)

def browse_directory():
    """Opens a dialog for the user to select a directory."""
    directory = filedialog.askdirectory()
    if directory:
        return directory
    else:
        return None

def add_field():
    """Handles the logic for the field addition through the GUI."""
    directory = browse_directory()
    if not directory:
        messagebox.showerror("Error", "No directory selected!")
        return

    field_name = simpledialog.askstring("Input", "Enter the field name to add:")
    if not field_name:
        messagebox.showerror("Error", "Field name cannot be empty!")
        return

    field_value = simpledialog.askstring("Input", f"Enter the value for {field_name} (leave blank for none):")

    process_directory(directory, field_name, field_value)
    messagebox.showinfo("Done", f"Field '{field_name}' added to all applicable files.")

# Create the main Tkinter window
root = tk.Tk()
root.title("YAML Frontmatter Modifier")
root.geometry("400x200")

# Create the button to trigger the directory selection and field addition
add_field_button = tk.Button(root, text="Select Folder and Add Field", command=add_field, height=2, width=30)
add_field_button.pack(pady=50)

# Start the Tkinter main loop
root.mainloop()
