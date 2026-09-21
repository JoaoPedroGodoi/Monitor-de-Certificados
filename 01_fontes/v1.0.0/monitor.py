from coletor import obter_certificados
from email_sender import enviar_email
from config import CERTIFICADOS_IGNORADOS, CERTIFICADOS_MONITORADOS


def main():

    print("Obtendo certificados...")
    certificados = obter_certificados()

    print(f"{len(certificados)} certificados encontrados.")
    problemas = []
    certificados_monitorados = []

    for certificado in certificados:
        identificador = certificado["identificador"]
        if identificador in CERTIFICADOS_IGNORADOS or identificador not in CERTIFICADOS_MONITORADOS:
            continue

        if certificado["status"].lower() == "inoperante":
            problemas.append(certificado)
        else:
            certificados_monitorados.append(certificado)

    print(f"Certificados monitorados: {len(certificados_monitorados)}")
    print(f"Certificados com problema: {len(problemas)}")

    enviar_email(
        problemas,
        certificados_monitorados
    )

if __name__ == "__main__":
    try:
        main()
    except Exception as erro:
        print("Erro:", erro)