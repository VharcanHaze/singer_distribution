import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set window properties
        self.setWindowTitle("Song-Singer Table")
        self.setGeometry(100, 100, 800, 600)

        # Create table widget
        self.table = QTableWidget(self)
        self.table.setGeometry(50, 50, 700, 500)

        # Populate table with data
        self.populate_table()

    def populate_table(self):
        # Define table properties
        self.table.setColumnCount(3)
        self.table.setRowCount(5)
        self.table.setHorizontalHeaderLabels(["Singer 1", "Singer 2", "Singer 3"])

        # Add data to table cells
        for row in range(5):
            for col in range(3):
                item = QTableWidgetItem()
                item.setCheckState(0)
                self.table.setItem(row, col, item)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())