# Verify user identity：
class UserVerification:
    def verify(self, user_id):
        if user_id != 'U001' and user_id != 'U002' and user_id != 'U003':
            raise ValueError("Invalid user ID")
    
# Verify the price of item：
class ItemVerification:
    def verify(self, item):
        if item['price'] < 0 :
            raise ValueError("Item price cannot be negative")
        
# Calculate the total order price：
class PriceCalculation:
    def calculate_total(self, items):
        total_price = 0
        for item in items:
            total_price += item['price']*item['quantity']
        return total_price
    
# Record Order:
class OrderRecord:
    def __init__(self):
        self.orders = []

    def add_order(self, user_id, items, total_price):
        self.orders.append({
            "user_id" : user_id,
            "items" : items,
            "total_price" : total_price
        })

# Send email notification:
class SendNotification:
    def send_notification(self, user_id, total_price):
        print(f"Email sent to user {user_id}: Your order of ${total_price} is confirmed.")



# Coordinate each responsibility class to complete the process:
class OrderProcessor:
    def __init__(self):
        self.user_valid = UserVerification()
        self.item_valid = ItemVerification()
        self.calculate_price = PriceCalculation()
        self.record_order = OrderRecord()
        self.notification = SendNotification()

    def process_order(self, user_id, items):
        # Verify user identity：
        self.user_valid.verify(user_id)
        # Verify the price of item：
        for item in items:
            self.item_valid.verify(item)
        # Calculate the total order price：
        total_price = self.calculate_price.calculate_total(items)
        # Record Order:
        self.record_order.add_order(user_id, items, total_price)
        # Send email notification:
        self.notification.send_notification(user_id, total_price)
        # return total_price:
        return total_price



# unit test cases:
import unittest
from unittest.mock import patch

class UnitTest(unittest.TestCase):
    def setUp(self):
        self.processor = OrderProcessor()
        self.valid_user = "U001"
        self.invalid_user = "U123"
        self.valid_items = [{"price": 100, "quantity": 5}]
        self.invalid_items =[{"price": -99, "quantity": 3}]

    # normal processes:
    def test_normal_processes(self):
        totalPrice = self.processor.process_order(self.valid_user, self.valid_items)
        self.assertEqual(totalPrice, 500)
    
    # invalid users:
    def test_invalid_user(self):
        with self.assertRaises(ValueError):
            self.processor.process_order(self.invalid_user, self.valid_items)

    # invalid items:
    def test_invalid_items(self):
        with self.assertRaises(ValueError):
            self.processor.process_order(self.valid_user, self.invalid_items)

if __name__ == "__main__":
    unittest.main()    