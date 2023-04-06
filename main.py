import conf
###     name   - MSTR
###     author - txello
###     version - 0.1b

salt = list(conf.salt())
# salt (( list[str] )) - соль для шифрования.

for i in range(len(salt)):
# len(salt) - количество символов в соли для шифрования.
    salt[i] = conf.word()[salt[i]]
    # salt[i] - определённый символ в соли.
    # пример: salt[0] (('q')) = words['q'] (( '43' ))
    # теперь соль стала цифрами из словаря слов.
# вводим входное сообщение
w = input("Введите сообщение: ")
w_input = list(w)
# w - входное сообщение.
# w_input - список из входного сообщения.

for i in range(len(w_input)):
# len(w_input) - количество символов в списке из входного сообщения.
    w_input[i] = conf.word()[w_input[i]]
    # w_input[i] - определённый символ в списке.
    # пример: w_input[0] (('1')) = words['1'] (( '53' ))
    # теперь входное сообщение стало цифрами из словаря слов.

salt_str = str((len(salt)*64)//32)
# salt_str - сумма соли для шифрования.
# теперь salt_str стал значением String.

j = 0
l = -10
for i in range(len(salt)):
# len(salt) - количество символов в соли для шифрования.
    w_input.insert(j,salt[i])
    w_input.insert(l,salt_str)
    # добавляем в зашифрованное слово символ из соли.
    # добавляем в зашифрованное слово символ из суммы длины соли.
    l = l + 2
    j = j + 2
    # добавляем символы через 2 других

print("Зашифрованное сообщение: "+ "".join(w_input))