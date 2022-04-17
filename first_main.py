import random

my_list = ["__","__","__"]
values = [".", "X", "."]
num = [1,2,3]

def shuffle_make_dic():
   random.shuffle(values)
   dic_list = dict(zip(num, values))
   #print(dic_list)
   choice = int(input("Type your selection (1,2,3): "))

   for i in dic_list:
       print(dic_list[i], end = " ")
   print("\n")

   return dic_list[choice] == "X"

print("Welcome to the Game :) ")

while True:

   for i in my_list:
       print(i, end = " ")
   print("\n")

   if shuffle_make_dic() == True:
       print("You won!!")
   else:
       print("You lost :(")

   again = input("Do you want to play again? y/n: ")

   if again == "y":
       continue
   else:
       break

