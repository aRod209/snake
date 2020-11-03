"""
An implementation of the classic Snake video game.
Module contains the main game loop and helper methods to
implement the game. Uses a-w-d-s keys to move the snake.
Total points are printed to the console when the game is over.
"""

__author__ = 'Anthony Rodriguez'

import random
import stddraw
import config
from snake import Snake
from apple import Apple

def end_game(snake):
    """ Detects the conditions for the end of the game. """
    snake_headx, snake_heady = snake.get_head()
    snake_body = snake.get_body()
    return (snake_headx, snake_heady) in snake_body \
           or snake_headx >= 20 or snake_headx <= 0 \
           or snake_heady >= 20 or snake_heady <= 0

def is_valid(new_key, old_key):
    """ Returns true if the new direction is valid, false otherwise.

    Keyword arguments:
    new_dir  -- The new direction to turn to (corresponds to  an a-d-w-s key).
    curr_dir -- The current direction the snake is traveling.
    """
    return  new_key == 'a' and old_key != 'd'\
            or new_key == 'w' and old_key != 's'\
            or new_key == 'd' and old_key != 'a'\
            or new_key == 's' and old_key != 'w'

def main():
    # Draw the board
    stddraw.setXscale(0, config.N)
    stddraw.setYscale(0, config.N)
    stddraw.clear(stddraw.BLACK)

    snake = Snake()
    apple = Apple(snake)
    
    key = new_key = old_key = None
    # Main game loop
    while not end_game(snake):
        if stddraw.hasNextKeyTyped():
            new_key = stddraw.nextKeyTyped()
            if is_valid(new_key, old_key):
                key = new_key
                old_key = new_key
        if key:
            snake.move(key, apple)
        stddraw.show(100)

    print('Game Over!')
    print('Total points:', config.PTS)


if __name__=='__main__':
    main()