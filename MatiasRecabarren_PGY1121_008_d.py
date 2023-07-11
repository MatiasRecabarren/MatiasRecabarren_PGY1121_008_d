import funciones as fs

while True:
    fs.mostrar_menu()
    opc=fs.validar_opcion()
    if opc == 1:
        fs.comprar_entrada()
    elif opc == 2:
        fs.mostrar_ubi_dis()
    elif opc == 3:
        fs.ver_lista_asis()
    elif opc == 4:
        fs.mostrar_ganancias_t()
    else:
        fs.salir()
