""" repeated steps """

n = 5
while n > 0:
    print(n)
    n = n-1

print('blastoff!')
print(n)

""" infinite loop example """

n = 5
while n > 0:
    print('Lather')
    print('Rinse')
print('Dry off!')

""" loop that doesnt loop """

n = 0
while n > 0 :
    print('lather')
    print('rinse')
print('dry off!')

""" breaking out of a loop """

"""this is a block of code"""
while True:
    line = input('> ')
    if line == 'done' :
        break
    print(line)
"""this is a block of code"""
print('Done!')

""" Finish an iteration with continue """

while True:
    line = input('> ')
    if line[0] == '#' :
        continue
    if line == 'done' :
        break
    print(line)
print('Done!')