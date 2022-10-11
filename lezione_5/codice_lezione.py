# esempio 1
rediroma = {'tito':'tazio','numa': 'pompilio', 'tullo':'ostilio','anco':'marzio', 'tarquinio':'prisco', 'servio':'tullio', 'tarquinio':'il superbio'}

for r,v in enumerate(rediroma):
    print(r, v)

# esempio 2
for i,v in enumerate(['tic','tac','toe']):
    print(i,v)

# esempio 3
s = "ABCD"
l = ["Alfa", "Beta", "Gamma", "Delta"]
for i in zip(s, l):
    print(i)

# esempio 4 - invertito
for i in reversed(range(1, 10, 2)):
    print(i)

# esempio 5 
gloria = ['ho', 'lasciato', 'la', 'patente', 'sul', 'tavolo']
for i in sorted(gloria):
    print(i)

# esempio 6
cesto = ['mela', 'arancia', 'mela', 'pera', 'arancia', 'banana']