from datetime import date
from datetime import timedelta


class Cake:
    """
    Cake class for our bakery solution
    """
    bakery_offer = []

    def __init__(self, name, kind, taste, additives, filling):
        """
        __init__ takes all the parameters and saves them
        """
        self.name = name
        self.kind = kind
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling
        self.bakery_offer.append(self)

    def show_info(self):
        print("{}".format(self.name.upper()))
        print("Kind:        {}".format(self.kind))
        print("Taste:       {}".format(self.taste))
        if len(self.additives) > 0:
            print("Additives:")
            for a in self.additives:
                print("\t\t{}".format(a))
        if len(self.filling) > 0:
            print("Filling:     {}".format(self.filling))
        print('-' * 20)

    @property
    def full_name(self):
        """
        Just return the most important attributes of the object
        """
        return "--== {} - {} ==--".format(self.name.upper(), self.kind)


class Promo:

    def __init__(self, name, discount, start_date, end_date, minimal_order):
        self.name = name
        self.discount = discount
        self.start_date = start_date
        self.end_date = end_date
        self.minimal_order = minimal_order

    @property
    def full_name(self):
        return "PROMO {0:s} {1:.0%}".format(self.name, self.discount)


class Promocake(Cake, Promo):

    def __init__(self, cake, promo):
        Cake.__init__(self, cake.name, cake.kind, cake.taste, cake.additives, cake.filling)
        Promo.__init__(self, promo.name, promo.discount, promo.start_date, promo.end_date, promo.minimal_order)


cake1 = Cake('Vanilla cake', 'cake', 'vanilla', ['chocolade', 'nuts'], 'cream')
cake1.show_info()
promo10 = Promo("DISCOUNT - no additional conditions", 0.15, date.today(), date.today() + timedelta(days=14), 0)
print(promo10.full_name)
promo_cake = Promocake(cake1, promo10)
promo_cake.show_info
print(promo_cake.full_name)
