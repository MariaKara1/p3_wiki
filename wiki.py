import wikipediaapi
import time

user_agent = "p3_wiki (mkartist528@gmail.com)"
wiki = wikipediaapi.Wikipedia(user_agent, "en")

def fetch_links(page):
    links_list=[]
    links=page.links

    for title in links.keys():
        links_list.append(title)

    return links_list

def wikipedia_game_solver(start_page, target_page):
    links = fetch_links(start_page)
    
    for link in links:
        if wiki.page(link) == target_page:
            print("We have found the page you're looking for!")
        if link != target_page:
            print("")

start_page = wiki.page("Sabrina Carpenter")
target_page = wiki.page("Skims")
wikipedia_game_solver(start_page, target_page)

print(fetch_links(start_page))