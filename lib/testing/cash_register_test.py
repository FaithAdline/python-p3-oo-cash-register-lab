import io
import sys
from lib.cash_register import CashRegister

class TestCashRegister:
    '''CashRegister in cash_register.py'''

    def test_add_item(self):
        '''adds items to the register.'''
        cash_register = CashRegister()
        cash_register.add_item("apple", 1.50)
        assert cash_register.items == [("apple", 1.50)]

    # Add other test methods for remaining functionalities...

      