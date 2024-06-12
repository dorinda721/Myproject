from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)
        bg = GRect(window_width, window_height)
        bg.filled = True
        bg.fill_color = "snow"
        bg.color = "white"
        self.window.add(bg)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, (window_width-paddle_width) / 2,
                        window_height-paddle_offset-paddle_height)
        self.paddle_off = window_height-paddle_offset-paddle_height
        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius * 2, ball_radius * 2)
        self.ball.filled = True
        self.window.add(self.ball, window_width*0.5 - ball_radius, window_height*0.5 - ball_radius)
        self.original_x = 0.5 * window_width - ball_radius
        self.original_y = 0.5 * window_height - ball_radius
        # Default initial velocity for the ball
        self.__dx = 0  # 初始速度0為靜止動作
        self.__dy = 0
        # Initialize our mouse listeners
        self.clicked = False  # 開始遊戲到結束的開關
        onmousemoved(self.paddle_move)
        onmouseclicked(self.star_ball)
        # Draw bricks
        color = ["brown", "dark orange", "gold", "ForestGreen", "RoyalBlue"]
        for i in range(brick_rows):
            x = (brick_width+brick_spacing)*i
            index = 0  # 決定顏色的數值
            for j in range(brick_cols):
                y = (brick_height + brick_spacing) * j + brick_offset
                self.r_brick = GRect(brick_width, brick_height)
                self.r_brick.filled = True
                self.r_brick.fill_color = color[index % len(color)]  # 避免數值超出有Error
                self.r_brick.color = color[index % len(color)]
                self.window.add(self.r_brick, x, y)
                if j % 2 == 1:  # 決定何時換顏色
                    index += 1
        self.brick_rows = brick_rows
        self.brick_cols = brick_cols
        self.brick_offset = brick_offset
        self.brick_spacing = brick_spacing
        self.score = 0
        self.score_label = GLabel("Score:" + str(self.score))
        self.score_label.font = "-25"
        self.window.add(self.score_label, x=0, y=window_height)

    def set_dx(self):
        self.__dx = -self.__dx

    def set_dy(self):
        self.__dy = -self.__dy

    def get_dx(self):
        return self.__dx

    def get_dy(self):
        return self.__dy

    def paddle_move(self, event):  # 滑鼠與板子的設定
        self.paddle.y = self.paddle_off
        if event.x - self.paddle.width*0.5 < 0:
            self.paddle.x = 0
        elif event.x + self.paddle.width*0.5 > self.window.width:
            self.paddle.x = self.window.width - self.paddle.width
        else:
            self.paddle.x = event.x - self.paddle.width * 0.5

    def star_ball(self, event):
        self.clicked = True  # 開始遊戲後即關閉開關
        if self.ball.x == self.original_x:
            if self.ball.y == self.original_y:
                self.__dx = random.randint(1, MAX_X_SPEED)
                self.__dy = INITIAL_Y_SPEED
                if random.random() > 0.5:
                    self.__dx = -self.__dx

    def score_number(self, event):  # 計算分數
        y = event.y  # 球的y值
        row = (y - self.brick_offset)//(self.r_brick.height+self.brick_spacing)
        if 0 <= row <= 1:
            self.score += 100
        elif 1 < row <= 3:
            self.score += 75
        elif 3 < row <= 5:
            self.score += 50
        elif 5 < row <= 7:
            self.score += 40
        elif 7 < row <= 9:
            self.score += 20
        self.score_label.text = "Score:" + str(self.score)
