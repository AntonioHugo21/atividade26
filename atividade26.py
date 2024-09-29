# Crie um programa que receba as notas de 5 alunos e as armazene em uma lista. O programa deve exibir a maior nota, a menor nota e a média das notas.

# Exemplo de entrada:
# Nota do aluno 1: 8
# Nota do aluno 2: 6
# Nota do aluno 3: 9
# Nota do aluno 4: 7
# Nota do aluno 5: 5

# Exemplo de saída:
# Maior nota: 9
# Menor nota: 5
# Média das notas: 7.0
média = 0
nota_alunos = []
for cont in range(0,5):
    nota_alunos.append(float(input('Digite um valor: ')))
    média = sum(nota_alunos) / len(nota_alunos)
print(f'A maior nota é = {max(nota_alunos)}')
print(f'A menor nota é = {min(nota_alunos)}')
print(f'A média de notas é = {média}')