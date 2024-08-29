import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit,QHBoxLayout
from PyQt5.QtCore import pyqtSignal

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('reality')       
        self.setGeometry(100, 100, 350, 200)

        
        main_layout = QVBoxLayout(self)

        label = QLabel("This is reality.", self)
        main_layout.addWidget(label)
        self.label = QLabel("", self)
        main_layout.addWidget(self.label)
        button = QPushButton('Open Dream', self)
        button.clicked.connect(self.open_sub_window)  
        main_layout.addWidget(button)
        button_close = QPushButton('Close Dream', self)
        button_close.clicked.connect(self.close)
        main_layout.addWidget(button_close)
    def open_sub_window(self):
        if not hasattr(self, 'sub_window'):
            self.sub_window = SubWindow()
            self.sub_window.sent_button.clicked.connect(self.handle_sub_input)
            self.sub_window.input_text.returnPressed.connect(self.handle_sub_input)
        self.sub_window.show()
    def handle_sub_input(self):
        input_text = self.sub_window.input_text.text()
        self.label.setText(f"dream say:{input_text}")
        
        

class SubWindow(QWidget):
    count = 1
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle(f"{SubWindow.count} dream")
        self.setGeometry(100+100*SubWindow.count, 100+100*SubWindow.count, 350, 200)

        main_layout = QVBoxLayout(self)
        label = QLabel(f"This dream is {SubWindow.count}.", self)
        main_layout.addWidget(label)
        self.label = QLabel("", self)
        main_layout.addWidget(self.label)
        # input line  
        h_layout = QHBoxLayout(self)
        self.input_text = QLineEdit(self)
        self.sent_button = QPushButton('Send', self)
        h_layout.addWidget(self.input_text)
        h_layout.addWidget(self.sent_button)
        main_layout.addLayout(h_layout)
        # open new or close self window
        button = QPushButton('Open Dream', self)
        button.clicked.connect(self.open_sub_window)  
        main_layout.addWidget(button)
        button_close = QPushButton('Close Dream', self)
        button_close.clicked.connect(self.close)
        main_layout.addWidget(button_close)

    def open_sub_window(self):
        SubWindow.count += 1
        if not hasattr(self, 'sub_window'):
            self.sub_window = SubWindow()
            self.sub_window.sent_button.clicked.connect(self.handle_sub_input)
            self.sub_window.input_text.returnPressed.connect(self.handle_sub_input)
        self.sub_window.show()

    def handle_sub_input(self):
        input_text = self.sub_window.input_text.text()
        self.label.setText(f"dream say:{input_text}")
    def on_submit_button_clicked(self):
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec_())