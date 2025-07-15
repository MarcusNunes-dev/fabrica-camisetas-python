# Fábrica de Camisetas

Simulador de pedidos de camisetas com opções de modelos, descontos por quantidade e escolha do tipo de frete.

## Funcionalidades

- Escolha do modelo de camiseta:
  - MCS: Manga curta simples – R$ 1,80
  - MLS: Manga longa simples – R$ 2,10
  - MCE: Manga curta com estampa – R$ 2,90
  - MLE: Manga longa com estampa – R$ 3,20
- Escolha da quantidade (com regras de desconto):
  - 20 a 199 camisetas: 5%
  - 200 a 1.999 camisetas: 7%
  - 2.000 a 20.000 camisetas: 12%
- Escolha do frete:
  - 0 – Retirada na fábrica: R$ 0
  - 1 – Transportadora: R$ 100
  - 2 – Sedex: R$ 200

## Cálculo final

O total é calculado com:
Total = (Preço_unitário * Quantidade * (1 - Desconto)) + Frete

## Exemplo de uso

```bash
Modelo: MCE
Preço do modelo escolhido: R$ 2.90
Quantidade: 250
Desconto aplicado: 7%
Frete: Transportadora (R$ 100)
Total do pedido: R$ 774.25

Tecnologias
Python 3.x

Autor
Marcus Vinicius da Silva Nunes
GitHub - MarcusNunes-dev
