s1 = float(input("Enter the marks of subject 1   "))
s2 = float(input("Enter the marks of subject 2   "))
s3 = float(input("Enter the marks of subject 3   "))

avg = (s1 + s2 + s3) / 3

if(avg>=90) :
    print("Grade is A")
elif(avg >=80 and avg <90):
    print("Grade is B")
elif(avg >=70 and avg <80):
    print("Grade is C")
elif(avg>=60 and avg <70):
    print("Grade is D")
else :
    print("Grade is F")


