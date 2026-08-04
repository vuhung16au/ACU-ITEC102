with open('cities.txt', 'a') as file:
    file.write('Sydney\n')

try:
    with open('cities.txt', 'r') as file:
        print(file.read())
except FileNotFoundError:
    print('File not found')
