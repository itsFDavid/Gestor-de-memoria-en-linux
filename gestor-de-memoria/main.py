#importamos librerias
import argparse as ap
from functions import ram_usage, vram_usage, iout_options


def run():
    #estableciendo las relas de los argumentos
    parser= ap.ArgumentParser(description="Aplicacion para manipular la memoria en "  
                            + "linux y dispositivos de disco") 
    parser.add_argument("-r", "--ram", 
                        action="store_true",
                        help="Acceder a las funciones de la memoria RAM")
    parser.add_argument("-v", "--vram",
                        action="store_true",
                        help="Acceder a las funciones de la memoria VIRTUAL")        
    parser.add_argument("-d", "--device", 
                        action="store_true", 
                        help="Acceder a las funciones de la administracion de discos")
    parser.add_argument("-m", "--manual", 
                        action="store_true", 
                        help="Ayuda de la aplicacion")
    parser.add_argument("opciones", 
                        nargs="?",
                        default=False,
                        help="opciones de la aplicacion como valor de entrada")
    #ahora los argumentos de la app
    args= parser.parse_args()
    
    if args.ram:
        ram_usage(args.opciones)
    elif args.vram:
        vram_usage()
    elif args.device:
        iout_options()
    else:
        print("""

[args]            
args:
              
-r      --ram       Acceder a las opciones de la memoria
-v      --vram      Acceder a las opciones de la memovia VIRTUAL
-d      --device    Acceder alas opciones de Discos montados en linux
-m      --manual    Muestra el menu de opciones de la app
              
ejemplo: py main.py -r
         python3 main.py -m



            """) 

if __name__== "__main__":
    run()
