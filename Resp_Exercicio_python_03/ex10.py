projetos = ['Python', 'Java', 'PHP', ' ', 'C', None, 'Jscript', 'HTML', 'SQL', ' ']

encontrados = 0
ausentes = 0
sem_nome = 0

for projeto in projetos:
    if projeto is None:
        ausentes += 1
    elif projeto.strip() == '':
        sem_nome += 1
    else:
        encontrados += 1

print(f"Cursos encontrados: {encontrados}")
print(f"Cursos ausentes: {ausentes}")
print(f"Cursos sem nome: {sem_nome}")