# Implementação do Algoritmo de Karatsuba

## Descrição do Projeto
Este projeto implementa o algoritmo de Karatsuba em Python para multiplicação eficiente de dois números inteiros grandes. O algoritmo reduz a complexidade da multiplicação tradicional de O(n²) para aproximadamente O(n^1.58), tornando-o mais eficiente para números grandes.

## Como Executar o Projeto

### Requisitos
- Python 3.x instalado

### Passos para execução
1. Clone este repositório:
   
   git clone <URL_DO_REPOSITORIO>
   
2. Acesse a pasta do projeto:
   
   cd <NOME_DA_PASTA>
   
3. Execute o código:
   
   python main.py
   

## Explicação do Algoritmo
1. Se os números forem pequenos (menores que 10), multiplica diretamente.
2. Divide os números em partes superiores e inferiores.
3. Calcula três produtos recursivamente:
   - `p1 = low_x * low_y`
   - `p3 = (low_x + high_x) * (low_y + high_y)`
   - `p2 = high_x * high_y`
4. Combina os resultados para obter o produto final.

## Análise da Complexidade

### Complexidade Ciclomática
A complexidade ciclomática mede a quantidade de caminhos independentes no código. O grafo de fluxo de controle inclui:
- Nós representando chamadas recursivas e operações matemáticas.
- Arestas ligando os nós conforme o fluxo do algoritmo.

A fórmula utilizada é:
\[ M = E - N + 2P \]
Onde:
- `E`: Número de arestas do grafo.
- `N`: Número de nós.
- `P`: Número de componentes conexos (1 para um único programa).

O cálculo para este algoritmo resultou em uma complexidade ciclomática de **4**, indicando um fluxo de controle simples e bem estruturado.

### Complexidade Assintótica
A complexidade do algoritmo é:
- **Melhor caso**: O(n^1.58)
- **Caso médio**: O(n^1.58)
- **Pior caso**: O(n^1.58)

Essa complexidade é derivada da relação de recorrência:
\[ T(n) = 3T(n/2) + O(n) \]
Que, ao resolver pelo método mestre, resulta em O(n^log2(3)), aproximadamente O(n^1.58).

## Conclusão
O algoritmo de Karatsuba é uma alternativa eficiente à multiplicação tradicional, especialmente para números grandes. Sua complexidade reduzida o torna uma escolha viável em aplicações que exigem operações matemáticas intensivas. Embora tenha um overhead inicial devido à recursão, seu desempenho melhora significativamente à medida que os números aumentam. Assim, ele é amplamente utilizado em computação científica, criptografia e outros domínios que exigem manipulação de grandes números inteiros.
