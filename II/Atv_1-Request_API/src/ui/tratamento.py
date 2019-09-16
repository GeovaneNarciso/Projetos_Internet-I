def tratamento_pokemon(content):
    abilities = content["abilities"]
    name = content["name"]

    print("\nNome:", name)
    print("\nHabilidades: ")
    for ability in abilities:
        print("     ", ability["ability"]["name"])


def tratamento_cat_fact(content1, content2):
    text_en = content1['fact']
    text_pt = content2["text"][0]

    print("\nFacts about Cats:", text_en)
    print("\nFatos sobre gatos:", text_pt)


def tratamento_meme_maker(content):
    link = content["data"]["url"]

    print("Link Meme:", link)
