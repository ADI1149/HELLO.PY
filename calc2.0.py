def main():
    x = float(input("What is the value of x"))
    print("x cubed is", cube(x))

def cube(n):
    #return n*n*n
    #return n***2
    return pow(n,3)


main() 