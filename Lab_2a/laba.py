#const
const_1 = True
print(const_1)
const_2 = None
print(const_2)
print("-------------------")

#function
a = pow(3, 4)
print(a)

b = (2, 50, 16, 17)
print(sum(b))
print("-------------------")

#loop and conditional branching
c = 4
if c / 2 == 2:
    print("It is right")
else:
    print("It is not right")


num = [2, 3, 10, 20]
sum = 0

for A in num:
    sum = sum+A

print(sum)
print("-------------------")

#try->except->finally
arr = ["a", "b", "c"]
try:
    value = arr[4]
except IndexError:
    print("The list is not correct")
finally:
    print("Finally result")
print("-------------------")

#with
with open('text.txt', 'w') as file:
    file.write('Hello World!!!!')

#lambdas
this_is_lambda = lambda x, y: x*(x+y)
print('This is function: ', this_is_lambda(2, 5))