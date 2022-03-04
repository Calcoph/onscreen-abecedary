import sys
from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5.QtGui import QFont
from click import style
from config import configuration, styles

class AbcWindow(QLabel):
    def __init__(self, config) -> None:
        super().__init__(configuration["text"][0])

        font = QFont(configuration["font family"][0])
        font.setPointSizeF(configuration["font size"][0])

        self.setFont(font)

        if configuration["color mode"][0] == "dark":
            self.setStyleSheet(styles["dark"])
        elif configuration["color mode"][0] == "light":
            self.setStyleSheet(styles["light"])
        else:
            self.setStyleSheet(styles["light"])

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    abc = AbcWindow(configuration)
    abc.showFullScreen()
    
    size = configuration["size"]
    abc.setFixedSize(size[0], size[1])
    pos = configuration["initial position"]
    abc.move(pos[0], pos[1])

    sys.exit(app.exec())