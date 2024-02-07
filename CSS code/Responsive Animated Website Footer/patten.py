for i in range(5):
    for j in range(5):

        if i >= 2:        
        
            if j==2:        
                print("_",end=" ")
            else:
                print("*",end=" ")
        else:
            if j==2:        
                print("*",end=" ")
            else:
                print("_",end=" ")

    print( )