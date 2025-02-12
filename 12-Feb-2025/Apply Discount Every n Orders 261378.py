# Problem: Apply Discount Every n Orders - https://leetcode.com/problems/apply-discount-every-n-orders/description/

class Cashier:
    def __init__(self, n, discount, products, prices):
        self.n = n  # Every nth customer gets a discount
        self.discount = discount  # Discount percentage
        self.count = 0  # Track the number of customers
        self.product_prices = {products[i]: prices[i] for i in range(len(products))}  # Store product prices in a dictionary

    def getBill(self, product, amount):
        self.count += 1
        bill = sum(self.product_prices[product[i]] * amount[i] for i in range(len(product)))
        
        if self.count % self.n == 0:  # Apply discount if it's the nth customer
            bill *= (100 - self.discount) / 100.0
        
        return bill

# Example usage:
cashier = Cashier(3, 50, [1,2,3,4,5,6,7], [100,200,300,400,300,200,100])
print(cashier.getBill([1,2], [1,2]))       # 500.0
print(cashier.getBill([3,7], [10,10]))     # 4000.0
print(cashier.getBill([1,2,3,4,5,6,7], [1,1,1,1,1,1,1])) # 800.0
print(cashier.getBill([4], [10]))          # 4000.0
print(cashier.getBill([7,3], [10,10]))     # 4000.0
print(cashier.getBill([7,5,3,1,6,4,2], [10,10,10,9,9,9,7])) # 7350.0
print(cashier.getBill([2,3,5], [5,3,2]))   # 2500.0
