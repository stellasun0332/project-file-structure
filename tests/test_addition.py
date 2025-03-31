<<<<<<< HEAD
import src.addition as addition
=======

from src import addition
>>>>>>> bf0bc2843b167989453dac9a80664f7ff179846c

def test_addition():
    # Assert
    assert addition.perform_operation(1, 1) == 2
    assert addition.perform_operation(800, 88) == 888
    assert addition.perform_operation(-1, 1) == 0