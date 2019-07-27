import requests
from bs4 import BeautifulSoup

def main(): 
    pageScrap('https://developer.wordpress.org/plugins/plugin-basics/') 
    response = requests.get('https://developer.wordpress.org/plugins/') 
    soup = BeautifulSoup(response.text, 'html.parser') 
    urls = soup.find(id='nav_menu-3').find_all('a') 
    numUrls = len(urls)
    f = open('plugin-handbook.html', 'w+')
    f.write('<!DOCTYPE html><html xmlns="http://www.w3.org/1999/xhtml" dir="ltr" lang="en-US">')
    f.write(str(soup.head))
    f.write('<body>')
    i = 0
    for a in urls:
        url = a['href'] 
        f.write(str(pageScrap(url)))
        i = i + 1
        output = "Scrapped " + str(i) + " webpages from " + str(numUrls) + " ..."
        print(output, end="\r")
    f.write('</body></html>')
    f.close()
    print("Done..\n")
    return;


def pageScrap(url):
    "get article content of given url"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    mainContent = soup.find(class_='site-main'); 
    #get rid of some parts we do not need i printed form
    table = mainContent.find(class_='table-of-contents') 
    if(table is not None):
        table.decompose()
    navTrail = mainContent.find(class_='breadcrumb-trail')
    if(navTrail is not None):
        navTrail.decompose()
    tops = mainContent.find_all(class_='toc-jump')
    for top in tops:
        top.decompose()
    nav = mainContent.find(class_='handbook-navigation')
    if(nav is not None):
        nav.decompose() 
    hashes = mainContent.find_all(class_='anchor')
    for hashsign in hashes:
        hashsign.decompose()
    #print(mainContent) 
    return mainContent;


if __name__=="__main__":
    main()
