# cd C:\Users\GamePC\Desktop\University-Project\3curs1semestr\TheoryOfAlgoritms\Laboratory2
# py -3.12 -m pytest -v

import math
import pandas as pd
from unittest.mock import patch
import report
from math_func import __math_func__
from report import __report__
import pytest

class TestMathFunc:

    # 1. Тесты для параллелепипеда
    def test_paral_volume(self):
        assert __math_func__.paral_volume_func(2, 3, 4) == 24.0
        assert __math_func__.paral_volume_func(1.5, 2.0, 3.0) == 9.0

    def test_paral_squaresurf(self):
        # 2*(2*3 + 2*4 + 3*4) = 2*(6 + 8 + 12) = 52
        assert __math_func__.paral_squaresurf_func(2, 3, 4) == 52.0

    # 2. Тесты для правильного тетраэдра
    def test_tetra_volume(self):
        # При a = 1: 1 / (6 * sqrt(2)) ≈ 0.117851
        expected = round(1 / (6 * math.sqrt(2)), 6)
        assert __math_func__.tetra_volume_func(1) == expected

    def test_tetra_squaresurf(self):
        # При a = 2: sqrt(3) * 4 ≈ 6.928203
        expected = round(math.sqrt(3) * 4, 6)
        assert __math_func__.tetra_squaresurf_func(2) == expected

    # 3. Тесты для шара ( сферы )
    def test_orb_volume(self):
        # При r = 3: (4 * pi * 27) / 3 = 36 * pi ≈ 113.097336
        expected = round(36 * math.pi, 6)
        assert __math_func__.orb_volume_func(3) == expected

    def test_orb_squaresurf(self):
        # При r = 2: 4 * pi * 4 = 16 * pi ≈ 50.265482
        expected = round(16 * math.pi, 6)
        assert __math_func__.orb_squaresurf_func(2) == expected

    # 4. Тесты расчета массы (Параметризация)
    @pytest.mark.parametrize("p, v, expected_mass", [
        (7850, 0.5, 3925.0),
        (2500, 0.1, 250.0),
        (0, 10, 0.0),
    ])
    def test_mass_func(self, p, v, expected_mass):
        assert __math_func__.mass_func(p, v) == expected_mass

class TestReport:

    # Фиктура для очистки DataFrame перед каждым тестом
    @pytest.fixture(autouse=True)
    def reset_dataframe(self):
        report.df.drop(report.df.index, inplace=True)

    # 1. Проверка добавления записи в DataFrame
    def test_add_record(self):
        assert len(report.df) == 0
        
        __report__.add_record("Параллелепипед", "Сталь", 2, 3, 4, 24.0, 52.0, 188400.0)
        
        assert len(report.df) == 1
        assert report.df.loc[0, "Figure"] == "Параллелепипед"
        assert report.df.loc[0, "Mass"] == 188400.0

    # 2. Проверка выброса Exception, если DataFrame пустой
    def test_export_report_empty_raises_exception(self):
        with pytest.raises(Exception):
            __report__.export_report()

    # 3. Проверка экспорта в Excel при наличии данных
    def test_export_report_success(self, tmp_path):
        # Добавляем данные
        __report__.add_record("Шар", "Стекло", 1, 0, 0, 4.18879, 12.566371, 10471.975)
        
        test_file = tmp_path / "Report0.xlsx"
        
        # Подменяем генерацию пути и функцию записи, чтобы проверить вызов to_excel
        with patch("report.path.exists", return_value=False), \
             patch.object(pd.DataFrame, "to_excel") as mock_to_excel:
            
            __report__.export_report()
            
            # Проверяем, что метод записи в excel действительно вызывался
            mock_to_excel.assert_called_once()

if __name__ == "__main__":
    pytest.main(["-v", "-s", __file__])