import argparse
import logging
from Scraping import Scraping

logging.basicConfig(filename='app.log',level=logging.INFO)

def main(Menu):
    try:
        if Menu == 1:
            x= input("Dame la url para descargar imagenes:")
            logging.info('Datos para scraping: ')
            logging.info(x)
            scraping = Scraping()
            scraping.scrapingImages(x)
            import Metadata
        elif Menu == 2:
            import Hash
        elif Menu == 3:
            import Api_Virustotal
        elif Menu == 4:
            import Cesar
    except FileNotFoundError as e:
        logging.error ("Ocurrio un error" + str(e))
        print("Opcion no valida momentaneamente")
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-Menu', type=int , help='Escoge el tipo de script que quieres usar 1=Metadata 2=Hash 3=Api_Virustotal 4=Cesar', default=0)
    args = parser.parse_args()
    main(args.Menu)
try:
    while True:
        Metadata = 1
        Apivirustotal = 2
        Hash = 3
        Cesar = 4
        socket =5
        print(f'''
                               ----Security Tools----
                                ¿ Que desea hacer ?

        {Metadata}) Extraer metadata y descargar imagenes de una URL determinada
        {Apivirustotal}) Checar urls sospechosas
        {Hash}) Obtener valor Hash
        {Cesar}) Cifrado,Descifrado y Crackeo Cesar

        ''')
        user = int(input('Eliga una opcion >: '))
        ContinueExecuting = True
        try:
            while ContinueExecuting:
                if user == 1:
                    x= input("Dame la url para descargar imagenes:")
                    logging.info('Datos para scraping: ')
                    logging.info(x)
                    scraping = Scraping()
                    scraping.scrapingImages(x)
                    import Metadata
                    ContinueExecuting = False
                elif user == 2:
                    import Api_Virustotal
                    ContinueExecuting = False
                elif user == 3:
                    import Hash
                    ContinueExecuting = False
                elif user == 4:
                    import Cesar
                    ContinueExecuting = False
                elif socket ==5:
                    print("in proccess")
                    ContinueExecuting = False
                else:
                    logging.info(print('opcion no valida'))
                    ContinueExecuting = False
        except FileNotFoundError as e:
            logging.error ("Ocurrio un error: " + str(e))
            print("Opcion no valida momentaneamente")
except ValueError as e:
    logging.error ("Ocurrio un error: " + str(e))
    print("El dato no es valido")
