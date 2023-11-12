def decrypt(ciphertext):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    keyboard = alphabet
    plugboard_permutation = 'RBCDEFKHIJGLMNXPQASTUVWOYZ'
    right_permutation = 'BDFHJLCPTXVZNYEIWGAKMUSQO'
    middle_permutation = 'AJDKSIRUXBLHWTMCQGZNPVFOEY'
    left_permutation = 'EKMFLODQVZNTOWYHXUSPAIBRCJ'
    reflector_permutation = 'YRUHQSLDPXNGOKMIEBFZCWVJAT'
    lista = []

    for i in ciphertext:
        if i in alphabet:
            plugboard_position = alphabet.index(i)
            right_letter = keyboard[right_permutation.index(
                alphabet[plugboard_position])]
            middle_letter = alphabet[middle_permutation.index(right_letter)]
            left_letter = alphabet[left_permutation.index(middle_letter)]
            reflector_letter = alphabet[reflector_permutation.index(
                left_letter)]

            left_letter2 = alphabet[left_permutation.index(reflector_letter)]
            middle_letter2 = alphabet[middle_permutation.index(left_letter2)]
            right_letter2 = alphabet[right_permutation.index(middle_letter2)]
            plugboard_letter = keyboard[plugboard_permutation.index(
                right_letter2)]
            lista.append(plugboard_letter)
        else:
            lista.append(i)

    return ''.join(lista)


ciphertext = "A"  # Twoja zaszyfrowana wiadomość
decrypted_message = decrypt(ciphertext)
print(decrypted_message)
