import conf, lib
###     name   - M2STR
###     author - txello
###     version - 1.0b
def encode(w_input):
    try:
        salt = list(conf.salt())
        if len(salt) == 0: raise lib.Error("Вы ввели пустую соль!")
        # salt (( list[str] )) - соль для шифрования.

        for i in range(len(salt)):
        # len(salt) - количество символов в соли для шифрования.
            salt[i] = conf.word()[salt[i]]
            # salt[i] - определённый символ в соли.
            # пример: salt[0] (('q')) = words['q'] (( '43' ))
            # теперь соль стала цифрами из словаря слов.

        w_input = list(w_input)
        if len(w_input) == 0: raise lib.Error("Вы ввели пустое сообщение!")
        # w_input - список из входного сообщения.
        # если сообщение пустое, то выводится ошибка #0.

        for i in range(len(w_input)):
        # len(w_input) - количество символов в списке из входного сообщения.
            w_input[i] = conf.word()[w_input[i]]
            # w_input[i] - определённый символ в списке.
            # пример: w_input[0] (('1')) = words['1'] (( '53' ))
            # теперь входное сообщение стало цифрами из словаря слов.
        
        salt_str = list(str(lib.euclid(len(salt)) % len(salt)))
        # salt_str - зашифрованная алгоритмом Евклида соль.

        j = 1
        for i in range(len(salt_str)):
        # len(salt_str) - количество символов в списке из зашифрованной алготимом Евклида соли.
            salt.insert(j,salt_str[i])
            j *= 2
            # Через каждые 2 значения списка записывается зашифрованная алготимом Евклида соль в основную соль.
        # salt - сумма соли для шифрования.

        j = 1
        for i in range(len(salt)):
        # len(salt) - количество символов в сумме соли для шифрования.
            w_input.insert(j,salt[i])
            if j > len(w_input): w_input.append('=');break
            w_input.insert(j,salt[i])
            j *= 3 if j < len(salt_str) else 2
            # каждые 2 или 3 значения списка записывается сумма соли во входящее сообщение.
            # если входящее сообщение короче суммы соли, то в конце записывается знак равенства как указатель на окончание записи соли.
            # если входящее сообщение длиннее суммы соли, то сумма соли дублируется каждые 2 или 3 значения списка во входящее сообщение.
        return w_input
    except KeyError:
        print("Error #1: Вы ввели сообщение, символы которых нет в вашем словаре!")
