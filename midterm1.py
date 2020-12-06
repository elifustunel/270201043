member_file = open('members.txt')
member_dict1 = {}
 
line = "name: email\n"
while line != "":
 name, email = line.split(':') 
 member_dict1[name] = email[1:].split('\n')[0]
 line = member_file.readline()
del member_dict1['name']
print(member_dict1)
member_file.close()

