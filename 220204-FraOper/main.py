# 首先你需要在引用的python文件内导入该对象所在的文件，也就是main_menu.py
import sys
import UI
from fractions import Fraction

Ui_MainWindow = UI.Ui_Form  # 指定Ui_MainWindow 为main_menu文件下的Ui_MainWindow对象。


class CoperQt(UI.QtWidgets.QWidget, Ui_MainWindow):  # 创建一个Qt对象
    # 这里的第一个变量是你该窗口的类型，第二个是该窗口对象。
    # 这里是主窗口类型。所以设置成当QtWidgets.QMainWindow。
    # 你的窗口是一个会话框时你需要设置成:QtWidgets.QDialog
    def __init__(self):
        UI.QtWidgets.QMainWindow.__init__(self)  # 创建主界面对象
        Ui_MainWindow.__init__(self)  # 主界面对象初始化
        self.setupUi(self)  # 配置主界面对象

    def b1Act(self):
        print(1)
    def b2Act(self):
        self.spinBox.setValue(0)
        self.spinBox_2.setValue(0)
        self.spinBox_3.setValue(0)
        self.spinBox_4.setValue(0)
        self.doubleSpinBox.setValue(0.00)
    def b3Act(self):
        print(1)
    def b4Act(self):
        print(1)
    def b5Act(self):
        print(1)
    def b6Act(self):
        print(1)
    def b7Act(self):
        print(1)
    def b8Act(self):
        print(1)
    def b9Act(self):
        print(1)
    def b10Act(self):
        print(1)
if __name__ == "__main__":
    app = UI.QtWidgets.QApplication(sys.argv)
    window = CoperQt()  # 创建QT对象
    window.show()  # QT对象显示
    sys.exit(app.exec_())
