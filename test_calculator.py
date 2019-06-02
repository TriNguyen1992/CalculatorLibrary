"""
Unit tests for the calculator library
"""

import calculator


class TestCalculator:

    def test_addition1(self):
        assert 4 == calculator.add(2, 2)

    def test_addition2(self):
        assert 0 == calculator.add(2, -2)

    def test_subtraction(self):
        assert 2 == calculator.subtract(4, 1)
