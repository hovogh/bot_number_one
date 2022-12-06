chapp = {}
chch = {}


def can_rev_apple(user_id):
    global chapp
    return user_id in chapp and chapp[user_id] > 1

def can_rev_ch(user_id):
    global chch
    return user_id in chch and chch[user_id] > 1


def addapp(user_id):
    global chapp
    if user_id in chapp:
        chapp[user_id] += 1
    else:
        chapp[user_id] = 1
    return chapp[user_id]


def revapp(user_id):
    global chapp
    if user_id in chapp:
        chapp[user_id] -= 1
    else:
        chapp[user_id] = 0
    return chapp[user_id]


def addch(user_id):
    global chch
    if user_id in chch:
        chch[user_id] += 1
    else:
        chch[user_id] = 1
    return chch[user_id]


def revch(user_id):
    global chch
    if user_id in chch:
        chch[user_id] -= 1
    else:
        chapp[user_id] = 0
    return chch[user_id]


def chekapp(user_id):
    global chapp
    return chapp[user_id]

def chekch(user_id):
    global chch
    return chch[user_id]


def dell_chapp(user_id):
    global chapp
    if user_id in chapp:
        chapp[user_id] = 0
        return chapp[user_id]


def dell_chch(user_id):
    global chch
    if user_id in chch:
        chch[user_id] = 0
        return chch[user_id]

def priceapp(user_id):
    global chapp
    if user_id in chapp:
        price_app = chch[user_id] * 1
        return price_app


def pricech(user_id):
    global chch
    if user_id in chch:
        price_ch = chch[user_id] * 3
        return price_ch






