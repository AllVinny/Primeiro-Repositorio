import unittest
import pytest

from ano_bissexto import is_leap_year

'''class TestIsLeapYear(unittest.TestCase): #teste do unittest
    def test_is_leap_year_1(self):
        assert is_leap_year(1900) == False
    def test_is_leap_year_2(self):
        assert is_leap_year(2002) == False
    def test_is_leap_year_3(self):
        assert is_leap_year(2019) == False
    def test_is_leap_year_4(self):
        assert is_leap_year(2016) == True
    def test_is_leap_year_5(self):
        assert is_leap_year(2010) == False'''

class TestIsLeapYear: #teste do pytest
    @pytest.mark.parametrize("year", [1996, 2000, 2004, 2008, 2012, 2016, 2020, 2024])
    def test_is_leap_year_true(self, year):
        assert is_leap_year(year) == True

    @pytest.mark.parametrize("year", [1996, 2002, 2013, 1994, 2021, 2017])
    def test_is_leap_year_false(self, year):
        assert is_leap_year(year) == False


