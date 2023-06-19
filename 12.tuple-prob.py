'''s1=input("Enter 1st student name :")
n1=int(input("Enter Marks :"))
s2=input("Enter 2nd student name :")
n2=int(input("Enter Marks :"))
s3=input("Enter 3rd student name :")
n3=int(input("Enter Marks :"))
s4=input("Enter 4th student name :")
n4=int(input("Enter Marks :"))
s5=input("Enter 5th student name :")
n5=int(input("Enter Marks :"))

sname=(s1,s2,s3,s4,s5)
snum=(n1,n2,n3,n4,n5)
print("Student Name :",sname)
print("Total Marks :",snum[0]+snum[1]+snum[2]+snum[3]+snum[4])'''

#another way...
'''marks=sum(snum)
print(marks)'''

#count the number of zeroes in a touple
a=(7,0,8,0,0,9)
print("The number of zeros",a.count(0),"times.")