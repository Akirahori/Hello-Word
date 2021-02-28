# Percorrendo uma lista inteira com um laço
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

# Executando mais tarefas em um laço for
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")

# Identação aqui acontece um erro de lógica
# Agora está certo a identação é a questão do espaçamento
magicians = ['bruce', 'jolene', 'samanta']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() +".\n")

# Identar desnecessariamente
message = "Hello Python world!"
print(message)

#Usando a função range
for value in range(1,5):
  print(value)

#Usando range para criar uma lista númerica
numbers = list(range(1,6))
print(numbers)

even_numbers = list(range(2,11,2))
print(even_numbers)

#Exponenciais
squares = []
for value in range(1,11):
 square = value**2
 squares.append(square)

print(squares)

#Estatisticas Simples
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
min(digits)

#List comprehensions
squares = [value**2 for value in range(1,11)]
print(squares)

#Fatiando uma lista
players = ['charles', 'robson', 'ferdinand','john', 'eli']
print(players[0:3])

players = ['charles', 'robson', 'ferdinand','john', 'eli']
print(players[1:4])

players = ['charles', 'robson', 'ferdinand','john', 'eli']
print(players[:4])
#sintaxe permite apresentar todos os elementos
players = ['charles', 'robson', 'ferdinand','john', 'eli']
print(players[-1])

#Percorrendo uma fatia com um laço
players = ['charles', 'robson', 'ferdinand','john', 'eli']
print("here are the first three players on my team")
for player in players[:3]:
    print(player.title())

#Copiando uma lista
my_foods = ['pizza', 'gyudon', 'sushi','chocolate']
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are: ")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

#Tupla
dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])

#Percorrendo todos os valores de uma tupla com um laço
dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)
