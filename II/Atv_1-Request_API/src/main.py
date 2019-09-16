from service.request_api import RequestApi
from ui.tratamento import *


def main():
    '''api = RequestApi("http://pokeapi.co/api/v2/pokemon/{}".format(input("Informe o nome do Pokémon: ").lower()))
    tratamento_pokemon(api.get())

    api1 = RequestApi("https://catfact.ninja/fact").get()
    api2 = RequestApi("https://translate.yandex.net/api/v1.5/tr.json/translate?key="
                      "trnsl.1.1.20190913T135807Z.678e51de51b8c319.f7611fe5f168e1fd8a17204acedd81911d42c245&text=" +
                      api1['fact']+"&lang=en-pt").get()
    tratamento_cat_fact(api1, api2)'''

    api = RequestApi('https://api.imgflip.com/caption_image')
    tratamento_meme_maker(api.post({"template_id": 8072285, "text0": "Nelson", "text1": "Safado",
                    "username": "*****", "password": "*******"}))


if __name__ == '__main__':
    main()
