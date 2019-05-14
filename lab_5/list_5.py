import requests
from numpy.random import*

# TASKS (11p)

# 1
# Find another public API with cryptocurrency and compare prices. As an output print:
# "Currently the XXX exchange market is better for buying whilst YYY is better for selling" (3p)

#def compare(exchange_market_1, exchange_market_2):

#    if  (exchange_market_1[] > exchange_market_2[]) and (exchange_market_1[] > exchange_market_2[]):
#        print('the XXX exchange market is better for buying and selling')

#    elif (exchange_market_1[] < exchange_market_2[]) and (exchange_market_1[] < exchange_market_2[]):
#        print('the XXX exchange market is better for buying and selling')

#    elif (exchange_market_1[] < exchange_market_2[]) and (exchange_market_1[] > exchange_market_2[]):
#        print('the XXX exchange market is better for buying but XXX is better for selling')

#    elif (exchange_market_1[] > exchange_market_2[]) and (exchange_market_1[] < exchange_market_2[]):
#        print('the XXX exchange market is better for buying but XXX is better for selling')

def get_BTC():

    response = requests.get('https://www.bitmarket.pl/json/BTCPLN/ticker.json?fbclid=IwAR39SkMxmWtSKK-m3pNmkjKEOeWD69iLISfiO6Y2NaNSfbUD6WdJO45QBAA')
    BTC = response.json()

    return BTC['last']

# 2
# Use https://randomuser.me API to download a random user data.
# Create and store 100 random users with ids, username, name (first + last name) using this API (2p)

def get_users():

    list_of_users = []

    response = requests.get('https://randomuser.me/api/?results=1000')
    data = response.json()

    i = 0
    while len(list_of_users) < 101:

        id = data['results'][i]['id']['value']

        if id != None:

            first = data['results'][i]['name']['first']
            last = data['results'][i]['name']['last']
            username = data['results'][i]['login']['username']
            user = {
                    'name': first.title() + ' ' + last.title(),
                    'username': username,
                    'id': id,
                    'BTC': uniform(1, 10),
                    'PLN': round(uniform(40000, 1000000), 2)
                    }
            list_of_users.append(user)

        i += 1

    return list_of_users

# 3
# Prepare a simulation of transactions between these users
# Take random user and pair him/her with another one. Assume a random amount but take real world price. Sum up the transaction printing:
# username1 exchanged X.XXX BTC with username2 for PLN YYYYY.YYY PLN. (2p)
# Simulate real time - do not proceed all transactions at once. Try to make around 100 transactions per minute (2p)
# Simulate user's assets. Creating a user assign random amount of a given currency. Take it into account while performing a transaction.
# Remember to amend user's assets after the transaction. (2p)

def transfer_of_BTC(buyer_PLN, seller_BTC, price_of_BTC):

    if (buyer_PLN / price_of_BTC) > seller_BTC:
        return uniform(0, int(seller_BTC))

    else:
        return uniform(0, int(buyer_PLN / price_of_BTC))

#number_of_users = int(input('Please enter the number of transactions: '))
number_of_users = 100

list_of_users = get_users()
print('users: ', list_of_users)
print('\nTRANSACTIONS')
for i in range(number_of_users):

    price_of_BTC = get_BTC()

    end = True
    while end != False:

        random_seller = randint(0, number_of_users)
        random_buyer = randint(0, number_of_users)

        if random_buyer != random_seller:
            end = False

    seller_BTC = list_of_users[random_seller]['BTC']
    buyer_PLN = list_of_users[random_buyer]['PLN']

    transfer = transfer_of_BTC(buyer_PLN, seller_BTC, price_of_BTC)
    transaction_cost = round(transfer * price_of_BTC, 2)

    #print(list_of_users[random_seller]['name'], 'exchanged', transfer, 'BTC with', list_of_users[random_buyer]['name'], 'for', transaction_cost, 'PLN')
    print('___________________________________________________________________________________________________________\n',
          'transaction number -', i + 1, '\n',
          list_of_users[random_seller]['name'], 'exchanged', transfer, 'BTC with', list_of_users[random_buyer]['name'], 'for', transaction_cost, 'PLN')

    list_of_users[random_seller]['BTC'] = list_of_users[random_seller]['BTC'] - transfer
    list_of_users[random_seller]['PLN'] = round(list_of_users[random_seller]['PLN'] + transaction_cost, 2)

    list_of_users[random_buyer]['BTC'] = list_of_users[random_buyer]['BTC'] + transfer
    list_of_users[random_buyer]['PLN'] = round(list_of_users[random_buyer]['PLN'] - transaction_cost, 2)