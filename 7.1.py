class Buyer:
    def __init__(self, money, bag_size):
        self.money = money
        self.bag_size = bag_size
        self.limited_goods = {'apple': [10000, 2],
                              'milks': [40000, 3],
                              'beef': [100000, 3]}  # goods: [cost, count]

    def buy(self, **goods_counts):  # goods: count
        try:
            count = 0
            for food in goods_counts:
                count += goods_counts[food]
                if goods_counts[food] > self.limited_goods[food][1]:
                    return 'Not enough {0} in store!'.format(food)
        except KeyError:
            return 'This food not in stock!'
            
            if count > self.bag_size:
                return "Not enough bag space!"
            else:
                costs = 0
                for food in goods_counts:
                    costs += self.limited_goods[food][0] * goods_counts[food]
                    # costs = cost_of_goods * count_of_buyer
                if costs > self.money:
                    return 'Not enough money!'
                else:
                    for food in goods_counts:
                        self.limited_goods[food][1] -= goods_counts[food]
                    self.money -= costs
                    self.bag_size -= count
                    return 'Traded!'
                    

if __name__ == '__main__':
    buyer1 = Buyer(300000, 7)
    buyer2 = Buyer(20000, 4)
    print buyer1.buy(apple=1, beef=2)
    print buyer1.buy(apple=2, beef=1)
    print buyer2.buy(apple=1, milks=2, beef=1)
    print buyer2.buy(apple=1, milks=3, beef=1)
    print buyer2.buy(nho=1, tao=2)

# output:
#     Traded!
#     Not enough apple in store!
#     Not enough money!
#     Not enough bag space!
#     This food not in stock!
