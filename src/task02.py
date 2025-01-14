# # #
# # # sequence = 'aacd'
# # #
# # #
# # #
# # # def my_recurs (sequences, s = 0, e = 1, res = None) :
# # #     if res is None:
# # #         res = []
# # #     res.append(sequences[s:e])
# # #     if e + 1 <= len (sequences):
# # #         my_recurs(sequences, s, e + 1, res)
# # #     elif s + 1 <= len (sequences) - 1:
# # #          my_recurs(sequences, s + 1, s + 2, res)
# # #     else: return res
# # #     return res
# # #
# # # print (my_recurs(sequence))
# # #
# # #
# #
# # my_set = {1,2}
# # my_set_copy= my_set
# # my_set.update({3,4})
# # print (my_set_copy)
#
# odd = lambda x: bool(x % 2)
# numbers = [n for n in range(10)]
# numbers_copy = numbers
# numbers [1:] = [n for n in numbers if not odd(n)]  # просто отбираем новые элементы
# print(numbers_copy)

i  = 5

def my_list_fun ():
    def my_inner (x):
        global i
        return x * i
    return my_inner

my_fun =  my_list_fun()
print (my_fun (2))

i  = 10
print (my_fun (2))
