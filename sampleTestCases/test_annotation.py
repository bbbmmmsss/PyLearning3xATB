import pytest

@pytest.mark.smoke

def test_addition():
    assert 2+2 == 4

@pytest.mark.regression

def test_addition():
    assert 2+2 == 4

@pytest.mark.sanity
def test_addition():
    assert 2+2 == 4
