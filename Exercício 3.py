print('Bem vindo à fábrica de camiseta do Marcus Vinicius da Silva Nunes!!') #Mensagem de boas vindas inicial

def escolha_modelo(): #Função para a escolha do modelo da camiseta
    while True:
        # Solicitação de escolha do modelo de camiseta, colocando o upper() para caso o cliente digite o modelo em letra minúscula e utilizando \n para quebra de linha e melhor visualização.
        modelo = input('Modelos disponíveis:\nMCS - Manga curta simples \nMLS - Manga longa simples \nMCE - Manga curta com estampa \nMLE - Manga longa com estampa \nQual sua escolha (MCS, MLS, MCE, MLE)? \nDigite aqui: ').upper()
        if modelo == 'MCS':
            return 1.80 #Preço da camiseta modelo MCS
        elif modelo == 'MLS':
            return 2.10 #Preço da camiseta modelo MLS
        elif modelo == 'MCE':
            return 2.90 #Preço da camiseta modelo MCE
        elif modelo == 'MLE':
            return 3.20 #Preço da camiseta modelo MLE
        else:
            # Caso não for escolhida nenhuma das opções válidas, o loop volta para a solicitação da escolha dos modelos existentes.
            print('\nModelo inválido! Por favor, digite um modelo entre MCS, MLS, MCE ou MLE.')

preco = escolha_modelo()
print(f"Preço do modelo escolhido: R$ {preco:.2f}")

def num_camisetas(): #Função para escolha da quantidade de camisetas
    while True:
        try: #Try com except ValueError ao final para identificar se o número digitado é inteiro
           quantidade = int(input('\nDigite o a quantidade de camisetas desejada: '))
           if quantidade > 20000:
               print('A quantidade não pode ser maior que 20000. Digite a quantidade novamente.')
               continue

           if quantidade >= 2000 and quantidade <= 20000:
               desconto = 0.12 #Desconto a ser aplicado na quantidade acima
           elif quantidade >= 200 and quantidade < 2000:
               desconto = 0.07 #Desconto a ser aplicado na quantidade acima
           elif quantidade >= 20 and quantidade < 200:
               desconto = 0.05 #Desconto a ser aplicado na quantidade acima
           else:
                desconto = 0
           #saída de console onde informa a quantidade de camisetas escolhidas e a porcentagem de desconto que será aplicada.
           print(f'Quantidade selecionada: {quantidade}. Desconto a ser aplicado: {desconto * 100:.0f}%')

           return quantidade, desconto

        except ValueError:
            #Caso não for um valor inteiro, voltará à pergunta inicial neste loop.
            print('Por favor, digite um valor inteiro.')

quantidade, desconto = num_camisetas()

def frete(): #Função para a escolha do frete
    while True:
        #escolhas de frete com \n para quebra de linha e melhor visualização das opções.
        tipo_frete = int(input('\nOpções de frete:\n0 - Retirar na Fábrica\n1 - Frete por transportadora\n2 - Sedex\nDigite sua escolha: '))
        if tipo_frete == 0:
            return 0
        elif tipo_frete == 1:
            return 100
        elif tipo_frete == 2:
            return 200
        else:
            print('Por favor, escolha entre as opções válidas de frete.')

valor_frete = frete()
print(f'O valor do frete é de: R$ {valor_frete:.2f}')

#cálculo final no main, para retornar o valor total do pedido,
#multiplicando o preço da camiseta escolhida pela quantidade e
#multiplicando o resultado desse cálculo pela % de desconto, somando-se ao frete no final.
total = (preco * quantidade * (1 - desconto)) + valor_frete

#saída de console ao final, com um resumo do que foi pedido na compra, com quantidades e valores
#valor de desconto aplicado e o valor total ao final, para melhor visualização do cliente.
print('\n ||| RESUMO DO PEDIDO |||')
print(f' | Modelo escolhido: R$ {preco:.2f} | ')
print(f' | Quantidade: {quantidade} camiseta(s) | ')
print(f' | Desconto aplicado: {desconto * 100:.0f}% | ')
print(f' | Frete: R$ {valor_frete:.2f} | ')
print(f' | Total do pedido: R$ {total:.2f} | ')