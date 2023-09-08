from gui import Ui_Dialog

from graph import Graph
from drawer import Drawer as drawer

import numpy as np
import matplotlib

matplotlib.use('TkAgg')


# КЛАСС АЛГОРИТМА ПРИЛОЖЕНИЯ
class GuiProgram(Ui_Dialog):

    def __init__(self, dialog):
        # Создаем окно
        Ui_Dialog.__init__(self)
        self.setupUi(dialog)  # Устанавливаем пользовательский интерфейс

        # ПОЛЯ КЛАССА
        # Параметры 1 графика
        self.graph_1 = Graph(
            layout=self.layout_plot_1,
            widget=self.widget_plot_1
        )

        # ДЕЙСТВИЯ ПРИ ВКЛЮЧЕНИИ
        # Для примера, от рисуем первичные данные
        self.draw()

        self.pushButton.clicked.connect(self.draw)  # Сохранить данные из таблицы в файл

    def draw(self):
        x = 10 * np.random.rand(5, 3)
        drawer.graph(self.graph_1, x)
