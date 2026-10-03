import sys
from packet.math_func import __math_func__
from packet.report import __report__
from PySide6.QtWidgets import QApplication, QMessageBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile

app = QApplication(sys.argv)

# Загружаем интерфейс из файла
ui_file = QFile("lab2.ui")
ui_file.open(QFile.ReadOnly)

loader = QUiLoader()
window = loader.load(ui_file)
ui_file.close()

P_WOOD_OAK = 700.0
P_WOOD_PINE = 500.0
P_METAL_STEEL = 7850.0
P_METAL_ALUMINIUM = 2700.0
P_GLASS = 2500.0
figures_list = ["Шар", "Тетраэдр", "Параллелепипед"]
materials_list = ["Дерево (Дуб)", "Дерево (Сосна)", "Металл (Сталь)", "Металл (Алюминий)", "Стекло"]
p_list = [P_WOOD_OAK, P_WOOD_PINE, P_METAL_STEEL, P_METAL_ALUMINIUM, P_GLASS]

class __interface_func__():

    def change_form():

        index = window.SelectFigureComboBox.currentIndex()
        window.stackedWidget.setCurrentIndex(index)

    def result_button():

        index = window.SelectFigureComboBox.currentText()
        pindex = window.SelectMaterialComboBox.currentIndex()

        if index == "Параллелепипед":
            try:
                x = float(window.ParalXTextbox.text())
                y = float(window.ParalYTextbox.text())
                z = float(window.ParalZTextbox.text())
                if x <= 0 or y <= 0 or z <= 0:
                    QMessageBox.critical(window, "Ошибка ввода!", f"Ожидается ПОЛОЖИТЕЛЬНОЕ число или число с плавающей точкой (0.0) {err}")
                else:
                    v = __math_func__.paral_volume_func(x, y, z)
                    s = __math_func__.paral_squaresurf_func(x, y, z)
                    mass = __math_func__.mass_func(p_list[pindex], v)
                    window.ParalVolumeTextbox.setText(str(v))
                    window.ParalSquaresurfTextbox.setText(str(s))
                    window.ParalMassTextbox.setText(str(mass))
                    __report__.add_record(index, materials_list[pindex], x, y, z, v, s, mass)
            except Exception as err: 
                QMessageBox.critical(window, "Ошибка ввода!", f"Ожидается положительное ЧИСЛО или число с плавающей точкой (0.0) {err}")
        elif index == "Тетраэдр":
            try:
                a = float(window.TetraATextbox.text())
                if a <= 0:
                    QMessageBox.critical(window, "Ошибка ввода!", f"Ожидается ПОЛОЖИТЕЛЬНОЕ число или число с плавающей точкой (0.0) {err}")
                else:
                    v = __math_func__.tetra_volume_func(a)
                    s = __math_func__.tetra_squaresurf_func(a)
                    mass = __math_func__.mass_func(p_list[pindex], v)
                    window.TetraVolumeTextbox.setText(str(v))
                    window.TetraSquaresurfTextbox.setText(str(s))
                    window.TetraMassTextbox.setText(str(mass))
                    __report__.add_record(index, materials_list[pindex], a, "-", "-", v, s, mass)
            except Exception as err: 
                QMessageBox.critical(window, "Ошибка ввода!", f"Ожидается положительное ЧИСЛО или число с плавающей точкой (0.0) {err}")
        elif index == "Шар":
            try:
                r = float(window.OrbRTextbox.text())
                if r <= 0:
                    QMessageBox.critical(window, "Ошибка ввода!", f"Ожидается ПОЛОЖИТЕЛЬНОЕ число или число с плавающей точкой (0.0) {err}")
                else:
                    v = __math_func__.orb_volume_func(r)
                    s = __math_func__.orb_squaresurf_func(r)
                    mass = __math_func__.mass_func(p_list[pindex], v)
                    window.OrbVolumeTextbox.setText(str(v))
                    window.OrbSquaresurfTextbox.setText(str(s))
                    window.OrbMassTextbox.setText(str(mass))
                    __report__.add_record(index, materials_list[pindex], r, "-", "-", v, s, mass)
            except Exception as err: 
                QMessageBox.critical(window, "Ошибка ввода!", f"Ожидается положительное ЧИСЛО или число с плавающей точкой (0.0) {err}")

    def report_button():
        try:
            __report__.export_report()
            QMessageBox.information(window, "Успех!", "Отчет успешно создан!")
        except Exception:
            QMessageBox.critical(window, "Ошибка отчета!", "Совершите вычисление, чтобы отчет не был пустым!")

    def note_button():
        QMessageBox.information(window, "Справка", """Программа предназначена для вычисления объема, площади поверхности и массы (по определенным материалам) для геометрических фигур.

        1. Для начала работы выберите фигуру и материал, для которых вы хотите провести расчеты. После выбора фигуры откроется панель для выбранной фигуры, в которую вы можете вводить данные.
        1.1 Для параллелепипеда вводятся 3 стороны параллелепипеда, для тетраэдра - вводиться длина ребра, для шара - длина радиус. Формат ввода - положительное число (0) или положительное число с плавающей точкой (0.0). Все расчеты ведутся в метрах (для объема и площади поверхности метры в кубе и метры в квадрате соответственно), а вывод массы ведется в килограммах.

        2. По нажатию кнопки "Получить результат" производятся расчеты по введенным данным. Результаты выводятся в панели, под соответствующими надписями. После каждого успешного проведения расчетов, результат временно записывается в датасет для последующего отчета.

        3. По нажатию кнопки "Получить отчет" производится создание отчета формата .xlsx со всеми проведенными операциями за текущую сессию. Отчет выводится в папку report. Создание нового отчета не удаляет старый отчет. Все проведенные операции обнуляются после выхода из программы.""")
    
class main():

    window.SelectFigureComboBox.addItems(figures_list)
    window.SelectMaterialComboBox.addItems(materials_list)

    window.ResultButton.clicked.connect(__interface_func__.result_button)
    window.SelectFigureComboBox.currentTextChanged.connect(__interface_func__.change_form)
    window.ExitButton.clicked.connect(QApplication.instance().quit)
    window.ReportButton.clicked.connect(__interface_func__.report_button)
    window.NoteButton.clicked.connect(__interface_func__.note_button)
    window.stackedWidget.setCurrentIndex(0)

    window.show()
    sys.exit(app.exec())