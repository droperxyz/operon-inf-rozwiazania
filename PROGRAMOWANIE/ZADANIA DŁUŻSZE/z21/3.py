def NWD(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a


def FactorizeNumber(number):
    factor = 2
    factors = []
    while factor*factor <= number:
        while number % factor == 0:
            factors.append(factor)
            number //= factor
        factor += 1
    if number > 1:
        factors.append(number)

    return factors

def CheckKey(p,q,e,d):
    if NWD(e, (p-1)*(q-1)) != 1 or (e*d) % ((p-1)*(q-1)) != 1:
        return False
    else:
        return True


def EncryptWord(e,n):
    word = "krasnoludowie"
    word_ascii = []
    encrypted_word = []

    for letter in word:
        word_ascii.append(ord(letter))

    filled_with_zeros = [f"{num:03}" for num in word_ascii]
    groups = [''.join(filled_with_zeros[i:i + 3]) for i in range(0, len(filled_with_zeros), 3)]

    for group in groups:
        group = int(group)
        encrypted_block = group**e % n
        encrypted_word.append(str(encrypted_block))

    encrypted_word = ''.join(encrypted_word)

    return encrypted_word


keys = open('klucze.txt', 'r')
message = open('wiadomosc.txt', 'r')
message = message.readline()
message_clean = message.replace(" ", "")

for line in keys:
    keys = line.split()

    n = int(keys[0])
    e = int(keys[1])
    d = int(keys[2])

    p, q = FactorizeNumber(n)

    if CheckKey(p, q, e, d):
        print("Klucz poprawny")
        encrypted_word = EncryptWord(e, n)
        if encrypted_word in message:
            print("Znaleziono ciag")
    else:
        print("Klucz niepoprawny")



