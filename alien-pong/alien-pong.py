import pgzrun
import pygame
import sys

ball = Actor('alien')
ball.left = 0
ball.top = 55

leftPaddle = Rect((20, 20), (40, 100))
rightPaddle = Rect((400, 400), (480, 480))

pygame.mouse.set_visible(False)

WIDTH = 800
HEIGHT = 600

PADDLE_VELOCITY = 5
BALL_VELOCITY = 5

BLUE = (0, 0, 255)

ball_x = BALL_VELOCITY
ball_y = BALL_VELOCITY

text_message1 = 'Welcome to my game'
text_message2 = 'more text'

def draw():
    screen.clear()
    ball.draw()
    screen.draw.filled_rect(leftPaddle, BLUE)
    screen.draw.text(text_message1, (100, 50))
    screen.draw.text(text_message2, (400, 50))

def update():
    global ball_x  
    global ball_y

    if keyboard.right:
        pass
    if keyboard.left:
        pass
    if keyboard.down:
        leftPaddle.y += PADDLE_VELOCITY
    if keyboard.up:
        leftPaddle.y -= PADDLE_VELOCITY

    if joysticks[0].get_axis(1) > 0:
        leftPaddle.y += PADDLE_VELOCITY

    if joysticks[0].get_axis(1) < 0:
        leftPaddle.y -= PADDLE_VELOCITY

    ball.x += ball_x
    ball.y += ball_y

    if leftPaddle.colliderect(Rect(ball.topleft, ball.bottomright)):
        ball_x = ball_x * -1
    
    if ball.right > WIDTH:
        ball_x = ball_x * -1
    elif ball.bottom > HEIGHT or ball.top < 0:
        ball_y = ball_y * -1

    if ball.left < 0:
        #normally game over
        ball_x = ball_x * -1

def on_key_down(key):
    global text_message2
    text_message2 = str(key)
    if key == keys.ESCAPE:
        quit()
        sys.exit(1)

def on_joy_button_down(joy, button):
    global text_message1
    text_message = str(button) + ' ' + str(joy)
    
def on_joy_axis_motion(joy, axis, value):
    global text_message1
    global text_message2
    text_message1 = str(joysticks[joy].get_axis(0))
    text_message2 = str(joysticks[joy].get_axis(1))

pgzrun.go()