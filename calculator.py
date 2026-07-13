# Now we could use int for integer rather than float becuase float can calculate for decimals and integers both
x = float (input("What is the value of x?"))
y = float(input("What is the value of y?"))
# or we could have done z = int(x) + int(y) 
# print (z)
#z = round(x+y)
#print(f"{z:,}")
z = round(x/y)
print(z)  