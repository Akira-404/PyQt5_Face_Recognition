import sys

from PyQt5.QtWidgets import QDialog
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QApplication, QAbstractItemView
from PyQt5.Qt import Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from ui_src.sqlite_main_window import Ui_SqliteMainWindow
from functools import partial

from tools.sqlite_func import Sqlite_Func


class Sqlite_UI(QtWidgets.QMainWindow, Ui_SqliteMainWindow):
    def __init__(self, parent=None):
        super(Sqlite_UI, self).__init__(parent)
        self.setupUi(self)

        # slot init
        self.slot_init()

        self.sf = Sqlite_Func()

        # 数据库路径
        self.file_path = ""

        # 表列表
        self.table_list = []
        # 字段列表
        self.field_list = []
        # 按钮字段列表
        self.btn_field_list = []
        # 选择的字段
        self.select_field_list = []

    def slot_init(self):
        print("slot init...")
        self.actionOpen_File.triggered.connect(self.open_db)
        self.radioButton_all.clicked.connect(self.selectAll_radiobtn)
        self.radioButton_notall.clicked.connect(self.selectNotAll_radiobtn)
        # 查询
        self.pushButton_query.clicked.connect(self.query)

    def open_db(self):
        print("打开文件")
        self.file_path, file_type = QFileDialog.getOpenFileName(self, "select db files", "",
                                                                "*.db;;*.png;;All Files(*)")
        print("文件路径:{}\n文件类型:{}\n".format(self.file_path, file_type))

        self.table_list = self.sf.check_table(self.file_path)
        print("当前数据库含有表：", self.table_list)

        # 设置窗口名字
        QDialog.setWindowTitle(self, self.file_path)

        self.create_radiobox_table()

    # 创建数据库表选项
    def create_radiobox_table(self):
        self.count = 0
        self.btn_layer = QWidget()
        for i, data in enumerate(self.table_list):
            self.count += 1
            self.btn = QtWidgets.QRadioButton(self.btn_layer)
            self.btn.setText(str(data))
            self.btn.clicked.connect(partial(self.create_checkbox_field, self.btn.text(), False))
            self.btn.move(10, i * 60)

        self.btn_layer.setMinimumSize(250, self.count * 60)
        self.scrollArea_table.setWidget(self.btn_layer)
        self.scrollArea_table.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

    # 创建字段表
    def create_checkbox_field(self, table, ischeck):
        # self.field_list.clear()
        # self.select_field_list.clear()
        self.btn_field_list.clear()
        self.count = 0

        self.table = table
        print("选择了{}表".format(str(table)))
        ret = self.sf.check_field(self.file_path, table)
        print("当前表含有{}字段:".format(ret))
        self.btn_layer = QWidget()
        for i, data in enumerate(ret):
            self.count += 1
            self.btn = QtWidgets.QCheckBox(self.btn_layer)
            self.btn.setText(str(data))
            self.btn.setChecked(ischeck)
            # self.btn.clicked.connect(partial(lambda x:self.select_field_list.append(x),self.btn.text()))
            self.btn.move(10, i * 60)

            self.btn_field_list.append(self.btn)
            # self.field_list.append(self.btn.text())

        self.btn_layer.setMinimumSize(250, self.count * 60)
        self.scrollArea_field.setWidget(self.btn_layer)
        self.scrollArea_field.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

    def selectAll_radiobtn(self):
        if self.btn_field_list == []:
            print("没有选择表")
        else:
            print("全选字段")
            self.create_checkbox_field(self.table, True)
            self.select_field_list.clear()
            for btn in self.btn_field_list:
                self.select_field_list.append(btn.text())

    def selectNotAll_radiobtn(self):
        if self.btn_field_list == []:
            print("没有选择表")
        else:
            print("全选字段")
            self.create_checkbox_field(self.table, False)
            self.select_field_list.clear()

    # param:字段，内容
    def show_table(self, fields, data):
        print("显示表内容")

        # 行数
        len_row = len(data)
        # 列数
        len_col = len(fields)
        print("field:{}\ndata:{}".format(fields, data))
        print("row:{},col:{}".format(len_row, len_col))
        self.model = QStandardItemModel(len_row, len_col, self)
        for row in range(len_row):
            for col in range(len(data[0])):
                item = QStandardItem("{}".format(data[row][col]))
                self.model.setItem(row, col, item)

        self.tableView_content.setModel(self.model)
        self.tableView_content.horizontalHeader().setStretchLastSection(True)
        self.tableView_content.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableView_content.clicked.connect(lambda x: print(self.tableView_content.currentIndex().data()))

    # 查询
    def query(self):
        self.select_field_list.clear()
        for btn in self.btn_field_list:
            print(btn.isChecked())
            if btn.isChecked() == True:
                self.select_field_list.append(btn.text())
        str_sql = self.sf.auto_select(self.select_field_list, self.table)
        print("str sql:{}".format(str_sql))
        ret = self.sf.executeCMD(self.file_path, str_sql)
        print(ret)
        for i, data in enumerate(ret):
            print("{}->{}\n".format(i, data))
        self.show_table(self.select_field_list, ret)

    def add(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = Sqlite_UI()
    ui.show()
    sys.exit((app.exec_()))