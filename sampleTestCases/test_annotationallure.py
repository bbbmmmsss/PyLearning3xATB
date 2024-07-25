import pytest
import allure

@allure.title("TC-1 verify that 2+2 is 4" )
@pytest.mark.smoke

def test_addition():
    assert 2+2 == 4
@allure.title("TC-2 verify that 2-2 is 0" )
@pytest.mark.regression

def test_subtraction():
    assert 2-2 == 0

@allure.title("TC-3 verify that 2*2 is 4" )
@pytest.mark.sanity
def test_multiplication():
    assert 2*2 == 4

@allure.title("TC-4cls verify that 2-2 is 4" )
@pytest.mark.smoke

def test_subtraction():
    assert 2-2 == 0
