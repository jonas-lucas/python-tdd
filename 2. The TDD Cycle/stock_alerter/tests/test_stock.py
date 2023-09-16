import unittest
from ..stock import Stock
from datetime import datetime

class StockTest(unittest.TestCase):
    def setUp(self):
        self.goog = Stock("GOOG")
    
    def test_price_of_a_new_stock_class_should_be_None(self):
        # stock = Stock("GOOG")
        self.assertIsNone(self.goog.price)
        
    def test_stock_update(self):
        """An update should be the price on the stock object
        We will be using the `datetime` module for the timestamp
        """
        # goog = Stock("GOOG")
        self.goog.update(datetime(2014, 2, 12), price=10)
        self.assertEqual(10, self.goog.price)
        
    # Test for Exceptions
    def test_negative_price_should_throw_ValueError(self):
        # goog = Stock("GOOG")
        self.assertRaises(ValueError, self.goog.update, datetime(2014, 2, 13), -1)
        with self.assertRaises(ValueError):
            self.goog.update(datetime(2014, 2, 13), -1)
        
    def test_stock_price_should_give_the_latest_price(self):
        # goog = Stock("GOOG")
        self.goog.update(datetime(2014, 2, 12), price=10)
        self.goog.update(datetime(2014, 2, 13), price=8.4)
        self.assertAlmostEqual(8.4, self.goog.price, delta=0.0001)
        self.assertAlmostEqual(8.4, self.goog.price, places=4)

class StockTrendTest(unittest.TestCase):
    def setUp(self):
        self.goog = Stock("GOOG")
        
    def given_a_series_of_prices(self, prices):
        timestamps = [datetime(2014, 2, 10), datetime(2014, 2, 11),
                      datetime(2014, 2, 12), datetime(2014, 2, 13)]
        for timestamp, price in zip(timestamps, prices):
            self.goog.update(timestamp, price)
        
    def test_increasing_trend_is_true_if_price_increase_for_3_updates(self):
        self.given_a_series_of_prices([8, 10, 12])
        self.assertTrue(self.goog.is_increasing_trend())
        
    def test_increasing_trend_is_false_if_price_decreases(self):
        self.given_a_series_of_prices([8, 12, 10])
        self.assertFalse(self.goog.is_increasing_trend())
        
    def test_increasing_trend_is_false_if_price_equal(self):
        self.given_a_series_of_prices([8, 10, 10])
        self.assertFalse(self.goog.is_increasing_trend())
        
# Add by me.
class StockExerciseTest(unittest.TestCase):
    def setUp(self):
        self.goog = Stock("GOOG")
        
    def test_older_timestamp_should_throw_ValueError(self):
        with self.assertRaises(ValueError):
            self.goog.update(datetime(2014, 2, 13), 1)
            self.goog.update(datetime(2014, 2, 12), 2)
        