from campy.gui.events.timer import pause
from campy.graphics.gimage import GImage
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    # Add the animation loop here!
    graphics = BreakoutGraphics()
    lives = NUM_LIVES
    all_bricks = -1
    hearts = []
    # 生命值的心型圖樣
    for i in range(1, lives+1):
        heart = GImage("heart.png")
        x = graphics.window.width-(heart.width+8)*i
        graphics.window.add(heart, x, graphics.window.height-heart.height-5)
        hearts.append(heart)
    graphics.hearts = hearts
    # 生命值不為0且磚塊數量小於100時，遊戲皆可繼續
    while lives > 0 and all_bricks <= 100:
        pause(FRAME_RATE)
        if graphics.clicked:  # 當clicked是True
            vx = graphics.get_dx()
            vy = graphics.get_dy()
            graphics.ball.move(vx, vy)
            # 設定x的反彈
            if graphics.ball.x <= 0 or graphics.ball.x+graphics.ball.width >= graphics.window.width:
                graphics.set_dx()
            # 設定y的反彈
            if graphics.ball.y <= 0:
                graphics.set_dy()
            # 所有磚塊消失時，即跳出遊戲
            if all_bricks == 100:
                break
            # 設定減少一命的條件
            if graphics.ball.y > graphics.window.height:
                lives -= 1
                heart = graphics.hearts.pop()
                graphics.window.remove(heart)
                graphics.window.add(graphics.ball, graphics.original_x, graphics.original_y)
                graphics.clicked = False  # 失敗時，才可打開開關
            else:
                # 球的四個點
                for i in range(0, graphics.ball.width + 1, graphics.ball.width):
                    vy = graphics.get_dy()
                    for j in range(0, graphics.ball.height + 1, graphics.ball.height):
                        ball_point = graphics.window.get_object_at(graphics.ball.x + i, graphics.ball.y + j)
                        # 判定球是否有撞擊及下一步動作
                        if ball_point is not None and ball_point is not graphics.score_label\
                                and ball_point not in hearts:
                            if ball_point is graphics.paddle:
                                if vy > 0:  # 確保只在向下移動時反彈
                                    graphics.set_dy()
                            else:
                                graphics.set_dy()
                                all_bricks += 1
                                graphics.score_number(ball_point)
                                graphics.window.remove(ball_point)
                            break
    graphics.window.remove(graphics.ball)
    if all_bricks == 100:
        end = GImage("you_win.png")
    else:
        end = GImage("game_over.png")
    graphics.window.add(end, x=(graphics.window.width-end.width)/2, y=graphics.window.height/2)


if __name__ == '__main__':
    main()
