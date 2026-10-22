import pytest
from main import areatriangulo

def test_area_triangulo():
    actual_result = areatriangulo(13, 3)
    assert actual_result == pytest.approx(19.5,abs=0.01)