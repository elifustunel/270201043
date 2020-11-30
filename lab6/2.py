std_num=input("enter number of students:")
for i in range(std_num):
 mid1=int(("enter your grade:"))
 mid2=int(("enter your grade:"))
 fin=int(("enter your grade:"))

grade_list.append([mid1,mid2,fin])
print(grade_list)

avg_grades = []

for a in grade_list:
 avg_grades.append(a[0]*0.3 + a[1]*0.3 + a[2]*0.4)

print(avg_grades)


grades = [[60,90,75],[50,80,20],[80,85,90]]

for i in grades:
 first = i[0]*(0.3)
 second = i[1]*(0.3)
 third = i[2]*(0.4)
 avarage = first + second + third
print(avarage)