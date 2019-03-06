# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 16:50:17 2019
@author: Jerrica Mulgrew
"""
import csv
import pygame
import ptext
from pygame.locals import *
from pygame import gfxdraw

# FUNCTIONS
def start_instruct(game, w):
    '''start_instruct
    Starts the instruction screen loop. Returns the values for experiment, and t0.
    Any key press will end the loop and start up the exposure period of the experiment.
    '''
    if pygame.KEYDOWN not in [event.type for event in pygame.event.get()]:
        draw_instruct(pygame, w)
    else:
        pygame.event.clear()
        experiment = True
        t0 = pygame.time.get_ticks()/1000
    return experiment, t0

def draw_instruct(game, w, BLACK = (0,0,0), WHITE = (255,255,255)):
    '''draw_instruct
    Draws the instruction screen.
    '''
    instructions = """In this experiment you will listen to a language made up of nonsense words. Please pay attention and listen carefully.\n\nLater in the experiment you will be tested on the words that you have learned.\n\nPress any key to start the experiment."""
    # draw background
    window_surface.fill(BLACK)
    # draw text
    ptext.draw(instructions, centerx = 450, centery = 300, width = w, align = "center", lineheight = 1.5, color = WHITE, fontsize = 24 , sysfontname ="Helvetica")

def start_exp(game, t, t_fin, freq, half_height, dot_space, dot_start):
    '''start_exp
    Starts the main exposure period of the experiment. Currently, experiment will end with any key press or when the animation finishes.
    '''
    if t <= t_fin and pygame.KEYDOWN not in [event.type for event in pygame.event.get()]:
        # calculate change in time/position
        move = int(freq*dot_space*t)
        dot_posn = [(x - move,half_height) for (x,y) in dot_start]

        # draw new animation
        pygame.display.set_caption(f'Dot Animation: {t}')
        draw_bg(pygame)
        draw_dots(pygame,dot_posn)
    else:
        experiment = False
        return experiment

def track_time(game, t, times, dot_posn):
    '''track_time
    Keeps track of the timing of the dots when they cross the fixation point. This will be written out to the .txt logfile eventually.
    '''
    for i in range(num_dots):
        if dot_posn[i][0] <= left_position and times[i] is None:
            times[i] = t
            time_dict[i] = t

def draw_bg(game, w = 900, h = 600, bg = (255,255,255), fg = (0,0,0), line = 4):
    '''draw_bg
    Draws the background of the animation (horizontal and vertical lines, fixation dot).
    This remains the same throughout the exposure period.
    '''
    # draw background
    window_surface.fill(bg)
    # draw lines
    game.draw.line(window_surface, fg,(0,h/2),(w,h/2),line) # horizontal line
    game.draw.line(window_surface, fg,(left_position,0),(left_position,h),line) # vertical line
    # draw fixation dot (always same spot)
    # fg outline
    game.gfxdraw.aacircle(window_surface, left_position, half_height, dot_size, fg)
    game.gfxdraw.filled_circle(window_surface, left_position, half_height, dot_size, fg)
    # bg inner part
    game.gfxdraw.aacircle(window_surface, left_position, half_height, dot_size - line, bg)
    game.gfxdraw.filled_circle(window_surface, left_position, half_height, dot_size - line, bg)

def draw_dots(game, posn, dot_size = 36, cl = (0,0,0)):
    '''draw_dots
    Draws the moving dots.
    '''
    for (x,y) in posn:
        game.gfxdraw.aacircle(window_surface, x, y, dot_size, cl)
        game.gfxdraw.filled_circle(window_surface, x, y, dot_size, cl)

# INTIALIZE VARIABLES
# duration, dot frequency, and frame rate
w,h = 900,600
freq = float(input("Type in the frequency:")) # user defined freq for testing, will be removed later
frame_rate = 45

# audio files
# audio_order = open('audio_stim/audio_stim_order.txt')

# positioning
half_height = int(h/2) # half of the screen height
left_position = 180 # how far the fixation dot should be to the left

# dots
num_dots = 12
dot_space = 180 # space between dots
dot_size = 36 # size of dots

dot_start = [(w+dot_space*i,half_height) for i in range(num_dots)] # starting dot positions
dot_posn = dot_start
times = [None for dot in dot_posn]
time_dict = {}

# animation length
t_fin = (num_dots+w/dot_space)/freq

# SET UP PYGAME
pygame.init()
clock = pygame.time.Clock()
window_surface = pygame.display.set_mode((w,h),pygame.FULLSCREEN)

# MAIN LOOP
t0 = None
experiment = False
while experiment:
    clock.tick(frame_rate)

    # INSTRUCTION SCREEN
    if t0 is None:
        experiment, t0 = start_instruct(game, w)

    # EXPOSURE PERIOD
    elif experiment:
        t = pygame.time.get_ticks()/1000 - t0
        experiment = start_exp(game, t, t_fin, freq, half_height, dot_space, dot_start)

    pygame.display.update()

# write the dot times to csv file
with open('time_list.csv', 'w') as f:
    for key in time_dict.keys():
        f.write("%s,%s\n"%(key,time_dict[key]))

exit()
