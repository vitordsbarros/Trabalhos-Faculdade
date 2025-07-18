# Essa é a Questão numero três, aqui apresento o que aprendi fora e dentro das aulas! 
print("Bem-vindo à Copiadora do João Vitor S. Barros") # Aqui aplico a mensagem de boas-vindas com meu nome. 

def escolha_servico(): # Aqui aplico uma função responsável por perguntar e validar o tipo de serviço solicitado. 
    while True: 

        print("Entre com o tipo de serviço desejado") 
        print("DIG - Digitalização") 
        print("ICO - Impressão Colorida")
        print("IPB - Impressão Preto e Branco") 
        print("FOT - Fotocópia") 

        servico = input(">").lower() # Nesse aqui recebe o input do usuário e transforma tudo em minúsculo para facilitar a validação. 
         
        if servico == "dig": # Aqui eu defino os valores dos serviços conforme o tipo escolhido. 
            return 1.10  # Preço por página da digitalização. 
        elif servico == "ico": 
            return 1.00  # Preço por página da impressão colorida. 
        elif servico == "ipb": 
            return 0.40  # Preço por página da impressão preto e branco. 
        elif servico == "fot": 
            return 0.20  # Preço por página da fotocópia. 
        else: 

            print("Escolha inválida, entre com o tipo do serviço novamente") # Aqui irá aparecer uma mensagem de erro caso o usuário digite uma opção invália. 
            print("erro o serviço\n") 

def num_pagina(): # Esta função será responsável por tratar o número de páginas, aplicar descontos e validar o limite. 
    while True: 
        try: 

            num_pag = int(input("Entre com o número de páginas: ")) # Aqui solicita ao usuário o número de páginas. 

            if num_pag < 20: # Aqui a validação de faixas para aplicar o desconto correto. 
                return num_pag 
            elif 20 <= num_pag < 200: 
                return num_pag * 0.85  # Há 15% de desconto. 
            elif 200 <= num_pag < 2000: 
                return num_pag * 0.80  # Há 20% de desconto. 
            elif 2000 <= num_pag < 20000: 
                return num_pag * 0.75  # Há 25% de desconto. 
            else: 

                print("Não aceitamos tantas páginas de uma vez. Ultrapassou o limite de páginas!") # Esse exibe mensagem se o número ultrapassar o limite aceito. 
                print("Por favor, entre com o número de páginas novamente.") 
        except: 

            print("Valor inválido. Digite um número inteiro.") # Aqui trata erros de digitação, como letras ou símbolos. 

def servico_extra(): # Aqui introduzo uma função responsável por perguntar e validar o serviço adicional de encadernação. 
    while True:

        print("Deseja adicionar algum serviço?") 
        print("1 - Encadernação Simples - R$ 15.00") 
        print("2 - Encadernação Capa Dura - R$ 40.00")  
        print("0 - Não desejo mais nada") 
        extra = input(">") 

        # Aqui ele valida a opção e retorna o valor correspondente 
        if extra == "1": 
            return 15.00 
        elif extra == "2": 
            return 40.00 
        elif extra == "0": 
            return 0.00 
        else: 
            print("Escolha inválida, entre com o serviço extra novamente") 

 

# Aqui começa o programa principal (main), onde juntamos tudo e mostramos o valor final. 
servico = escolha_servico() # Valor por página. 
paginas = num_pagina() # Quantidade de páginas já com desconto aplicado. 
extra = servico_extra() # Valor extra de encadernação. 

# Aqui apresento a fórmula final onde total = (serviço * páginas) + extra. 
total = (servico * paginas) + extra 

# Apresenta o valor final com duas casas decimais e a decomposição do cálculo e só ir pro abraço. 
print(f"Total: R$ {total:.2f} (serviço: R$ {servico:.2f} * páginas: {paginas:.0f}pag + extra: R$ {extra:.2f})") 