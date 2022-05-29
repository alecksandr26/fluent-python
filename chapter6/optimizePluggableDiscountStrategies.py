"""
An Optmize Interface Strategy program

Here no we don't use classes and also we calculate the best discount
"""

from abc import ABC, abstractmethod
from collections import namedtuple


Custumer = namedtuple('Custumer', 'name fidelity')


class LineItem:
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price


    def total(self):
        return self.price * self.quantity



class Order: # the Context

    def __init__(self, custumer, cart, promotion = None):
        self.custumer = custumer
        self.cart = list(cart)
        self.promotion = promotion

    def total(self):
        # __total is a private attribute 
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion(self)

        return self.total() - discount


    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())

    
# Another thing is that we replace all the classes with simple functions removing the abstract class

def fidelity_promo(order):
    return order.total() * 0.05 if order.custumer.fidelity >= 1000 else 0


def bulk_item_promo(order):
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * 0.1
    return discount


def large_order_promo(order):
    distinc_items = {item.product for item in order.cart}
    if len(distinc_items) >= 10:
        return order.total() * 0.07
    return 0
    

# globals returns a dictionary of all the functions
promos = [globals()[name] for name in globals()
          if name.endswith('_promo') and name != 'best_promo']


def best_promo(order):
    """ Returnt the best discount """
    return max(promo(order) for promo in promos)


# main: A few examples of how to use this strategy 
def main():
    # Customers
    joe = Custumer('John Doe', 0)
    ann = Custumer('Ann Smith', 1100)

    # the cart
    cart = [LineItem('Banana', 4, 0.5), LineItem('apple', 10, 1.5), LineItem('watermellon', 5, 5.0)]

    # Apply the strategy
    print("Fidelity Promo: ", Order(joe, cart, best_promo))
    
    banana_cart = [LineItem('banana', 30, 0.5), LineItem('apple', 10, 1.5)]
    print("BulkItemPromo: ", Order(ann, banana_cart, best_promo))
    
    long_order = [LineItem(str(item_code), 1, 1.0) for item_code in range(10)]
    print("LargeOrderPromo: ", Order(joe, long_order, best_promo))
    


if __name__ == "__main__":
    main()





