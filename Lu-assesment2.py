n=int(input("ENTER A NUMBER:"))
if n>1:
    for i in range(2,n):
        if n%i==0:
            print("THE GIVEN NUMBER IS NOT A PRIME")
            break
    else:
        print("THE GIVEN NUMBER IS A PRIME")
