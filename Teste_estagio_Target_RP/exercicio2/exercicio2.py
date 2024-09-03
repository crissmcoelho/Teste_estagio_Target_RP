#2) Escreva um programa que verifique, em uma string, a existência 
# da letra ‘a’, seja maiúscula ou minúscula, além de informar a quantidade
# de vezes em que ela ocorre.

#IMPORTANTE: Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;

def contar_letra_a(string):
    # Contar a ocorrência de 'a' e 'A' na string
    quantidade_a = string.lower().count('a')
    
    # Verificar se há pelo menos uma ocorrência
    if quantidade_a > 0:
        print(f"A letra 'a' (maiúscula ou minúscula) foi encontrada {quantidade_a} vezes.")
    else:
        print("A letra 'a' (maiúscula ou minúscula) não foi encontrada.")



# Chamando a função
contar_letra_a(string_exemplo)