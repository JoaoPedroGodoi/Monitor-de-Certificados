import requests
from bs4 import BeautifulSoup
try:
    from config_local import URL, TIMEOUT
except ImportError:
    from config import URL, TIMEOUT

def obter_certificados():
    response = requests.get(URL, timeout=TIMEOUT)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "lxml")
    tabela = soup.find("table", class_="table table-striped")
    if tabela is None:
        raise Exception("Tabela de certificados não encontrada.")

    cabecalhos = []
    for th in tabela.find("thead").find_all("th"):
        texto = th.get_text(" ", strip=True)
        if texto != "Logins para captura de intimações logadas":
            cabecalhos.append(texto)

    indices = {
        nome: indice
        for indice, nome in enumerate(cabecalhos)
    }

    certificados = []
    tbody = tabela.find("tbody")
    for linha in tbody.find_all("tr"):
        colunas = linha.find_all("td")
        if len(colunas) < len(indices):
            continue
        certificados.append({
            "codigo": colunas[
                indices["Código Acesso"]
            ].get_text(strip=True),
            "identificador": colunas[
                indices["Identificador"]
            ].get_text(strip=True),
            "status": colunas[
                indices["Status Login no Tribunal"]
            ].get_text(strip=True),
            "classificacao": colunas[
                indices["Classificação"]
            ].get_text(" ", strip=True)
        })

    return certificados