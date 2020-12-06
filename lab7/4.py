employees={}
for i in range(0,5):
  name=input("name:")
  salary=input("salary:")
  employees[name] = salary

best_three = sorted(employees.values())[-3:]
for name in employees.keys():
    salary = employees[name]
    if salary in best_three:
        print(name)
