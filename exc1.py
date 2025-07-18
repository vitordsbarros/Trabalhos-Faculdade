# Essa é a Questão numero um, aqui apresento o que aprendi fora e dentro das aulas! 
print("Bem-vindo à loja do João Vitor S. Barros")  # Aqui inicio com a mensagem de boas-vindas com nome da loja. 

def calculo_desconto(): 
    valor = float(input("Entre com o valor do produto: "))  # Aqui solicita o valor unitário do produto ao usuário. 
    quantidade = int(input("Entre com a quantidade do produto: "))  # Aqui solicita a quantidade de produtos desejada. 

    totals_desconto = valor * quantidade # Aqui calcula o valor total sem desconto. 

    if totals_desconto < 2500:  # Aqui define o percentual de desconto com base no total sem desconto. 
        desconto = 0  # Não há nenhum desconto aplicado. 
    elif 2500 <= totals_desconto < 6000: 
        desconto = 4  # Há desconto de 4% 
    elif 6000 <= totals_desconto < 10000: 
        desconto = 7  # Há desconto de 7% 
    else: 
        desconto = 11  # Há desconto de 11% para compras acima de R$10.000 

    valor_desconto = totals_desconto * desconto / 100 # Aqui calcula o valor de desconto em reais. 
    totalc_desconto = totals_desconto - valor_desconto # Aqui aplica o desconto ao total da compra. 

    # E aqui exibe os valores finais ao usuário. 
    print(f"O valor da sua compra SEM o desconto será de: R${totals_desconto:.2f}") 
    print(f"O valor da sua compra COM o desconto será de: R${totalc_desconto:.2f}") 

# E por fim, qui chama a função para executar o algoritmo. 
calculo_desconto() 