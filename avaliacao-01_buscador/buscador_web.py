from buscador_web_class import Buscador

"""
Buscador de links que possuem uma keyword no corpo da pagina
Autores:
    Luan da Silva Rodrigues
    Geovane Narciso da Silva
"""


def main():
    url = input("Informe a URL: ")  # exemplo de url: 'https://www.ojogos.com.br/'
    keyword = input("Informe a palavra-chave: ")
    depth = int(input("Informe a profundidade da busca: "))

    x = Buscador(url=url, keyword=keyword, max_depth=depth, max_links_por_pag=5)
    x.search()

    for link in x.get_trecho_and_url().keys():
        print(x.url_trecho_econtrados[link], link)


if __name__ == '__main__':
    main()
