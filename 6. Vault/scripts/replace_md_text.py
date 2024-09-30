# Tìm kiếm và thay thế đoạn văn bản trong tất cả các file thuộc 1 thư mục cha bất kỳ với một đoạn văn bản mới
# Cú pháp mẫu: python3 replace_md_text.py /Users/mrthinh/Library/CloudStorage/OneDrive-Personal/Github/osidian_flow_public "old_word" "new_word"

import os
import sys

def replace_string_in_file(file_path, target, replacement):
    """Replaces target string with replacement in the specified file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Replace target string with the new one
    updated_content = content.replace(target, replacement)

    # Write updated content back to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(updated_content)

def process_directory(directory, target, replacement):
    """Loops over all *.md files in a directory and its subdirectories, replacing target string."""
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                print(f"Processing file: {file_path}")
                replace_string_in_file(file_path, target, replacement)

def main():
    if len(sys.argv) != 4:
        print("Usage: python script.py <directory> <target_string> <replacement_string>")
        sys.exit(1)

    # Get the command line arguments
    directory = sys.argv[1]
    target_string = sys.argv[2]
    replacement_string = sys.argv[3]

    # Process the directory
    process_directory(directory, target_string, replacement_string)
    print("Replacement completed.")

if __name__ == "__main__":
    main()
