import os 
import subprocess
from grafica import grafic_Mem


def ram_usage(opcion):
    """
    Funcion que muestra las opciones de la memoria ram
    """

    os.system('clear')
    ram=""" 
#           _____                    _____                    _____ #
#          /\    \                  /\    \                  /\    \ #
#         /::\    \                /::\    \                /::\____\ #
#        /::::\    \              /::::\    \              /::::|   | #
#       /::::::\    \            /::::::\    \            /:::::|   | #
#      /:::/\:::\    \          /:::/\:::\    \          /::::::|   | #
#     /:::/__\:::\    \        /:::/__\:::\    \        /:::/|::|   | #
#    /::::\   \:::\    \      /::::\   \:::\    \      /:::/ |::|   | #
#   /::::::\   \:::\    \    /::::::\   \:::\    \    /:::/  |::|___|______ #
#  /:::/\:::\   \:::\____\  /:::/\:::\   \:::\    \  /:::/   |::::::::\    \ #
# /:::/  \:::\   \:::|    |/:::/  \:::\   \:::\____\/:::/    |:::::::::\____\ #
# \::/   |::::\  /:::|____|\::/    \:::\  /:::/    /\::/    / ~~~~~/:::/    / #
#  \/____|:::::\/:::/    /  \/____/ \:::\/:::/    /  \/____/      /:::/    / #
#        |:::::::::/    /            \::::::/    /               /:::/    / #
#        |::|\::::/    /              \::::/    /               /:::/    / #
#        |::| \::/____/               /:::/    /               /:::/    / #
#        |::|  ~|                    /:::/    /               /:::/    / #
#        |::|   |                   /:::/    /               /:::/    / #
#        \::|   |                  /:::/    /               /:::/    / #
#         \:|   |                  \::/    /                \::/    / #
#          \|___|                   \/____/                  \/____/ #


       """
    print(ram)
    
    if opcion and opcion.upper()== "I":
        output = subprocess.getoutput('cat /proc/meminfo | grep "Mem" && cat /proc/meminfo | grep "Cache" ')
        print(output)
        grafic_Mem()
    elif opcion and opcion.upper()== "M":
        os.system('free -m | grep "caché" | awk \'{print$5}\' && sudo free -m | grep "Mem" | awk \'{print$6}\' '  )
    elif opcion and opcion.upper()== "E":
        os.system('sudo sync && sudo sysctl vm.drop_caches=1')
    elif opcion and opcion.upper()== "O":
        print("""
[opciones]
args:
                  

I     Muestra la informacion de la memoria Real
M     muestra informacion de la memoria cache
E     Elimina la memoria cache
O   Muestra las opciones
                  
ej:  py main.py -r i
     py main.py -r e
     py main.py -r m
              
                  """) 
    elif opcion is False:
            while True:
               
                res= input("""

(I)nformacion de la memoria real         
(M)ostar informacion de la memoria cache 
(E)liminar la memoria cache               
(S)alir                                   


--->  """)
                if res.upper()== "I":
                    output = subprocess.getoutput('cat /proc/meminfo | grep "Mem" && cat /proc/meminfo | grep "Cache" ')
                    print(output)
                    grafic_Mem()
                elif res.upper()== "M":
                    os.system('free -m | grep "caché" | awk \'{print$5}\' && sudo free -m | grep "Mem" | awk \'{print$6}\' '  )
                elif res.upper()== "E":
                    os.system('sudo sync && sudo sysctl vm.drop_caches=1')
                elif res.upper()== "S":
                    return
    else:
        print("Opcion incorrecta")
        


def vram_usage():
    """
    Funcion que muestra las opciones de la memoria virtual
    """
    print("""

#          _____                          _____                    _____                    _____#
#         /\    \                        /\    \                  /\    \                  /\    \#
#        /::\____\                      /::\    \                /::\    \                /::\____\#
#       /:::/    /                     /::::\    \              /::::\    \              /::::|   |#
#      /:::/    /                     /::::::\    \            /::::::\    \            /:::::|   |#
#     /:::/    /                     /:::/\:::\    \          /:::/\:::\    \          /::::::|   |#
#    /:::/____/                     /:::/__\:::\    \        /:::/__\:::\    \        /:::/|::|   |#
#    |::|    |                     /::::\   \:::\    \      /::::\   \:::\    \      /:::/ |::|   |#
#    |::|    |     _____          /::::::\   \:::\    \    /::::::\   \:::\    \    /:::/  |::|___|______#
#    |::|    |    /\    \        /:::/\:::\   \:::\____\  /:::/\:::\   \:::\    \  /:::/   |::::::::\    \#
#    |::|    |   /::\____\      /:::/  \:::\   \:::|    |/:::/  \:::\   \:::\____\/:::/    |:::::::::\____\#
#    |::|    |  /:::/    /      \::/   |::::\  /:::|____|\::/    \:::\  /:::/    /\::/    / ~~~~~/:::/    /#
#    |::|    | /:::/    /        \/____|:::::\/:::/    /  \/____/ \:::\/:::/    /  \/____/      /:::/    /#
#    |::|____|/:::/    /               |:::::::::/    /            \::::::/    /               /:::/    /#
#    |:::::::::::/    /                |::|\::::/    /              \::::/    /               /:::/    /#
#    \::::::::::/____/                 |::| \::/____/               /:::/    /               /:::/    /#
#     ~~~~~~~~~~                       |::|  ~|                    /:::/    /               /:::/    /#
#                                      |::|   |                   /:::/    /               /:::/    /#
#                                      \::|   |                  /:::/    /               /:::/    /#
#                                       \:|   |                  \::/    /                \::/    /#
#                                        \|___|                   \/____/                  \/____/#



          """)
    while True:
        respuesta= input("""
                    

(I)nformacion de la memoria VIRTUAL   
(S)alir                               
                 
                    
--->""")
        if respuesta.upper()== "I":
            os.system('cat /proc/meminfo | grep  "Swap"')
        else:
            return
                         


def iout_options():
    """
    Funcion para mostrar discos montados en la maquina
    """
    print("""
#          _____                    _____                    _____                    _____                   _______                   _____#
#         /\    \                  /\    \                  /\    \                  /\    \                 /::\    \                 /\    \#
#        /::\    \                /::\    \                /::\    \                /::\    \               /::::\    \               /::\    \#
#       /::::\    \               \:::\    \              /::::\    \              /::::\    \             /::::::\    \             /::::\    \#
#      /::::::\    \               \:::\    \            /::::::\    \            /::::::\    \           /::::::::\    \           /::::::\    \#
#     /:::/\:::\    \               \:::\    \          /:::/\:::\    \          /:::/\:::\    \         /:::/~~\:::\    \         /:::/\:::\    \#
#    /:::/  \:::\    \               \:::\    \        /:::/__\:::\    \        /:::/  \:::\    \       /:::/    \:::\    \       /:::/__\:::\    \#
#   /:::/    \:::\    \              /::::\    \       \:::\   \:::\    \      /:::/    \:::\    \     /:::/    / \:::\    \      \:::\   \:::\    \#
#  /:::/    / \:::\    \    ____    /::::::\    \    ___\:::\   \:::\    \    /:::/    / \:::\    \   /:::/____/   \:::\____\   ___\:::\   \:::\    \#
# /:::/    /   \:::\ ___\  /\   \  /:::/\:::\    \  /\   \:::\   \:::\    \  /:::/    /   \:::\    \ |:::|    |     |:::|    | /\   \:::\   \:::\    \#
#/:::/____/     \:::|    |/::\   \/:::/  \:::\____\/::\   \:::\   \:::\____\/:::/____/     \:::\____\|:::|____|     |:::|    |/::\   \:::\   \:::\____\#
#\:::\    \     /:::|____|\:::\  /:::/    \::/    /\:::\   \:::\   \::/    /\:::\    \      \::/    / \:::\    \   /:::/    / \:::\   \:::\   \::/    /#
# \:::\    \   /:::/    /  \:::\/:::/    / \/____/  \:::\   \:::\   \/____/  \:::\    \      \/____/   \:::\    \ /:::/    /   \:::\   \:::\   \/____/#
#  \:::\    \ /:::/    /    \::::::/    /            \:::\   \:::\    \       \:::\    \                \:::\    /:::/    /     \:::\   \:::\    \#
#   \:::\    /:::/    /      \::::/____/              \:::\   \:::\____\       \:::\    \                \:::\__/:::/    /       \:::\   \:::\____\#
#    \:::\  /:::/    /        \:::\    \               \:::\  /:::/    /        \:::\    \                \::::::::/    /         \:::\  /:::/    /#
#     \:::\/:::/    /          \:::\    \               \:::\/:::/    /          \:::\    \                \::::::/    /           \:::\/:::/    /#
#      \::::::/    /            \:::\    \               \::::::/    /            \:::\    \                \::::/    /             \::::::/    /#
#       \::::/    /              \:::\____\               \::::/    /              \:::\____\                \::/____/               \::::/    /#
#        \::/____/                \::/    /                \::/    /                \::/    /                 ~~                      \::/    /#
#         ~~                       \/____/                  \/____/                  \/____/                                           \/____/#



          """)
    while True:
        response=  input("""
                        

(L)istar Discos       
(D)esmoontar discos   
(S)salir              

                            
---->       """)
        if response.upper()== "L":
            os.system('lsblk -o NAME,TYPE,SIZE,MOUNTPOINT |grep "sd"')
        elif response.upper()== "D":
            os.system('lsblk -o NAME,TYPE,SIZE,MOUNTPOINT |grep "sd"')
            disco= input("Escriba el nombre del disco a desmontar (ej.) sda o sde")
            os.system(f"sudo eject /dev/{disco}")
        elif response.upper()== "S":
            return
        else:
            print('Opcion incorrecta')