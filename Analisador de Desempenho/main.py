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

def calcular_kda(kills, deaths):
    kills = float(kills)
    deaths = float(deaths)

    if deaths == 0:
        return kills

    return kills / deaths

if __name__ == "__main__":
    performance = leitor_txt("exemplo.txt")
    print("PERFORMANCE: ")
    for item in performance:
        print(item)
    
    print("\nKDA: ")
    for item in performance:
        kda = calcular_kda(item["kills"], item["deaths"])
        print(f"{item['nome']} - KDA: {kda:.2f}")
    
    print("\nFILTRAGEM POR CLASSE (MAGOS): ")
    magos = [item for item in performance if item["classe"] == "Mago"]

    for mago in magos:
        print(mago)

    print("\nJOGADOR COM MAIOR DANO: ")
    maior_dano = max(performance, key=lambda x: x["dano"])
    print(maior_dano)

    print("\nMÉDIA DE KILLS: ")
    media_kills = sum(int(item["kills"]) for item in performance) / len(performance)
    print(f"{media_kills:.2f}")

    print("\nJOGADORES COM KDA MAIOR QUE 2: ")
    for item in performance:
        kda = calcular_kda(item["kills"], item["deaths"])
        if kda > 2:
            print(f"{item['nome']} - KDA: {kda:.2f}")