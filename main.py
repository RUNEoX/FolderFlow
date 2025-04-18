import sys
from gui_interface import launch_gui
from cli_interface import handle_cli

if __name__ == "__main__":
    if "--cli" in sys.argv:
        handle_cli()  # Start in CLI mode if the --cli argument is passed
    else:
        launch_gui()  # Default: launch the GUI