arr = []

for x in range(10): #we are looping 10 times
    a,b,c,d,e = input("Enter your numbers here: ").split()
    arr.extend([a,b,c,d,e])
    print(arr)

