import unittest
from client3 import (
  getDataPoint,
  getRatio
)

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote['stock'], float(quote['top_bid']['price']), float(quote['top_ask']['price']), round((float(quote['top_bid']['price']) + float(quote['top_ask']['price'])) / 2, 2)))

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 177.87, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 121.68, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote['stock'], float(quote['top_bid']['price']), float(quote['top_ask']['price']), round((float(quote['top_bid']['price']) + float(quote['top_ask']['price'])) / 2, 2)))

  """ ------------ Add more unit tests ------------ """
  def test_getDataPoint_calculatePriceBidSmallerThanAsk(self):
    quotes = [
      {'top_ask': {'price': 120.48, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 119.2, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote['stock'], float(quote['top_bid']['price']), float(quote['top_ask']['price']),round((float(quote['top_bid']['price']) + float(quote['top_ask']['price'])) / 2, 2)))

  def test_getRatio(self):
    price_a = 10
    price_b = 20

    self.assertEqual(getRatio(price_a,price_b), round(price_a/price_b, 2))


  def test_getRatio_denominator_equals_0(self):
    price_a = 10
    price_b = 0

    self.assertEqual(getRatio(price_a,price_b), None, "The function should return None when b is 0")


if __name__ == '__main__':
    unittest.main()
