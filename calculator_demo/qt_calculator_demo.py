from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QVBoxLayout, QLineEdit
from PyQt5.QtCore import Qt
from m_calculator_817 import Calculator
# 创建主窗口类
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置窗口标题
        self.setWindowTitle('Calculator')
        #创建一个文本框
        self.text_box = QLineEdit()
        self.text_box.setPlaceholderText("")
        self.text_box.setReadOnly(True)
        self.text_box.setAlignment(Qt.AlignRight)
        self.calculator = Calculator(0)

        # 创建布局
        
        layout = QGridLayout()
        # 创建一个按钮

        buttons = [
            ('7',0,0), ('8',0,1),('9',0,2),('*',0,3),
            ('4',1,0),('5',1,1),('6',1,2),('c',1,3),
            ('1',2,0),('2',2,1),('3',2,2),('/',2,3),
            ('+',3,0),('0',3,1),('-',3,2),('=',3,3),
        ]
        
        for button_text, row, col in buttons:
            button = QPushButton(button_text)
            button.clicked.connect(self.on_button_clicked)
            layout.addWidget(button, row, col)

        
        # 主要的垂直布局
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.text_box)
        main_layout.addLayout(layout)


        # 设置窗口布局
        self.setLayout(main_layout)
    
    def on_button_clicked(self):
        button_sender = self.sender()
        button_text = button_sender.text()
        

        if button_text in ("+","-","*","/"):
            if not self.calculator.text_stack.is_empty():
                current_text = self.calculator.text_stack.to_string()
                self.calculator.num_stack.push(int(current_text))
            self.calculator.operator_stack.push(button_text)
            self.calculator.text_stack.clear()
            self.text_box.setText(self.calculator.num_stack.all_text)

            
        elif button_text == "=":
            current_text = self.calculator.text_stack.to_string()
            self.calculator.num_stack.push(int(current_text))
            self.calculator.text_stack.clear()
            result = self.calculator.amount()
            self.text_box.setText(self.calculator.num_stack.all_text + "=" +str(result))

        else:
            self.calculator.text_stack.push(button_text)
            self.text_box.setText(self.calculator.num_stack.all_text)


        
       
        

        # if button_text == '=':
        #     try:
        #         result = eval(current_text)
        #         button_text = self.calculator.text_stack.to_string()+"="+str(result)
        #         self.text_box.setText(button_text)
        #     except Exception as e:
        #         self.text_box.setText('Error')
        # elif button_text == 'c':
        #     self.text_box.clear()
        # else:

        #     self.text_box.setText(current_text + button_text)


        
    def remove_chars(source_str, chars_to_remove):
        # 创建一个空字符串用于存储结果
        result = ""
        
        # 遍历 source_str 中的每个字符
        for char in source_str:
            # 如果当前字符不在 chars_to_remove 中，则添加到结果字符串中
            if char not in chars_to_remove:
                result += char
    
        


# 主函数
if __name__ == '__main__':
    app = QApplication([])

    # 创建并显示主窗口
    window = MainWindow()
    window.show()

    # 运行应用
    app.exec_()