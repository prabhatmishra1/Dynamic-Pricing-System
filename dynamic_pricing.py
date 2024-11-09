class Product:
    """
    This class will manage the product related information
    """

    def __init__(self, name, base_price):
        self.name = name
        self.base_price = base_price

    def get_price(self):
        return self.base_price


class SeasonalProduct(Product):
    """
    This class will offer the discount for seasonal product
    """

    def __init__(self, name, base_price, season_discount):
        super().__init__(name, base_price)
        # perform the discount validation here
        if not (0 <= season_discount < 1):
            raise ValueError(
                "Seasonal discount must be a percentage value between 0 and 1.")
        self.season_discount = season_discount

    def get_price(self):
        # Get the price from thr product and then perform the calculation
        return max(0, super().get_price()*(1 - self.season_discount))


class BulkProduct(Product):
    """
    This class will offer the discount for bulk product
    """

    def __init__(self, name, base_price,  bulk_discount):
        super().__init__(name, base_price)
        if not (0 <= bulk_discount < 1):
            raise ValueError(
                "Bulk discount must be a percentage value between 0 and 1.")
        self.bulk_discount = bulk_discount

    def get_price(self):
        # Get the price from the product price and then perform the calculation
        return max(0, super().get_price()*(1 - self.bulk_discount))


class Discount:
    """
    Base class to manage the discounts
    """

    def __init__(self, discount_value):
        self.discount_value = discount_value

    def apply_discount(self, price):
        raise NotImplementedError("Subclasses must implement this")


class PercentageDiscount(Discount):
    """
    Manage percentage discount
    """

    def __init__(self, discount_value):
        if not (0 <= discount_value < 1):
            raise ValueError("Percentage discount must be between 0 and 1.")
        super().__init__(discount_value)

    def apply_discount(self, price):
        # Discount does not exceed price and avoid negative prices
        discounted_price = price * (1 - self.discount_value)
        return max(0, discounted_price)


class FixedAmountDiscount(Discount):
    """
    Manage fixed discount
    """

    def apply_discount(self, price):
        # Discount does not exceed price and avoid negative prices
        if self.discount_value > price:
            raise ValueError("Fixed discount cannot exceed the original price.")
        return max(0, price - self.discount_value)


class Order:
    """
    This class will have the order related information
    """

    def __init__(self):
        self.products = []
        # Order can have discount or not ?
        self.discount = None

    def add_product(self, product):
        # Add product for the order
        self.products.append(product)

    def set_discount(self, discount):
        # Add discount for the order
        self.discount = discount

    def calculate_total_price(self):
        # get the final price of an order after discounts
        total_price = 0
        for product in self.products:
            total_price += product.get_price()
        if self.discount:
            total_price = self.discount.apply_discount(total_price)
        return total_price


if __name__ == "__main__":
    # First the create the products
    timex_watch = Product('Timex Watch', 30000)
    # Create the seasonal product
    winter_jacket = SeasonalProduct('Winter Jacket', 4000, 0.10)  # 10% seasonal discount
    # Create the bulk product
    bulk_products = BulkProduct('Household Products', 10000, 0.15)  # 15% bulk discount

    # Add create the order
    order = Order()
    products = [timex_watch, winter_jacket, bulk_products]
    #  Add products
    for product in products:
        order.add_product(product)

    # Calculate total price without any additional order discount
    print("Total Price without additional discount:", order.calculate_total_price())

    # Set a percentage discount on the entire order and calculate the new total
    order.set_discount(PercentageDiscount(0.05))  # 5% order-wide discount
    print("Total Price with 5% order-wide discount:", order.calculate_total_price())

    # Set a fixed discount on the entire order and calculate the new total
    order.set_discount(FixedAmountDiscount(100))  # 100 order-wide discount
    print("Total Price with 100 order-wide discount:", order.calculate_total_price())
