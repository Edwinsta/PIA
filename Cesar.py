import os

def Cesar():
    def cifrado():
        message = input('Ingresa el mensaje: ')
        espacios = 1
        while espacios > 0:
            clave = input('Ingresa tu palabra clave para cifrar: ')
            espacios = clave.count(' ')
            if clave.isalpha() == False:
                espacios += 1
        key = len(clave)

        SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

        translated = ''

        for symbol in message:
            # Note: Only symbols in the `SYMBOLS` string can be encrypted/decrypted.
            if symbol in SYMBOLS:
                symbolIndex = SYMBOLS.find(symbol)
                translatedIndex = symbolIndex + key

                print(translatedIndex)

                if translatedIndex >= len(SYMBOLS):
                    translatedIndex = translatedIndex - len(SYMBOLS)
                elif translatedIndex < 0:
                    translatedIndex = translatedIndex + len(SYMBOLS)

                translated = translated + SYMBOLS[translatedIndex]
            else:
                # Append the symbol without encrypting/decrypting:
                translated = translated + symbol

        print(translated)

    def Crackeo():
        message = input('ingresa el mensaje: ')
        SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

        for key in range(len(SYMBOLS)):
            translated = ''

            for symbol in message:
                if symbol in SYMBOLS:
                    symbolIndex = SYMBOLS.find(symbol)
                    translatedIndex = symbolIndex - key

                    if translatedIndex < 0:
                        translatedIndex = translatedIndex + len(SYMBOLS)

                    translated = translated + SYMBOLS[translatedIndex]

                else:
                    translated = translated + symbol

            print('key #%s: %s' % (key, translated))

    def descifrado():
        message = input('Ingresa el mensaje: ')
        espacios = 1
        while espacios > 0:
            clave = input('Ingresa tu palabra clave para cifrar: ')
            espacios = clave.count(' ')
            if clave.isalpha() == False:
                espacios += 1
        key = len(clave)

        SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

        translated = ''

        for symbol in message:
            # Note: Only symbols in the `SYMBOLS` string can be encrypted/decrypted.
            if symbol in SYMBOLS:
                symbolIndex = SYMBOLS.find(symbol)
                translatedIndex = symbolIndex - key

                print(translatedIndex)

                if translatedIndex >= len(SYMBOLS):
                    translatedIndex = translatedIndex - len(SYMBOLS)
                elif translatedIndex < 0:
                    translatedIndex = translatedIndex + len(SYMBOLS)

                translated = translated + SYMBOLS[translatedIndex]
            else:
                # Append the symbol without encrypting/decrypting:
                translated = translated + symbol


    while True:
        CIFRADO = 1
        DESCIFRADO = 2
        CRACKEO = 3
        print(f'''
                                ---Cesar Tools---

        {CIFRADO}) cifrar
        {DESCIFRADO}) descifrar
        {CRACKEO}) crackear
        ''')
        user = int(input('eliga una opcion >> '))
        if user == 1:
            cifrado()
        elif user == 2:
            descifrado()
        elif user == 3:
            Crackeo()
        elif user > 3 and user < 1:
            break
        else:
            print("")
            print('opcion no valida')

Cesar()
