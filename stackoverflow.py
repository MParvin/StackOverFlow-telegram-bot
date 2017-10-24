import bs4 as bs
import requests
import webbrowser

#values = input('Enter the question or error ')  #Getting the query from the user to proceed further.
values = "python+import+error"

try:
    url = 'https://stackoverflow.com/search?q='+values  #The URL which will get encoded in UTF-8 format and sent.

    resp = requests.get(url).text #A GET request being sent and the Py object is converted into text.
    soup = bs.BeautifulSoup(resp,'lxml')    #Using an external parser 'lxml' for parsing using bs4 instead of the conventional html.parser (internal) and html5lib (external).
    print(soup.title.text)
    URLS = []
    title = []
    upvotes = []    #Respective lists to store the URLs, title and upvotes
    dicts = {}

    for votes in soup.find_all('span',class_='vote-count-post '): #loop used to find all the 'span' tags with class, 'vote-count-post ' from the bs4-obj 'soup' to get the upvotes of all the answers.
        upvotes.append(votes.text)

    for div in soup.find_all('div',class_='question-summary search-result'):    #loop used to find all the 'div' tags with class, 'question-summary search-result' from the bs4-obj 'soup' to get the 'a' tags whose 'href' attribute is used to store in the URL list and and 'title' to store in the title list.
        a = div.find('a')
        URLS.append('https://stackoverflow.com' + a.attrs['href'])
        title.append(a.attrs['title'])

    print(str(len(URLS)) + ' number of hits!') #Shows the total number of results , max = 15

    print('Choice \t Upvotes \t Title of the question')
    for eachHit in range(len(title)):
        print(str(eachHit+1) + '\t' + upvotes[eachHit] + '\t\t' + title[eachHit])
    for eachurl in range(len(URLS)):    #Dictionary to store serial number (choice) against URLs
        dicts[eachurl+1] = URLS[eachurl]

    ch = int(input("Enter the choice "))
    answer = dicts.get(ch)
    webbrowser.open_new(answer)

except Exception as e:
    print(str(e))

