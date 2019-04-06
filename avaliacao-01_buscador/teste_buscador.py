import requests
import re
from bs4 import BeautifulSoup
import requests_cache

requests_cache.install_cache('cache_responses')


def main():

    def remove_caract_espcial_html(texto):
        """

       :param texto: string
       :return: texto sem caracteres especiais HTML, caso tenha
       """

        temp = texto
        if '&' in temp:
            anterior = temp[:temp.find('&')]  # parte do texto antes do caractere
            temp = temp[temp.find('&'):]  # texto do caractere para frente
            posterior = temp[temp.find(';') + 1:]  # texto do fim do caractere especial pra frente (fim = ;)

            temp = anterior + posterior

        return temp

    def textos_da_pag(html_text):
        """Pega os textos sem as tags uma documento html

       :param html_text: String
       :return string com (apenas) os textos da pagina
       """
        start, middle, end = '<[^>]*>', '[^>]*', '</[^>]*>'
        regex = start + middle + end  # expressao regualar para pegar tag

        tags = re.findall(regex, html_text)

        text = ''
        for i in tags:
            if len(re.findall('<script[^>]*>' + middle + '</script>', i)) != 0 \
                    or len(re.findall('<style[^>]*>' + middle + '</style>', i)) != 0:  # ignora tag script e style
                continue

            x = re.findall('>[^>]*<', i)
            x[0] = remove_caract_espcial_html(x[0])
            text += ' ' + x[0][1:len(x) - 2].strip()  # remove o '>' e o '<' da string

        return text

    def get_links(html, prioridade=None, max_links=None):
        """

       :param html: objeto BeautifulSoup
       :param prioridade: palavra chave que pode estar em um link, para que eles sejam os primeiros
       :param max_links: limite de links para serem retornados
       :return: lista de links dentro da pagina
       """
        links = []

        all_links = html.find_all('a')

        #  primeiros links são os que possuem prioridade em alguma parte do link
        if prioridade is not None:
            for i in all_links:
                href = str(i)
                if prioridade in href:

                    if 'href="https://' in href:
                        href = href[href.find('href="https://') + len('href="'):]
                        href = href[:href.find('"')]

                        links.append(href)
                        all_links.remove(i)

                    elif 'href="http://' in href:
                        href = href[href.find('href="http://') + len('href="'):]
                        href = href[:href.find('"')]

                        links.append(href)
                        all_links.remove(i)

        for i in all_links:
            href = str(i)
            if 'href="https://' in href:
                href = href[href.find('href="https://') + len('href="'):]
                href = href[:href.find('"')]

                links.append(href)

            elif 'href="http://' in href:
                href = href[href.find('href="http://') + len('href="'):]
                href = href[:href.find('"')]

                links.append(href)

        return links[:max_links] if max_links is not None else links

    class Buscador:
        def __init__(self, url, keyword, max_depth=4, max_links_por_pag=None):
            self.set_url(url)
            self.set_keyword(keyword)
            self.set_max_depth(max_depth)
            self.set_max_links_por_pag(max_links_por_pag)

            self.url_trecho_econtrados = {}
            self.trechos_encontrados = []
            self.urls_encontradas = []

        def set_max_links_por_pag(self, max_links_por_pag):
            self.max_links_por_pag = max_links_por_pag

        def set_keyword(self, keyword):
            self.keyword = keyword

        def set_max_depth(self, max_depth):
            self.max_depth = max_depth

        def set_url(self, url):
            self.url = url

        def get_trechos_econtrados(self):
            return self.trechos_encontrados

        def get_urls_encontradas(self):
            return self.urls_encontradas

        def get_trecho_and_url(self):
            return self.url_trecho_econtrados

        def search(self):
            print('--------------------------- COMEÇA A BUSCA ---------------------------')
            self._search(self.url)
            print('--------------------------- FIM DA BUSCA ---------------------------')

        # private method _
        def _search(self, url, depth=0):

            if depth < self.max_depth:
                print('\nprofundidade ', depth, url)
                try:
                    response = requests.get(url)
                except:
                    print('Error')
                    return

                print('status code:', response.status_code)

                if response.status_code == 200:
                    html = BeautifulSoup(response.text, 'html5lib')

                    texto = textos_da_pag(response.text).lower()

                    print('Possui keyword:', self.keyword in texto)
                    if self.keyword in texto:
                        find = texto.find(self.keyword)

                        inicio = 0 if find < 20 else find - 20
                        fim = find if find > len(texto) - 20 else find + 20

                        trecho = texto[inicio: fim]
                        print('trecho_encontrado = ', trecho)

                        # add aos atributos da classe: trecho, url, e no dic {url: trecho}
                        if url not in self.urls_encontradas:  # nao permite repeticao de url
                            self.url_trecho_econtrados[url] = trecho
                            self.trechos_encontrados.append(trecho)
                            self.urls_encontradas.append(url)

                            novos_links = get_links(html, self.keyword, self.max_links_por_pag)
                            for link in novos_links:
                                self._search(link, depth + 1)

    url2 = 'https://www.ojogos.com.br/'
    x = Buscador(url=url2, keyword='jogos', max_depth=4, max_links_por_pag=5)
    x.search()

    for link in x.get_trecho_and_url().keys():
        print(x.url_trecho_econtrados[link], link)


if __name__ == '__main__':
    main()
