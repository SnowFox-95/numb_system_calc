import functions

if __name__ == "__main__":
    print(
        "Привет! Я калькулятор систем счисления. Помогу перевести любое число в десятичную систему.\n"
        "Загадай число для перевода:"
    )
    digit = input()
    print(
        "Замечательно! \n"
        "А в какой системе счислений изначально это число? \n"
        "\n"
        "HEX - шестнадцатеричная, \n"
        "OCT - восмеричная, \n"
        "QUA - четверичная, \n"
        "BIN - бинарная(двоичная).\n"
    )
    system_calc = input()