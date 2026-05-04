def leitor_txt(txt):
    with open (txt) as arquivo:
        texto = arquivo.read()

    lista = []
    texto_tratado = texto.split(";")
    registro = {}
    contador = 0

    for dado in texto_tratado:
        if contador == 0:
            registro["nome"] = dado
        elif contador == 1:
            registro["classe"] = dado
        elif contador == 2:
            registro["kills"] = dado
        elif contador == 3:
            registro["deaths"] = dado
        elif contador == 4:
            registro["dano"] = dado
            contador += 1
        if contador == 5:
            lista.append(registro)
            registro = {}
            contador = 0
        else:
            contador += 1
    
    return lista

if __name__ == "__main__":
    performance = leitor_txt("exemplo.txt")
    for item in performance:
        print(item)