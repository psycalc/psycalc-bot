import os
import pyperclip
import argparse
import datetime

# Define a dictionary to store the limitations for different GPT models
MODEL_LIMITATIONS = {
    'GPT': 1024,
    'GPT-2': 2048,
    'GPT-3': 4096,
    'GPT-Neo': 2048,
    'GPT-3.5B': 4096,
    'GPT-3.6B': 4096
}

def is_file_ignored(file_path):
    ignored_files = ['.env', '.gitignore', '.dockerignore']
    return any(file_path.endswith(ignored_file) for ignored_file in ignored_files)

def is_directory_ignored(dir_path):
    ignored_directories = ['node_modules', '.git', '.venv', '.vscode', 'dist', 'build', 'venv', '__pycache__']
    return any(dir_path.endswith(ignored_directory) for ignored_directory in ignored_directories)

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Concatenate the contents of the three most recently modified files in a folder within the last 30 minutes.')
    parser.add_argument('folder_path', help='the folder path to scan')
    parser.add_argument('-m', '--max-chars', type=int, default=10000, help='the maximum number of characters in the concatenated buffer (default: 10000)')
    parser.add_argument('-g', '--gpt-model', default='GPT-3', help='the GPT model being used (default: GPT-3)')
    args = parser.parse_args()

    # Determine the maximum number of characters in the concatenated buffer
    max_chars = MODEL_LIMITATIONS.get(args.gpt_model, 10000)

    # Recursively scan the folder for files modified within the last 30 minutes and sort by modification time
    file_paths = []
    now = datetime.datetime.now()
    threshold = now - datetime.timedelta(minutes=30)
    for root, dirs, files in os.walk(args.folder_path):
        if is_directory_ignored(root):
            continue
        for name in files:
            file_path = os.path.join(root, name)
            if is_file_ignored(file_path):
                continue
            if file_path.endswith('.py') or file_path.endswith('.txt'):
                mod_time = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
                if mod_time > threshold:
                    file_paths.append((file_path, mod_time))
    file_paths.sort(key=lambda x: x[1], reverse=True)

    # Concatenate the contents of the three most recently modified files into a buffer, taking character count into consideration
    contents = []
    chars = 0
    for file_path, _ in file_paths[:3]:
        with open(file_path, 'r') as f:
            file_content = f.read().strip()
            if file_content:
                chars += len(file_content)
                if chars <= max_chars:
                    contents.append(file_content)
                else:
                    break
    buffer = ''.join(contents)

    # Copy buffer to clipboard
    pyperclip.copy(buffer)
    print(f"Copied {chars} characters from the following {len(contents)} files modified within the last 30 minutes:")
    for file_path, mod_time in file_paths[:len(contents)]:
        # print(f"{file_path} ({mod_time})")
        # same as above, but full path
        full_file_path = os.path.abspath(file_path)
        print(f"{full_file_path} ({chars})")

if __name__ == '__main__':
    main()
