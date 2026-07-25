import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

class Dashboard(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("COVID-19 Outbreak Spread Predictor")
        self.setGeometry(300, 200, 600, 400)

        layout = QVBoxLayout()

        title = QLabel("COVID-19 Outbreak Spread Predictor")
        title.setStyleSheet("font-size:20px; font-weight:bold;")

        info = QLabel(
            "This dashboard displays the COVID-19 outbreak prediction project.\n"
            "Analysis and prediction were performed using Machine Learning."
        )

        layout.addWidget(title)
        layout.addWidget(info)

        self.setLayout(layout)

app = QApplication(sys.argv)
window = Dashboard()
window.show()
sys.exit(app.exec())