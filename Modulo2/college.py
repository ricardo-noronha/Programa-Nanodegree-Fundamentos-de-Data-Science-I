'''
names =  # capture e processe o input para uma lista de nomes
assignments =  # capture e processe o input para uma lista do número de tarefas
grades =  # capture e processe o input para uma lista de notas
'''
names = input("Enter names separated by commas: ").title().split(',')
assignments =input("Enter assignments counts separated by commas: ").split(',')
grades = input("Enter grades separated by commas: ").split(',')

# string de mensagem a ser usada para cada aluno
# DICA: use .format() com esta string no seu loop for
message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

# escreva um loop for que realize uma iteração em cada conjunto de nomes, tarefas e notas para imprimir a mensagem de cada aluno
for name, assign, grade in zip(names, assignments, grades):
    print(message.format(name, assign, grade, float(grade) + float(assign) * 2.0))