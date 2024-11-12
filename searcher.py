import wikipediaapi

def search(user_input):
    wiki_wiki = wikipediaapi.Wikipedia(language='ru', extract_format=wikipediaapi.ExtractFormat.WIKI, 
                                    user_agent='MyWikiBot/1.0 (https://example.com/mywikibot)')

    page = wiki_wiki.page(user_input)


    article_text = page.text
    return article_text