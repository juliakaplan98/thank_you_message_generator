import sys
from typing import List

from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QHBoxLayout,
    QWidget,
    QTabWidget,
)

from .side_panel.side_panel import SidePanel
from .side_panel.button_tuple import ButtonAction
from .menu_bar.action_tuple import MenuAction
from .menu_bar.menu_bar import MenuBar


class MainWindow(QMainWindow):
    """Main Window class, creates application window"""

    def __init__(self) -> None:
        super().__init__()
        # Central widget top container for app
        self.central_widget = QWidget()
        # Main layout for app (horizontal)
        self.main_h_box = QHBoxLayout()
        # Left side tab widget for all doc's and table's
        self.tab_bar = QTabWidget()
        self.tab_bar.setMovable(True)
        self.tab_bar.setTabsClosable(True)
        # Right side panel settings
        self.side_panel = QWidget()
        self.initialize_ui()

    def initialize_ui(self) -> None:
        """Set up the application's GUI"""
        self.setMinimumSize(1200, 800)
        self.setWindowTitle("Thank You Message Generator")
        self.setup_main_window()
        MenuBar(self, self.config_menu_bar())
        # Initialize side panel
        self.sp = SidePanel(self.side_panel)
        self.sp.set_fille_buttons(self.config_side_buttons())
        self.show()

    def setup_main_window(self) -> None:
        """Create and arrange widgets in the main window."""
        self.main_h_box.addWidget(self.tab_bar)
        self.main_h_box.addWidget(self.side_panel)
        self.central_widget.setLayout(self.main_h_box)
        self.setCentralWidget(self.central_widget)

    def config_menu_bar(self) -> dict[str, List[MenuAction]]:
        """Describes menu bar actions"""
        menu_bar_dict: dict[str, List[MenuAction]] = {
            "File": [
                MenuAction("Open File...", "Ctrl+O", self.open_pdf_file),
                MenuAction("&Quit", "Ctrl+Q", self.close),
            ]
        }
        return menu_bar_dict

    def config_side_buttons(self):
        """Describes side panel buttons"""
        side_bar_buttons_dict: dict[str, List[ButtonAction]] = {
            "File": [
                ButtonAction("Open", self.open_pdf_file),
                ButtonAction("Save As...", self.seve_selected_fales_as),
                ButtonAction("Save All As...", self.save_all_files_as),
                ButtonAction("Close", self.close_file),
                ButtonAction("Close All", self.close_all_files),
            ]
        }
        return side_bar_buttons_dict

    def open_pdf_file(self) -> None:
        pass

    def seve_selected_fales_as(self) -> None:
        pass

    def save_all_files_as(self) -> None:
        pass

    def close_file(self) -> None:
        pass

    def close_all_files(self) -> None:
        pass


def main():
    """Main method, start point"""
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
