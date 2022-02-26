from argparse import ArgumentParser
from decimal import Decimal, setcontext
import unittest

from balancetwofunds import *

setcontext(CONTEXT)


class StorePercentageActionTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.parser = ArgumentParser()
        self.parser.add_argument('positionalArg', action=StorePercentageAction)

    def test_valid_percentage(self) -> None:
        value = '0.5'
        ns = self.parser.parse_args([value])
        expected = Decimal(value)
        actual = ns.positionalArg
        self.assertEqual(expected, actual)

    def test_greater_than_one(self) -> None:
        value = '1.1'
        with self.assertRaises(ValueError):
            self.parser.parse_args([value])

    def test_less_than_zero(self) -> None:
        value = '-0.1'
        with self.assertRaises(ValueError):
            self.parser.parse_args([value])

    def test_doesnt_truncate(self) -> None:
        value = '0.55555'
        ns = self.parser.parse_args([value])
        truncated = Decimal(value).quantize(TWO_PLACES)
        parsed = ns.positionalArg
        self.assertNotEqual(truncated, parsed)


class StorePercentageActionTestCaseNoSetup(unittest.TestCase):

    def test_adjusted_metavar(self):
        expected = 'NewMetavar'
        parser = ArgumentParser()
        parser.add_argument('_', action=StorePercentageAction, metavar=expected)
        actual = parser._actions[1].metavar  # StorePercentageAction
        self.assertEqual(expected, actual)

    def test_nargs_errors(self):
        error_symbols = [1, 2, '*', '+']
        for symbol in error_symbols:
            with self.subTest(symbol=symbol):
                parser = ArgumentParser()
                with self.assertRaises(ValueError):
                    parser.add_argument('_', nargs=symbol, action=StorePercentageAction)

    def test_nargs_valid(self) -> None:
        symbols = [None, '?']
        for symbol in symbols:
            with self.subTest(symbol=symbol):
                parser = ArgumentParser()
                try:
                    parser.add_argument('_', nargs=symbol, action=StorePercentageAction)
                except ValueError:
                    self.fail()


class StoreFundBalanceActionTest(unittest.TestCase):

    def setUp(self) -> None:
        self.parser = ArgumentParser()
        self.parser.add_argument('positionalArg', action=StoreFundBalanceAction)

    def test_valid_balance(self):
        value = '330.21'
        ns = self.parser.parse_args([value])
        expected = Decimal(value)
        actual = ns.positionalArg
        self.assertEqual(expected, actual)

    def test_negative_balance(self):
        value = '-0.01'
        with self.assertRaises(ValueError):
            self.parser.parse_args([value])

    def test_truncation(self):
        value = '1082.44444'
        ns = self.parser.parse_args([value])
        expected = Decimal('1082.44')
        actual = ns.positionalArg
        self.assertEqual(expected, actual)


class StoreFundBalanceActionTestNoSetup(unittest.TestCase):

    def test_adjusted_metavar(self):
        expected = 'NewMetavar'
        parser = ArgumentParser()
        parser.add_argument('_', action=StoreFundBalanceAction, metavar=expected)
        actual = parser._actions[1].metavar  # StorePercentageAction
        self.assertEqual(expected, actual)

    def test_nargs_errors(self):
        error_symbols = [1, 2, '*', '+']
        for symbol in error_symbols:
            with self.subTest(symbol=symbol):
                parser = ArgumentParser()
                with self.assertRaises(ValueError):
                    parser.add_argument('_', nargs=symbol, action=StoreFundBalanceAction)

    def test_nargs_valid(self) -> None:
        symbols = [None, '?']
        for symbol in symbols:
            with self.subTest(symbol=symbol):
                parser = ArgumentParser()
                try:
                    parser.add_argument('_', nargs=symbol, action=StoreFundBalanceAction)
                except ValueError:
                    self.fail()


if __name__ == '__main__':
    unittest.main()
