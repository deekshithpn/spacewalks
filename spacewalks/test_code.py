import pytest
from eva_data_analysis import (
    text_to_duration,
    calculate_crew_size)

def test_text_to_duration_integer():
    assert text_to_duration("10:00") == 10

def test_text_to_duration_float():
    assert text_to_duration("10:15") == 10.25

def test_text_to_duration_rational():
    assert text_to_duration("10:20") == pytest.approx(10.333333)

def test_calculate_crew_size():
    actual_result = calculate_crew_size("Valentina Tereshkova;")
    expected_result = 1
    assert actual_result == expected_result

    actual_result = calculate_crew_size("Judith Resnik; Sally Ride;")
    expected_result = 2
    assert actual_result == expected_result