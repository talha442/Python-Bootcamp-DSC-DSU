#Define a function to print a string diagonally as well as Reversed:

#FOR FORWARD:
Name= "TALHA"
for x in range(len(Name)):
    print ( ' ' * (x), Name[x])

print("")    
#FOR REVERSED:
Name= "TALHA"
for x in reversed(range(len(Name))):
    print ( ' ' * (x), Name[x])