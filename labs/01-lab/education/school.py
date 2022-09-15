def draw_school():
    print()
    k = 5 - 1
 
    for i in range(0, 5):
        for j in range(0, k):
            print(end=" ")
     
        k = k - 1
     
        for j in range(0, i+1):
         
            print("* ", end="")
     
        print("\r")
    currLine = ("|       | ")
    for i in range(2):  
        print(currLine,end="\n")
    print("|SCHOOL!|")

    print("|_______|")
    return
draw_school()