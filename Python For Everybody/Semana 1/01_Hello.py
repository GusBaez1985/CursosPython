from cgitb import small


largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        fnum = int(num)

    except:
        print("Invalid input")
    
    else:
        
        if largest == None:
            largest = fnum
        elif largest < fnum:
            largest = fnum
        elif smallest == None:
            smallest = fnum
        elif smallest > fnum:
            smallest = fnum

    #print(fnum)

print("Maximum is", largest)
print("Minimum is", smallest)