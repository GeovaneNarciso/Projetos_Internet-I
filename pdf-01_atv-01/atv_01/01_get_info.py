def main():

    import requests

    response = requests.get(input("Informe a url (http://exemplo.com): "))

    print("Status: ", response.status_code, "\n")
    print("Headers: ", response.headers['content-type'], "\n")
    print("Content length: ", response.content.__len__(), "\n")
    print("Text: ", response.text.split(), "\n")


if __name__ == '__main__':
    main()
