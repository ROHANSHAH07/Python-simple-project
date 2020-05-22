import xlsxwriter
from openpyxl import load_workbook

#create file (workbook) and worksheet
outworkbook = xlsxwriter.Workbook("out.xlsx")
outsheet = outworkbook.add_worksheet()
outsheet.set_column('A:N', 30)
#declare data of id
i = int(input("enter howmany recoard for Test-Scenario-Id you want\n"))
list1=[]
for i in range(0,i):
    x = input("enter Test-Scenario-Id\n")
    list1.append(x)
    print(list1)
outsheet.write("A1","Test-Scenario-Id")
#outsheet.width = 7000
#write data to file
for item1 in range(len(list1)):
    outsheet.write(item1+1,0,list1[item1])
# declare data of test case scenario description
d =input("enter howmany  recoard for Test-Scenario-Description you want\n")
list2=[]
for i in range(0,int(d)):
    x = input("enter Test-Scenario-Description\n")
    list2.append(x)
    print(list2)
outsheet.write("B1","Test-Scenario-Description")
#outsheet.width = 7000
#write data to file
for item2 in range(len(list2)):
    outsheet.write(item2+1,1,list2[item2])
# decalre data  os test case id
I =int(input("enter howmany  recoard for Test-case-id you want\n"))
list3=[]
for i in range(0,I):
    x = input("enter Test-Scenario-id\n")
    list3.append(x)
    print(list3)
outsheet.write("C1","Test-case-id")
#outsheet.width = 7000
#write data to file
for item3 in range(len(list3)):
    outsheet.write(item3+1,2,list3[item3])
#write a data test-case-description
D =int(input("enter howmany  recoard for Test-case-description  you want\n"))
list4=[]
for i in range(0,D):
    x = input("enter Test-case-description \n")
    list4.append(x)
    print(list4)
outsheet.write("D1","Test-case-description")
#outsheet.width = 7000
#write data to file
for item4 in range(len(list4)):
    outsheet.write(item4+1,3,list4[item4])
# write data for Test-case-steps
S =input("enter howmany  recoard for Test-case-steps  you want\n")
list5=[]
for i in range(0,int(S)):
    x = int(input("enter Test-case-steps \n"))
    list5.append(x)
    print(list5)
outsheet.write("E1","Test-case-steps")
#outsheet.width = 7000
#write data to file
for item5 in range(len(list5)):
    outsheet.write(item5+1,4,list5[item5])
#write data for pre-condition
pc =input("enter howmany  recoard for pre-condition   you want\n")
list6=[]
for i in range(0,int(pc)):
    x = input("enter pre-condition \n")
    list6.append(x)
    print(list6)
outsheet.write("F1","pre-condition")
#outsheet.width = 7000
#write data to file
for item6 in range(len(list6)):
    outsheet.write(item6+1,5,list6[item6])
# write data for post condition
post =input("enter howmany  recoard for post-condition   you want\n")
list7=[]
for i in range(0,int(post)):
    x = input("enter post-condition \n")
    list7.append(x)
    print(list7)
outsheet.write("G1","Post-condition")
#outsheet.width = 7000
#write data to file
for item7 in range(len(list7)):
    outsheet.write(item7+1,6,list6[item7])
r =input("enter howmany  recoard for expected result   you want\n")
list8=[]
for i in range(0,int(r)):
    x = input("enter expected result \n")
    list8.append(x)
    print(list8)
outsheet.write("H1","Expected result")
#outsheet.width = 7000
#write data to file
for item8 in range(len(list8)):
    outsheet.write(item8+1,7,list8[item8])
a =input("enter howmany  recoard for actual result   you want\n")
list9=[]
for i in range(0,int(a)):
    x = input("enter actual result \n")
    list9.append(x)
    print(list9)
outsheet.write("I1","Actual result result")
#outsheet.width = 7000
#write data to file
for item9 in range(len(list9)):
    outsheet.write(item9+1,8,list9[item9])
q =input("enter howmany  recoard for project Status    you want\n")
list10=[]
for i in range(0,int(q)):
    x = input("enter project Status \n")
    list10.append(x)
    print(list10)
outsheet.write("J1","project Status")
#outsheet.width = 7000
#write data to file
for item10 in range(len(list10)):
    outsheet.write(item10+1,9,list10[item10])
p =input("enter howmany  recoard for  the name of person who can executed test-case   you want\n")
list11=[]
for i in range(0,int(p)):
    x = input("enter  the name of person who can executed test-case \n")
    list11.append(x)
    print(list11)
outsheet.write("K1","Executed-By")
#outsheet.width = 7000
#write data to file
for item11 in range(len(list11)):
    outsheet.write(item11+1,10,list11[item11])
z =input("enter howmany  recoard for  the date in exactly  DD-MM-YYYY format   you want\n")
list12=[]
for i in range(0,int(z)):
    x = input("enter the date in exactly  DD-MM-YYYY format  \n")
    list12.append(x)
    print(list12)
outsheet.write("K1","Executed-Date")
#outsheet.width = 7000
#write data to file
for item12 in range(len(list12)):
    outsheet.write(item12+1,11,list12[item12])
co =input("enter howmany  recoard for  comments   you want\n")
list13=[]
for i in range(0,int(co)):
    x = input("enter comments  \n")
    list13.append(x)
    print(list13)
outsheet.write("K1","comments")
#outsheet.width = 7000
#write data to file
for item13 in range(len(list13)):
    outsheet.write(item13+1,12,list13[item13])


outworkbook.close()