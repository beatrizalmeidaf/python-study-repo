S = 'Spam'
print(S.find('am')) # find() retorna o índice da primeira ocorrência de um caractere ou substring

print(S.replace('am', 'ammer')) # replace() substitui uma substring por outra

print(S.split('a')) # split() divide a string em uma lista de substrings

line = 'aaa,bbb,ccc,ddd'
print(line.split(','))

print(''.join(['aaa', 'bbb', 'ccc', 'ddd'])) # join() concatena uma lista de strings em uma única string

print('%s, emails, and %s' % ('spam', 'FOOD'))