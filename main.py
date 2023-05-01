from conf import Conf
from lib import Math, Error
###     name   - M2STR
###     author - txello
###     version - 1.3b
class M2STR:
    'M2STR - симметричное шифрование.'
    def encode(w_input, words = {}, salt = '') -> list:
        '''
        Возвращает w_input в виде списка в зашифрованном виде.\n
        ------\n
        :param str w_input: Входное сообщение.
        :param list words: (необязательно) Словарь символов. Тип: {'syblol':'number'}
        :param str salt: (необязательно) Секретный ключ(соль).
        '''
        try:
            salt = list(Conf.salt(salt))
            if len(salt) == 0: raise Error("Error #2: Вы ввели пустую соль!")
            # salt - секретный ключ(соль) для шифрования.
            # если указана пользовательская соль, то заменяется.
            
            words = Conf.word(words)
            if len(words) == 0: raise Error("Error #3: Вы ввели пустой словарь!")
            # words - словарь символов.
            # если указан пользовательский словарь символов, то заменяется.

            for i in range(len(salt)):
            # len(salt) - количество символов в соли для шифрования.
                salt[i] = words[salt[i]]
                # salt[i] - определённый символ в соли.
                # пример: salt[0] (( 'q' )) = words['q'] (( '43' ))
                # теперь соль стала цифрами из словаря символов.
                
            w_input = list(w_input)
            if len(w_input) == 0: raise Error("Error #1: Вы ввели пустое сообщение!")
            # w_input - список из входного сообщения.
            # если сообщение пустое, то выводится ошибка #0.

            for i in range(len(w_input)):
            # len(w_input) - количество символов в списке из входного сообщения.
                w_input[i] = words[w_input[i]]
                # w_input[i] - определённый символ в списке.
                # пример: w_input[0] (('1')) = words['1'] (( '53' ))
                # теперь входное сообщение стало цифрами из словаря символов.
            
            salt_str = list(str(Math.euclid(len(salt)) % len(salt)))
            # salt_str - зашифрованная алгоритмом Евклида соль.

            j = 1
            for i in range(len(salt_str)):
            # len(salt_str) - количество символов в списке из зашифрованной алготимом Евклида соли.
                salt.insert(j,salt_str[i])
                j *= 2
                # Через каждые 2 значения списка записывается зашифрованная алготимом Евклида соль в основную соль.
            # salt - сумма соли для шифрования.

            j = 1
            l = 3
            for i in range(len(salt)):
            # len(salt) - количество символов в сумме соли для шифрования.
                w_input.insert(j,salt[i])
                if j > len(w_input): w_input.append('=');break
                # если входящее сообщение короче суммы соли, то в конце записывается знак равенства как указатель на окончание записи соли.
                for k in range(len(salt_str)):
                    w_input.insert(l,salt[i])
                    w_input.insert(l,salt_str[k])
                    l *= 3
                    # каждые 3 значения списка, начиная с 3-го, записывается соль и сумма соли.
                w_input.insert(j,salt[i])
                j *= 3 if j < len(salt_str) else 2
                # каждые 2 или 3 значения списка записывается соль во входящее сообщение.
                # если входящее сообщение длиннее суммы соли, то соль дублируется каждые 2 или 3 значения списка во входящее сообщение.
            return w_input
            # возвращает список зашифрованного сообщения.
        except KeyError:
            print("Error #4: Вы ввели сообщение, символы которых нет в вашем словаре!")
