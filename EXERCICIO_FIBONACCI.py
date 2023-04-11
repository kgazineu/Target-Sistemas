numero = int(input("Determine um valor para verificar se pertence à sequencia Fibonacci"))
penultimo = 0
ultimo = 1
while penultimo < numero:
    penultimo, ultimo = ultimo, penultimo
    ultimo = penultimo + ultimo

if (penultimo == numero) == True:
    print('O numero pertence à sequencia de Fibonacci')
else: 
    print("O numero nao pertence à sequencia de Fibonacci")
