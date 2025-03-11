for i in range(1,10, 2):
    print(i)
else:
    print("Loop completed...")
    
i = 1
while(i < 10):
    if(i == 5):
        i += 1
        continue
    print(i)
    
   
    i += 1


n = int(input("Enter a number to print its table: "))

for i in range(1, 11):
    print(i*n)
    
# greet  only the name starts with 'v'
l = ["Vedant", "Shivam","Dhiraj", "Vishal"]
for name in l:
    if(name.lower().startswith('v')):
        print(f"Hello {name}")
        
        
n = int(input("Enter a number to calculate its factorial: "))
fact = 1
for i in range(1 , n + 1):
    fact *= i

print(f"Factorial of {n} is {fact}")

n = 6
for i in range(1, n):
    s = (n-i)
    print(" " * int(s), "* " * i )
  
for i in range(1, n):
    if i == 1 or i == n - 1:
        print("*" * n)
    else:
        print("*" + " " * (n-2) + "*")
        
n = 5     
for i in range(1, n+1):
    if i == 1 or i == n:
        print(" " * (n-i) + "* " * i)
    else:
        print(" " * (n-i) +"*" + "  " * (i - 2) + " *" )
        
for i in range(n, 0, -1):
    if i == 1 or i == n:
        print(" " * (n-i) + "* " * i)
    else:
        print(" " * (n-i) +"*" + "  " * (i - 2) + " *" )