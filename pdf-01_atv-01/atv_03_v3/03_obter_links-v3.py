def main():

    import requests
    import re

    response = requests.get(input("Informe a url (http://google.com): \n"))
    html = requests.get(response.url).text
    urls = re.findall('(?<=href=["\'])https?://.+?(?=["\'])', html)

    links_txt = ""
    for tag in urls:
        links_txt += tag + '\n'

    nome_arquivo = input("Informe o nome do arquivo: (exemplo.txt) \n\n")
    txt = open(nome_arquivo, "w")
    txt.write(links_txt)


if __name__ == '__main__':
    main()
