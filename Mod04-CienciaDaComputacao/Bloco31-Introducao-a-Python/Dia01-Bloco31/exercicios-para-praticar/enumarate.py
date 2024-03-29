languages = ['Python', 'Java', 'JavaScript']

enumerate_prime = enumerate(languages)

# converte um objeto enumerate em uma lista
print(list(enumerate_prime))

# Saída: [(0, 'Python'), (1, 'Java'), (2, 'JavaScript')]


languages = ['Python', 'Java', 'JavaScript']

for index, language in enumerate(['Python', 'Java']): # o enumarate cria um indice em cada posição.
    print(f'{index} - {language}')

# Saída:
# 0 - Python
# 1 - Java