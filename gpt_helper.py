import os
import pyperclip
import argparse
import datetime
import yaml
import glob

# Load the configuration from the YAML file
with open("gpt_helper_configuration.yaml", "r") as config_file:
    config = yaml.safe_load(config_file)

ignored_directories = config["ignored_directories"]
ignored_files = config["ignored_files"]
config_files = config["files"]

# Define a dictionary to store the limitations for different GPT models
MODEL_LIMITATIONS = {
    'GPT-3': 4096,
    'GPT-4': 8192,
}

def is_file_ignored(file_path):
    return any(file_path.endswith(ignored_file) for ignored_file in ignored_files)

def is_directory_ignored(dir_path):
    return any(ignored_directory in dir_path.split(os.path.sep) for ignored_directory in ignored_directories)

def get_files_from_config():
    all_files = []
    for file_pattern in config_files:
        matched_files = glob.glob(file_pattern, recursive=True)
        all_files.extend(matched_files)
    return all_files

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Concatenate the contents of the specified files in the configuration file.')
    parser.add_argument('-m', '--max-chars', type=int, default=10000, help='the maximum number of characters in the concatenated buffer (default: 10000)')
    parser.add_argument('-g', '--gpt-model', default='GPT-3', help='the GPT model being used (default: GPT-3)')
    args = parser.parse_args()

    # Determine the maximum number of characters in the concatenated buffer
    max_chars = min(MODEL_LIMITATIONS.get(args.gpt_model, 1024), args.max_chars)

    # Get the list of files specified in the config
    file_paths = get_files_from_config()

    # Concatenate the contents of the specified files into a buffer, taking character count into consideration
    contents = []
    chars = 0
    for file_path in file_paths:
        with open(file_path, 'r') as f:
            file_content = os.path.abspath(file_path) + '\n' + f.read()
            if file_content:
                chars += len(file_content)
                if chars <= max_chars:
                    contents.append(file_content)
                else:
                    break
    buffer = ''.join(contents)

    # Copy buffer to clipboard
    pyperclip.copy(buffer)
    print(f"Copied {chars} characters from the following {len(contents)} files:")
    for file_path in file_paths[:len(contents)]:
        full_file_path = os.path.abspath(file_path)
        print(f"{full_file_path} ({len(open(file_path).read())})")

if __name__ == '__main__':
    main()
