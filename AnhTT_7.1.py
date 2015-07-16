class Buyer:
    def __init__(self, money, bag_size):
        self.money = money
        self.bag_size = bag_size

    def trade(self, seller, **goods_counts):
        try:
            count = 0
            for food in goods_counts:
                count += goods_counts[food]
                if goods_counts[food] > seller.limited_goods[food]['quantity']:
                    return 'Not enough {0} in store!'.format(food)
        except KeyError:
            return 'This food is not available in stock!'
        if count > self.bag_size:
            return "Not enough bag space!"
        else:
            costs = 0
            for food in goods_counts:
                costs += seller.limited_goods[food]['price'] * goods_counts[food]
                # costs = cost_of_goods * count_of_buyer
            if costs > self.money:
                return 'Not enough money!'
            else:
                for food in goods_counts:
                    seller.limited_goods[food]['quantity'] -= goods_counts[food]
                self.money -= costs
                self.bag_size -= count
                return 'Traded! Seller has {0}, Buyer remaining {1}'.format(
                    costs, self.money
                )


class Seller:
    def __init__(self):
        self.limited_goods = {'apple': {'price': 10000, 'quantity': 2},
                              'milk': {'price': 40000, 'quantity': 3},
                              'beef': {'price': 100000, 'quantity': 3}
                              }


if __name__ == '__main__':
    buyer = Buyer(300000, 7)
    seller = Seller()
    print buyer.trade(seller, apple=1, beef=2)
    print buyer.trade(seller, apple=2, beef=1)
    print buyer.trade(seller, apple=1, beef=1, milk=2)
    print buyer.trade(seller, apple=1, beef=1, milk=3)
    print buyer.trade(seller, nho=2, tao=1, buoi=3)

# output:
#     Traded! Seller has 210000, Buyer remaining 90000
#     Not enough apple in store!
#     Not enough money!
#     Not enough bag space!
#     This food is not available in stock!
