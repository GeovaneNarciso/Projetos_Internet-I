def main():

    import requests
    from lxml import html

    response = requests.get(input("Informe a url (http://google.com): \n"))
    url = response.url
    webpage = html.fromstring(response.content)

    links_list = webpage.xpath('//a/@href')

    links_txt = ""
    for link in links_list:
        if 'http' in link:
            links_txt += link + '\n'

    nome_arquivo = input("Informe o nome do arquivo: (exemplo.txt) \n\n")
    txt = open(nome_arquivo, "w")
    txt.write(links_txt)


if __name__ == '__main__':
    main()
