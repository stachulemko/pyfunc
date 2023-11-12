import random
from turtle import right


def data(masage_do_szyfrowania):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    random_permutation = random.sample(alphabet, len(alphabet))
    keyboard = alphabet
    # ------------
    plugboard = ''.join(random_permutation)
    # ------------
    right = ''.join(random_permutation)
    # ------------
    middle = ''.join(random_permutation)
    # -----------
    left = ''.join(random_permutation)
    # -----------
    reflector = ''.join(random_permutation)
    lista = []

    for i in masage_do_szyfrowania:
        plugboard_position = plugboard.index(i)
        right_letter = right[plugboard_position]
        right_stock_position = alphabet.index(right_letter)
        middle_letter = middle[right_stock_position]
        middle_stock_position = alphabet.index(middle_letter)
        left_letter = left[middle_stock_position]
        left_stock_position = alphabet.index(left_letter)
        reflector_letter = reflector[left_stock_position]
        reflector_stock_position = alphabet.index(reflector_letter)
        # kodowanie w lewo
        # -----------
        # kodowanie w prawo
        reflector_position = reflector_stock_position
        left_letter2 = alphabet[reflector_position]
        left_position = left.index(left_letter2)
        middle_letter2 = alphabet[left_position]
        middle_position = middle.index(middle_letter2)
        right_letter2 = alphabet[middle_position]
        right_position = right.index(right_letter2)
        plugboard_letter = plugboard_position[right_position]
        plugboard_position2 = alphabet.index(plugboard_letter)
        keyboard_letter = keyboard[plugboard_position2]
        lista.append(keyboard_letter)
    print(keyboard_letter)

    # print(plugboard)
print(data("a"))
