ch = 3
app = 1
cartapp = 0
cartch = 0
mas = '0 - Exit\n1 - Repeat this message\n2 - Add one apple to cart (apple price is 1$)\n3 - Remove one apple from cart\n4 - Add one chocolate to cart (chocolate price is 3$)\n5 - Remove one chocolate from cart\n6 - Show my cart\n7 - Show checkout information'
print(mas)
while True:
    n = int(input('Please select a number:'))
    if n == 0:
        print('Thanks for visiting our store.')
        break
    elif n == 1:
        print(mas)
    elif n == 2:
        cartapp = cartapp + 1
        print('You have', cartapp, 'apples.')
        print('You have', cartch, 'chocolates')
    elif n == 3:
        if cartapp > 0:
            cartapp = cartapp - 1
            print('You have', cartapp, 'apples.')
            print('You have', cartch, 'chocolates')
        else:
            print("You don't have apples")
    elif n == 4:
        cartch = cartch + 1
        print('You have', cartapp, 'apples.')
        print('You have', cartch, 'chocolates')
    elif n == 5:
        if cartch > 0:
            cartch = cartch - 1
            print('You have', cartapp, 'apples.')
            print('You have', cartch, 'chocolates')
        else:
            print("You don't have chocolates")
    elif n == 6:
        print('You have', cartapp, 'apples.')
        print('You have', cartch, 'chocolates')
    elif n == 7:
        print('You have', cartapp, 'apples.')
        print('You have', cartch, 'chocolates')
        print('\033[1m' + 'BILL')
        print(f' Apple          :{cartapp * app}' + '$')
        print(f' Chocolates     :{cartapp * ch}' + '$')
        print('----------------------')
        print('\033[1m' + 'TOTAL           :' + f'{cartapp * app + cartapp * ch}' + '$')
    elif n > 7:
        print('Incorrect number')





















