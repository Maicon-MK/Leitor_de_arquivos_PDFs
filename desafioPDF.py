import os
import fitz  # PyMuPDF

def lerTitulosPDFs(caminho):
    titulos_pdf = []
    for i in os.listdir(caminho):
        if i.endswith('.pdf'):
            caminho_completo = os.path.join(caminho, i)

            pdf = fitz.open(caminho_completo)
            titulo_pdf = pdf.metadata.get('title', 'Título não disponível')
            pdf.close()

            titulos_pdf.append(titulo_pdf)

    return titulos_pdf

def buscarPDF(caminho, palavra_chave):
    encontrados = []
    titulos_pdf = lerTitulosPDFs(caminho)

    for i in os.listdir(caminho):
        if i.endswith('.pdf'):
            caminho_completo = os.path.join(caminho, i)

            pdf = fitz.open(caminho_completo)
            for pagina_num in range(pdf.page_count):
                pagina = pdf.load_page(pagina_num)
                texto_completo = pagina.get_text()

                if palavra_chave.lower() in texto_completo.lower():
                    encontrados.append({
                        'nome_arquivo': i,
                        'pagina': pagina_num + 1,
                        
                    })

            pdf.close()

    return titulos_pdf, encontrados

while True:
    pasta = input('Digite o caminho da pasta onde estão seus PDFs (ou "sair" para encerrar o aplicativo):\n')
    if pasta.lower() == 'sair':
        print("Encerrando o aplicativo.")
        break

    print("Menu:")
    print("1. Visualizar todos os PDFs na pasta")
    print("2. Pesquisar por palavra-chave")

    escolha = input("Digite o número da opção desejada (ou 'sair' para encerrar o aplicativo): ")

    if escolha == '1':
        titulos = lerTitulosPDFs(pasta)

        if titulos:
            print("Títulos de todos os PDFs na pasta:")
            for titulo in titulos:
                print(f"- {titulo}")
        else:
            print("Nenhum arquivo PDF encontrado na pasta.")

    elif escolha == '2':
        palavra_chave = input("Digite a palavra que você deseja procurar: ")

        titulos, resultado = buscarPDF(pasta, palavra_chave)

        if titulos:
            print("Títulos de todos os PDFs na pasta:")
            for titulo in titulos:
                print(f"- {titulo}")

        if resultado:
            for arquivo in resultado:
                print(f"Arquivo encontrado: {arquivo ['nome_arquivo']}")
                
                print(f"Página: {arquivo ['pagina']}")
                
        else:
            print("Nenhum arquivo encontrado.")

    elif escolha.lower() == 'sair':
        print("Encerrando o aplicativo.")
        break

    else:
        print("Opção inválida. Tente novamente.")
