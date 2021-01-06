#Calculate Total Marks and Average:
print("Enter Marks Obtained in 6 Subjects: ")
print("===================================")
sub1=int(input("Enter Subject1 Marks:"))
sub2=int(input("Enter Subject2 Marks:"))
sub3=int(input("Enter Subject3 Marks:"))
sub4=int(input("Enter Subject4 Marks:"))
sub5=int(input("Enter Subject5 Marks:"))
sub6=int(input("Enter Subject6 Marks:"))
list=[sub1,sub2,sub3,sub4,sub5,sub6]
Total_marks=sub1+sub2+sub3+sub4+sub5+sub6
avg=Total_marks/6
print("marks storing in list:",list)
print("Total Marks:",Total_marks)
print("Average:",avg)