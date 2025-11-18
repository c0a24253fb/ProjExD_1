import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img, True, False) #2枚目の背景(反転)
    tmr = 0

    kk_img = pg.image.load("fig/3.png") #こうかとん画像読み込み
    kk_img = pg.transform.flip(kk_img, True, False) #こうかとん左右反転

    kk_rct = kk_img.get_rect() #こうかとんのrect
    kk_rct.center = 300, 200 #こうかとん中心座標

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        x = tmr % 3200 #xは3200ごとにループ
        key_lst = pg.key.get_pressed() #キーの押下状態取得
        if key_lst[pg.K_UP]: #上キーが押されたら移動
            kk_rct.move_ip((0,-1))
        if key_lst[pg.K_DOWN]: #下キーが押されたら移動
            kk_rct.move_ip((0,1))
        if key_lst[pg.K_RIGHT]: #右キーが押されたら移動
            kk_rct.move_ip((2,0))
        if key_lst[pg.K_LEFT]: #左キーが押されたら移動
            kk_rct.move_ip((-1,0))

        kk_rct.centerx -= 1

        screen.blit(bg_img, [-x, 0]) #背景画像
        screen.blit(bg_img2, [-x + 1600, 0]) #背景画像2
        screen.blit(bg_img, [-x + 3200, 0]) #背景画像3
        screen.blit(kk_img, kk_rct) #こうかとん
        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()