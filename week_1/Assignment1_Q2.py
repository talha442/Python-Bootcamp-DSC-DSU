# Create a program to take as input 5 student records And then output the records in a tabular form with class average, class highest and class lowest at end in the following format.
# Use dictionaries (list of dictionaries in exact)
# Insert atleast 5 records
# Input must be user-given
# (Optional) validate the user input, i.e marks aren't greater 100 and other such validations you think there might be

for i in range(5):
    roll_num = int(input("Enter Your Roll Number  "))
    Name = str(input("Enter Your Name  "))
    Age = int(input("Enter Your Age  "))
    Marks = int(input("Enter Your Marks  "))

    print('Roll Number', 'Name', 'Age', 'Marks')
    Data = [roll_num, Name, Age, Marks]

    for i in Data:
        print(Data)
    pass

if Marks > 100:
    print("Please Enter Marks Below 100")
    Marks = int(input("Enter Your Marks  "))
    pass
else:
    print(Marks)
pass