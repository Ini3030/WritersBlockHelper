from PySide6.QtCore import QTimer
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QWidget, QTextEdit, QPushButton, QHBoxLayout, QVBoxLayout


# Constants
TIMER_LENGTH_SECONDS: int = 5
TIME: int = TIMER_LENGTH_SECONDS * 1000


class WritingHelper(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Writing Helper")
        self.setMinimumSize(1100, 600)

        # Timer
        self.timer: QTimer = QTimer()

        # Text Editor
        self.text_edit: QTextEdit = QTextEdit()
        self.text_edit.setDisabled(True)

        font: QFont = QFont()
        font.setPointSize(14)
        self.text_edit.setFont(font)

        # Buttons
        self.start_button: QPushButton = QPushButton("Start")
        copy_button: QPushButton = QPushButton("Copy Text")
        log_button: QPushButton = QPushButton("Logs")

        # Layouts
        button_layout: QHBoxLayout = QHBoxLayout()
        button_layout.addWidget(self.start_button)
        button_layout.addWidget(copy_button)
        button_layout.addWidget(log_button)

        main_layout: QVBoxLayout = QVBoxLayout()
        main_layout.addWidget(self.text_edit)
        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)

        # Signals
        self.start_button.clicked.connect(self.unblock_app)
        self.text_edit.textChanged.connect(self.start_timer)
        self.timer.timeout.connect(self.countdown_finished)
        copy_button.clicked.connect(self.copy_text)

    def unblock_app(self):
        self.text_edit.clear()
        self.text_edit.setEnabled(True)
        self.start_button.setDisabled(True)

    def start_timer(self):
        self.timer.start(TIME)

    def countdown_finished(self):
        self.text_edit.setDisabled(True)
        self.start_button.setEnabled(True)

    def copy_text(self):
        self.text_edit.selectAll()
        self.text_edit.copy()
