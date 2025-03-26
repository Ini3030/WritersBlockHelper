from writing_helper import WritingHelper
import sys

from PySide6.QtWidgets import QApplication


app: QApplication = QApplication(sys.argv)
window: WritingHelper = WritingHelper()


if __name__ == "__main__":
    window.show()
    app.exec()
