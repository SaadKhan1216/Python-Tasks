sub1=int(input("Enter marks of the Maths: "))
sub2=int(input("Enter marks of the Eng: "))
sub3=int(input("Enter marks of the Isl: "))
sub4=int(input("Enter marks of the Urdu: "))
sub5=int(input("Enter marks of the Science: "))
avg=(sub1+sub2+sub3+sub4+sub4)/500
perc = avg*100
if(perc>=80 and perc<=100):
    print("Grade: A+")
elif(perc>=70 and perc<80):
    print("Grade: A")
elif(perc>=60 and perc<70):
    print("Grade: B")
elif(perc>=50 and perc<60):
    print("Grade: C")
elif(perc>=40 and perc<50):
    print('Grade: D')
else:
    print("Grade: F")