#
# class Animal:
#
#
#     def sound (self, env = None):
#         if env is None:
#             return 'Animal'
#         return 'Arch'
#
#
#
#     def print_sound (self):
#         print (self.__class__)
#
#
# class Dog (Animal):
#
#
#     def sound (self, env = None):
#         if env is None:
#             return 'III'
#         return 'Doc'
#
#
# class Exist (Animal):
#     pass
#
#
# def main ():
#
#     def sound (self, env = None):
#         if env is None:
#             print ('bul')
#         else:
#             print ('Am')
#
#
#     Fish = type ('Fish', (Animal,), dict (sound = lambda self, x = None: sound(self, x) ))
#
#     fish = Fish ()
#
#     fish.sound("f")
#     fish.print_sound()
#
#     # dog = Dog ()
#     # ex  = Exist ()
#     #
#     # Dog ().print_sound(dog.sound('g'))
#     # ex.print_sound(ex.sound())
#     #
#
#
# main ()
#

class Car:


    def __init__(self, weel  = None):
        if weel is not None:
            self.weel = weel


    def __repr__(self):
        return super().__repr__()


    def go (self):
        print ('GGG')

car_not_weel = Car ()
car_whit_weel = Car (4)

print (car_whit_weel.__repr__())

# print (type (car_whit_weel))
#
# car_not_weel.go()
#
# print (dir(car_not_weel))
#
# # print (car_not_weel.weel)
# print(car_whit_weel.weel)
#
