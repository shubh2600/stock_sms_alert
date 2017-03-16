import requests
from bs4 import BeautifulSoup
from twilio.rest import TwilioRestClient

sen = []
Nifty_50 = []
Stocks = []
Price = []
Change = []
Nif_Stocks = []
Nif_Price = []
Nif_Change = []
Stocks_las = []
Price_las = []
Change_las = []
Nif_Stocks_las = []
Nif_Price_las = []
Nif_Change_las = []


account_sid = "paste_code"
auth_token = "paste_code"
client = TwilioRestClient(account_sid, auth_token)

def start(url):

    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code, "html5lib")




    for post_text in soup.findAll("span", {"id": "S&P BSE sensex_value_tb"}):
        content = post_text.get_text()
        sen.append(content)


    for post_text1 in soup.findAll("span", {"id": "nifty 50_value_tb"}):
        content = post_text1.get_text()
        Nifty_50.append(content)



def topfivesensex(url):
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code, "html5lib")
    # loop through each post and get text



    for post_text in soup.findAll("table", {"class": "stck_tbl MT5 brdtp_gry", "id": "load_1sensex"}):
        for tr in post_text.findAll("tr"):
            for td in tr.findAll("td"):
                for a in td.findAll("a"):
                    content = a.get_text()
                    Stocks.append(content)

            for td in tr.findAll("td",{"class":"rb_gd14 TAR"}) :
                content = td.get_text()
                Price.append(content)

            for td in tr.findAll("td", {"class": "rb_grn14"}):
                for span in td.findAll("span",{"class":"fnt14 grn"}):
                    content = span.get_text()
                    Change.append(content)


def topfivenifty(url):
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code, "html5lib")
    # loop through each post and get text



    for post_text in soup.findAll("table", {"class": "stck_tbl MT5 brdtp_gry", "id": "load_1nifty"}):
        for tr in post_text.findAll("tr"):
            for td in tr.findAll("td"):
                for a in td.findAll("a"):
                    content = a.get_text()
                    Nif_Stocks.append(content)

            for td in tr.findAll("td",{"class":"rb_gd14 TAR"}) :
                content = td.get_text()
                Nif_Price.append(content)

            for td in tr.findAll("td", {"class": "rb_grn14"}):
                for span in td.findAll("span",{"class":"fnt14 grn"}):
                    content = span.get_text()
                    Nif_Change.append(content)

def lastfivesensex(url):
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code, "html5lib")
    # loop through each post and get text



    for post_text in soup.findAll("table", {"class": "stck_tbl MT5 brdtp_gry", "id": "load_2sensex"}):
        for tr in post_text.findAll("tr"):
            for td in tr.findAll("td"):
                for a in td.findAll("a"):
                    content = a.get_text()
                    Stocks_las.append(content)

            for td in tr.findAll("td",{"class":"rb_gd14 TAR"}) :
                content = td.get_text()
                Price_las.append(content)

            for td in tr.findAll("td", {"class": "rb_grn14"}):
                for span in td.findAll("span",{"class":"fnt14 red"}):
                    content = span.get_text()
                    Change_las.append(content)


def lastfivenifty(url):
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code, "html5lib")
    # loop through each post and get text



    for post_text in soup.findAll("table", {"class": "stck_tbl MT5 brdtp_gry", "id": "load_2nifty"}):
        for tr in post_text.findAll("tr"):
            for td in tr.findAll("td"):
                for a in td.findAll("a"):
                    content = a.get_text()
                    Nif_Stocks_las.append(content)

            for td in tr.findAll("td",{"class":"rb_gd14 TAR"}) :
                content = td.get_text()
                Nif_Price_las.append(content)

            for td in tr.findAll("td", {"class": "rb_grn14"}):
                for span in td.findAll("span",{"class":"fnt14 red"}):
                    content = span.get_text()
                    Nif_Change_las.append(content)


start('http://m.moneycontrol.com/stocksmarketsindia/')
topfivesensex('http://m.moneycontrol.com/more_market_movers_action.php')
topfivenifty('http://m.moneycontrol.com/more_market_movers_action.php')
lastfivesensex('http://m.moneycontrol.com/more_market_movers_action.php')
lastfivenifty('http://m.moneycontrol.com/more_market_movers_action.php')
print(Stocks[0],Price[0],Change[0])
print(Nif_Stocks[0],Nif_Price[0],Nif_Change[0])
print(Nif_Stocks_las[0],Nif_Price_las[0],Nif_Change_las[0])
print(Stocks_las[0],Price_las[0],Change_las[0])
text = "S&P BSE sensex= " + str(sen[0]) + " " + "Nifty 50 = " + str(Nifty_50[0]) + "\n" + "Top three Gainers sensex ="+ "\n" + str(Stocks[0]) + " " + str(Price[0]) +" " + str(Change[0]) + "\n" + str(Stocks[1]) + " " + str(Price[1]) + " " + str(Change[1]) + "\n" + str(Stocks[2]) + " " + str(Price[2]) + " " + str(Change[2]) + "\n" + "Top three Gainers Nifty 50 ="+ "\n" + str(Nif_Stocks[0]) + " " + str(Nif_Price[0]) +" " + str(Nif_Change[0]) + "\n" + str(Nif_Stocks[1]) + " " + str(Nif_Price[1]) + " " + str(Nif_Change[1]) + "\n" + str(Nif_Stocks[2]) + " " + str(Nif_Price[2]) + " " + str(Nif_Change[2])
print(text)
client.messages.create(
    to="paste_phno",
    from_="paste_phno",
    body=text,
)