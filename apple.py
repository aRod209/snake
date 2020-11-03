import random
import stddraw
import config
from snake import Snake

class  Apple:
    """The apple that the snake is trying to eat."""
    def __init__(self, snake):
        x = random.randint(0,config.N-1) + 0.5
        y = random.randint(0, config.N-1) + 0.5
        self.location = (x,y)
        self.new_location(snake)

    def new_location(self, snake):
        """Creates a new location for an apple after it is eaten.
           Technically, a new apple object is not created. It is the
           same apple object with a new location.
        """
        x,y = self.location
        while self.location in snake.body:
            x = random.randint(0,config.N-1) + .5
            y = random.randint(0,config.N-1) + .5
            self.location = (x,y)
        stddraw.setPenColor(stddraw.RED)
        stddraw.filledSquare(x, y, .5)