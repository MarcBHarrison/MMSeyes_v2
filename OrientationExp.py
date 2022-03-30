#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on Tue Mar 29 18:50:09 2022
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

import psychopy
psychopy.useVersion('2021.2.3')


from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, iohub, hardware
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = 'OrientationExp'  # from the Builder filename that created this script
expInfo = {'participant': '', 'age': '', 'biological sex assigned at birth': '', 'eyetracking': '1'}
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/marcharrison/Desktop/verPy/OrientationExp.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.DEBUG)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1440, 900], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='Screen2', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='norm')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Setup eyetracking
ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Welcome_Screen"
Welcome_ScreenClock = core.Clock()
textWelcomeMessage = visual.TextStim(win=win, name='textWelcomeMessage',
    text='Welcome to the experiment !!!\n\nYou are about to see a series of rooms containing a target object. Each room presentation will be preceded by the presentation of a word or phrase representing the target object. \n\nEach time a room is presented, locate the target object in the room and press SPACEBAR when you have found it.\n\nIf the target word is “none,” withhold your response for that trial.\n\nKeep your eyes on the cross symbol (+) that appears on the screen between trials\n\nIf you understand the instructions and are ready to start the task, Press RETURN.\n\n',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
keyWelcome = keyboard.Keyboard()
win.mouseVisible = False

# Initialize components for Routine "trial"
trialClock = core.Clock()
FX_start = visual.TextStim(win=win, name='FX_start',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
text_preWord = visual.TextStim(win=win, name='text_preWord',
    text='',
    font='Open Sans',
    pos=(0,0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
FX = visual.TextStim(win=win, name='FX',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
imageRoom = visual.ImageStim(
    win=win,
    name='imageRoom', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(2,2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
key_resp_RTencode = keyboard.Keyboard()

# Initialize components for Routine "Continue_Screen"
Continue_ScreenClock = core.Clock()
Continue_text1 = visual.TextStim(win=win, name='Continue_text1',
    text='You are about to see a series of rooms containing a target object. Each room presentation will be preceded by the presentation of a word or phrase representing the target object. \n\nEach time a room is presented, locate the target object in the room and press SPACEBAR when you have found it.\n\nIf the target word is “none,” withhold your response for that trial.\n\nKeep your eyes on the cross symbol (+) that appears on the screen between trials\n\nOnce you are ready to start the task, Press RETURN.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "trial"
trialClock = core.Clock()
FX_start = visual.TextStim(win=win, name='FX_start',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
text_preWord = visual.TextStim(win=win, name='text_preWord',
    text='',
    font='Open Sans',
    pos=(0,0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
FX = visual.TextStim(win=win, name='FX',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
imageRoom = visual.ImageStim(
    win=win,
    name='imageRoom', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(2,2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
key_resp_RTencode = keyboard.Keyboard()

# Initialize components for Routine "Continue_Screen"
Continue_ScreenClock = core.Clock()
Continue_text1 = visual.TextStim(win=win, name='Continue_text1',
    text='You are about to see a series of rooms containing a target object. Each room presentation will be preceded by the presentation of a word or phrase representing the target object. \n\nEach time a room is presented, locate the target object in the room and press SPACEBAR when you have found it.\n\nIf the target word is “none,” withhold your response for that trial.\n\nKeep your eyes on the cross symbol (+) that appears on the screen between trials\n\nOnce you are ready to start the task, Press RETURN.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "trial"
trialClock = core.Clock()
FX_start = visual.TextStim(win=win, name='FX_start',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
text_preWord = visual.TextStim(win=win, name='text_preWord',
    text='',
    font='Open Sans',
    pos=(0,0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
FX = visual.TextStim(win=win, name='FX',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
imageRoom = visual.ImageStim(
    win=win,
    name='imageRoom', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(2,2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
key_resp_RTencode = keyboard.Keyboard()

# Initialize components for Routine "Continue_Screen"
Continue_ScreenClock = core.Clock()
Continue_text1 = visual.TextStim(win=win, name='Continue_text1',
    text='You are about to see a series of rooms containing a target object. Each room presentation will be preceded by the presentation of a word or phrase representing the target object. \n\nEach time a room is presented, locate the target object in the room and press SPACEBAR when you have found it.\n\nIf the target word is “none,” withhold your response for that trial.\n\nKeep your eyes on the cross symbol (+) that appears on the screen between trials\n\nOnce you are ready to start the task, Press RETURN.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "trial"
trialClock = core.Clock()
FX_start = visual.TextStim(win=win, name='FX_start',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
text_preWord = visual.TextStim(win=win, name='text_preWord',
    text='',
    font='Open Sans',
    pos=(0,0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
FX = visual.TextStim(win=win, name='FX',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
imageRoom = visual.ImageStim(
    win=win,
    name='imageRoom', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(2,2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
key_resp_RTencode = keyboard.Keyboard()

# Initialize components for Routine "Continue_Screen"
Continue_ScreenClock = core.Clock()
Continue_text1 = visual.TextStim(win=win, name='Continue_text1',
    text='You are about to see a series of rooms containing a target object. Each room presentation will be preceded by the presentation of a word or phrase representing the target object. \n\nEach time a room is presented, locate the target object in the room and press SPACEBAR when you have found it.\n\nIf the target word is “none,” withhold your response for that trial.\n\nKeep your eyes on the cross symbol (+) that appears on the screen between trials\n\nOnce you are ready to start the task, Press RETURN.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "trial"
trialClock = core.Clock()
FX_start = visual.TextStim(win=win, name='FX_start',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
text_preWord = visual.TextStim(win=win, name='text_preWord',
    text='',
    font='Open Sans',
    pos=(0,0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
FX = visual.TextStim(win=win, name='FX',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
imageRoom = visual.ImageStim(
    win=win,
    name='imageRoom', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(2,2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
key_resp_RTencode = keyboard.Keyboard()

# Initialize components for Routine "Continue_Screen"
Continue_ScreenClock = core.Clock()
Continue_text1 = visual.TextStim(win=win, name='Continue_text1',
    text='You are about to see a series of rooms containing a target object. Each room presentation will be preceded by the presentation of a word or phrase representing the target object. \n\nEach time a room is presented, locate the target object in the room and press SPACEBAR when you have found it.\n\nIf the target word is “none,” withhold your response for that trial.\n\nKeep your eyes on the cross symbol (+) that appears on the screen between trials\n\nOnce you are ready to start the task, Press RETURN.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "trial"
trialClock = core.Clock()
FX_start = visual.TextStim(win=win, name='FX_start',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
text_preWord = visual.TextStim(win=win, name='text_preWord',
    text='',
    font='Open Sans',
    pos=(0,0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
FX = visual.TextStim(win=win, name='FX',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
imageRoom = visual.ImageStim(
    win=win,
    name='imageRoom', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(2,2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
key_resp_RTencode = keyboard.Keyboard()

# Initialize components for Routine "Math_instructions"
Math_instructionsClock = core.Clock()
EqualInstructions = visual.TextStim(win=win, name='EqualInstructions',
    text='For the next section you will see a series of math statements\n\nFor each trial, press the ’t’ key on the keyborad if the statement is true, press the ‘f’ key is the statement is false\n\nYou must respond to each statement to move to the next trial\n\nWhen you are ready to begin press the ‘RETURN’ key',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_4 = keyboard.Keyboard()

# Initialize components for Routine "Math"
MathClock = core.Clock()
fixcross = visual.TextStim(win=win, name='fixcross',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Equalities = visual.TextStim(win=win, name='Equalities',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
math_Resp = keyboard.Keyboard()

# Initialize components for Routine "Test_instructions_loc"
Test_instructions_locClock = core.Clock()
text_Test_loc = visual.TextStim(win=win, name='text_Test_loc',
    text='For each room, using the mouse, click on where you remember the target object being located\n\nYou must click on a location to move to the next trial\n\nPress the RETURN key to start',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "Trial_TestLocation"
Trial_TestLocationClock = core.Clock()
text_prepare_plus = visual.TextStim(win=win, name='text_prepare_plus',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
image_TestRoom = visual.ImageStim(
    win=win,
    name='image_TestRoom', units='norm', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(2,2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
text_TrialStart = visual.TextStim(win=win, name='text_TrialStart',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='red', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
mouse_location = event.Mouse(win=win)
x, y = [None, None]
mouse_location.mouseClock = core.Clock()

# Initialize components for Routine "Test_instructions_loc"
Test_instructions_locClock = core.Clock()
text_Test_loc = visual.TextStim(win=win, name='text_Test_loc',
    text='For each room, using the mouse, click on where you remember the target object being located\n\nYou must click on a location to move to the next trial\n\nPress the RETURN key to start',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "Trial_TestLocation"
Trial_TestLocationClock = core.Clock()
text_prepare_plus = visual.TextStim(win=win, name='text_prepare_plus',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
image_TestRoom = visual.ImageStim(
    win=win,
    name='image_TestRoom', units='norm', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(2,2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
text_TrialStart = visual.TextStim(win=win, name='text_TrialStart',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='red', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
mouse_location = event.Mouse(win=win)
x, y = [None, None]
mouse_location.mouseClock = core.Clock()

# Initialize components for Routine "Test_instructions_obj"
Test_instructions_objClock = core.Clock()
text_Test_obj = visual.TextStim(win=win, name='text_Test_obj',
    text='After seeing each room, give your best response to question. \n\nWhen completed press the mouse clicker to move to the next trial\n\nPress the RETURN key to start',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_3 = keyboard.Keyboard()

# Initialize components for Routine "ObjMem_text"
ObjMem_textClock = core.Clock()
text_1500ms = visual.TextStim(win=win, name='text_1500ms',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
image_ObjMem = visual.ImageStim(
    win=win,
    name='image_ObjMem', units='norm', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(2,2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
text_2 = visual.TextStim(win=win, name='text_2',
    text='What was the target object associated with this room?\n\nType your response below\n\nWhen finished, use the left mouse clicker to begin the next trial',
    font='Open Sans',
    pos=(0, .3), height=0.05, wrapWidth=None, ori=0.0, 
    color='blue', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()
textbox_ObjMemResponse = visual.TextBox2(
     win, text=None, font='Open Sans',
     pos=(0, 0),     letterHeight=0.05,
     size=None, borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=True, italic=False,
     lineSpacing=1.0,
     padding=None,
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=True,
     editable=True,
     name='textbox_ObjMemResponse',
     autoLog=True,
)

# Initialize components for Routine "Test_instructions_obj"
Test_instructions_objClock = core.Clock()
text_Test_obj = visual.TextStim(win=win, name='text_Test_obj',
    text='After seeing each room, give your best response to question. \n\nWhen completed press the mouse clicker to move to the next trial\n\nPress the RETURN key to start',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_3 = keyboard.Keyboard()

# Initialize components for Routine "ObjMem_text"
ObjMem_textClock = core.Clock()
text_1500ms = visual.TextStim(win=win, name='text_1500ms',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
image_ObjMem = visual.ImageStim(
    win=win,
    name='image_ObjMem', units='norm', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(2,2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
text_2 = visual.TextStim(win=win, name='text_2',
    text='What was the target object associated with this room?\n\nType your response below\n\nWhen finished, use the left mouse clicker to begin the next trial',
    font='Open Sans',
    pos=(0, .3), height=0.05, wrapWidth=None, ori=0.0, 
    color='blue', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()
textbox_ObjMemResponse = visual.TextBox2(
     win, text=None, font='Open Sans',
     pos=(0, 0),     letterHeight=0.05,
     size=None, borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=True, italic=False,
     lineSpacing=1.0,
     padding=None,
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=True,
     editable=True,
     name='textbox_ObjMemResponse',
     autoLog=True,
)

# Initialize components for Routine "Goodbye_Screen"
Goodbye_ScreenClock = core.Clock()
textGoodbye = visual.TextStim(win=win, name='textGoodbye',
    text='Thanks for your time!',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Welcome_Screen"-------
continueRoutine = True
# update component parameters for each repeat
keyWelcome.keys = []
keyWelcome.rt = []
_keyWelcome_allKeys = []
win.mouseVisible = False
# keep track of which components have finished
Welcome_ScreenComponents = [textWelcomeMessage, keyWelcome]
for thisComponent in Welcome_ScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Welcome_ScreenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Welcome_Screen"-------
while continueRoutine:
    # get current time
    t = Welcome_ScreenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Welcome_ScreenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textWelcomeMessage* updates
    if textWelcomeMessage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textWelcomeMessage.frameNStart = frameN  # exact frame index
        textWelcomeMessage.tStart = t  # local t and not account for scr refresh
        textWelcomeMessage.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textWelcomeMessage, 'tStartRefresh')  # time at next scr refresh
        textWelcomeMessage.setAutoDraw(True)
    
    # *keyWelcome* updates
    waitOnFlip = False
    if keyWelcome.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        keyWelcome.frameNStart = frameN  # exact frame index
        keyWelcome.tStart = t  # local t and not account for scr refresh
        keyWelcome.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(keyWelcome, 'tStartRefresh')  # time at next scr refresh
        keyWelcome.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(keyWelcome.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(keyWelcome.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if keyWelcome.status == STARTED and not waitOnFlip:
        theseKeys = keyWelcome.getKeys(keyList=['return'], waitRelease=False)
        _keyWelcome_allKeys.extend(theseKeys)
        if len(_keyWelcome_allKeys):
            keyWelcome.keys = _keyWelcome_allKeys[-1].name  # just the last key pressed
            keyWelcome.rt = _keyWelcome_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Welcome_ScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Welcome_Screen"-------
for thisComponent in Welcome_ScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('textWelcomeMessage.started', textWelcomeMessage.tStartRefresh)
thisExp.addData('textWelcomeMessage.stopped', textWelcomeMessage.tStopRefresh)
# check responses
if keyWelcome.keys in ['', [], None]:  # No response was made
    keyWelcome.keys = None
thisExp.addData('keyWelcome.keys',keyWelcome.keys)
if keyWelcome.keys != None:  # we had a response
    thisExp.addData('keyWelcome.rt', keyWelcome.rt)
thisExp.addData('keyWelcome.started', keyWelcome.tStartRefresh)
thisExp.addData('keyWelcome.stopped', keyWelcome.tStopRefresh)
thisExp.nextEntry()
# the Routine "Welcome_Screen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trialsRoom = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Encode_1a.xlsx'),
    seed=None, name='trialsRoom')
thisExp.addLoop(trialsRoom)  # add the loop to the experiment
thisTrialsRoom = trialsRoom.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrialsRoom.rgb)
if thisTrialsRoom != None:
    for paramName in thisTrialsRoom:
        exec('{} = thisTrialsRoom[paramName]'.format(paramName))

for thisTrialsRoom in trialsRoom:
    currentLoop = trialsRoom
    # abbreviate parameter names if possible (e.g. rgb = thisTrialsRoom.rgb)
    if thisTrialsRoom != None:
        for paramName in thisTrialsRoom:
            exec('{} = thisTrialsRoom[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    routineTimer.add(11.500000)
    # update component parameters for each repeat
    text_preWord.setText(word_label)
    imageRoom.setImage(Room_image)
    key_resp_RTencode.keys = []
    key_resp_RTencode.rt = []
    _key_resp_RTencode_allKeys = []
    # keep track of which components have finished
    trialComponents = [FX_start, text_preWord, FX, imageRoom, key_resp_RTencode]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *FX_start* updates
        if FX_start.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            FX_start.frameNStart = frameN  # exact frame index
            FX_start.tStart = t  # local t and not account for scr refresh
            FX_start.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(FX_start, 'tStartRefresh')  # time at next scr refresh
            FX_start.setAutoDraw(True)
        if FX_start.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > FX_start.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                FX_start.tStop = t  # not accounting for scr refresh
                FX_start.frameNStop = frameN  # exact frame index
                win.timeOnFlip(FX_start, 'tStopRefresh')  # time at next scr refresh
                FX_start.setAutoDraw(False)
        
        # *text_preWord* updates
        if text_preWord.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
            # keep track of start time/frame for later
            text_preWord.frameNStart = frameN  # exact frame index
            text_preWord.tStart = t  # local t and not account for scr refresh
            text_preWord.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_preWord, 'tStartRefresh')  # time at next scr refresh
            text_preWord.setAutoDraw(True)
        if text_preWord.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_preWord.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                text_preWord.tStop = t  # not accounting for scr refresh
                text_preWord.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_preWord, 'tStopRefresh')  # time at next scr refresh
                text_preWord.setAutoDraw(False)
        
        # *FX* updates
        if FX.status == NOT_STARTED and tThisFlip >= 3.5-frameTolerance:
            # keep track of start time/frame for later
            FX.frameNStart = frameN  # exact frame index
            FX.tStart = t  # local t and not account for scr refresh
            FX.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(FX, 'tStartRefresh')  # time at next scr refresh
            FX.setAutoDraw(True)
        if FX.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > FX.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                FX.tStop = t  # not accounting for scr refresh
                FX.frameNStop = frameN  # exact frame index
                win.timeOnFlip(FX, 'tStopRefresh')  # time at next scr refresh
                FX.setAutoDraw(False)
        
        # *imageRoom* updates
        if imageRoom.status == NOT_STARTED and tThisFlip >= 5.5-frameTolerance:
            # keep track of start time/frame for later
            imageRoom.frameNStart = frameN  # exact frame index
            imageRoom.tStart = t  # local t and not account for scr refresh
            imageRoom.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageRoom, 'tStartRefresh')  # time at next scr refresh
            imageRoom.setAutoDraw(True)
        if imageRoom.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageRoom.tStartRefresh + 6.0-frameTolerance:
                # keep track of stop time/frame for later
                imageRoom.tStop = t  # not accounting for scr refresh
                imageRoom.frameNStop = frameN  # exact frame index
                win.timeOnFlip(imageRoom, 'tStopRefresh')  # time at next scr refresh
                imageRoom.setAutoDraw(False)
        
        # *key_resp_RTencode* updates
        waitOnFlip = False
        if key_resp_RTencode.status == NOT_STARTED and tThisFlip >= 5.5-frameTolerance:
            # keep track of start time/frame for later
            key_resp_RTencode.frameNStart = frameN  # exact frame index
            key_resp_RTencode.tStart = t  # local t and not account for scr refresh
            key_resp_RTencode.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_RTencode, 'tStartRefresh')  # time at next scr refresh
            key_resp_RTencode.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_RTencode.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_RTencode.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_RTencode.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_RTencode.tStartRefresh + 6.0-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_RTencode.tStop = t  # not accounting for scr refresh
                key_resp_RTencode.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp_RTencode, 'tStopRefresh')  # time at next scr refresh
                key_resp_RTencode.status = FINISHED
        if key_resp_RTencode.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_RTencode.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_RTencode_allKeys.extend(theseKeys)
            if len(_key_resp_RTencode_allKeys):
                key_resp_RTencode.keys = _key_resp_RTencode_allKeys[-1].name  # just the last key pressed
                key_resp_RTencode.rt = _key_resp_RTencode_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trialsRoom.addData('FX_start.started', FX_start.tStartRefresh)
    trialsRoom.addData('FX_start.stopped', FX_start.tStopRefresh)
    trialsRoom.addData('text_preWord.started', text_preWord.tStartRefresh)
    trialsRoom.addData('text_preWord.stopped', text_preWord.tStopRefresh)
    trialsRoom.addData('FX.started', FX.tStartRefresh)
    trialsRoom.addData('FX.stopped', FX.tStopRefresh)
    trialsRoom.addData('imageRoom.started', imageRoom.tStartRefresh)
    trialsRoom.addData('imageRoom.stopped', imageRoom.tStopRefresh)
    # check responses
    if key_resp_RTencode.keys in ['', [], None]:  # No response was made
        key_resp_RTencode.keys = None
    trialsRoom.addData('key_resp_RTencode.keys',key_resp_RTencode.keys)
    if key_resp_RTencode.keys != None:  # we had a response
        trialsRoom.addData('key_resp_RTencode.rt', key_resp_RTencode.rt)
    trialsRoom.addData('key_resp_RTencode.started', key_resp_RTencode.tStartRefresh)
    trialsRoom.addData('key_resp_RTencode.stopped', key_resp_RTencode.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trialsRoom'


# ------Prepare to start Routine "Continue_Screen"-------
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
Continue_ScreenComponents = [Continue_text1, key_resp]
for thisComponent in Continue_ScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Continue_ScreenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Continue_Screen"-------
while continueRoutine:
    # get current time
    t = Continue_ScreenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Continue_ScreenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Continue_text1* updates
    if Continue_text1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Continue_text1.frameNStart = frameN  # exact frame index
        Continue_text1.tStart = t  # local t and not account for scr refresh
        Continue_text1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Continue_text1, 'tStartRefresh')  # time at next scr refresh
        Continue_text1.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['return'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Continue_ScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Continue_Screen"-------
for thisComponent in Continue_ScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Continue_text1.started', Continue_text1.tStartRefresh)
thisExp.addData('Continue_text1.stopped', Continue_text1.tStopRefresh)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.addData('key_resp.started', key_resp.tStartRefresh)
thisExp.addData('key_resp.stopped', key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "Continue_Screen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trialsRoom2 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Encode_1a-2.xlsx'),
    seed=None, name='trialsRoom2')
thisExp.addLoop(trialsRoom2)  # add the loop to the experiment
thisTrialsRoom2 = trialsRoom2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrialsRoom2.rgb)
if thisTrialsRoom2 != None:
    for paramName in thisTrialsRoom2:
        exec('{} = thisTrialsRoom2[paramName]'.format(paramName))

for thisTrialsRoom2 in trialsRoom2:
    currentLoop = trialsRoom2
    # abbreviate parameter names if possible (e.g. rgb = thisTrialsRoom2.rgb)
    if thisTrialsRoom2 != None:
        for paramName in thisTrialsRoom2:
            exec('{} = thisTrialsRoom2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    routineTimer.add(11.500000)
    # update component parameters for each repeat
    text_preWord.setText(word_label)
    imageRoom.setImage(Room_image)
    key_resp_RTencode.keys = []
    key_resp_RTencode.rt = []
    _key_resp_RTencode_allKeys = []
    # keep track of which components have finished
    trialComponents = [FX_start, text_preWord, FX, imageRoom, key_resp_RTencode]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *FX_start* updates
        if FX_start.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            FX_start.frameNStart = frameN  # exact frame index
            FX_start.tStart = t  # local t and not account for scr refresh
            FX_start.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(FX_start, 'tStartRefresh')  # time at next scr refresh
            FX_start.setAutoDraw(True)
        if FX_start.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > FX_start.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                FX_start.tStop = t  # not accounting for scr refresh
                FX_start.frameNStop = frameN  # exact frame index
                win.timeOnFlip(FX_start, 'tStopRefresh')  # time at next scr refresh
                FX_start.setAutoDraw(False)
        
        # *text_preWord* updates
        if text_preWord.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
            # keep track of start time/frame for later
            text_preWord.frameNStart = frameN  # exact frame index
            text_preWord.tStart = t  # local t and not account for scr refresh
            text_preWord.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_preWord, 'tStartRefresh')  # time at next scr refresh
            text_preWord.setAutoDraw(True)
        if text_preWord.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_preWord.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                text_preWord.tStop = t  # not accounting for scr refresh
                text_preWord.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_preWord, 'tStopRefresh')  # time at next scr refresh
                text_preWord.setAutoDraw(False)
        
        # *FX* updates
        if FX.status == NOT_STARTED and tThisFlip >= 3.5-frameTolerance:
            # keep track of start time/frame for later
            FX.frameNStart = frameN  # exact frame index
            FX.tStart = t  # local t and not account for scr refresh
            FX.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(FX, 'tStartRefresh')  # time at next scr refresh
            FX.setAutoDraw(True)
        if FX.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > FX.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                FX.tStop = t  # not accounting for scr refresh
                FX.frameNStop = frameN  # exact frame index
                win.timeOnFlip(FX, 'tStopRefresh')  # time at next scr refresh
                FX.setAutoDraw(False)
        
        # *imageRoom* updates
        if imageRoom.status == NOT_STARTED and tThisFlip >= 5.5-frameTolerance:
            # keep track of start time/frame for later
            imageRoom.frameNStart = frameN  # exact frame index
            imageRoom.tStart = t  # local t and not account for scr refresh
            imageRoom.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageRoom, 'tStartRefresh')  # time at next scr refresh
            imageRoom.setAutoDraw(True)
        if imageRoom.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageRoom.tStartRefresh + 6.0-frameTolerance:
                # keep track of stop time/frame for later
                imageRoom.tStop = t  # not accounting for scr refresh
                imageRoom.frameNStop = frameN  # exact frame index
                win.timeOnFlip(imageRoom, 'tStopRefresh')  # time at next scr refresh
                imageRoom.setAutoDraw(False)
        
        # *key_resp_RTencode* updates
        waitOnFlip = False
        if key_resp_RTencode.status == NOT_STARTED and tThisFlip >= 5.5-frameTolerance:
            # keep track of start time/frame for later
            key_resp_RTencode.frameNStart = frameN  # exact frame index
            key_resp_RTencode.tStart = t  # local t and not account for scr refresh
            key_resp_RTencode.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_RTencode, 'tStartRefresh')  # time at next scr refresh
            key_resp_RTencode.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_RTencode.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_RTencode.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_RTencode.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_RTencode.tStartRefresh + 6.0-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_RTencode.tStop = t  # not accounting for scr refresh
                key_resp_RTencode.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp_RTencode, 'tStopRefresh')  # time at next scr refresh
                key_resp_RTencode.status = FINISHED
        if key_resp_RTencode.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_RTencode.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_RTencode_allKeys.extend(theseKeys)
            if len(_key_resp_RTencode_allKeys):
                key_resp_RTencode.keys = _key_resp_RTencode_allKeys[-1].name  # just the last key pressed
                key_resp_RTencode.rt = _key_resp_RTencode_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trialsRoom2.addData('FX_start.started', FX_start.tStartRefresh)
    trialsRoom2.addData('FX_start.stopped', FX_start.tStopRefresh)
    trialsRoom2.addData('text_preWord.started', text_preWord.tStartRefresh)
    trialsRoom2.addData('text_preWord.stopped', text_preWord.tStopRefresh)
    trialsRoom2.addData('FX.started', FX.tStartRefresh)
    trialsRoom2.addData('FX.stopped', FX.tStopRefresh)
    trialsRoom2.addData('imageRoom.started', imageRoom.tStartRefresh)
    trialsRoom2.addData('imageRoom.stopped', imageRoom.tStopRefresh)
    # check responses
    if key_resp_RTencode.keys in ['', [], None]:  # No response was made
        key_resp_RTencode.keys = None
    trialsRoom2.addData('key_resp_RTencode.keys',key_resp_RTencode.keys)
    if key_resp_RTencode.keys != None:  # we had a response
        trialsRoom2.addData('key_resp_RTencode.rt', key_resp_RTencode.rt)
    trialsRoom2.addData('key_resp_RTencode.started', key_resp_RTencode.tStartRefresh)
    trialsRoom2.addData('key_resp_RTencode.stopped', key_resp_RTencode.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trialsRoom2'


# ------Prepare to start Routine "Continue_Screen"-------
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
Continue_ScreenComponents = [Continue_text1, key_resp]
for thisComponent in Continue_ScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Continue_ScreenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Continue_Screen"-------
while continueRoutine:
    # get current time
    t = Continue_ScreenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Continue_ScreenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Continue_text1* updates
    if Continue_text1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Continue_text1.frameNStart = frameN  # exact frame index
        Continue_text1.tStart = t  # local t and not account for scr refresh
        Continue_text1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Continue_text1, 'tStartRefresh')  # time at next scr refresh
        Continue_text1.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['return'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Continue_ScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Continue_Screen"-------
for thisComponent in Continue_ScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Continue_text1.started', Continue_text1.tStartRefresh)
thisExp.addData('Continue_text1.stopped', Continue_text1.tStopRefresh)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.addData('key_resp.started', key_resp.tStartRefresh)
thisExp.addData('key_resp.stopped', key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "Continue_Screen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trialsRoom3 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Encode_1a-3.xlsx'),
    seed=None, name='trialsRoom3')
thisExp.addLoop(trialsRoom3)  # add the loop to the experiment
thisTrialsRoom3 = trialsRoom3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrialsRoom3.rgb)
if thisTrialsRoom3 != None:
    for paramName in thisTrialsRoom3:
        exec('{} = thisTrialsRoom3[paramName]'.format(paramName))

for thisTrialsRoom3 in trialsRoom3:
    currentLoop = trialsRoom3
    # abbreviate parameter names if possible (e.g. rgb = thisTrialsRoom3.rgb)
    if thisTrialsRoom3 != None:
        for paramName in thisTrialsRoom3:
            exec('{} = thisTrialsRoom3[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    routineTimer.add(11.500000)
    # update component parameters for each repeat
    text_preWord.setText(word_label)
    imageRoom.setImage(Room_image)
    key_resp_RTencode.keys = []
    key_resp_RTencode.rt = []
    _key_resp_RTencode_allKeys = []
    # keep track of which components have finished
    trialComponents = [FX_start, text_preWord, FX, imageRoom, key_resp_RTencode]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *FX_start* updates
        if FX_start.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            FX_start.frameNStart = frameN  # exact frame index
            FX_start.tStart = t  # local t and not account for scr refresh
            FX_start.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(FX_start, 'tStartRefresh')  # time at next scr refresh
            FX_start.setAutoDraw(True)
        if FX_start.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > FX_start.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                FX_start.tStop = t  # not accounting for scr refresh
                FX_start.frameNStop = frameN  # exact frame index
                win.timeOnFlip(FX_start, 'tStopRefresh')  # time at next scr refresh
                FX_start.setAutoDraw(False)
        
        # *text_preWord* updates
        if text_preWord.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
            # keep track of start time/frame for later
            text_preWord.frameNStart = frameN  # exact frame index
            text_preWord.tStart = t  # local t and not account for scr refresh
            text_preWord.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_preWord, 'tStartRefresh')  # time at next scr refresh
            text_preWord.setAutoDraw(True)
        if text_preWord.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_preWord.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                text_preWord.tStop = t  # not accounting for scr refresh
                text_preWord.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_preWord, 'tStopRefresh')  # time at next scr refresh
                text_preWord.setAutoDraw(False)
        
        # *FX* updates
        if FX.status == NOT_STARTED and tThisFlip >= 3.5-frameTolerance:
            # keep track of start time/frame for later
            FX.frameNStart = frameN  # exact frame index
            FX.tStart = t  # local t and not account for scr refresh
            FX.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(FX, 'tStartRefresh')  # time at next scr refresh
            FX.setAutoDraw(True)
        if FX.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > FX.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                FX.tStop = t  # not accounting for scr refresh
                FX.frameNStop = frameN  # exact frame index
                win.timeOnFlip(FX, 'tStopRefresh')  # time at next scr refresh
                FX.setAutoDraw(False)
        
        # *imageRoom* updates
        if imageRoom.status == NOT_STARTED and tThisFlip >= 5.5-frameTolerance:
            # keep track of start time/frame for later
            imageRoom.frameNStart = frameN  # exact frame index
            imageRoom.tStart = t  # local t and not account for scr refresh
            imageRoom.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageRoom, 'tStartRefresh')  # time at next scr refresh
            imageRoom.setAutoDraw(True)
        if imageRoom.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageRoom.tStartRefresh + 6.0-frameTolerance:
                # keep track of stop time/frame for later
                imageRoom.tStop = t  # not accounting for scr refresh
                imageRoom.frameNStop = frameN  # exact frame index
                win.timeOnFlip(imageRoom, 'tStopRefresh')  # time at next scr refresh
                imageRoom.setAutoDraw(False)
        
        # *key_resp_RTencode* updates
        waitOnFlip = False
        if key_resp_RTencode.status == NOT_STARTED and tThisFlip >= 5.5-frameTolerance:
            # keep track of start time/frame for later
            key_resp_RTencode.frameNStart = frameN  # exact frame index
            key_resp_RTencode.tStart = t  # local t and not account for scr refresh
            key_resp_RTencode.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_RTencode, 'tStartRefresh')  # time at next scr refresh
            key_resp_RTencode.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_RTencode.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_RTencode.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_RTencode.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_RTencode.tStartRefresh + 6.0-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_RTencode.tStop = t  # not accounting for scr refresh
                key_resp_RTencode.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp_RTencode, 'tStopRefresh')  # time at next scr refresh
                key_resp_RTencode.status = FINISHED
        if key_resp_RTencode.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_RTencode.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_RTencode_allKeys.extend(theseKeys)
            if len(_key_resp_RTencode_allKeys):
                key_resp_RTencode.keys = _key_resp_RTencode_allKeys[-1].name  # just the last key pressed
                key_resp_RTencode.rt = _key_resp_RTencode_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trialsRoom3.addData('FX_start.started', FX_start.tStartRefresh)
    trialsRoom3.addData('FX_start.stopped', FX_start.tStopRefresh)
    trialsRoom3.addData('text_preWord.started', text_preWord.tStartRefresh)
    trialsRoom3.addData('text_preWord.stopped', text_preWord.tStopRefresh)
    trialsRoom3.addData('FX.started', FX.tStartRefresh)
    trialsRoom3.addData('FX.stopped', FX.tStopRefresh)
    trialsRoom3.addData('imageRoom.started', imageRoom.tStartRefresh)
    trialsRoom3.addData('imageRoom.stopped', imageRoom.tStopRefresh)
    # check responses
    if key_resp_RTencode.keys in ['', [], None]:  # No response was made
        key_resp_RTencode.keys = None
    trialsRoom3.addData('key_resp_RTencode.keys',key_resp_RTencode.keys)
    if key_resp_RTencode.keys != None:  # we had a response
        trialsRoom3.addData('key_resp_RTencode.rt', key_resp_RTencode.rt)
    trialsRoom3.addData('key_resp_RTencode.started', key_resp_RTencode.tStartRefresh)
    trialsRoom3.addData('key_resp_RTencode.stopped', key_resp_RTencode.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trialsRoom3'


# ------Prepare to start Routine "Continue_Screen"-------
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
Continue_ScreenComponents = [Continue_text1, key_resp]
for thisComponent in Continue_ScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Continue_ScreenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Continue_Screen"-------
while continueRoutine:
    # get current time
    t = Continue_ScreenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Continue_ScreenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Continue_text1* updates
    if Continue_text1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Continue_text1.frameNStart = frameN  # exact frame index
        Continue_text1.tStart = t  # local t and not account for scr refresh
        Continue_text1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Continue_text1, 'tStartRefresh')  # time at next scr refresh
        Continue_text1.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['return'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Continue_ScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Continue_Screen"-------
for thisComponent in Continue_ScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Continue_text1.started', Continue_text1.tStartRefresh)
thisExp.addData('Continue_text1.stopped', Continue_text1.tStopRefresh)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.addData('key_resp.started', key_resp.tStartRefresh)
thisExp.addData('key_resp.stopped', key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "Continue_Screen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trialsRoom4 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Encode_1b.xlsx'),
    seed=None, name='trialsRoom4')
thisExp.addLoop(trialsRoom4)  # add the loop to the experiment
thisTrialsRoom4 = trialsRoom4.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrialsRoom4.rgb)
if thisTrialsRoom4 != None:
    for paramName in thisTrialsRoom4:
        exec('{} = thisTrialsRoom4[paramName]'.format(paramName))

for thisTrialsRoom4 in trialsRoom4:
    currentLoop = trialsRoom4
    # abbreviate parameter names if possible (e.g. rgb = thisTrialsRoom4.rgb)
    if thisTrialsRoom4 != None:
        for paramName in thisTrialsRoom4:
            exec('{} = thisTrialsRoom4[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    routineTimer.add(11.500000)
    # update component parameters for each repeat
    text_preWord.setText(word_label)
    imageRoom.setImage(Room_image)
    key_resp_RTencode.keys = []
    key_resp_RTencode.rt = []
    _key_resp_RTencode_allKeys = []
    # keep track of which components have finished
    trialComponents = [FX_start, text_preWord, FX, imageRoom, key_resp_RTencode]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *FX_start* updates
        if FX_start.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            FX_start.frameNStart = frameN  # exact frame index
            FX_start.tStart = t  # local t and not account for scr refresh
            FX_start.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(FX_start, 'tStartRefresh')  # time at next scr refresh
            FX_start.setAutoDraw(True)
        if FX_start.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > FX_start.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                FX_start.tStop = t  # not accounting for scr refresh
                FX_start.frameNStop = frameN  # exact frame index
                win.timeOnFlip(FX_start, 'tStopRefresh')  # time at next scr refresh
                FX_start.setAutoDraw(False)
        
        # *text_preWord* updates
        if text_preWord.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
            # keep track of start time/frame for later
            text_preWord.frameNStart = frameN  # exact frame index
            text_preWord.tStart = t  # local t and not account for scr refresh
            text_preWord.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_preWord, 'tStartRefresh')  # time at next scr refresh
            text_preWord.setAutoDraw(True)
        if text_preWord.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_preWord.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                text_preWord.tStop = t  # not accounting for scr refresh
                text_preWord.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_preWord, 'tStopRefresh')  # time at next scr refresh
                text_preWord.setAutoDraw(False)
        
        # *FX* updates
        if FX.status == NOT_STARTED and tThisFlip >= 3.5-frameTolerance:
            # keep track of start time/frame for later
            FX.frameNStart = frameN  # exact frame index
            FX.tStart = t  # local t and not account for scr refresh
            FX.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(FX, 'tStartRefresh')  # time at next scr refresh
            FX.setAutoDraw(True)
        if FX.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > FX.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                FX.tStop = t  # not accounting for scr refresh
                FX.frameNStop = frameN  # exact frame index
                win.timeOnFlip(FX, 'tStopRefresh')  # time at next scr refresh
                FX.setAutoDraw(False)
        
        # *imageRoom* updates
        if imageRoom.status == NOT_STARTED and tThisFlip >= 5.5-frameTolerance:
            # keep track of start time/frame for later
            imageRoom.frameNStart = frameN  # exact frame index
            imageRoom.tStart = t  # local t and not account for scr refresh
            imageRoom.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageRoom, 'tStartRefresh')  # time at next scr refresh
            imageRoom.setAutoDraw(True)
        if imageRoom.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageRoom.tStartRefresh + 6.0-frameTolerance:
                # keep track of stop time/frame for later
                imageRoom.tStop = t  # not accounting for scr refresh
                imageRoom.frameNStop = frameN  # exact frame index
                win.timeOnFlip(imageRoom, 'tStopRefresh')  # time at next scr refresh
                imageRoom.setAutoDraw(False)
        
        # *key_resp_RTencode* updates
        waitOnFlip = False
        if key_resp_RTencode.status == NOT_STARTED and tThisFlip >= 5.5-frameTolerance:
            # keep track of start time/frame for later
            key_resp_RTencode.frameNStart = frameN  # exact frame index
            key_resp_RTencode.tStart = t  # local t and not account for scr refresh
            key_resp_RTencode.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_RTencode, 'tStartRefresh')  # time at next scr refresh
            key_resp_RTencode.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_RTencode.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_RTencode.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_RTencode.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_RTencode.tStartRefresh + 6.0-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_RTencode.tStop = t  # not accounting for scr refresh
                key_resp_RTencode.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp_RTencode, 'tStopRefresh')  # time at next scr refresh
                key_resp_RTencode.status = FINISHED
        if key_resp_RTencode.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_RTencode.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_RTencode_allKeys.extend(theseKeys)
            if len(_key_resp_RTencode_allKeys):
                key_resp_RTencode.keys = _key_resp_RTencode_allKeys[-1].name  # just the last key pressed
                key_resp_RTencode.rt = _key_resp_RTencode_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trialsRoom4.addData('FX_start.started', FX_start.tStartRefresh)
    trialsRoom4.addData('FX_start.stopped', FX_start.tStopRefresh)
    trialsRoom4.addData('text_preWord.started', text_preWord.tStartRefresh)
    trialsRoom4.addData('text_preWord.stopped', text_preWord.tStopRefresh)
    trialsRoom4.addData('FX.started', FX.tStartRefresh)
    trialsRoom4.addData('FX.stopped', FX.tStopRefresh)
    trialsRoom4.addData('imageRoom.started', imageRoom.tStartRefresh)
    trialsRoom4.addData('imageRoom.stopped', imageRoom.tStopRefresh)
    # check responses
    if key_resp_RTencode.keys in ['', [], None]:  # No response was made
        key_resp_RTencode.keys = None
    trialsRoom4.addData('key_resp_RTencode.keys',key_resp_RTencode.keys)
    if key_resp_RTencode.keys != None:  # we had a response
        trialsRoom4.addData('key_resp_RTencode.rt', key_resp_RTencode.rt)
    trialsRoom4.addData('key_resp_RTencode.started', key_resp_RTencode.tStartRefresh)
    trialsRoom4.addData('key_resp_RTencode.stopped', key_resp_RTencode.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trialsRoom4'


# ------Prepare to start Routine "Continue_Screen"-------
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
Continue_ScreenComponents = [Continue_text1, key_resp]
for thisComponent in Continue_ScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Continue_ScreenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Continue_Screen"-------
while continueRoutine:
    # get current time
    t = Continue_ScreenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Continue_ScreenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Continue_text1* updates
    if Continue_text1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Continue_text1.frameNStart = frameN  # exact frame index
        Continue_text1.tStart = t  # local t and not account for scr refresh
        Continue_text1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Continue_text1, 'tStartRefresh')  # time at next scr refresh
        Continue_text1.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['return'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Continue_ScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Continue_Screen"-------
for thisComponent in Continue_ScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Continue_text1.started', Continue_text1.tStartRefresh)
thisExp.addData('Continue_text1.stopped', Continue_text1.tStopRefresh)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.addData('key_resp.started', key_resp.tStartRefresh)
thisExp.addData('key_resp.stopped', key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "Continue_Screen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trialsRooms5 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Encode_1b-2.xlsx'),
    seed=None, name='trialsRooms5')
thisExp.addLoop(trialsRooms5)  # add the loop to the experiment
thisTrialsRooms5 = trialsRooms5.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrialsRooms5.rgb)
if thisTrialsRooms5 != None:
    for paramName in thisTrialsRooms5:
        exec('{} = thisTrialsRooms5[paramName]'.format(paramName))

for thisTrialsRooms5 in trialsRooms5:
    currentLoop = trialsRooms5
    # abbreviate parameter names if possible (e.g. rgb = thisTrialsRooms5.rgb)
    if thisTrialsRooms5 != None:
        for paramName in thisTrialsRooms5:
            exec('{} = thisTrialsRooms5[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    routineTimer.add(11.500000)
    # update component parameters for each repeat
    text_preWord.setText(word_label)
    imageRoom.setImage(Room_image)
    key_resp_RTencode.keys = []
    key_resp_RTencode.rt = []
    _key_resp_RTencode_allKeys = []
    # keep track of which components have finished
    trialComponents = [FX_start, text_preWord, FX, imageRoom, key_resp_RTencode]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *FX_start* updates
        if FX_start.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            FX_start.frameNStart = frameN  # exact frame index
            FX_start.tStart = t  # local t and not account for scr refresh
            FX_start.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(FX_start, 'tStartRefresh')  # time at next scr refresh
            FX_start.setAutoDraw(True)
        if FX_start.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > FX_start.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                FX_start.tStop = t  # not accounting for scr refresh
                FX_start.frameNStop = frameN  # exact frame index
                win.timeOnFlip(FX_start, 'tStopRefresh')  # time at next scr refresh
                FX_start.setAutoDraw(False)
        
        # *text_preWord* updates
        if text_preWord.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
            # keep track of start time/frame for later
            text_preWord.frameNStart = frameN  # exact frame index
            text_preWord.tStart = t  # local t and not account for scr refresh
            text_preWord.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_preWord, 'tStartRefresh')  # time at next scr refresh
            text_preWord.setAutoDraw(True)
        if text_preWord.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_preWord.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                text_preWord.tStop = t  # not accounting for scr refresh
                text_preWord.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_preWord, 'tStopRefresh')  # time at next scr refresh
                text_preWord.setAutoDraw(False)
        
        # *FX* updates
        if FX.status == NOT_STARTED and tThisFlip >= 3.5-frameTolerance:
            # keep track of start time/frame for later
            FX.frameNStart = frameN  # exact frame index
            FX.tStart = t  # local t and not account for scr refresh
            FX.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(FX, 'tStartRefresh')  # time at next scr refresh
            FX.setAutoDraw(True)
        if FX.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > FX.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                FX.tStop = t  # not accounting for scr refresh
                FX.frameNStop = frameN  # exact frame index
                win.timeOnFlip(FX, 'tStopRefresh')  # time at next scr refresh
                FX.setAutoDraw(False)
        
        # *imageRoom* updates
        if imageRoom.status == NOT_STARTED and tThisFlip >= 5.5-frameTolerance:
            # keep track of start time/frame for later
            imageRoom.frameNStart = frameN  # exact frame index
            imageRoom.tStart = t  # local t and not account for scr refresh
            imageRoom.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageRoom, 'tStartRefresh')  # time at next scr refresh
            imageRoom.setAutoDraw(True)
        if imageRoom.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageRoom.tStartRefresh + 6.0-frameTolerance:
                # keep track of stop time/frame for later
                imageRoom.tStop = t  # not accounting for scr refresh
                imageRoom.frameNStop = frameN  # exact frame index
                win.timeOnFlip(imageRoom, 'tStopRefresh')  # time at next scr refresh
                imageRoom.setAutoDraw(False)
        
        # *key_resp_RTencode* updates
        waitOnFlip = False
        if key_resp_RTencode.status == NOT_STARTED and tThisFlip >= 5.5-frameTolerance:
            # keep track of start time/frame for later
            key_resp_RTencode.frameNStart = frameN  # exact frame index
            key_resp_RTencode.tStart = t  # local t and not account for scr refresh
            key_resp_RTencode.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_RTencode, 'tStartRefresh')  # time at next scr refresh
            key_resp_RTencode.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_RTencode.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_RTencode.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_RTencode.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_RTencode.tStartRefresh + 6.0-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_RTencode.tStop = t  # not accounting for scr refresh
                key_resp_RTencode.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp_RTencode, 'tStopRefresh')  # time at next scr refresh
                key_resp_RTencode.status = FINISHED
        if key_resp_RTencode.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_RTencode.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_RTencode_allKeys.extend(theseKeys)
            if len(_key_resp_RTencode_allKeys):
                key_resp_RTencode.keys = _key_resp_RTencode_allKeys[-1].name  # just the last key pressed
                key_resp_RTencode.rt = _key_resp_RTencode_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trialsRooms5.addData('FX_start.started', FX_start.tStartRefresh)
    trialsRooms5.addData('FX_start.stopped', FX_start.tStopRefresh)
    trialsRooms5.addData('text_preWord.started', text_preWord.tStartRefresh)
    trialsRooms5.addData('text_preWord.stopped', text_preWord.tStopRefresh)
    trialsRooms5.addData('FX.started', FX.tStartRefresh)
    trialsRooms5.addData('FX.stopped', FX.tStopRefresh)
    trialsRooms5.addData('imageRoom.started', imageRoom.tStartRefresh)
    trialsRooms5.addData('imageRoom.stopped', imageRoom.tStopRefresh)
    # check responses
    if key_resp_RTencode.keys in ['', [], None]:  # No response was made
        key_resp_RTencode.keys = None
    trialsRooms5.addData('key_resp_RTencode.keys',key_resp_RTencode.keys)
    if key_resp_RTencode.keys != None:  # we had a response
        trialsRooms5.addData('key_resp_RTencode.rt', key_resp_RTencode.rt)
    trialsRooms5.addData('key_resp_RTencode.started', key_resp_RTencode.tStartRefresh)
    trialsRooms5.addData('key_resp_RTencode.stopped', key_resp_RTencode.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trialsRooms5'


# ------Prepare to start Routine "Continue_Screen"-------
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
Continue_ScreenComponents = [Continue_text1, key_resp]
for thisComponent in Continue_ScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Continue_ScreenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Continue_Screen"-------
while continueRoutine:
    # get current time
    t = Continue_ScreenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Continue_ScreenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Continue_text1* updates
    if Continue_text1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Continue_text1.frameNStart = frameN  # exact frame index
        Continue_text1.tStart = t  # local t and not account for scr refresh
        Continue_text1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Continue_text1, 'tStartRefresh')  # time at next scr refresh
        Continue_text1.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['return'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Continue_ScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Continue_Screen"-------
for thisComponent in Continue_ScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Continue_text1.started', Continue_text1.tStartRefresh)
thisExp.addData('Continue_text1.stopped', Continue_text1.tStopRefresh)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.addData('key_resp.started', key_resp.tStartRefresh)
thisExp.addData('key_resp.stopped', key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "Continue_Screen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trialsRoom6 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Encode_1b-3.xlsx'),
    seed=None, name='trialsRoom6')
thisExp.addLoop(trialsRoom6)  # add the loop to the experiment
thisTrialsRoom6 = trialsRoom6.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrialsRoom6.rgb)
if thisTrialsRoom6 != None:
    for paramName in thisTrialsRoom6:
        exec('{} = thisTrialsRoom6[paramName]'.format(paramName))

for thisTrialsRoom6 in trialsRoom6:
    currentLoop = trialsRoom6
    # abbreviate parameter names if possible (e.g. rgb = thisTrialsRoom6.rgb)
    if thisTrialsRoom6 != None:
        for paramName in thisTrialsRoom6:
            exec('{} = thisTrialsRoom6[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    routineTimer.add(11.500000)
    # update component parameters for each repeat
    text_preWord.setText(word_label)
    imageRoom.setImage(Room_image)
    key_resp_RTencode.keys = []
    key_resp_RTencode.rt = []
    _key_resp_RTencode_allKeys = []
    # keep track of which components have finished
    trialComponents = [FX_start, text_preWord, FX, imageRoom, key_resp_RTencode]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *FX_start* updates
        if FX_start.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            FX_start.frameNStart = frameN  # exact frame index
            FX_start.tStart = t  # local t and not account for scr refresh
            FX_start.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(FX_start, 'tStartRefresh')  # time at next scr refresh
            FX_start.setAutoDraw(True)
        if FX_start.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > FX_start.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                FX_start.tStop = t  # not accounting for scr refresh
                FX_start.frameNStop = frameN  # exact frame index
                win.timeOnFlip(FX_start, 'tStopRefresh')  # time at next scr refresh
                FX_start.setAutoDraw(False)
        
        # *text_preWord* updates
        if text_preWord.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
            # keep track of start time/frame for later
            text_preWord.frameNStart = frameN  # exact frame index
            text_preWord.tStart = t  # local t and not account for scr refresh
            text_preWord.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_preWord, 'tStartRefresh')  # time at next scr refresh
            text_preWord.setAutoDraw(True)
        if text_preWord.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_preWord.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                text_preWord.tStop = t  # not accounting for scr refresh
                text_preWord.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_preWord, 'tStopRefresh')  # time at next scr refresh
                text_preWord.setAutoDraw(False)
        
        # *FX* updates
        if FX.status == NOT_STARTED and tThisFlip >= 3.5-frameTolerance:
            # keep track of start time/frame for later
            FX.frameNStart = frameN  # exact frame index
            FX.tStart = t  # local t and not account for scr refresh
            FX.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(FX, 'tStartRefresh')  # time at next scr refresh
            FX.setAutoDraw(True)
        if FX.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > FX.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                FX.tStop = t  # not accounting for scr refresh
                FX.frameNStop = frameN  # exact frame index
                win.timeOnFlip(FX, 'tStopRefresh')  # time at next scr refresh
                FX.setAutoDraw(False)
        
        # *imageRoom* updates
        if imageRoom.status == NOT_STARTED and tThisFlip >= 5.5-frameTolerance:
            # keep track of start time/frame for later
            imageRoom.frameNStart = frameN  # exact frame index
            imageRoom.tStart = t  # local t and not account for scr refresh
            imageRoom.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageRoom, 'tStartRefresh')  # time at next scr refresh
            imageRoom.setAutoDraw(True)
        if imageRoom.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageRoom.tStartRefresh + 6.0-frameTolerance:
                # keep track of stop time/frame for later
                imageRoom.tStop = t  # not accounting for scr refresh
                imageRoom.frameNStop = frameN  # exact frame index
                win.timeOnFlip(imageRoom, 'tStopRefresh')  # time at next scr refresh
                imageRoom.setAutoDraw(False)
        
        # *key_resp_RTencode* updates
        waitOnFlip = False
        if key_resp_RTencode.status == NOT_STARTED and tThisFlip >= 5.5-frameTolerance:
            # keep track of start time/frame for later
            key_resp_RTencode.frameNStart = frameN  # exact frame index
            key_resp_RTencode.tStart = t  # local t and not account for scr refresh
            key_resp_RTencode.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_RTencode, 'tStartRefresh')  # time at next scr refresh
            key_resp_RTencode.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_RTencode.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_RTencode.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_RTencode.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_RTencode.tStartRefresh + 6.0-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_RTencode.tStop = t  # not accounting for scr refresh
                key_resp_RTencode.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp_RTencode, 'tStopRefresh')  # time at next scr refresh
                key_resp_RTencode.status = FINISHED
        if key_resp_RTencode.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_RTencode.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_RTencode_allKeys.extend(theseKeys)
            if len(_key_resp_RTencode_allKeys):
                key_resp_RTencode.keys = _key_resp_RTencode_allKeys[-1].name  # just the last key pressed
                key_resp_RTencode.rt = _key_resp_RTencode_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trialsRoom6.addData('FX_start.started', FX_start.tStartRefresh)
    trialsRoom6.addData('FX_start.stopped', FX_start.tStopRefresh)
    trialsRoom6.addData('text_preWord.started', text_preWord.tStartRefresh)
    trialsRoom6.addData('text_preWord.stopped', text_preWord.tStopRefresh)
    trialsRoom6.addData('FX.started', FX.tStartRefresh)
    trialsRoom6.addData('FX.stopped', FX.tStopRefresh)
    trialsRoom6.addData('imageRoom.started', imageRoom.tStartRefresh)
    trialsRoom6.addData('imageRoom.stopped', imageRoom.tStopRefresh)
    # check responses
    if key_resp_RTencode.keys in ['', [], None]:  # No response was made
        key_resp_RTencode.keys = None
    trialsRoom6.addData('key_resp_RTencode.keys',key_resp_RTencode.keys)
    if key_resp_RTencode.keys != None:  # we had a response
        trialsRoom6.addData('key_resp_RTencode.rt', key_resp_RTencode.rt)
    trialsRoom6.addData('key_resp_RTencode.started', key_resp_RTencode.tStartRefresh)
    trialsRoom6.addData('key_resp_RTencode.stopped', key_resp_RTencode.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trialsRoom6'


# ------Prepare to start Routine "Math_instructions"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_4.keys = []
key_resp_4.rt = []
_key_resp_4_allKeys = []
# keep track of which components have finished
Math_instructionsComponents = [EqualInstructions, key_resp_4]
for thisComponent in Math_instructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Math_instructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Math_instructions"-------
while continueRoutine:
    # get current time
    t = Math_instructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Math_instructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *EqualInstructions* updates
    if EqualInstructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        EqualInstructions.frameNStart = frameN  # exact frame index
        EqualInstructions.tStart = t  # local t and not account for scr refresh
        EqualInstructions.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(EqualInstructions, 'tStartRefresh')  # time at next scr refresh
        EqualInstructions.setAutoDraw(True)
    
    # *key_resp_4* updates
    waitOnFlip = False
    if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_4.frameNStart = frameN  # exact frame index
        key_resp_4.tStart = t  # local t and not account for scr refresh
        key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_4.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_4.getKeys(keyList=['return'], waitRelease=False)
        _key_resp_4_allKeys.extend(theseKeys)
        if len(_key_resp_4_allKeys):
            key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
            key_resp_4.rt = _key_resp_4_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Math_instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Math_instructions"-------
for thisComponent in Math_instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('EqualInstructions.started', EqualInstructions.tStartRefresh)
thisExp.addData('EqualInstructions.stopped', EqualInstructions.tStopRefresh)
# check responses
if key_resp_4.keys in ['', [], None]:  # No response was made
    key_resp_4.keys = None
thisExp.addData('key_resp_4.keys',key_resp_4.keys)
if key_resp_4.keys != None:  # we had a response
    thisExp.addData('key_resp_4.rt', key_resp_4.rt)
thisExp.addData('key_resp_4.started', key_resp_4.tStartRefresh)
thisExp.addData('key_resp_4.stopped', key_resp_4.tStopRefresh)
thisExp.nextEntry()
# the Routine "Math_instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_math = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('trialsMath.xlsx'),
    seed=None, name='trials_math')
thisExp.addLoop(trials_math)  # add the loop to the experiment
thisTrials_math = trials_math.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials_math.rgb)
if thisTrials_math != None:
    for paramName in thisTrials_math:
        exec('{} = thisTrials_math[paramName]'.format(paramName))

for thisTrials_math in trials_math:
    currentLoop = trials_math
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_math.rgb)
    if thisTrials_math != None:
        for paramName in thisTrials_math:
            exec('{} = thisTrials_math[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Math"-------
    continueRoutine = True
    # update component parameters for each repeat
    Equalities.setText(Math)
    math_Resp.keys = []
    math_Resp.rt = []
    _math_Resp_allKeys = []
    # keep track of which components have finished
    MathComponents = [fixcross, Equalities, math_Resp]
    for thisComponent in MathComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    MathClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Math"-------
    while continueRoutine:
        # get current time
        t = MathClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=MathClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixcross* updates
        if fixcross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixcross.frameNStart = frameN  # exact frame index
            fixcross.tStart = t  # local t and not account for scr refresh
            fixcross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixcross, 'tStartRefresh')  # time at next scr refresh
            fixcross.setAutoDraw(True)
        if fixcross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixcross.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                fixcross.tStop = t  # not accounting for scr refresh
                fixcross.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fixcross, 'tStopRefresh')  # time at next scr refresh
                fixcross.setAutoDraw(False)
        
        # *Equalities* updates
        if Equalities.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
            # keep track of start time/frame for later
            Equalities.frameNStart = frameN  # exact frame index
            Equalities.tStart = t  # local t and not account for scr refresh
            Equalities.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Equalities, 'tStartRefresh')  # time at next scr refresh
            Equalities.setAutoDraw(True)
        
        # *math_Resp* updates
        waitOnFlip = False
        if math_Resp.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
            # keep track of start time/frame for later
            math_Resp.frameNStart = frameN  # exact frame index
            math_Resp.tStart = t  # local t and not account for scr refresh
            math_Resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(math_Resp, 'tStartRefresh')  # time at next scr refresh
            math_Resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(math_Resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(math_Resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if math_Resp.status == STARTED and not waitOnFlip:
            theseKeys = math_Resp.getKeys(keyList=['t', 'f'], waitRelease=False)
            _math_Resp_allKeys.extend(theseKeys)
            if len(_math_Resp_allKeys):
                math_Resp.keys = _math_Resp_allKeys[-1].name  # just the last key pressed
                math_Resp.rt = _math_Resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in MathComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Math"-------
    for thisComponent in MathComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_math.addData('fixcross.started', fixcross.tStartRefresh)
    trials_math.addData('fixcross.stopped', fixcross.tStopRefresh)
    trials_math.addData('Equalities.started', Equalities.tStartRefresh)
    trials_math.addData('Equalities.stopped', Equalities.tStopRefresh)
    # check responses
    if math_Resp.keys in ['', [], None]:  # No response was made
        math_Resp.keys = None
    trials_math.addData('math_Resp.keys',math_Resp.keys)
    if math_Resp.keys != None:  # we had a response
        trials_math.addData('math_Resp.rt', math_Resp.rt)
    trials_math.addData('math_Resp.started', math_Resp.tStartRefresh)
    trials_math.addData('math_Resp.stopped', math_Resp.tStopRefresh)
    # the Routine "Math" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials_math'


# ------Prepare to start Routine "Test_instructions_loc"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# keep track of which components have finished
Test_instructions_locComponents = [text_Test_loc, key_resp_2]
for thisComponent in Test_instructions_locComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Test_instructions_locClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Test_instructions_loc"-------
while continueRoutine:
    # get current time
    t = Test_instructions_locClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Test_instructions_locClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_Test_loc* updates
    if text_Test_loc.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_Test_loc.frameNStart = frameN  # exact frame index
        text_Test_loc.tStart = t  # local t and not account for scr refresh
        text_Test_loc.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_Test_loc, 'tStartRefresh')  # time at next scr refresh
        text_Test_loc.setAutoDraw(True)
    
    # *key_resp_2* updates
    waitOnFlip = False
    if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.tStart = t  # local t and not account for scr refresh
        key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_2.getKeys(keyList=['return'], waitRelease=False)
        _key_resp_2_allKeys.extend(theseKeys)
        if len(_key_resp_2_allKeys):
            key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
            key_resp_2.rt = _key_resp_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Test_instructions_locComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Test_instructions_loc"-------
for thisComponent in Test_instructions_locComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_Test_loc.started', text_Test_loc.tStartRefresh)
thisExp.addData('text_Test_loc.stopped', text_Test_loc.tStopRefresh)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys = None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.addData('key_resp_2.started', key_resp_2.tStartRefresh)
thisExp.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
thisExp.nextEntry()
# the Routine "Test_instructions_loc" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_Test_set1 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Test_1a.xlsx'),
    seed=None, name='trials_Test_set1')
thisExp.addLoop(trials_Test_set1)  # add the loop to the experiment
thisTrials_Test_set1 = trials_Test_set1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials_Test_set1.rgb)
if thisTrials_Test_set1 != None:
    for paramName in thisTrials_Test_set1:
        exec('{} = thisTrials_Test_set1[paramName]'.format(paramName))

for thisTrials_Test_set1 in trials_Test_set1:
    currentLoop = trials_Test_set1
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_Test_set1.rgb)
    if thisTrials_Test_set1 != None:
        for paramName in thisTrials_Test_set1:
            exec('{} = thisTrials_Test_set1[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Trial_TestLocation"-------
    continueRoutine = True
    # update component parameters for each repeat
    image_TestRoom.setImage(Room_image)
    # setup some python lists for storing info about the mouse_location
    mouse_location.x = []
    mouse_location.y = []
    mouse_location.leftButton = []
    mouse_location.midButton = []
    mouse_location.rightButton = []
    mouse_location.time = []
    gotValidClick = False  # until a click is received
    mouse.setPos(newPos=(0,0))
    win.mouseVisible = True
    # keep track of which components have finished
    Trial_TestLocationComponents = [text_prepare_plus, image_TestRoom, text_TrialStart, mouse_location]
    for thisComponent in Trial_TestLocationComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Trial_TestLocationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Trial_TestLocation"-------
    while continueRoutine:
        # get current time
        t = Trial_TestLocationClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Trial_TestLocationClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_prepare_plus* updates
        if text_prepare_plus.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_prepare_plus.frameNStart = frameN  # exact frame index
            text_prepare_plus.tStart = t  # local t and not account for scr refresh
            text_prepare_plus.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_prepare_plus, 'tStartRefresh')  # time at next scr refresh
            text_prepare_plus.setAutoDraw(True)
        if text_prepare_plus.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 3.5-frameTolerance:
                # keep track of stop time/frame for later
                text_prepare_plus.tStop = t  # not accounting for scr refresh
                text_prepare_plus.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_prepare_plus, 'tStopRefresh')  # time at next scr refresh
                text_prepare_plus.setAutoDraw(False)
        
        # *image_TestRoom* updates
        if image_TestRoom.status == NOT_STARTED and tThisFlip >= 3.5-frameTolerance:
            # keep track of start time/frame for later
            image_TestRoom.frameNStart = frameN  # exact frame index
            image_TestRoom.tStart = t  # local t and not account for scr refresh
            image_TestRoom.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_TestRoom, 'tStartRefresh')  # time at next scr refresh
            image_TestRoom.setAutoDraw(True)
        
        # *text_TrialStart* updates
        if text_TrialStart.status == NOT_STARTED and tThisFlip >= 3.5-frameTolerance:
            # keep track of start time/frame for later
            text_TrialStart.frameNStart = frameN  # exact frame index
            text_TrialStart.tStart = t  # local t and not account for scr refresh
            text_TrialStart.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_TrialStart, 'tStartRefresh')  # time at next scr refresh
            text_TrialStart.setAutoDraw(True)
        if text_TrialStart.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_TrialStart.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                text_TrialStart.tStop = t  # not accounting for scr refresh
                text_TrialStart.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_TrialStart, 'tStopRefresh')  # time at next scr refresh
                text_TrialStart.setAutoDraw(False)
        # *mouse_location* updates
        if mouse_location.status == NOT_STARTED and t >= 4.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_location.frameNStart = frameN  # exact frame index
            mouse_location.tStart = t  # local t and not account for scr refresh
            mouse_location.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_location, 'tStartRefresh')  # time at next scr refresh
            mouse_location.status = STARTED
            mouse_location.mouseClock.reset()
            prevButtonState = mouse_location.getPressed()  # if button is down already this ISN'T a new click
        if mouse_location.status == STARTED:  # only update if started and not finished!
            buttons = mouse_location.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    x, y = mouse_location.getPos()
                    mouse_location.x.append(x)
                    mouse_location.y.append(y)
                    buttons = mouse_location.getPressed()
                    mouse_location.leftButton.append(buttons[0])
                    mouse_location.midButton.append(buttons[1])
                    mouse_location.rightButton.append(buttons[2])
                    mouse_location.time.append(mouse_location.mouseClock.getTime())
                    # abort routine on response
                    continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Trial_TestLocationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Trial_TestLocation"-------
    for thisComponent in Trial_TestLocationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_Test_set1.addData('text_prepare_plus.started', text_prepare_plus.tStartRefresh)
    trials_Test_set1.addData('text_prepare_plus.stopped', text_prepare_plus.tStopRefresh)
    trials_Test_set1.addData('image_TestRoom.started', image_TestRoom.tStartRefresh)
    trials_Test_set1.addData('image_TestRoom.stopped', image_TestRoom.tStopRefresh)
    trials_Test_set1.addData('text_TrialStart.started', text_TrialStart.tStartRefresh)
    trials_Test_set1.addData('text_TrialStart.stopped', text_TrialStart.tStopRefresh)
    # store data for trials_Test_set1 (TrialHandler)
    if len(mouse_location.x): trials_Test_set1.addData('mouse_location.x', mouse_location.x[0])
    if len(mouse_location.y): trials_Test_set1.addData('mouse_location.y', mouse_location.y[0])
    if len(mouse_location.leftButton): trials_Test_set1.addData('mouse_location.leftButton', mouse_location.leftButton[0])
    if len(mouse_location.midButton): trials_Test_set1.addData('mouse_location.midButton', mouse_location.midButton[0])
    if len(mouse_location.rightButton): trials_Test_set1.addData('mouse_location.rightButton', mouse_location.rightButton[0])
    if len(mouse_location.time): trials_Test_set1.addData('mouse_location.time', mouse_location.time[0])
    trials_Test_set1.addData('mouse_location.started', mouse_location.tStart)
    trials_Test_set1.addData('mouse_location.stopped', mouse_location.tStop)
    win.mouseVisible = False
    # the Routine "Trial_TestLocation" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials_Test_set1'


# ------Prepare to start Routine "Test_instructions_loc"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# keep track of which components have finished
Test_instructions_locComponents = [text_Test_loc, key_resp_2]
for thisComponent in Test_instructions_locComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Test_instructions_locClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Test_instructions_loc"-------
while continueRoutine:
    # get current time
    t = Test_instructions_locClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Test_instructions_locClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_Test_loc* updates
    if text_Test_loc.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_Test_loc.frameNStart = frameN  # exact frame index
        text_Test_loc.tStart = t  # local t and not account for scr refresh
        text_Test_loc.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_Test_loc, 'tStartRefresh')  # time at next scr refresh
        text_Test_loc.setAutoDraw(True)
    
    # *key_resp_2* updates
    waitOnFlip = False
    if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.tStart = t  # local t and not account for scr refresh
        key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_2.getKeys(keyList=['return'], waitRelease=False)
        _key_resp_2_allKeys.extend(theseKeys)
        if len(_key_resp_2_allKeys):
            key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
            key_resp_2.rt = _key_resp_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Test_instructions_locComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Test_instructions_loc"-------
for thisComponent in Test_instructions_locComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_Test_loc.started', text_Test_loc.tStartRefresh)
thisExp.addData('text_Test_loc.stopped', text_Test_loc.tStopRefresh)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys = None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.addData('key_resp_2.started', key_resp_2.tStartRefresh)
thisExp.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
thisExp.nextEntry()
# the Routine "Test_instructions_loc" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_Test_set2 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Test_1b.xlsx'),
    seed=None, name='trials_Test_set2')
thisExp.addLoop(trials_Test_set2)  # add the loop to the experiment
thisTrials_Test_set2 = trials_Test_set2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials_Test_set2.rgb)
if thisTrials_Test_set2 != None:
    for paramName in thisTrials_Test_set2:
        exec('{} = thisTrials_Test_set2[paramName]'.format(paramName))

for thisTrials_Test_set2 in trials_Test_set2:
    currentLoop = trials_Test_set2
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_Test_set2.rgb)
    if thisTrials_Test_set2 != None:
        for paramName in thisTrials_Test_set2:
            exec('{} = thisTrials_Test_set2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Trial_TestLocation"-------
    continueRoutine = True
    # update component parameters for each repeat
    image_TestRoom.setImage(Room_image)
    # setup some python lists for storing info about the mouse_location
    mouse_location.x = []
    mouse_location.y = []
    mouse_location.leftButton = []
    mouse_location.midButton = []
    mouse_location.rightButton = []
    mouse_location.time = []
    gotValidClick = False  # until a click is received
    mouse.setPos(newPos=(0,0))
    win.mouseVisible = True
    # keep track of which components have finished
    Trial_TestLocationComponents = [text_prepare_plus, image_TestRoom, text_TrialStart, mouse_location]
    for thisComponent in Trial_TestLocationComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Trial_TestLocationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Trial_TestLocation"-------
    while continueRoutine:
        # get current time
        t = Trial_TestLocationClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Trial_TestLocationClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_prepare_plus* updates
        if text_prepare_plus.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_prepare_plus.frameNStart = frameN  # exact frame index
            text_prepare_plus.tStart = t  # local t and not account for scr refresh
            text_prepare_plus.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_prepare_plus, 'tStartRefresh')  # time at next scr refresh
            text_prepare_plus.setAutoDraw(True)
        if text_prepare_plus.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 3.5-frameTolerance:
                # keep track of stop time/frame for later
                text_prepare_plus.tStop = t  # not accounting for scr refresh
                text_prepare_plus.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_prepare_plus, 'tStopRefresh')  # time at next scr refresh
                text_prepare_plus.setAutoDraw(False)
        
        # *image_TestRoom* updates
        if image_TestRoom.status == NOT_STARTED and tThisFlip >= 3.5-frameTolerance:
            # keep track of start time/frame for later
            image_TestRoom.frameNStart = frameN  # exact frame index
            image_TestRoom.tStart = t  # local t and not account for scr refresh
            image_TestRoom.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_TestRoom, 'tStartRefresh')  # time at next scr refresh
            image_TestRoom.setAutoDraw(True)
        
        # *text_TrialStart* updates
        if text_TrialStart.status == NOT_STARTED and tThisFlip >= 3.5-frameTolerance:
            # keep track of start time/frame for later
            text_TrialStart.frameNStart = frameN  # exact frame index
            text_TrialStart.tStart = t  # local t and not account for scr refresh
            text_TrialStart.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_TrialStart, 'tStartRefresh')  # time at next scr refresh
            text_TrialStart.setAutoDraw(True)
        if text_TrialStart.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_TrialStart.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                text_TrialStart.tStop = t  # not accounting for scr refresh
                text_TrialStart.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_TrialStart, 'tStopRefresh')  # time at next scr refresh
                text_TrialStart.setAutoDraw(False)
        # *mouse_location* updates
        if mouse_location.status == NOT_STARTED and t >= 4.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_location.frameNStart = frameN  # exact frame index
            mouse_location.tStart = t  # local t and not account for scr refresh
            mouse_location.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_location, 'tStartRefresh')  # time at next scr refresh
            mouse_location.status = STARTED
            mouse_location.mouseClock.reset()
            prevButtonState = mouse_location.getPressed()  # if button is down already this ISN'T a new click
        if mouse_location.status == STARTED:  # only update if started and not finished!
            buttons = mouse_location.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    x, y = mouse_location.getPos()
                    mouse_location.x.append(x)
                    mouse_location.y.append(y)
                    buttons = mouse_location.getPressed()
                    mouse_location.leftButton.append(buttons[0])
                    mouse_location.midButton.append(buttons[1])
                    mouse_location.rightButton.append(buttons[2])
                    mouse_location.time.append(mouse_location.mouseClock.getTime())
                    # abort routine on response
                    continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Trial_TestLocationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Trial_TestLocation"-------
    for thisComponent in Trial_TestLocationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_Test_set2.addData('text_prepare_plus.started', text_prepare_plus.tStartRefresh)
    trials_Test_set2.addData('text_prepare_plus.stopped', text_prepare_plus.tStopRefresh)
    trials_Test_set2.addData('image_TestRoom.started', image_TestRoom.tStartRefresh)
    trials_Test_set2.addData('image_TestRoom.stopped', image_TestRoom.tStopRefresh)
    trials_Test_set2.addData('text_TrialStart.started', text_TrialStart.tStartRefresh)
    trials_Test_set2.addData('text_TrialStart.stopped', text_TrialStart.tStopRefresh)
    # store data for trials_Test_set2 (TrialHandler)
    if len(mouse_location.x): trials_Test_set2.addData('mouse_location.x', mouse_location.x[0])
    if len(mouse_location.y): trials_Test_set2.addData('mouse_location.y', mouse_location.y[0])
    if len(mouse_location.leftButton): trials_Test_set2.addData('mouse_location.leftButton', mouse_location.leftButton[0])
    if len(mouse_location.midButton): trials_Test_set2.addData('mouse_location.midButton', mouse_location.midButton[0])
    if len(mouse_location.rightButton): trials_Test_set2.addData('mouse_location.rightButton', mouse_location.rightButton[0])
    if len(mouse_location.time): trials_Test_set2.addData('mouse_location.time', mouse_location.time[0])
    trials_Test_set2.addData('mouse_location.started', mouse_location.tStart)
    trials_Test_set2.addData('mouse_location.stopped', mouse_location.tStop)
    win.mouseVisible = False
    # the Routine "Trial_TestLocation" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials_Test_set2'


# ------Prepare to start Routine "Test_instructions_obj"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_3.keys = []
key_resp_3.rt = []
_key_resp_3_allKeys = []
# keep track of which components have finished
Test_instructions_objComponents = [text_Test_obj, key_resp_3]
for thisComponent in Test_instructions_objComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Test_instructions_objClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Test_instructions_obj"-------
while continueRoutine:
    # get current time
    t = Test_instructions_objClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Test_instructions_objClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_Test_obj* updates
    if text_Test_obj.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_Test_obj.frameNStart = frameN  # exact frame index
        text_Test_obj.tStart = t  # local t and not account for scr refresh
        text_Test_obj.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_Test_obj, 'tStartRefresh')  # time at next scr refresh
        text_Test_obj.setAutoDraw(True)
    
    # *key_resp_3* updates
    waitOnFlip = False
    if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.tStart = t  # local t and not account for scr refresh
        key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_3.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_3.getKeys(keyList=['return'], waitRelease=False)
        _key_resp_3_allKeys.extend(theseKeys)
        if len(_key_resp_3_allKeys):
            key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
            key_resp_3.rt = _key_resp_3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Test_instructions_objComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Test_instructions_obj"-------
for thisComponent in Test_instructions_objComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_Test_obj.started', text_Test_obj.tStartRefresh)
thisExp.addData('text_Test_obj.stopped', text_Test_obj.tStopRefresh)
# check responses
if key_resp_3.keys in ['', [], None]:  # No response was made
    key_resp_3.keys = None
thisExp.addData('key_resp_3.keys',key_resp_3.keys)
if key_resp_3.keys != None:  # we had a response
    thisExp.addData('key_resp_3.rt', key_resp_3.rt)
thisExp.addData('key_resp_3.started', key_resp_3.tStartRefresh)
thisExp.addData('key_resp_3.stopped', key_resp_3.tStopRefresh)
thisExp.nextEntry()
# the Routine "Test_instructions_obj" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_TestObj1 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Test_1a.xlsx'),
    seed=None, name='trials_TestObj1')
thisExp.addLoop(trials_TestObj1)  # add the loop to the experiment
thisTrials_TestObj1 = trials_TestObj1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials_TestObj1.rgb)
if thisTrials_TestObj1 != None:
    for paramName in thisTrials_TestObj1:
        exec('{} = thisTrials_TestObj1[paramName]'.format(paramName))

for thisTrials_TestObj1 in trials_TestObj1:
    currentLoop = trials_TestObj1
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_TestObj1.rgb)
    if thisTrials_TestObj1 != None:
        for paramName in thisTrials_TestObj1:
            exec('{} = thisTrials_TestObj1[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "ObjMem_text"-------
    continueRoutine = True
    routineTimer.add(16.000000)
    # update component parameters for each repeat
    image_ObjMem.setImage(Room_image)
    # setup some python lists for storing info about the mouse
    gotValidClick = False  # until a click is received
    textbox_ObjMemResponse.reset()
    textbox_ObjMemResponse.setText('')
    win.mouseVisible = True
    # keep track of which components have finished
    ObjMem_textComponents = [text_1500ms, image_ObjMem, text_2, mouse, textbox_ObjMemResponse]
    for thisComponent in ObjMem_textComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ObjMem_textClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "ObjMem_text"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = ObjMem_textClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ObjMem_textClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_1500ms* updates
        if text_1500ms.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_1500ms.frameNStart = frameN  # exact frame index
            text_1500ms.tStart = t  # local t and not account for scr refresh
            text_1500ms.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_1500ms, 'tStartRefresh')  # time at next scr refresh
            text_1500ms.setAutoDraw(True)
        if text_1500ms.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_1500ms.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                text_1500ms.tStop = t  # not accounting for scr refresh
                text_1500ms.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_1500ms, 'tStopRefresh')  # time at next scr refresh
                text_1500ms.setAutoDraw(False)
        
        # *image_ObjMem* updates
        if image_ObjMem.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
            # keep track of start time/frame for later
            image_ObjMem.frameNStart = frameN  # exact frame index
            image_ObjMem.tStart = t  # local t and not account for scr refresh
            image_ObjMem.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_ObjMem, 'tStartRefresh')  # time at next scr refresh
            image_ObjMem.setAutoDraw(True)
        if image_ObjMem.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 6.0-frameTolerance:
                # keep track of stop time/frame for later
                image_ObjMem.tStop = t  # not accounting for scr refresh
                image_ObjMem.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_ObjMem, 'tStopRefresh')  # time at next scr refresh
                image_ObjMem.setAutoDraw(False)
        
        # *text_2* updates
        if text_2.status == NOT_STARTED and tThisFlip >= 6.0-frameTolerance:
            # keep track of start time/frame for later
            text_2.frameNStart = frameN  # exact frame index
            text_2.tStart = t  # local t and not account for scr refresh
            text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
            text_2.setAutoDraw(True)
        if text_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_2.tStartRefresh + 10.0-frameTolerance:
                # keep track of stop time/frame for later
                text_2.tStop = t  # not accounting for scr refresh
                text_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
                text_2.setAutoDraw(False)
        # *mouse* updates
        if mouse.status == NOT_STARTED and t >= 6.0-frameTolerance:
            # keep track of start time/frame for later
            mouse.frameNStart = frameN  # exact frame index
            mouse.tStart = t  # local t and not account for scr refresh
            mouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
            mouse.status = STARTED
            mouse.mouseClock.reset()
            prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
        if mouse.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mouse.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                mouse.tStop = t  # not accounting for scr refresh
                mouse.frameNStop = frameN  # exact frame index
                win.timeOnFlip(mouse, 'tStopRefresh')  # time at next scr refresh
                mouse.status = FINISHED
        if mouse.status == STARTED:  # only update if started and not finished!
            buttons = mouse.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # abort routine on response
                    continueRoutine = False
        
        # *textbox_ObjMemResponse* updates
        if textbox_ObjMemResponse.status == NOT_STARTED and tThisFlip >= 6.0-frameTolerance:
            # keep track of start time/frame for later
            textbox_ObjMemResponse.frameNStart = frameN  # exact frame index
            textbox_ObjMemResponse.tStart = t  # local t and not account for scr refresh
            textbox_ObjMemResponse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textbox_ObjMemResponse, 'tStartRefresh')  # time at next scr refresh
            textbox_ObjMemResponse.setAutoDraw(True)
        if textbox_ObjMemResponse.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > textbox_ObjMemResponse.tStartRefresh + 10.0-frameTolerance:
                # keep track of stop time/frame for later
                textbox_ObjMemResponse.tStop = t  # not accounting for scr refresh
                textbox_ObjMemResponse.frameNStop = frameN  # exact frame index
                win.timeOnFlip(textbox_ObjMemResponse, 'tStopRefresh')  # time at next scr refresh
                textbox_ObjMemResponse.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ObjMem_textComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ObjMem_text"-------
    for thisComponent in ObjMem_textComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_TestObj1.addData('text_1500ms.started', text_1500ms.tStartRefresh)
    trials_TestObj1.addData('text_1500ms.stopped', text_1500ms.tStopRefresh)
    trials_TestObj1.addData('image_ObjMem.started', image_ObjMem.tStartRefresh)
    trials_TestObj1.addData('image_ObjMem.stopped', image_ObjMem.tStopRefresh)
    trials_TestObj1.addData('text_2.started', text_2.tStartRefresh)
    trials_TestObj1.addData('text_2.stopped', text_2.tStopRefresh)
    # store data for trials_TestObj1 (TrialHandler)
    x, y = mouse.getPos()
    buttons = mouse.getPressed()
    trials_TestObj1.addData('mouse.x', x)
    trials_TestObj1.addData('mouse.y', y)
    trials_TestObj1.addData('mouse.leftButton', buttons[0])
    trials_TestObj1.addData('mouse.midButton', buttons[1])
    trials_TestObj1.addData('mouse.rightButton', buttons[2])
    trials_TestObj1.addData('mouse.started', mouse.tStart)
    trials_TestObj1.addData('mouse.stopped', mouse.tStop)
    trials_TestObj1.addData('textbox_ObjMemResponse.text',textbox_ObjMemResponse.text)
    trials_TestObj1.addData('textbox_ObjMemResponse.started', textbox_ObjMemResponse.tStartRefresh)
    trials_TestObj1.addData('textbox_ObjMemResponse.stopped', textbox_ObjMemResponse.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials_TestObj1'


# ------Prepare to start Routine "Test_instructions_obj"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_3.keys = []
key_resp_3.rt = []
_key_resp_3_allKeys = []
# keep track of which components have finished
Test_instructions_objComponents = [text_Test_obj, key_resp_3]
for thisComponent in Test_instructions_objComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Test_instructions_objClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Test_instructions_obj"-------
while continueRoutine:
    # get current time
    t = Test_instructions_objClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Test_instructions_objClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_Test_obj* updates
    if text_Test_obj.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_Test_obj.frameNStart = frameN  # exact frame index
        text_Test_obj.tStart = t  # local t and not account for scr refresh
        text_Test_obj.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_Test_obj, 'tStartRefresh')  # time at next scr refresh
        text_Test_obj.setAutoDraw(True)
    
    # *key_resp_3* updates
    waitOnFlip = False
    if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.tStart = t  # local t and not account for scr refresh
        key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_3.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_3.getKeys(keyList=['return'], waitRelease=False)
        _key_resp_3_allKeys.extend(theseKeys)
        if len(_key_resp_3_allKeys):
            key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
            key_resp_3.rt = _key_resp_3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Test_instructions_objComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Test_instructions_obj"-------
for thisComponent in Test_instructions_objComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_Test_obj.started', text_Test_obj.tStartRefresh)
thisExp.addData('text_Test_obj.stopped', text_Test_obj.tStopRefresh)
# check responses
if key_resp_3.keys in ['', [], None]:  # No response was made
    key_resp_3.keys = None
thisExp.addData('key_resp_3.keys',key_resp_3.keys)
if key_resp_3.keys != None:  # we had a response
    thisExp.addData('key_resp_3.rt', key_resp_3.rt)
thisExp.addData('key_resp_3.started', key_resp_3.tStartRefresh)
thisExp.addData('key_resp_3.stopped', key_resp_3.tStopRefresh)
thisExp.nextEntry()
# the Routine "Test_instructions_obj" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_TestObj2 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Test_1b.xlsx'),
    seed=None, name='trials_TestObj2')
thisExp.addLoop(trials_TestObj2)  # add the loop to the experiment
thisTrials_TestObj2 = trials_TestObj2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials_TestObj2.rgb)
if thisTrials_TestObj2 != None:
    for paramName in thisTrials_TestObj2:
        exec('{} = thisTrials_TestObj2[paramName]'.format(paramName))

for thisTrials_TestObj2 in trials_TestObj2:
    currentLoop = trials_TestObj2
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_TestObj2.rgb)
    if thisTrials_TestObj2 != None:
        for paramName in thisTrials_TestObj2:
            exec('{} = thisTrials_TestObj2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "ObjMem_text"-------
    continueRoutine = True
    routineTimer.add(16.000000)
    # update component parameters for each repeat
    image_ObjMem.setImage(Room_image)
    # setup some python lists for storing info about the mouse
    gotValidClick = False  # until a click is received
    textbox_ObjMemResponse.reset()
    textbox_ObjMemResponse.setText('')
    win.mouseVisible = True
    # keep track of which components have finished
    ObjMem_textComponents = [text_1500ms, image_ObjMem, text_2, mouse, textbox_ObjMemResponse]
    for thisComponent in ObjMem_textComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ObjMem_textClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "ObjMem_text"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = ObjMem_textClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ObjMem_textClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_1500ms* updates
        if text_1500ms.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_1500ms.frameNStart = frameN  # exact frame index
            text_1500ms.tStart = t  # local t and not account for scr refresh
            text_1500ms.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_1500ms, 'tStartRefresh')  # time at next scr refresh
            text_1500ms.setAutoDraw(True)
        if text_1500ms.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_1500ms.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                text_1500ms.tStop = t  # not accounting for scr refresh
                text_1500ms.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_1500ms, 'tStopRefresh')  # time at next scr refresh
                text_1500ms.setAutoDraw(False)
        
        # *image_ObjMem* updates
        if image_ObjMem.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
            # keep track of start time/frame for later
            image_ObjMem.frameNStart = frameN  # exact frame index
            image_ObjMem.tStart = t  # local t and not account for scr refresh
            image_ObjMem.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_ObjMem, 'tStartRefresh')  # time at next scr refresh
            image_ObjMem.setAutoDraw(True)
        if image_ObjMem.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 6.0-frameTolerance:
                # keep track of stop time/frame for later
                image_ObjMem.tStop = t  # not accounting for scr refresh
                image_ObjMem.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_ObjMem, 'tStopRefresh')  # time at next scr refresh
                image_ObjMem.setAutoDraw(False)
        
        # *text_2* updates
        if text_2.status == NOT_STARTED and tThisFlip >= 6.0-frameTolerance:
            # keep track of start time/frame for later
            text_2.frameNStart = frameN  # exact frame index
            text_2.tStart = t  # local t and not account for scr refresh
            text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
            text_2.setAutoDraw(True)
        if text_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_2.tStartRefresh + 10.0-frameTolerance:
                # keep track of stop time/frame for later
                text_2.tStop = t  # not accounting for scr refresh
                text_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
                text_2.setAutoDraw(False)
        # *mouse* updates
        if mouse.status == NOT_STARTED and t >= 6.0-frameTolerance:
            # keep track of start time/frame for later
            mouse.frameNStart = frameN  # exact frame index
            mouse.tStart = t  # local t and not account for scr refresh
            mouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
            mouse.status = STARTED
            mouse.mouseClock.reset()
            prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
        if mouse.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mouse.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                mouse.tStop = t  # not accounting for scr refresh
                mouse.frameNStop = frameN  # exact frame index
                win.timeOnFlip(mouse, 'tStopRefresh')  # time at next scr refresh
                mouse.status = FINISHED
        if mouse.status == STARTED:  # only update if started and not finished!
            buttons = mouse.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # abort routine on response
                    continueRoutine = False
        
        # *textbox_ObjMemResponse* updates
        if textbox_ObjMemResponse.status == NOT_STARTED and tThisFlip >= 6.0-frameTolerance:
            # keep track of start time/frame for later
            textbox_ObjMemResponse.frameNStart = frameN  # exact frame index
            textbox_ObjMemResponse.tStart = t  # local t and not account for scr refresh
            textbox_ObjMemResponse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textbox_ObjMemResponse, 'tStartRefresh')  # time at next scr refresh
            textbox_ObjMemResponse.setAutoDraw(True)
        if textbox_ObjMemResponse.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > textbox_ObjMemResponse.tStartRefresh + 10.0-frameTolerance:
                # keep track of stop time/frame for later
                textbox_ObjMemResponse.tStop = t  # not accounting for scr refresh
                textbox_ObjMemResponse.frameNStop = frameN  # exact frame index
                win.timeOnFlip(textbox_ObjMemResponse, 'tStopRefresh')  # time at next scr refresh
                textbox_ObjMemResponse.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ObjMem_textComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ObjMem_text"-------
    for thisComponent in ObjMem_textComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_TestObj2.addData('text_1500ms.started', text_1500ms.tStartRefresh)
    trials_TestObj2.addData('text_1500ms.stopped', text_1500ms.tStopRefresh)
    trials_TestObj2.addData('image_ObjMem.started', image_ObjMem.tStartRefresh)
    trials_TestObj2.addData('image_ObjMem.stopped', image_ObjMem.tStopRefresh)
    trials_TestObj2.addData('text_2.started', text_2.tStartRefresh)
    trials_TestObj2.addData('text_2.stopped', text_2.tStopRefresh)
    # store data for trials_TestObj2 (TrialHandler)
    x, y = mouse.getPos()
    buttons = mouse.getPressed()
    trials_TestObj2.addData('mouse.x', x)
    trials_TestObj2.addData('mouse.y', y)
    trials_TestObj2.addData('mouse.leftButton', buttons[0])
    trials_TestObj2.addData('mouse.midButton', buttons[1])
    trials_TestObj2.addData('mouse.rightButton', buttons[2])
    trials_TestObj2.addData('mouse.started', mouse.tStart)
    trials_TestObj2.addData('mouse.stopped', mouse.tStop)
    trials_TestObj2.addData('textbox_ObjMemResponse.text',textbox_ObjMemResponse.text)
    trials_TestObj2.addData('textbox_ObjMemResponse.started', textbox_ObjMemResponse.tStartRefresh)
    trials_TestObj2.addData('textbox_ObjMemResponse.stopped', textbox_ObjMemResponse.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials_TestObj2'


# ------Prepare to start Routine "Goodbye_Screen"-------
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
Goodbye_ScreenComponents = [textGoodbye]
for thisComponent in Goodbye_ScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Goodbye_ScreenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Goodbye_Screen"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Goodbye_ScreenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Goodbye_ScreenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textGoodbye* updates
    if textGoodbye.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textGoodbye.frameNStart = frameN  # exact frame index
        textGoodbye.tStart = t  # local t and not account for scr refresh
        textGoodbye.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textGoodbye, 'tStartRefresh')  # time at next scr refresh
        textGoodbye.setAutoDraw(True)
    if textGoodbye.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > textGoodbye.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            textGoodbye.tStop = t  # not accounting for scr refresh
            textGoodbye.frameNStop = frameN  # exact frame index
            win.timeOnFlip(textGoodbye, 'tStopRefresh')  # time at next scr refresh
            textGoodbye.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Goodbye_ScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Goodbye_Screen"-------
for thisComponent in Goodbye_ScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('textGoodbye.started', textGoodbye.tStartRefresh)
thisExp.addData('textGoodbye.stopped', textGoodbye.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
