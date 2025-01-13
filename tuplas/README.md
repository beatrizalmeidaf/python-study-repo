# Tuplas

## O que são Tuplas?
Uma tupla é uma coleção ordenada de itens que é **imutável**, ou seja, seus valores não podem ser alterados após a sua criação. Python refere-se a valores que não podem mudar como imutáveis, e uma lista imutável é chamada de **tupla**. 

As tuplas são definidas usando parênteses (`()`), com os elementos separados por vírgulas. Assim como as listas, elas são ordenadas e os elementos podem ser acessados pelo índice.

---

## Por que usar Tuplas?

- **Imutabilidade:** Garantem que os dados armazenados permaneçam inalterados, tornando-as ideais para representar coleções de itens constantes, como coordenadas ou configurações.
- **Eficiência:** São mais leves e mais rápidas que listas para operações que não envolvem modificações.
- **Segurança:** Evitam modificações acidentais dos dados.

---

## Como Criar Tuplas

### Criando uma Tupla
Para criar uma tupla, basta colocar os elementos entre parênteses e separá-los com vírgulas:
```python
cores = ("vermelho", "azul", "verde")
print(cores)
```

---

## Convertendo Entre Listas e Tuplas
Você pode converter listas em tuplas e vice-versa:
- **Lista para Tupla:**
  ```python
  lista = [1, 2, 3]
  tupla = tuple(lista)
  print(tupla)  # Saída: (1, 2, 3)
  ```
- **Tupla para Lista:**
  ```python
  tupla = ("a", "b", "c")
  lista = list(tupla)
  print(lista)  # Saída: ["a", "b", "c"]
  ```

---

## Recursos Adicionais
- [Documentação Oficial do Python - Tuplas](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences)
