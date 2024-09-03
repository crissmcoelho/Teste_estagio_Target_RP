#3) Observe o trecho de código abaixo: int INDICE = 12, SOMA = 0, 
# K = 1; enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; } 
# imprimir(SOMA);

# Dados do exercicio#

indice = 13
soma = 0
k = 0

while k <= indice:
    soma += k
    k += 1

print("A soma dos números de 0 a", indice, "é:", soma)