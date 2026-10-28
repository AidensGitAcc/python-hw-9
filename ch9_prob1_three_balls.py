# Chapter 9, Problem 1 — Three Bouncing Balls (list of balls, based on Ch 7 Problem 4)
# Each ball's graphics object and current bounce height are stored together in a list.

from graphics import *
import time

def main():
    win = GraphWin("Three Bouncing Balls", 600, 600)
    win.setBackground("lightyellow")

    prompt = Text(Point(300, 300), "Release height (m):")
    prompt.draw(win)
    entry = Entry(Point(300, 330), 6)
    entry.draw(win)
    btn = Rectangle(Point(260, 355), Point(340, 380))
    btn.setFill("lightblue")
    btn.draw(win)
    btnLabel = Text(Point(300, 367), "Start")
    btnLabel.draw(win)
    win.getMouse()

    initialHeight = float(entry.getText())

    prompt.undraw()
    entry.undraw()
    btn.undraw()
    btnLabel.undraw()

    win.setCoords(0, 0, 1, initialHeight)

    radius = initialHeight * 0.03
    xPositions = [0.2, 0.5, 0.8]
    colors = ["tomato", "mediumseagreen", "cornflowerblue"]

    balls = []
    i = 0
    while i < 3:
        ball = Circle(Point(xPositions[i], initialHeight), radius)
        ball.setFill(colors[i])
        ball.setOutline("black")
        ball.draw(win)
        balls.append([ball, initialHeight])
        i = i + 1

    anyBouncing = True
    while anyBouncing:
        i = 0
        while i < len(balls):
            ball = balls[i][0]
            dy = radius - ball.getCenter().getY()
            ball.move(0, dy)
            i = i + 1
        time.sleep(0.35)

        anyBouncing = False
        i = 0
        while i < len(balls):
            balls[i][1] = balls[i][1] * 0.6
            ball = balls[i][0]
            dy = balls[i][1] - ball.getCenter().getY()
            ball.move(0, dy)
            if balls[i][1] >= 0.001:
                anyBouncing = True
            i = i + 1
        time.sleep(0.35)

    i = 0
    while i < len(balls):
        ball = balls[i][0]
        dy = radius - ball.getCenter().getY()
        ball.move(0, dy)
        i = i + 1

    done = Text(Point(0.5, initialHeight * 0.9), "Done! Click to exit.")
    done.draw(win)
    win.getMouse()
    win.close()

main()
