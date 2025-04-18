
import sys
import subprocess
import logging
import tkinter as tk
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton,
    QFileDialog, QLabel, QMessageBox
)
from core.mover import move_files_to_parent
from utils.logger import setup_logger

logger = setup_logger()

class FileMoverApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Folder Flattener")
        self.setGeometry(200, 200, 400, 200)

        layout = QVBoxLayout()

        self.path_label = QLabel("No folder selected.")
        layout.addWidget(self.path_label)

        browse_btn = QPushButton("Choose Main Folder (big1)")
        browse_btn.clicked.connect(self.browse_folder)
        layout.addWidget(browse_btn)

        move_btn = QPushButton("Move Files Now")
        move_btn.clicked.connect(self.run_mover)
        layout.addWidget(move_btn)

        cli_btn = QPushButton("Switch to CLI Mode")
        cli_btn.clicked.connect(self.open_cli_mode)
        layout.addWidget(cli_btn)

        self.setLayout(layout)
        self.folder_path = None
        self.set_dark_mode()

    def set_dark_mode(self):
        self.setStyleSheet("""
            QWidget {
                background-color: #2b2b2b;
                color: #f0f0f0;
            }
            QPushButton {
                background-color: #444;
                color: white;
                padding: 5px;
                border: 1px solid #666;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: #555;
            }
        """)

    def browse_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Folder")
        if folder:
            self.folder_path = folder
            self.path_label.setText(f"Selected: {folder}")

    def run_mover(self):
        if not self.folder_path:
            QMessageBox.warning(self, "Error", "Please select a folder first.")
            return
        try:
            moved, skipped, _ = move_files_to_parent(self.folder_path)
            msg = f"Moved: {moved} files\nSkipped: {skipped} (conflicts or errors)"
            QMessageBox.information(self, "Done", msg)
        except Exception as e:
            logger.error(f"Exception: {e}")
            QMessageBox.critical(self, "Error", str(e))

    def open_cli_mode(self):
        subprocess.Popen(["cmd", "/k", "python cli_interface.py"], creationflags=subprocess.CREATE_NEW_CONSOLE)

def launch_gui():
    app = QApplication(sys.argv)
    window = FileMoverApp()
    window.show()
    sys.exit(app.exec_())
