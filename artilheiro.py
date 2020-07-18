jogo = dict()
gols = list()
jogo['jogador'] = str(input('Nome do Jogador: '))
nome = jogo['jogador']

partidas = int(input('Nº de Partidas: '))
for x in range(partidas):
    gol = int(input(f'Quantos gols na partida {x}? '))
    gols.append(gol)

jogo['gols'] = gols        
jogo['total_Gols'] = sum(gols)
total = jogo['total_Gols']

print('---------------------------------------------------')
print(jogo)
print('---------------------------------------------------')
print(f'{nome} jogou {partidas} partidas')

for x in range(partidas):
    print(f'Na partida {x + 1}, fez {gols[x]} gols')
    
print(f'Foi um total de {total} gols')
