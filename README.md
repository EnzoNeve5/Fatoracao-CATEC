# Documento de Especificação de Produto (PRD): Calculadora de Fatoração

---

## 1. Visão Geral do Produto

O software é uma ferramenta educacional e utilitária via terminal que realiza o cálculo e a demonstração passo a passo de diversos métodos de fatoração algébrica com base em quatro entradas numéricas fornecidas pelo usuário.

---

## 2. Objetivos
*	Automatizar o cálculo de expressões algébricas comuns.
*	Exibir a resolução estruturada de produtos notáveis e fatoração.
*	Validar entradas para garantir que apenas dados numéricos sejam processados.

---

## 3. Requisitos Funcionais
### 3.1 Entrada de Dados (Inputs)

O sistema deve solicitar quatro valores de ponto flutuante:

*	a: Primeiro coeficiente/termo.
*	b: Segundo coeficiente/termo.
*	x: Primeira variável de agrupamento.
*	y: Segunda variável de agrupamento.

### 3.2 Lógica de Cálculo e Fatoração

O sistema deve processar e exibir os seguintes modelos matemáticos:
Método	Fórmula Base
Fator Comum	$ax + bx = x(a + b)$
Agrupamento	$ax + bx + ay + by = (a + b)(x + y)$
Diferença de Quadrados	$a^2 - b^2 = (a + b)(a - b)$
Trinômio Quadrado Perfeito	$a^2 \pm 2ab + b^2 = (a \pm b)^2$
Soma/Diferença de Cubos	$a^3 \pm b^3 = (a \pm b)(a^2 \mp ab + b^2)$
Cubo Perfeito	$a^3 \pm 3a^2b + 3ab^2 \pm b^3 = (a \pm b)^3$

### 3.3 Tratamento de Erros

•	O sistema deve capturar exceções do tipo ValueError caso o usuário insira caracteres não numéricos.
•	Deve exibir uma mensagem de erro amigável em vermelho: "Você não digitou ou digitou dados não numéricos!".

---

## 4. Interface e Experiência do Usuário (UX)
### 4.1 Formatação Visual

O software utiliza códigos de escape ANSI para melhorar a legibilidade no terminal:

*	Cores de Destaque: Ciano (\033[36m) para resultados e variáveis.
*	Cabeçalhos: Fundo ciano com texto preto e sublinhado para separar as seções de fatoração.
*	Mensagens de Erro: Texto em vermelho (\033[31m).

### 4.2 Fluxo de Saída

1.	Título principal: ##################FATORAÇÃO##################.
2.	Seção de Fator Comum.
3.	Seção de Agrupamento.
4.	Seção de Diferença de Quadrados.
5.	Seção de Quadrado Perfeito (Soma e Subtração).
6.	Seção de Soma e Diferença de Cubos.
7.	Seção de Cubo Perfeito.
8.	Mensagem de encerramento: "A CATEC agradece a sua consulta!".

---

## 5. Requisitos Não Funcionais
*	Linguagem: Python 3.x.
*	Ambiente: Interface de Linha de Comando (CLI).
*	Confiabilidade: O bloco finally deve garantir que a mensagem de encerramento seja exibida independentemente de falhas durante a execução.

---

## 6. Fluxograma Lógico (Resumido)
1.	Início
2.	Entrada: Usuário digita $a, b, x, y$.
3.	Processamento: Cálculo de potências ($a^2, a^3$, etc.) e produtos.
4.	Saída: Impressão dos blocos formatados de fatoração.
5.	Fim

