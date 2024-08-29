import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget,QTextEdit
from PyQt5.QtCore import QTimer, Qt
import threading
import time

class Stopwatch(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt5 Stopwatch")
        self.resize(400, 200)

        #cr  QLabel 
        self.time_label = QLabel("00:00:00", self)
        self.time_label.setAlignment(Qt.AlignCenter)

        self.display_record_time = QTextEdit(self)
        self.display_record_time.setReadOnly(True)
        self.display_record_time.setAlignment(Qt.AlignCenter)
        self.display_record_time.setMinimumHeight(200)
        self.display_record_time.verticalScrollBar().setVisible(False)


        # 创建一个 QTimer 用于计n
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)

        # create a button with two states : Start and Pause  
        self.button1 = QPushButton("Start",self)
        self.button1.clicked.connect(self.click_button1)

        self.button2 = QPushButton("Reset", self)
        self.button2.clicked.connect(self.click_button2)
        self.button2.setEnabled(False)


        # 设置布局
        layout = QVBoxLayout()
        layout.addWidget(self.time_label)
        layout.addWidget(self.display_record_time)
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)

        # 创建一个中心部件并设置布局
        central_widget = QWidget(self)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # 初始化计时器
        self.elapsed_time = 0
        self.is_running = False
        self.record_count = 0

    def update_time(self):
        self.elapsed_time += 1

        seconds, millisecond = divmod(self.elapsed_time,100 )
        minutes, seconds = divmod(seconds, 60)
        time_str = f"{minutes:02d}:{seconds:02d}.{millisecond:02d}"
        self.time_label.setText(time_str)

    def click_button1(self):
        if not self.is_running:
            self.timer.start(10)  # 更新间隔为10毫秒，表示每10毫秒更新一次时间

            self.is_running = True

        if self.button1.text() == "Start":
            self.button1.setText("Pause")
            self.button2.setEnabled(True)
            self.button2.setText("Record")
        else:
            self.button1.setText("Start")
            self.button2.setText("Reset")
            self.pause_stopwatch()

    def click_button2(self):
        if self.button2.text() == "Record":
            self.show_record_time()
        else:
            self.reset_stopwatch()
            self.display_record_time.setPlainText("")
            self.display_record_time.setAlignment(Qt.AlignCenter)
            self.button2.setEnabled(False)
            self.record_count = 0
        
    def pause_stopwatch(self):
        if self.is_running:
            self.timer.stop()
            self.is_running = False
    def show_record_time(self):
        self.record_count += 1
        self.display_record_time.insertPlainText("{:02}".format(self.record_count) +"  "+ self.time_label.text()+"\n")

       
    

    def reset_stopwatch(self):
        self.timer.stop()
        self.elapsed_time = 0
        self.time_label.setText("00:00.00")
        self.is_running = False
    #定义一个线程执行的函数
counter = 0
def my_thread_function1(name, delay):
   
    stopwatch.show()
    count = 0
    while count < 5:
        time.sleep(delay)
        global counter
        counter += 1
        count += 1
        print(f"Thread {name}: {count}" + f" counter:{counter}")

def my_thread_function2(name, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        global counter
        counter += 1
        count += 1
        print(f"Thread {name}: {count}"+ f" counter:{counter}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    stopwatch = Stopwatch()


    t1 = threading.Thread(target=my_thread_function1, args=("Thread-1", 1))

    t2 = threading.Thread(target=my_thread_function2, args=("Thread-2", 0.5))

    # 启动线程
    t1.start()
    print("t1 start")
    t2.start()
    print("t2 start")

    # 等待所有线程完成
    t1.join()
    print("Main thread waiting for threads to complete...")
    t2.join()
    print("All threads completed.")
    stopwatch.show()
    sys.exit(app.exec_())
    # 创建两个线程


