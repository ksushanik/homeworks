import sympy
import random
import base64

def is_prime(n):
    if n <= 1:
        return False
    return sympy.isprime(n)

def generate_prime(bits):
    p = sympy.randprime(2 ** (bits - 1), 2 ** bits - 1)
    return p

def generate_keys(bits):
    p = generate_prime(bits)
    q = generate_prime(bits)
    while p == q:
        q = generate_prime(bits)
    n = p * q
    phi = (p - 1) * (q - 1)
    e = random.randint(2, phi)
    while sympy.gcd(e, phi) != 1:
        e = random.randint(2, phi)
    d = sympy.mod_inverse(e, phi)
    return (e, n), (d, n)

def str_to_int(s):
    return int.from_bytes(s.encode(), 'big')

def int_to_str(n):
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()

if __name__ == "__main__":
    bits = 128  # Задайте желаемый размер ключа
    (e, n), (d, n) = generate_keys(bits)
    print("Открытый ключ:", (e, n))
    print("Закрытый ключ:", (d, n))

    # Генерируем исходное текстовое сообщение
    message = "This is a test message."
    print("Исходное сообщение:", message)

    # Шифруем и кодируем сообщение
    encrypted_message = []
    for char in message:
        char_int = str_to_int(char)
        char_encrypted = pow(char_int, e, n)
        char_base64 = base64.b64encode(char_encrypted.to_bytes((char_encrypted.bit_length() + 7) // 8, 'big')).decode()
        encrypted_message.append(char_base64)

    print("Зашифрованное и закодированное сообщение:", " ".join(encrypted_message))

    # Дешифруем и декодируем сообщение
    decrypted_message = []
    for char_base64 in encrypted_message:
        char_encrypted_bytes = base64.b64decode(char_base64.encode())
        char_encrypted = int.from_bytes(char_encrypted_bytes, 'big')
        char_int = pow(char_encrypted, d, n)
        char = int_to_str(char_int)
        decrypted_message.append(char)

    print("Расшифрованное сообщение:", "".join(decrypted_message))
