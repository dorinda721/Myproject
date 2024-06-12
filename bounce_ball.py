from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40


window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE)
time = 0
button = False


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    ball.filled = True
    window.add(ball, START_X, START_Y)
    onmouseclicked(bounce)


def bounce(event):
    global time, button
    if not button and time < 3:  # 確認是否為有效點擊，以及次數是否已達三次
        button = True
        y = 0
        time += 1
        while ball.x < window.width:  # x不超過時就一直執行整個while
            y = GRAVITY + y
            ball.move(VX, y)  # move為會執行的距離
            pause(DELAY)
            if ball.y + ball.height >= window.height and y > 0:  # 當超出範圍的時候即反彈
                ball.y = window.height - ball.height
                y = -y*REDUCE
        window.add(ball, START_X, START_Y)
        button = False

#2


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    global time, button
    ball.filled = True
    window.add(ball, START_X, START_Y)
    onmouseclicked(bounce)
    y = 0
    while time < 3:  # 確認是否為有效點擊，以及次數是否已達三次
        if button:
            if ball.x < window.width:  # x不超過時就一直執行整個while
                y = GRAVITY + y
                ball.move(VX, y)  # move為會執行的距離
                if ball.y + ball.height >= window.height and y > 0:  # 當超出範圍的時候即反彈
                    ball.y = window.height - ball.height
                    y = -y*REDUCE
            else:
                window.add(ball, START_X, START_Y)
                button = False
                time += 1
        pause(DELAY)


def bounce(event):
    global button
    if not button:
        button = True



if __name__ == "__main__":
    main()
