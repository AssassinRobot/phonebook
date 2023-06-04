names = []
phon_numberes = []
num = 3
for item in range(num):
    name = input('Name:')
    phon_number = input('Phon number:')
    names.append(name)
    phon_numberes.append(phon_number)
print('''\nName\t\t\tPhon number\n''')    
for item in range(num):
    print(f'{names[item]}\t\t\t{phon_numberes[item]}')
search_term = input('\n Enter search term:')
print('Search resulte:')
if search_term in names :
    index = names.index(search_term)
    phon_number = phon_numberes[index]
    print(f'''Name : {search_term}
Phon number: {phon_number}''')
else :
    print('Name not found')
