import unittest
from unittest.mock import patch, MagicMock
from main import *

class TestListAll(unittest.TestCase):
    @patch('main.mysql.connector.connect')
    def test_list_all_accounts(self, mock_connect):
        # Mock the cursor and its execute method
        mock_cursor = MagicMock()
        mock_cursor.execute.return_value = None
        mock_cursor.fetchall.return_value = [
            (1001,	'John Doe',	            11000,	4321,	0),
            (1002,	'Jane Smith',	            7500,	5678,	0),
            (1003,	'Michael Johnson',	    3000,	9876,	0),
            (1004,	'Emily Brown',            10000,	4321,	0),
            (1005,	'David Lee',	            2000,	7890,	0),
            (1006,	'Sarah Wilson',	        6000,	2468,	0),
            (1007,	'Robert Garcia',	        9000,	1357,	0),
            (1008,	'Lisa Taylor',	        4000,	8024,	0),
            (1009,	'William Martinez'	   ,8500,	6489,	0),
            (1010,	'Jennifer White'	       ,7000,	3579,	0),
            (1011,	'Christopher Rodriguez',  5500,	2460,	0),
            # Add more data here...
        ]
        mock_connect.return_value.cursor.return_value = mock_cursor

        # Call the function
        listAll()

        # Assert that the cursor's execute method was called
        mock_cursor.execute.assert_called_once()

        # Assert that the fetched data was printed correctly
        mock_cursor.fetchall.assert_called_once()
        # You can add more assertions here based on the expected output
class TestWithdraw(unittest.TestCase):

    @patch('builtins.input', side_effect=['1001', '4321', '2000'])
    def test_withdraw_successful(self, mock_input):
        withdraw('1001', '4321', 2000)
        # Add assertions here to verify the withdrawal was successful

    @patch('builtins.input', side_effect=['1001', '0000', '2000'])
    def test_withdraw_invalid_pin(self, mock_input):
        withdraw('1001', '0000', 2000)
        # Add assertions here to verify that the withdrawal failed due to invalid PIN

class TestDeposit(unittest.TestCase):

    @patch('builtins.input', side_effect=['1001', '2000'])
    def test_deposit_successful(self, mock_input):
        deposit('1001', 2000)
        # Add assertions here to verify the deposit was successful

    @patch('builtins.input', side_effect=['1001', '-500'])  # Incorrect input (-500 is a string)
    def test_deposit_invalid_amount(self, mock_input):
        deposit('1001', -500)  # Incorrect parameter count and type
        # Add assertions here to verify that the deposit failed due to invalid amount

class TestChangePin(unittest.TestCase):

    @patch('builtins.input', side_effect=['1001', '4321', '4321'])
    def test_change_pin_successful(self, mock_input):
        change_pin('1001', '4321', '4321')
        # Add assertions here to verify the PIN was successfully changed

    @patch('builtins.input', side_effect=['1001', '0000', '1111'])
    def test_change_pin_invalid_current_pin(self, mock_input):
        change_pin('1001', '0000', '1111')
        # Add assertions here to verify that the PIN change failed due to invalid current PIN

class TestViewAccount(unittest.TestCase):

    @patch('builtins.input', return_value='1001')
    def test_view_account_successful(self, mock_input):
        viewAccount('1001')
        # Add assertions here to verify that the account details are correctly displayed

    @patch('builtins.input', return_value='9999')
    def test_view_account_nonexistent(self, mock_input):
        viewAccount('9999')
        # Add assertions here to verify that the function handles a nonexistent account correctly

if __name__ == '__main__':
    unittest.main()
