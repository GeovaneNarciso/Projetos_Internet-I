def main():

    import requests
    import urllib.request
    import re
    from bs4 import BeautifulSoup

    response = requests.get(input("Informe a url (http://google.com): \n"))
    url = response.url
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, features="lxml")
    urls = soup.findAll('a', attrs={'href': re.compile("^https?://")})

    links_txt = ""
    for tag in urls:
        links_txt += tag['href'] + '\n'

    nome_arquivo = input("Informe o nome do arquivo: (exemplo.txt) \n\n")
    txt = open(nome_arquivo, "w")
    txt.write(links_txt)


if __name__ == '__main__':
    main()
