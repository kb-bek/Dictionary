#problem1

dict = {
       'drink1' : 'Coca-Cola',
       'drink2' : 'Sprite',
       'drink3' : 'Fanta'
       }
print(dict)


#problem2


user = {}

for i in range(3):
       name = input('Name: ')
       password = input('Password: ')
       user[name] = password
       print(user)

#problem3

dict3 = {
       'Аслан' : 'Оператор',
       'Жаныбек' : 'Программист',
       'Асан' : 'Повар'}


for name , professional in dict3.items():
       print('Здраствуйте {}'.format(name),  'Прекрасная профессия {}'.format(professional))

#problem4


menu = {'lagman' : 120, 'plov' : '120', 'borsh' : 100 }
menu.update(besh_barmak = 130)
print(menu)

menu.update(lagman = 135)
print(menu)

del menu['borsh']

print(menu)




#problem3







south_american_countries = ['Argentina', 'Bolivia', 'Colombia', 'Ecuator', 'Guyana', 'Paraguay', 'Peru', 'Surname', 'Uruguay', 'Venezuela', 'Surname']

country = {}


for i, v in enumerate(set(south_american_countries)):
       country[i] = v

print(country)
