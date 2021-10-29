#the following program take the student rollno, name and marks and stores it in the dictionary

n=int(int(input("Enter n: "))) 
d={}

for i in range(n): 
    roll_no=int(input("Enter roll no: ")) 
    name=input("Enter name: ") 
    marks=int(input("Enter marks: "))
    #adding the name and marks in dictionary data type in the refrence of roll number
    d[roll_no]=[name,marks] 

#print the complete dictionary data stored above 
print(d.items())
