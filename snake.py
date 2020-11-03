import random
import stddraw
import config

class Snake:
    """ The snake the player controls. """
    def __init__(self):
        x = random.randint(0,config.N-1) + .5
        y = random.randint(0,config.N-1) + .5
        self.body = [(x,y)]
        stddraw.setPenColor(stddraw.PURPLE)
        stddraw.filledSquare(x, y, .5)

    def move(self, dir, apple):
        """ Changes the direction of the snake.

        Keyword parameters:
        dir   -- That key that will change the direction of the snake (a string).
        apple -- The apple that the snake is trying to eat.
        """
        x, y = self.body[0]
        if dir == 'a':
            self.body.insert(0, (x-1,y))
        elif dir == 'w':
            self.body.insert(0, (x,y+1))
        elif dir == 'd':
            self.body.insert(0, (x+1,y))
        elif dir == 's':
            self.body.insert(0, (x,y-1))

        front = self.body[0]
        stddraw.setPenColor(stddraw.PURPLE)
        stddraw.filledSquare(front[0], front[1], 0.5)

        if front != apple.location:
            back = self.body.pop()
            stddraw.setPenColor(stddraw.BLACK)
            stddraw.filledSquare(back[0], back[1], 0.5)
        else:
            apple.new_location(self)
            config.PTS += 1

    def get_head(self):
        """ Returns the head of the snake. """
        return self.body[0]

    def get_body(self):
        """ Returns the body of the snake (minus the head). """
        return self.body[1:]