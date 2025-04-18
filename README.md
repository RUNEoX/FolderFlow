# FolderFlow
📂 Reorganizer Tool A simple and efficient Python tool for moving files from subfolders to their main parent folder. It features a GUI, CLI, file conflict handling, and built-in logging. Optimized for performance with large file structures.

A very simple and efficient Python tool for moving files from subfolders to their main parent folder. Includes a GUI  and a  CLI mode. Handles file conflicts, logs all actions. Built for clarity, speed, and flexibility.

##  Features
- Drag-and-drop files from subfolders to the main folder
- Clean, dark-mode enabled GUI for smooth navigation
- Functional "Switch to CLI Mode" button for command-line flexibility
- Smart file conflict resolution with overwrite or skip options
- Logging system to track operations and enable undo functionality
- Optimized for performance with large file structures
- Modular project structure ready for future expansion

## 💻 CLI Highlights
- Supports simplified syntax with alias support (e.g., `f:` for `from`, etc.)
- Confirmation prompts before critical actions
- Interactive fallback if required arguments are missing

## Usage

When you run the `.exe`, you can add the `--cli` argument to force it into CLI mode:

## Example Folder Tree (GUI)

Here’s an example of a folder structure before using the Folderflow Tool :
```plaintext
MainFolder/
│
├── Subfolder1/
│   ├── File1.txt
│   └── File2.txt
│
├── Subfolder2/
│   ├── File3.txt
│   └── File4.txt
│
└── Subfolder3/
    ├── File5.txt
    └── File6.txt

After running the tool:

MainFolder/
│
├── File1.txt
├── File2.txt
├── File3.txt
├── File4.txt
├── File5.txt
└── File6.txt
```

## 📁 Example Folder Tree (CLI):

```plaintext
MainFolder/
│
├── Subfolder1/
│   ├── Subfolder1-1/
│   │   ├── File1.txt
│   │   └── File2.txt
│   ├── Subfolder1-2/
│   │   ├── File3.txt
│   │   └── File4.txt
│   └── Subfolder1-3/
│       ├── File5.txt
│       └── File6.txt
│
├── Subfolder2/
│   ├── Subfolder2-1/
│   │   ├── File7.txt
│   │   └── File8.txt
│   ├── Subfolder2-2/
│   │   ├── File9.txt
│   │   └── File10.txt
│   └── Subfolder2-3/
│       ├── File11.txt
│       └── File12.txt
│
└── Subfolder3/
    ├── Subfolder3-1/
    │   ├── File13.txt
    │   └── File14.txt
    ├── Subfolder3-2/
    │   ├── File15.txt
    │   └── File16.txt
    └── Subfolder3-3/
        ├── File17.txt
        └── File18.txt
```
# Moving files from Subfolder1 to a custom backup location on another drive (only in CLI):
FileMover.exe --cli -in "MainFolder\\Subfolder1" -to "D:\\Backup\\Reports"

# Moving files from Subfolder1 and Subfolder2 to a custom location
FileMover.exe --cli -in "MainFolder\\Subfolder1, MainFolder\\Subfolder2" -to "D:\\Backup\\Reports"

Key Differences Between CLI and GUI
CLI:

-Custom Locations: You can specify any location (even external drives) as the destination for your files.

-Complex Operations: You can move multiple subfolders or files in one command.

-No Limitations: It’s perfect for organizing files across different drives or consolidating large projects.

GUI:

-Parent Folder Only: You can only move files to the parent folder (MainFolder), no custom destinations.

-User-Friendly: Ideal for basic use when you just want to move files from subfolders to the main folder, with no complex operations.

 ## Realistic Situation for Using the Tool:
Imagine you're organizing a project where you’ve collected files from various sources and stored them in several subfolders within a main project folder. Over time, your folder structure has gotten more complex, and now, you want to clean things up by moving all files into the main parent folder (MainFolder), or even move them to a custom location on another drive for better access and organization.

For instance:

You received a project from a client, and the folder structure looks like the one above.

The files in Subfolder1 and Subfolder2 are reports from different departments that need to be consolidated into a single folder for final submission.

You're trying to create backups by moving the consolidated files to another drive (e.g., D:\\Backup\\Reports), but want to avoid manually copying each file or folder.

## ⚠️ Important
CLI mode is slower than the GUI mode, but it allows you to move files to a custom location, whereas the GUI can only move files to the parent folder.
