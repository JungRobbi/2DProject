from Mario_class import *

map1 = None
map2 = None

WINx = 1024
WINy = 600
movex = 0
movey = 0

def mapmove(mario):
    global WINx
    global WINy
    global moveWinx
    global moveWiny
    global movex
    global movey

    mapmax = -(4222 * 2 + WINx - 15)

    if movex < mapmax:
        movex = mapmax
    if movex > 0:
        movex = 0

    if movex < 0 and mario.x < WINx * 3 / 5 and mario.dir == -1:
        if mario.x + mario.xMAX >= WINx * 3 / 5:
            movex += mario.xspeed
        else:
            movex += mario.xspeed*2
        mario.x += mario.xspeed*2
        if mario.x > WINx * 3 / 5:
            mario.x = WINx * 3 / 5

    if movex > mapmax and mario.x > WINx * 2 / 5 and mario.dir == 1:
        if mario.x - mario.xMAX <= WINx * 2 / 5:
            movex -= mario.xspeed
        else:
            movex -= mario.xspeed*2

        mario.x -= mario.xspeed*2
        if mario.x < WINx * 2 / 5:
            mario.x = WINx * 2 / 5

        # 완료
    moveWinx = movex
    moveWiny = movey

def mapcreate(map):
    global mario, coin, Qblock, brick, skbrick, Steelblock
    global goomba

    if map == 1:
        ground1 = 65
        Qblock.append(object(48 * 12, ground1 + 60 * 2, 100))
        Qblock.append(object(48 * 15, ground1 + 60 * 2, 100))
        Qblock.append(object(48 * 15 + 32, ground1 + 60 * 2, 100))

        coin.append(object(48 * 22, ground1 + 60 * 1, 0))
        coin.append(object(48 * 22 + 32, ground1 + 60 * 1 + 32, 0))
        coin.append(object(48 * 22 + 32 * 2, ground1 + 60 * 1 + 32, 0))

        coin.append(object(48 * 26, ground1 + 60 * 2, 0))
        coin.append(object(48 * 26 + 32, ground1 + 60 * 2 + 32, 0))
        coin.append(object(48 * 26 + 32 * 2, ground1 + 60 * 2 + 32, 0))

        skbrick.append(object(48 * 29, ground1 + 60 * 4, 3))

        brick.append(object(48 * 35, ground1 + 60 * 2, 2))
        skbrick.append(object(48 * 35 + 32, ground1 + 60 * 2, 3))
        brick.append(object(48 * 35 + 32 * 2, ground1 + 60 * 2, 2))
        Qblock.append(object(48 * 35 + 32, ground1 + 60 * 5, 100))

        coin.append(object(48 * 42, ground1 + 60 * 2, 0))
        coin.append(object(48 * 42 + 32, ground1 + 60 * 2 + 32, 0))
        coin.append(object(48 * 42 + 32 * 2, ground1 + 60 * 2 + 32, 0))
        coin.append(object(48 * 42 + 32 * 3, ground1 + 60 * 2, 0))

        coin.append(object(48 * 61, ground1 + 60 * 2, 0))
        coin.append(object(48 * 61 + 32, ground1 + 60 * 2 + 32, 0))
        coin.append(object(48 * 61 + 32 * 2, ground1 + 60 * 2 + 32, 0))
        coin.append(object(48 * 61 + 32 * 3, ground1 + 60 * 2, 0))

        brick.append(object(48 * 75, ground1 + 60 * 2, 2))
        Qblock.append(object(48 * 75 + 32, ground1 + 60 * 2, 100))
        brick.append(object(48 * 75 + 32 * 2, ground1 + 60 * 2, 2))

        Qblock.append(object(48 * 81, ground1 + 60 * 2, 100))
        Qblock.append(object(48 * 81 + 32, ground1 + 60 * 2, 100))

        coin.append(object(48 * 86, ground1 + 60 * 2, 0))
        coin.append(object(48 * 86 + 32, ground1 + 60 * 2 + 32, 0))
        coin.append(object(48 * 86 + 32 * 2, ground1 + 60 * 2 + 32, 0))
        coin.append(object(48 * 86 + 32 * 3, ground1 + 60 * 2, 0))

        coin.append(object(48 * 94, ground1 + 60 * 4, 0))
        coin.append(object(48 * 94 + 32, ground1 + 60 * 4 + 32, 0))
        coin.append(object(48 * 94 + 32 * 2, ground1 + 60 * 4 + 32, 0))
        Qblock.append(object(48 * 94 + 32 * 2, ground1 + 60 * 3, 100))
        Qblock.append(object(48 * 94 + 32 * 3, ground1 + 60 * 3, 101))
        Qblock.append(object(48 * 94 + 32 * 4, ground1 + 60 * 3, 100))
        brick.append(object(48 * 94 + 32 * 5, ground1 + 60 * 3, 2))
        brick.append(object(48 * 94 + 32 * 6, ground1 + 60 * 3, 2))

        brick.append(object(48 * 108 , ground1 + 60 * 2, 2))
        brick.append(object(48 * 108 + 32, ground1 + 60 * 2, 2))
        skbrick.append(object(48 * 108 + 32 * 2, ground1 + 60 * 2, 2))
        Qblock.append(object(48 * 108 + 32 * 3, ground1 + 60 * 2, 100))
        Qblock.append(object(48 * 108 + 32 * 4, ground1 + 60 * 2, 100))
        Qblock.append(object(48 * 108 + 32 * 5, ground1 + 60 * 2, 100))
        Qblock.append(object(48 * 108 + 32 * 6, ground1 + 60 * 2, 100))
        brick.append(object(48 * 108 + 32 * 7, ground1 + 60 * 2, 2))
        brick.append(object(48 * 108 + 32 * 8, ground1 + 60 * 2, 2))

        Qblock.append(object(48 * 108 + 32 * 3, ground1 + 60 * 4 + 32, 100))
        Qblock.append(object(48 * 108 + 32 * 4, ground1 + 60 * 4 + 32, 100))
        Qblock.append(object(48 * 108 + 32 * 5, ground1 + 60 * 4 + 32, 100))

        skbrick.append(object(48 * 125, ground1 + 60 * 2, 2))
        skbrick.append(object(48 * 127, ground1 + 60 * 2, 2))
        skbrick.append(object(48 * 129, ground1 + 60 * 2, 2))

        coin.append(object(48 * 136, ground1 + 60 * 2, 0))
        coin.append(object(48 * 136 + 32, ground1 + 60 * 2 + 32, 0))
        coin.append(object(48 * 136 + 32 * 2, ground1 + 60 * 2 + 32, 0))
        coin.append(object(48 * 136 + 32 * 3, ground1 + 60 * 2, 0))

        Qblock.append(object(48 * 142, ground1 + 60 * 2, 102))

        brick.append(object(48 * 151 - 37, ground1 + 60 + 20 , 2))
        brick.append(object(48 * 151 - 5, ground1 + 60 + 20, 2))
        brick.append(object(48 * 151 + 27, ground1 + 60 + 20 , 2))
        brick.append(object(48 * 151 + 32 * 2 - 5, ground1 + 60 + 20 , 2))

        Qblock.append(object(48 * 156, ground1 + 60 * 4, 100))

        coin.append(object(48 * 162 + 32, ground1 + 60 * 2 + 32, 0))
        coin.append(object(48 * 162 + 32 * 2, ground1 + 60 * 2 + 32, 0))
        coin.append(object(48 * 162 + 32 * 3, ground1 + 60 * 2, 0))

        brick.append(object(48 * 175, ground1 + 60 * 2, 2))
        brick.append(object(48 * 175 + 32, ground1 + 60 * 2, 2))
        brick.append(object(48 * 175 + 32 * 2, ground1 + 60 * 2, 2))
        brick.append(object(48 * 175 + 32 * 3, ground1 + 60 * 2, 2))

        brick.append(object(48 * 189, ground1 + 60 * 2, 2))
        brick.append(object(48 * 189 + 32, ground1 + 60 * 2, 2))
        brick.append(object(48 * 189 + 32 * 2, ground1 + 60 * 2, 2))


        for k in range(8, 1, -1):
            for i in range(0,k):
                Steelblock.append(object(48 * 200 - 32 * i, ground1 + 32 * 8 - 32 * k - 10, 98))


        goomba.append(monster(48 * 10, ground1 - 10, 0))
        item.append(object_item(48 * 3, ground1 - 15, 0))
        item.append(object_item(48 * 4, ground1 - 15, 1))
        item.append(object_item(48 * 5, ground1 - 15, 2))
        item.append(object_item(48 * 6, ground1 - 15, 3))

    elif map == 2:
        mario = hero(50, 60)