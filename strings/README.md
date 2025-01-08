# Strings 

## O que são Strings?
Strings são sequências de caracteres imutáveis em Python, usadas para armazenar e manipular texto. Elas podem ser definidas usando aspas simples (`'`), aspas duplas (`"`), ou três aspas (`'''` ou `"""`) para strings de múltiplas linhas.

---

## Principais Operações com Strings

### 1. Indexação e Fatiamento
- **Indexação:** Acessar caracteres individuais usando índices.
- **Fatiamento:** Obter substrings usando intervalos.


### 2. Concatenar e Repetir Strings
- Usar o operador `+` para concatenar.
- Usar o operador `*` para repetir.


### 3. Funções e Métodos Comuns
Python possui várias funções e métodos embutidos para trabalhar com strings. Aqui estão alguns:

#### Funções:
```python
len("Python")  # Retorna o tamanho da string: 6
```

#### Métodos:
```python
text = "python"

print(text.upper())    # 'PYTHON' (maiúsculas)
print(text.lower())    # 'python' (minúsculas)
print(text.capitalize()) # 'Python' (primeira letra maiúscula)
print(text.replace("py", "Py")) # 'Python' (substituir substrings)
print(text.startswith("py")) # True (começa com 'py')
print(text.endswith("on"))   # True (termina com 'on')
```

---

## Técnicas Avançadas

### 1. Formatação de Strings
Existem três principais maneiras de formatar strings:
- Usando o operador `%` (estilo antigo).
- Usando o método `.format()`.
- Usando f-strings (Python 3.6+).


### 2. Strings e Expressões Regulares
Expressões regulares permitem encontrar padrões em strings.

---

## Recursos Adicionais
- [Documentação Oficial do Python](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)

---


