import os
import shutil
from utils.logger import setup_logger

logger = setup_logger()

def move_files_to_parent(parent_folder):
    moved = 0
    skipped = 0
    moved_files = []  

    for root, dirs, files in os.walk(parent_folder):
        if root == parent_folder:
            continue
        if os.path.basename(root).startswith("."):
            continue

        for file in files:
            src_path = os.path.join(root, file)
            dest_path = os.path.join(parent_folder, file)

            if os.path.isfile(dest_path):
                base, ext = os.path.splitext(file)
                counter = 1
                while os.path.exists(dest_path):
                    dest_path = os.path.join(parent_folder, f"{base}_{counter}{ext}")
                    counter += 1

            try:
                shutil.move(src_path, dest_path)
                moved += 1
                moved_files.append((src_path, dest_path))  
                logger.info(f"Moved: {src_path} → {dest_path}")
            except Exception as e:
                logger.warning(f"Skipped: {src_path} | Error: {e}")
                skipped += 1

    return moved, skipped, moved_files

def undo_move(moved_files):
    for src, dest in reversed(moved_files):  
        try:
            shutil.move(dest, src)
            logger.info(f"Undo move: {dest} → {src}")
        except Exception as e:
            logger.warning(f"Failed to undo move: {dest} → {src} | Error: {e}")

