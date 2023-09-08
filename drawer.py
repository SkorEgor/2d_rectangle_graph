from graph import Graph
from mpl_toolkits.axes_grid1 import make_axes_locatable


# ШАБЛОНЫ ОТРИСОВКИ ГРАФИКОВ
# Очистка и подпись графика (вызывается в начале)
def cleaning_and_chart_graph(graph: Graph, x_label, y_label, title):
    graph.toolbar.home()  # Возвращаем зум в домашнюю позицию
    graph.toolbar.update()  # Очищаем стек осей (от старых x, y lim)
    # Очищаем график
    graph.axis.clear()
    # Задаем название осей
    graph.axis.set_xlabel(x_label)
    graph.axis.set_ylabel(y_label)
    # Задаем название графика
    graph.axis.set_title(title)


# Отрисовка (вызывается в конце)
def draw_graph(graph: Graph):
    # Убеждаемся, что все помещается внутри холста
    graph.figure.tight_layout()
    # Показываем новую фигуру в интерфейсе
    graph.canvas.draw()


# Отрисовка при отсутствии данных
def no_data(graph: Graph):
    graph.axis.text(0.5, 0.5, "Нет данных",
                    fontsize=14,
                    horizontalalignment='center',
                    verticalalignment='center')
    # Отрисовка, без подписи данных графиков
    draw_graph(graph)


# Класс художник. Имя холст (graph), рисует на нем данные
class Drawer:
    # ПАРАМЕТРЫ ГРАФИКОВ
    # График №1 Данные
    title_data = "График №1. Данные с исследуемым веществом и без вещества"
    horizontal_axis_name_data = "Частота [МГц]"
    vertical_axis_name_data = "Гамма [усл.ед.]"

    # ОТРИСОВКИ
    # (1) Без данных и с данными
    @staticmethod
    def graph(
            graph: Graph,
            data
    ):

        # Очистка, подпись графика и осей (вызывается в начале)
        cleaning_and_chart_graph(
            # Объект графика
            graph=graph,
            # Название графика
            title=Drawer.title_data,
            # Подпись осей
            x_label=Drawer.horizontal_axis_name_data, y_label=Drawer.vertical_axis_name_data
        )

        # Рисуем график
        im = graph.axis.imshow(data)
        # Если color bar нет- создаем, иначе обновляем
        if not graph.colorbar:
            divider = make_axes_locatable(graph.axis)
            cax = divider.append_axes("right", "10%", pad="3%")
            graph.colorbar = graph.figure.colorbar(im, orientation='vertical', cax=cax)


        else:
            graph.colorbar.update_normal(im)

        # Отрисовка (вызывается в конце)
        draw_graph(graph)
