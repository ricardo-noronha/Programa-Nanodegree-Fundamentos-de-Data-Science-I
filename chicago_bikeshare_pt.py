# coding: utf-8

# Começando com os imports
import csv
import matplotlib.pyplot as plt

# Vamos ler os dados como uma lista
print("Lendo o documento...")
with open("chicago.csv", "r") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)
print("Ok!")

# Vamos verificar quantas linhas nós temos
print("Número de linhas:")
print(len(data_list))

# Imprimindo a primeira linha de data_list para verificar se funcionou.
print("Linha 0: ")
print(data_list[0])
# É o cabeçalho dos dados, para que possamos identificar as colunas.

# Imprimindo a segunda linha de data_list, ela deveria conter alguns dados
print("Linha 1: ")
print(data_list[1])

input("Aperte Enter para continuar...")
# TAREFA 1
# TODO: Imprima as primeiras 20 linhas usando um loop para identificar os dados.
print("\n\nTAREFA 1: Imprimindo as primeiras 20 amostras")
for item in data_list[1:21]:
    print(item)

# Vamos mudar o data_list para remover o cabeçalho dele.
data_list = data_list[1:]

# Nós podemos acessar as features pelo índice
# Por exemplo: sample[6] para imprimir gênero, ou sample[-2]

input("Aperte Enter para continuar...")
# TAREFA 2
# TODO: Imprima o `gênero` das primeiras 20 linhas

print("\nTAREFA 2: Imprimindo o gênero das primeiras 20 amostras")
#print(data_list[:20][6])
for item in data_list[:20]:
    print(item[6])
# Ótimo! Nós podemos pegar as linhas(samples) iterando com um for, e as colunas(features) por índices.
# Mas ainda é difícil pegar uma coluna em uma lista. Exemplo: Lista com todos os gêneros

input("Aperte Enter para continuar...")
# TAREFA 3
# TODO: Crie uma função para adicionar as colunas(features) de uma lista em outra lista, na mesma ordem
def column_to_list(data, index, type='none'):
    """
    def column_to_list(data: list, index: int) -> list:

    Função para adicionar as colunas(features) de uma lista em outra lista, na mesma ordem.
    Argumentos:
         data: list com os dados de entrada
         index: index do ítem da lista que será usada para montar a outra lista
         type: tipo de dado que a lista será criado, onde:
             none: não será realizado nenhuma conversão
             float: será convertido para float antes de inserir o ítem na lista
             int: será convertido para int antes de inserir o ítem na lista
    Retorna:
         Uma lista com os valores dos ítens determinados pelo parâmetro index.
    """    
    column_list = []
    # Dica: Você pode usar um for para iterar sobre as amostras, pegar a feature pelo seu índice, e dar append para uma lista
    for item in data:
        if (type == 'float'):
            column_list.append(float(item[index]))
        elif (type == 'int'):
            column_list.append(int(item[index]))
        else:
            column_list.append(item[index])
    return column_list

def CountItem(data, index, column_name):
    """
    def CountItem(data: list, index: int, item: string) -> list:

    Função para contar número de ocorrências de um ítem em uma lista
    Argumentos:
         data: list com os dados de entrada
         index: index do ítem da lista que será usada verificar com o nome da coluna para a contagem
         column_name: nome do ítem que se deseja realizar a contagem
    Retorna:
         Um valor inteiro com a contagem do ítem
    """
    count = 0
    for item in data:
        if (item[index] == column_name):
            count += 1
    return count    

# Vamos checar com os gêneros se isso está funcionando (apenas para os primeiros 20)
print("\nTAREFA 3: Imprimindo a lista de gêneros das primeiras 20 amostras")
print(column_to_list(data_list, -2)[:20])

print("Count:" , len(column_to_list(data_list, -2)))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(column_to_list(data_list, -2)) is list, "TAREFA 3: Tipo incorreto retornado. Deveria ser uma lista."
assert len(column_to_list(data_list, -2)) == 1551505, "TAREFA 3: Tamanho incorreto retornado."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[1] == "Male", "TAREFA 3: A lista não coincide."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora sabemos como acessar as features, vamos contar quantos Male (Masculinos) e Female (Femininos) o dataset tem
# TAREFA 4
# TODO: Conte cada gênero. Você não deveria usar uma função parTODO isso.
#male = column_to_list(data_list, -2).count("Male")
#female = column_to_list(data_list, -2).count("Female")
male = CountItem( data_list, -2, 'Male')
female = CountItem( data_list, -2, 'Female')

# Verificando o resultado
print("\nTAREFA 4: Imprimindo quantos masculinos e femininos nós encontramos")
print("Masculinos: ", male, "\nFemininos: ", female)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert male == 935854 and female == 298784, "TAREFA 4: A conta não bate."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Por que nós não criamos uma função parTODO isso?
# TAREFA 5
# TODO: Crie uma função para contar os gêneros. Retorne uma lista.
# Isso deveria retornar uma lista com [count_male, count_female] (exemplo: [10, 15] significa 10 Masculinos, 15 Femininos)
def count_gender(data_list):
    """
    def count_gender(data_list: list) -> list:
        
    Função para contar os gêneros.
    Argumentos:
        data: list com os dados de entrada
    Retorna:
        Uma lista contendo dois ítens que corresponde a soma das ocorrências do ítem 'Male' e 'Female'.

    """
    #gender_list = column_to_list(data_list, -2)
    #male = gender_list.count("Male")
    #female = gender_list.count("Female")
    male = CountItem(data_list, -2, "Male")
    female = CountItem(data_list, -2, "Female")
    return [male, female]

def count_user_types(data_list):
    """
    def count_user_types(data_list: list) -> list:
        
    Função para contar os tipos de usuários.
    Argumentos:
        data: list com os dados de entrada
    Retorna:
        Uma lista contendo dois ítens que corresponde a soma das ocorrências do ítem 'Subscriber' e 'Customer'.

    """
    subscriberCount = CountItem(data_list, -3, "Subscriber")
    customerCount = CountItem(data_list, -3, "Customer")
    return [subscriberCount, customerCount]


print("\nTAREFA 5: Imprimindo o resultado de count_gender")
print(count_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(count_gender(data_list)) is list, "TAREFA 5: Tipo incorreto retornado. Deveria retornar uma lista."
assert len(count_gender(data_list)) == 2, "TAREFA 5: Tamanho incorreto retornado."
assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[1] == 298784, "TAREFA 5: Resultado incorreto no retorno!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora que nós podemos contar os usuários, qual gênero é mais prevalente?
# TAREFA 6
# TODO: Crie uma função que pegue o gênero mais popular, e retorne este gênero como uma string.
# Esperamos ver "Masculino", "Feminino", ou "Igual" como resposta.
def most_popular_gender(data_list):
    """
    def most_popular_gender(data_list: list) -> list:
        
    Função para verificar o gênero com maior ocorrência.
    Argumentos:
        data: list com os dados de entrada
    Retorna:
        Um string com o nome do gênero com maior ocorrência

    """
    male_count, female_count = count_gender(data_list)
    answer = ""
    if (male_count > female_count):
        answer = "Male"
    elif (male_count < female_count):
        answer = "Female"
    else:
        answer = "Equal"
    return answer


print("\nTAREFA 6: Qual é o gênero mais popular na lista?")
print("O gênero mais popular na lista é: ", most_popular_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(most_popular_gender(data_list)) is str, "TAREFA 6: Tipo incorreto no retorno. Deveria retornar uma string."
assert most_popular_gender(data_list) == "Male", "TAREFA 6: Resultado de retorno incorreto!"
# -----------------------------------------------------

# Se tudo está rodando como esperado, verifique este gráfico!
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Gênero')
plt.xticks(y_pos, types)
plt.title('Quantidade por Gênero')
plt.show(block=True)

input("Aperte Enter para continuar...")
# TAREFA 7
# TODO: Crie um gráfico similar para user_types. Tenha certeza que a legenda está correta.
print("\nTAREFA 7: Verifique o gráfico!")

types = ["Subscriber", "Customer"]
quantity = count_user_types(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Tipos de Usuários')
plt.xticks(y_pos, types)
plt.title('Quantidade por Tipos de Usuários')
plt.show(block=True)

input("Aperte Enter para continuar...")
# TAREFA 8
# TODO: Responda a seguinte questão
male, female = count_gender(data_list)
print("\nTAREFA 8: Por que a condição a seguir é Falsa?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = "Porque existem registros com gênero não definido."
print("resposta:", answer)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert answer != "Escreva sua resposta aqui.", "TAREFA 8: Escreva sua própria resposta!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Vamos trabalhar com trip_duration (duração da viagem) agora. Não conseguimos tirar alguns valores dele.
# TAREFA 9
# TODO: Ache a duração de viagem Mínima, Máxima, Média, e Mediana.
# Você não deve usar funções prontas parTODO isso, como max() e min().
trip_duration_list = column_to_list(data_list, 2, 'float')
min_trip = 0.
max_trip = 0.
mean_trip = 0.
median_trip = 0.
sum_trip = 0.
count_trip = 0
for trip_duration_item in trip_duration_list:
    trip_duration_value = trip_duration_item
    count_trip += 1
    sum_trip += trip_duration_value
    if min_trip == 0 or min_trip > trip_duration_value:
        min_trip = trip_duration_value
    if max_trip < trip_duration_value:
        max_trip = trip_duration_value
mean_trip = sum_trip / count_trip
trip_duration_list.sort()
index_median = round(float(count_trip + 1) / 2)
print(trip_duration_list[index_median-10:index_median+10])
median_trip = trip_duration_list[index_median]

print("\nTAREFA 9: Imprimindo o mínimo, máximo, média, e mediana")
print("Min: ", min_trip, "Max: ", max_trip, "Média: ", mean_trip, "Mediana: ", median_trip)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert round(min_trip) == 60, "TAREFA 9: min_trip com resultado errado!"
assert round(max_trip) == 86338, "TAREFA 9: max_trip com resultado errado!"
assert round(mean_trip) == 940, "TAREFA 9: mean_trip com resultado errado!"
assert round(median_trip) == 670, "TAREFA 9: median_trip com resultado errado!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 10
# Gênero é fácil porque nós temos apenas algumas opções. E quanto a start_stations? Quantas opções ele tem?
# TODO: Verifique quantos tipos de start_stations nós temos, usando set()
user_types = set()
start_stations_list = column_to_list(data_list, 3)
for start_stations_item in start_stations_list:
    user_types.add(start_stations_item)
print("\nTAREFA 10: Imprimindo as start stations:")
print(len(user_types))
print(user_types)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert len(user_types) == 582, "TAREFA 10: Comprimento errado de start stations."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 11
# Volte e tenha certeza que você documenteou suas funções. Explique os parâmetros de entrada, a saída, e o que a função faz. Exemplo:
# def new_function(param1: int, param2: str) -> list:
#      """
#      Função de exemplo com anotações.
#      Argumentos:
#          param1: O primeiro parâmetro.
#          param2: O segundo parâmetro.
#      Retorna:
#          Uma lista de valores x.
#
#      """

input("Aperte Enter para continuar...")
# TAREFA 12 - Desafio! (Opcional)
# TODO: Crie uma função para contar tipos de usuários, sem definir os tipos
# para que nós possamos usar essa função com outra categoria de dados.
print("Você vai encarar o desafio? (yes ou no)")
answer = "yes"

def count_user_types_items(data_list, index):
    """
    def count_user_types_items(data_list: list, index: int) -> list, list:

    Função para relacionar e contar tipos de ítens de uma lista.
    Argumentos:
        data_list: list com os dados de entrada
        index: index do ítem da lista que será usada para montar a outra lista
    Retorna:
        Uma lista com os valores dos tipos de ítem.
        Outra lista com as quantidades de cada tipo de ítems

    """    
    item_types = []
    count_items = []
    user_types = set()

    for start_stations_item in column_to_list(data_list, index):
        user_types.add(start_stations_item)

    for user_types_item in user_types:
        item_types.append(user_types_item)
        count_items.append(CountItem(data_list, index, user_types_item))

    return item_types, count_items


if answer == "yes":
    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
    #column_list = column_to_list(data_list, -2)
    types, counts = count_user_types_items(data_list, -2)
    print("\nTAREFA 11: Imprimindo resultados para count_items()")
    print("Tipos:", types, "Counts:", counts)
    assert len(types) == 3, "TAREFA 11: Há 3 tipos de gênero!"
    assert sum(counts) == 1551505, "TAREFA 11: Resultado de retorno incorreto!"
    # -----------------------------------------------------