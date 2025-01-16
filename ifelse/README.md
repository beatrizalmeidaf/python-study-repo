# Estruturas Condicionais

As estruturas condicionais em Python são fundamentais para o controle de fluxo em um programa. Elas permitem que diferentes blocos de código sejam executados com base em condições específicas.

---

## O que são estruturas condicionais?

- **Controle de fluxo:** Estruturas condicionais determinam qual parte do código será executada com base em uma condição.
- **Decisões dinâmicas:** Elas permitem que programas sejam mais flexíveis e dinâmicos, adaptando-se a diferentes situações em tempo de execução.
- **Base lógica:** As condições são baseadas em expressões booleanas, que resultam em `True` ou `False`.

---

## Características principais das estruturas condicionais

- **if, elif e else:**
  - O **`if`** executa um bloco de código se a condição for verdadeira.
  - O **`elif`** (abreviação de "else if") testa outra condição se a anterior for falsa.
  - O **`else`** executa um bloco de código se nenhuma das condições anteriores for verdadeira.

- **Expressões booleanas:**
  - Utilizam operadores como `==`, `!=`, `<`, `>`, `<=`, `>=`, `and`, `or`, `not` para avaliar condições.

- **Indentação obrigatória:**
  - Em Python, blocos de código dentro de estruturas condicionais são definidos por indentação.

- **Aninhamento:**
  - Estruturas condicionais podem ser aninhadas para lidar com decisões mais complexas.

---

## Exemplos de uso

### Estrutura básica:
```python
x = 10

if x > 5:
    print("x é maior que 5")
elif x == 5:
    print("x é igual a 5")
else:
    print("x é menor que 5")
```

### Usando múltiplas condições:
```python
idade = 20

if idade >= 18 and idade < 65:
    print("Adulto")
elif idade < 18:
    print("Menor de idade")
else:
    print("Idoso")
```

### Condicional em uma única linha (Ternário):
```python
par_ou_impar = "Par" if x % 2 == 0 else "Ímpar"
print(par_ou_impar)
```

---

## Quando usar estruturas condicionais?

As estruturas condicionais são úteis quando você precisa:
- Tomar decisões com base no valor de uma variável.
- Executar diferentes blocos de código para diferentes situações.
- Implementar validações ou cálculos condicionais em seu programa.

---

## Recursos Adicionais
- [Documentação Oficial do Python - Controle de Fluxo](https://docs.python.org/3/tutorial/controlflow.html) 