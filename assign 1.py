print("online examz grading system")
print("please enter course work marks")
assignment1=float(input("enter assignment1 marks"))
assignment2=float(input("enter assignment2 marks"))
cat1=float(input("enter cat1 marks"))
cat2=float(input("enter cat2 marks"))
coursework=(assignment1+assignment2+cat1+cat2)
print("your course work is",coursework)
fexamz=float(input("enter fexamz marks"))
grade=((fexamz+coursework))
if grade>=70 and grade<=100:
    print("your grade is = A")
    print("grade mark is",grade)
elif grade>=60 and grade<70:
    print("your grade is = B")
    print("gpa mark is", grade)
elif grade>=50 and grade<60:
    print("your grade is = C")
    print("grade mark is", grade)
elif grade>=40 and grade<50:
    print("your grade is = D")
    print("grade mark is", grade)
elif grade>=0 and grade<40:
    print("your grade is = E")
    print("grade mark is", grade)

else:
    print("your grade is = invalid grade")
print("grade mark is",grade)
