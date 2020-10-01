print("SI DESEAS EMPEZAR EL JUEGO ESCRIBRE PLAY!")
empezar = input("->")
while (empezar == "play"):
    print("""CON QUE NIVEL QUIERES EMPEZAR
    1) FACIL
    2) NORMAL
    3) DIFICIL""")
    break
nivel = input()
if nivel == "facil":
    print("""VEO VEO ALGO LENTO  (SI NO SABES CUAL ES LA RESPUESTA PON "PISTA"  )""")
    rp1 = input("QUE ESTA VIENDO DREK : ")
    if  rp1 == "pista":
        print("-------------->TE QUEDA UNA VIDA<----------------")
        print("TIENE UN CAPARAZON DURO , QUE LO USA COMO CASA")
        rp2 = input("QUE ESTA VIENDO DREK : ")
        if rp2 == "caracol":
            print("USTED ACERTO")
            print("-------------->YOU WIN<---------------- :)")
        else:
            print("GAME OVER SERRANO ")
else:
    rp1 == "caracol"
    print("USTED ACERTO")
    print("YOU WIN :)")