

def  fizz_buzz(n):
 for x in range( n + 1):
         if x % 3 == 0 and  x % 5 == 0:
            print("FizzBuzz")
   
         elif x % 3 == 0:
            print("Fizz")

         elif x % 5 == 0:
            print("Buzz") 
         else: 
            print(x)

input_value = int(input("Введите число:" ))

fizz_buzz(input_value)
