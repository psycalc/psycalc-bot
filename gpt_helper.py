import argparse
import datetime
import logging
import os
from pathlib import Path

import pyperclip
import yaml


def load_config(config_path: Path) -> dict:
    """Load configuration from the specified file."""
    with open(config_path, 'r') as f:
        return yaml.safe_load(f)


def is_file_ignored(file_path: Path, ignored_files: list) -> bool:
    """Return True if the file should be ignored."""
    return any(file_path.name.endswith(ignored_file) for ignored_file in ignored_files)


def is_directory_ignored(dir_path: Path, ignored_directories: list) -> bool:
    """Return True if the directory should be ignored."""
    return any(ignored_directory in dir_path.parts for ignored_directory in ignored_directories)


def concatenate_files(config: dict, max_chars: int = 10000) -> list:
    """Concatenate the contents of the specified files into multiple buffers."""
    ignored_directories = config["ignored_directories"]
    ignored_files = config["ignored_files"]
    config_files = config["files"]

    included_files = []
    buffers = []
    buffer = ''
    part_number = 1
    before_message = config["before_message"]
    after_part_message = config["after_part_message"]
    after_message = config["after_message"]

    for file_pattern in config_files:
        file_paths = list(Path().glob(file_pattern))
        for file_path in file_paths:
            if is_file_ignored(file_path, ignored_files) or is_directory_ignored(file_path.parent, ignored_directories):
                continue

            with open(file_path, 'r') as f:
                file_content = f"{file_path.resolve()}\n{f.read()}"
                if not file_content:
                    continue

                content_length = len(file_content)
                buffer_length = len(buffer)
                part_number_message_length = len(f"This is my project part {part_number}. ")
                after_part_message_length = len(after_part_message)

                if buffer_length + content_length + part_number_message_length + after_part_message_length > max_chars:
                    buffers.append(buffer + f"\n{after_message}")
                    buffer = ''
                    part_number += 1

                if not buffer:
                    buffer = f"This is my project part {part_number}. "
                buffer += file_content
                included_files.append(file_path.resolve())

    buffers.append(buffer + f"\n{after_message}")

    # Print information about each buffer and copy it to clipboard
    for i, buffer in enumerate(buffers):
        buffer_length = len(buffer)
        print(f"Part {i + 1}: {buffer_length} characters")
        pyperclip.copy(buffer)
        if i < len(buffers) - 1:
            input("Press enter to copy the next part...")

    return included_files


if __name__ == '__main__':
    config_path = Path('gpt_helper_configuration.yaml')
    config = load_config(config_path)
    included_files = concatenate_files(config)
    print("Included files:")
    for file_path in included_files:
        print(file_path)
