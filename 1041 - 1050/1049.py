# Accepted

subfilo = input()
classe = input()
metabolismo = input()

if subfilo == "vertebrado":
    if classe == "ave":
        if metabolismo == "carnivoro":
            print("aguia")
        else:
            print("pomba")
    else:
        if metabolismo == "onivoro":
            print("homem")
        else:
            print("vaca")
else:
    if classe == "inseto":
        if metabolismo == "hematofago":
            print("pulga")
        else:
            print("lagarta")
    else:
        if metabolismo == "hematofago":
            print("sanguessuga")
        else:
            print("minhoca")
