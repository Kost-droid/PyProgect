class MyString (str):

    def __add__(self, other):
        return MyString (f'This is two strings {self} and {other}')

str_1 = MyString ('str1')
str_2 = MyString ('str2')

print (str_1 + str_2)


