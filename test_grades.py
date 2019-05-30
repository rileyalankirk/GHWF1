
from grades import compute_hw_average

def test_zero_grades():
    grades = []
    assert compute_hw_average(grades) == 0


def test_single_grade():
    grades = [42]
    assert compute_hw_average(grades) == 42

def test_many_grades():
    grades = [30, 15, 15]
    assert compute_hw_average(grades) == 20
