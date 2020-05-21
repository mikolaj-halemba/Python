import pickle
import glob
import types


def export_1_cake_to_html(obj, path):
    template = """
<table border=1>
     <tr>
       <th colspan=2>{}</th>
     </tr>
       <tr>
         <td>Kind</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Taste</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Additives</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Filling</td>
         <td>{}</td>
       </tr>
</table>"""
    with open(path, "w") as file:
        content = template.format(obj.name, obj.kind, obj.taste, obj.additives, obj.filling)
        file.write(content)


def export_all_cakes_to_html(cls, path):
    template_header = """
<table border=1>"""
    template_data = """
     <tr>
       <th colspan=2>{}</th>
     </tr>
     <tr>
         <td>Kind</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Taste</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Additives</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Filling</td>
         <td>{}</td>
       </tr>"""
    template_footer = """</indent>
</table>"""
    with open(path, "w") as f:
        f.write(template_header)
        for c in cls.bakery_offer:
            content = template_data.format(c.name, c.kind, c.taste, c.additives, c.filling)
            f.write(content)
        f.write(template_footer)


def export_this_cake_to_html(self, path):
    template = """
<table border=1>
     <tr>
       <th colspan=2>{}</th>
     </tr>
       <tr>
         <td>Kind</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Taste</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Additives</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Filling</td>
         <td>{}</td>
       </tr>
</table>"""

    with open(path, "w") as f:
        content = template.format(self.name, self.kind, self.taste, self.additives, self.filling)
        f.write(content)


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

Cake.export_1_cake_to_html = export_1_cake_to_html
Cake.export_1_cake_to_html(cake1, r'C:\Users\Mikołaj\Desktop\PYT\cake1.html')

Cake.export_all_cakes_to_html = types.MethodType(export_all_cakes_to_html, Cake)
Cake.export_all_cakes_to_html(r'C:\Users\Mikołaj\Desktop\PYT\cakes.html')

for c in Cake.bakery_offer:
    c.export_this_cake_to_html = types.MethodType(export_this_cake_to_html, c)
for c in Cake.bakery_offer:
    c.export_this_cake_to_html(r'C:\Users\Mikołaj\Desktop\PYT/{}.html'.format(c.name.replace(' ', '_')))
