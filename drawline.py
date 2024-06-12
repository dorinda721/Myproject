from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked
SIZE = 10
window = GWindow()
count = 1
start_x, start_y = 0, 0
circle = GOval(SIZE, SIZE)

def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(draw)


def draw(event):
    global count
    n = count % 2  # 判斷奇偶數點擊
    count += 1
    if n == 1:  # 奇數加一個圓圈
        window.add(circle, event.x - SIZE*0.5, event.y - SIZE*0.5)
    else:
        # 偶數點擊，拿掉原本的奇數圓圈並畫出一直線
        window.remove(circle)
        line = GLine(circle.x+SIZE*0.5, circle.y+SIZE*0.5, event.x, event.y)
        window.add(line)


if __name__ == "__main__":
    main()
