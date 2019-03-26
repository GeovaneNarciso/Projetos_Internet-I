def main():

    import requests

    # exemplo: https://s.aficionados.com.br/imagens/goku-instinto.jpg
    response = requests.get(input("Informe a url da imagem (http://exemplo.com/imagem.jpg): \n"))
    nome_imagem = input("Informe um nome para a imagem (exemplo.jpg ou exemplo.gif): ")

    with open('imagens/' + nome_imagem, 'wb') as code:
        code.write(response.content)


if __name__ == '__main__':
    main()
