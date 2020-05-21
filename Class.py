import pickle
import glob


class Cake:
    known_types = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel', 'other']
    bakery_offer = []

    def __init__(self, name, kind, taste, additives, filling, gluten_free, text):
        self.name = name
        if kind in Cake.known_types:
            self.kind = kind
        else:
            self.kind = 'other'
        self.taste = taste
        self.additives = additives
        self.filling = filling
        self.bakery_offer.append(self)
        self.__gluten_free = gluten_free
        if kind == 'cake' or text == "":
            self.__text = text
        else:
            self.__text = ""
            print('Text can be set only for cake ({})'.format(name))

    def show_info(self):
        print('{}'.format(self.name).upper())
        print('Kind: {}'.format(self.kind))
        print('Taste: {}'.format(self.taste))
        if len(self.additives) > 0:
            print('Additives: {}'.format(self.additives))
        if len(self.filling) > 0:
            print('Filling: {}'.format(self.filling))
        print('Gluten free: {}'.format(self.__gluten_free))
        print("Text : {}".format(self.__text))
        print('-' * 30)

    def set_filling(self, filling):
        self.filling = filling

    def add_additives(self, additives):
        self.additives.extend(additives)

    @property
    def Text(self):
        return self.__text

    @Text.setter
    def Text(self, new_text):
        if self.kind == 'cake':
            self.__text = new_text
        else:
            print('>>>>>Text can be set only for cake ({})'.format(self.name))

    @Text.deleter
    def Text(self):
        self.__text = None

    def save_to_file(self, path):
        with open(path, "wb") as f:
            pickle.dump(self, f)

    @classmethod
    def read_from_file(cls, path):
        with open(path, "rb") as f:
            new_cake = pickle.load(f)
        cls.bakery_offer.append(new_cake)
        return new_cake

    @staticmethod
    def get_bakery_files(path_directory):
        result = glob.glob(path_directory + "/*.bake")
        return result


cake1 = Cake('Vanilla Cake', 'cake', 'vanilla ', ['chocolade', 'nuts'], 'cream', True, 'B-DAY')
cake2 = Cake('Chocolade Muffin', 'muffin', 'chocolade', ['chocolade'], 'dd', False, '')
cake3 = Cake('Super Sweet Maringue', 'meringue', 'very sweet  ', [], '', True, '')
cake4 = Cake('Cocoa waffle', 'waffle', 'cocoa', [], 'cocoa', False, "STO LAT")

cake2.set_filling('Cream')
cake3.add_additives(['kokos', 'kakaoo'])

print("Today in our offer:\n")
for cake in Cake.bakery_offer:
    cake.show_info()

cake1.Text = 'HAPPY BIRTHDAY'
cake4.Text = 'HAPPY B-DAY'

for cake in Cake.bakery_offer:
    cake.show_info()

cake1.save_to_file(r"C:\Users\Mikołaj\Desktop\PYT\plik.bake")
cake5 = Cake.read_from_file(r"C:\Users\Mikołaj\Desktop\PYT\plik.bake")
