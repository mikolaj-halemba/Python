class NoDuplicates:
    def __init__(self, func):
        self.func = func

    def __call__(self, cake, additives):
        self.no_duplicate_list = []
        for additive in additives:
            if not additive in cake.additives:
                self.no_duplicate_list.append(additive)
        self.func(cake, self.no_duplicate_list)


class Cake:
    bakery_offer = []

    def __init__(self, name, kind, taste, additives, filling):

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

    def add_additives(self, additives):
        self.additives.extend(additives)

    def __str__(self):
        return "Kind: {} Name: {} Additives {}".format(self.kind, self.name, self.additives)

    def __iadd__(self, other):
       if type(other) == str:
           self.additives.append(other)
           return self
       elif type(other) == list:
           self.additives.extend(other)
           return self
       else:
           raise Exception('Sorry - operation not implemented')




@NoDuplicates
def add_extra_additives(cake, additives):
    cake.add_additives(additives)


cake01 = Cake('Vanilla Cake', 'cake', 'vanilla', ['chocolade', 'nuts'], 'cream')

add_extra_additives(cake01, ['strawberries', 'sugar-flowers', 'chocolade', 'nuts'])
cake01.show_info()

print("*" * 50)
cake01 += ['whipped cream', 'raspberry']
print(cake01)
