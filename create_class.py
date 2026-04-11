class Cookie:
    def __init__(self, color, size):
        self.color = color
        self.size = size

    def change_color(self, color):
        self.color = color

    def get_color(self):
        return self.color
    
    def get_size(self):
        return self.size

    def add_cream(self, cream):
        self.cream = cream


cookie1 = Cookie('Blue','XL')
print(cookie1.color)
print(cookie1.size)
cookie1.add_cream(f'Cream: {True}\n')
print(cookie1.cream)

cookie2 = Cookie('white','XXL')
print(cookie2.color)
print(cookie2.size)
cookie2.add_cream(f'Cream: {False}\n')
print(cookie2.cream)


print(f"Cookie 1 color is {cookie1.get_color()} and size is {cookie1.get_size()} And cream adding is {cookie1.cream}")

print(f"Cookie 2 color is {cookie2.get_color()} and size is {cookie2.get_size()} And cream adding is {cookie2.cream}")

cookie1.change_color("yellow")

print(f"Cookie 1 color is {cookie1.get_color()} and size is {cookie1.get_size()} And cream adding is {cookie1.cream}")
print(f"Cookie 2 color is {cookie2.get_color()} and size is {cookie2.get_size()} And cream adding is {cookie2.cream}")
