def binary_to_hex_decimal(binary_str):
    try:
        decimal_value = int(binary_str, 2)
        hex_value = hex(decimal_value)
        return decimal_value, hex_value
    except ValueError:
        return None, None


def process_binary_file(file_path):
    try:
        with open(file_path, 'r') as file:
            binary_input = file.read().strip()
            return binary_input
    except FileNotFoundError:
        return None


def save_hex_to_file(hex_value, output_file_path):
    try:
        with open(output_file_path, 'w') as file:
            file.write(hex_value)
            print("Reprezentacja heksadecymalna zapisana do pliku.")
    except Exception as e:
        print("Wystąpił błąd podczas zapisu do pliku:", e)


binary_file_path = "zmienione_bity5.txt"
output_file_path = "C:\\tmp\\heks.txt"

binary_input = process_binary_file(binary_file_path)

if binary_input is not None:
    decimal_value, hex_value = binary_to_hex_decimal(binary_input)

    if decimal_value is not None and hex_value is not None:
        print("Reprezentacja dziesiętna:", decimal_value)
        print("Reprezentacja heksadecymalna:", hex_value)
        save_hex_to_file(hex_value, output_file_path)
    else:
        print("Podano niepoprawną liczbę binarną.")
else:
    print("Nie można odczytać pliku z bitami.")
