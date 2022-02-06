# 首先你需要在引用的python文件内导入该对象所在的文件，也就是main_menu.py
import sys
import UI
from PyQt5.QtWidgets import *
from pyperclip import copy
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
        QMessageBox.information(self,'帮助','此工具运用Python的fractions模块，实现了简单的分数运算功能。\n使用方式：\n  1、如果要对分数进行四则运算操作，则在“分数1”和“分数2”两栏里填上分数，在右边的“四则运算”中自己想进行的运算；\n  2、如果想要对一个分数进行约分的操作，则在“分数1”一栏中填入分数，在右边的“其他运算”中点击“约分”，即可完成约分；\n  3、如果要将一个小数化为分数，则在“小数”一栏中填入小数，在右边的“其他运算”中点击“小数化分数”，即可完成运算；\n  4、运算的结果会显示在“结果”一栏，不可编辑，点击“复制”按钮复制结果，结果将在下一次运算时清空；\n  5、点击清零按钮清空所有数。')
    def b2Act(self):
        self.spinBox.setValue(0)
        self.spinBox_2.setValue(0)
        self.spinBox_3.setValue(0)
        self.spinBox_4.setValue(0)
        self.doubleSpinBox.setValue(0.00)
        self.result.setText('0')
    def b3Act(self):
        self.result.setText(str(Fraction(self.spinBox.value(), self.spinBox_2.value()) + Fraction(self.spinBox_3.value(), self.spinBox_4.value())))
    def b4Act(self):
        self.result.setText(
            str(Fraction(self.spinBox.value(), self.spinBox_2.value()) - Fraction(self.spinBox_3.value(),
                                                                                  self.spinBox_4.value())))
    def b5Act(self):
        self.result.setText(
            str(Fraction(self.spinBox.value(), self.spinBox_2.value()) * Fraction(self.spinBox_3.value(),
                                                                                  self.spinBox_4.value())))
    def b6Act(self):
        self.result.setText(
            str(Fraction(self.spinBox.value(), self.spinBox_2.value()) / Fraction(self.spinBox_3.value(),
                                                                                  self.spinBox_4.value())))
    def b8Act(self):
        self.result.setText(str(Fraction(self.spinBox.value(), self.spinBox_2.value())))
    def b9Act(self):
        self.result.setText(str(Fraction(self.doubleSpinBox.value())))
    def b10Act(self):
        copy(self.result.text())
if __name__ == "__main__":
    app = UI.QtWidgets.QApplication(sys.argv)
    window = CoperQt()  # 创建QT对象
    window.show()  # QT对象显示
    sys.exit(app.exec_())
