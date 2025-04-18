import os
import shutil
import json
import argparse
from datetime import datetime

folder_path = ""
folders_to_move = []
destination = ""
show_commands = True

def print_commands():
    if show_commands:
        print("""
Available commands:
- import <full_path>: Provide the full folder path.
- in <subfolders>: Specify the subfolders to move.
- to <path>: Set destination path.
- move: Execute the move.
- undo: Undo the last move.
- commands: Show available commands.
- hide: Hide this command list.
""")

def handle_cli():
    global folder_path, folders_to_move, destination, show_commands

    command_input = input("Enter a command: ").strip()
    if not command_input:
        return

    commands = command_input.split(" ")
    i = 0 
    while i < len(commands):
        cmd = commands[i]

        if cmd == "import":
            i += 1
            path_parts = []
            while i < len(commands) and commands[i] not in {"in", "to", "move", "undo", "commands", "hide"}:
                path_parts.append(commands[i])
                i += 1
            folder_path = " ".join(path_parts).strip('"')
            print(f"Imported path: {folder_path}")

        elif cmd == "in":
            i += 1
            folders_raw = []
            while i < len(commands) and commands[i] not in {"to", "move", "undo", "commands", "hide"}:
                folders_raw.append(commands[i].strip('"'))
                i += 1

            folders_to_move = [folder.strip() for folder in ' '.join(folders_raw).split(',')]
            print(f"Folders to move: {folders_to_move}")

        elif cmd == "to":
            i += 1
            dest_parts = []
            while i < len(commands) and commands[i] not in {"move", "undo", "commands", "hide"}:
                dest_parts.append(commands[i])
                i += 1
            destination = " ".join(dest_parts).strip('"')
            print(f"Destination set to: {destination}")

        elif cmd == "move":
            i += 1
            if not (folder_path and destination and folders_to_move):
                print("Missing info. Use 'import', 'in', and 'to' first.")
            else:
                move_files(folder_path, destination, folders_to_move)

        elif cmd == "undo":
            i += 1
            undo_move()

        elif cmd == "commands":
            i += 1
            show_commands = True
            print_commands()

        elif cmd == "hide":
            i += 1
            show_commands = False
            print("Commands hidden. Type 'commands' to show again.")

        else:
            print(f"Unknown command: {cmd}")
            break  # Break out of the loop if an unknown command is encountered

def move_files(src_folder, dest_folder, folders_to_move):
    for folder_name in folders_to_move:
        folder_path = os.path.join(src_folder, folder_name)
        print(f"Checking if folder exists: {folder_path}")  # Debugging line

        if os.path.exists(folder_path):
            dest_path = os.path.join(dest_folder, folder_name)
            print(f"Moving contents of folder: {folder_path} → {dest_path}")

            if not os.path.exists(dest_path):
                os.makedirs(dest_path)

            for item in os.listdir(folder_path):
                src_item = os.path.join(folder_path, item)
                dst_item = os.path.join(dest_path, item)
                try:
                    shutil.move(src_item, dst_item)
                    print(f"Moved: {src_item} → {dst_item}")
                    log_move("move", src_item, dst_item)
                except Exception as e:
                    print(f"Error moving {src_item} to {dst_item}: {e}")

            if not os.listdir(folder_path):
                os.rmdir(folder_path)
        else:
            print(f"Folder not found: {folder_path}")

def log_move(operation, src, dest):
    log_entry = {
        "operation": operation,
        "src": src,
        "dest": dest,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    log_file = "move_log.json"
    logs = []

    if os.path.exists(log_file):
        with open(log_file, "r") as f:
            logs = json.load(f)

    logs.append(log_entry)

    with open(log_file, "w") as f:
        json.dump(logs, f, indent=4)

def undo_move():
    log_file = "move_log.json"
    if not os.path.exists(log_file):
        print("No log file found. Cannot undo.")
        return

    with open(log_file, "r") as f:
        logs = json.load(f)

    if not logs:
        print("No operations to undo.")
        return

    last_log = logs.pop()
    src, dest = last_log["dest"], last_log["src"]

    if os.path.exists(src):
        shutil.move(src, dest)
        print(f"Undone: {src} → {dest}")
    else:
        print("Destination folder not found. Cannot undo.")

    with open(log_file, "w") as f:
        json.dump(logs, f, indent=4)

if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Folder Flow CLI Tool")
    parser.add_argument('--cli', action='store_true', help="Run the tool in CLI mode")

    args = parser.parse_args()

    # If --cli is passed, run the CLI mode
    if args.cli:
        print_commands()
        while True:
            handle_cli()

    else:
        print("Use --cli to run the tool in CLI mode.")
