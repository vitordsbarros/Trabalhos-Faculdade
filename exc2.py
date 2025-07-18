# Essa é a Questão numero dois, aqui apresento o que aprendi fora e dentro das aulas! 
print("Bem-vindo à Loja de Gelados do João Vitor S. Barros") # Mostra o nome da loja e o cardápio com os preços. 
print("-" * 60) 
print("------------ Cardápio ------------") 
print("| Tamanho | Cupuaçu (CP) | Açaí (AC) |") 
print("|   P     |   R$ 9.00    | R$ 11.00  |") 
print("|   M     |   R$ 14.00   | R$ 16.00  |") 
print("|   G     |   R$ 18.00   | R$ 20.00  |") 
print("-" * 60) 

# Aqui eu crio uma variável pra somar o valor total dos pedidos. 
total = 0 

# Começo o loop pra repetir o pedido enquanto a pessoa quiser. 
while True: 

    # Pede o sabor e transforma em maiúscula pra evitar erro com letra minúscula. 
    sabor = input("Entre com o sabor desejado (CP/AC): ").upper() # Apresentei dificuldades, então pesquisei melhor sobre o upper. 

    # Verifica se digitou algo que não é CP ou AC. 
    if sabor not in ["CP", "AC"]: 
        print("Sabor inválido. Tente novamente.")  # mostra erro se digitou errado. 
        continue  # volta pro começo do loop. 

    # Pede o tamanho do pedido. 
    tamanho = input("Entre com o tamanho desejado (P/M/G): ").upper() 

    # Verifica se digitou um tamanho inválido. 
    if tamanho not in ["P", "M", "G"]: 
        print("Tamanho inválido. Tente novamente.")  # mostra erro se digitou errado. 
        continue  # volta pro começo do loop. 

    # Cria a variável pra guardar o valor do item escolhido. 
    preco = 0 

    # Aqui eu verifico o sabor e tamanho pra saber o valor. 
    if sabor == "CP": 
        if tamanho == "P": 
            preco = 9 
        elif tamanho == "M": 
            preco = 14 
        else: 
            preco = 18 
        print(f"Você pediu um Cupuaçu no tamanho {tamanho}: R$ {preco:.2f}") 

    elif sabor == "AC": 
        if tamanho == "P": 
            preco = 11 
        elif tamanho == "M": 
            preco = 16 
        else: 
            preco = 20 
        print(f"Você pediu um Açaí no tamanho {tamanho}: R$ {preco:.2f}") 

    # Aqui eu somo o valor do pedido no total geral. 
    total += preco 

    # Pergunto se a pessoa quer pedir mais alguma coisa. 
    continuar = input("Deseja mais alguma coisa? (S/N): ").upper() 
    if continuar != "S": 
        break  # se não quiser mais, sai do loop. 

# Mostra o valor total que a pessoa tem que pagar. 
print(f"\nO valor total a ser pago: R$ {total:.2f}")