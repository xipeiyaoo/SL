#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on 三月 09, 2025, at 17:04
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
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
expName = 'SL_base'  # from the Builder filename that created this script
expInfo = {'participant': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\admin\\Desktop\\SL_new\\sl\\psy_sl_base\\SL_base_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1707, 960], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='pix')
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

# Initialize components for Routine "instr"
instrClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='欢迎来到本次实验\n\n您的任务是找到元素中的独特形状\n（如圆形中的菱形），\n并判断该独特形状内线段的方向，\n如果是竖直的，请按“上”键，\n如果是水平的，请按“左”键。\n首先呈现练习，随后开始正式实验。\n\n明白后请按空格键开始。',
    font='Open Sans',
    pos=(0, 0), height=30.0, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "fix"
fixClock = core.Clock()
fix_circle = visual.ShapeStim(
    win=win, name='fix_circle', vertices=9999,
    size=(20, 20),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=None, depth=0.0, interpolate=True)

# Initialize components for Routine "trial"
trialClock = core.Clock()
fixation = visual.ShapeStim(
    win=win, name='fixation', vertices=9999,
    size=(20, 20),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=None, depth=0.0, interpolate=True)
loc1_shape = visual.Rect(
    win=win, name='loc1_shape',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=45.0, pos=(200, 0),
    lineWidth=2.0,     colorSpace='rgb',  lineColor='white', fillColor=None,
    opacity=None, depth=-1.0, interpolate=True)
loc1_line = visual.Line(
    win=win, name='loc1_line',
    start=(-(1, 1)[0]/2.0, 0), end=(+(1, 1)[0]/2.0, 0),
    ori=0.0, pos=(200, 0),
    lineWidth=2.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=None, depth=-2.0, interpolate=True)
loc2_shape = visual.ShapeStim(
    win=win, name='loc2_shape',
    size=(2, 2), vertices='triangle',
    ori=45.0, pos=(141, 141),
    lineWidth=2.0,     colorSpace='rgb',  lineColor='red', fillColor=None,
    opacity=None, depth=-3.0, interpolate=True)
loc2_line = visual.Line(
    win=win, name='loc2_line',
    start=(-(1,1)[0]/2.0, 0), end=(+(1,1)[0]/2.0, 0),
    ori=0.0, pos=(141, 141),
    lineWidth=2.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=None, depth=-4.0, interpolate=True)
loc3_shape = visual.ShapeStim(
    win=win, name='loc3_shape',
    size=(2, 2), vertices='triangle',
    ori=45.0, pos=(0, 200),
    lineWidth=2.0,     colorSpace='rgb',  lineColor='red', fillColor=None,
    opacity=None, depth=-5.0, interpolate=True)
loc3_line = visual.Line(
    win=win, name='loc3_line',
    start=(-(1, 1)[0]/2.0, 0), end=(+(1, 1)[0]/2.0, 0),
    ori=0.0, pos=(0, 200),
    lineWidth=2.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=None, depth=-6.0, interpolate=True)
loc4_shape = visual.ShapeStim(
    win=win, name='loc4_shape',
    size=(2,2), vertices='triangle',
    ori=45.0, pos=(-141,141),
    lineWidth=2.0,     colorSpace='rgb',  lineColor='red', fillColor=None,
    opacity=None, depth=-7.0, interpolate=True)
loc4_line = visual.Line(
    win=win, name='loc4_line',
    start=(-(1, 1)[0]/2.0, 0), end=(+(1, 1)[0]/2.0, 0),
    ori=0.0, pos=(-141,141),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=None, depth=-8.0, interpolate=True)
loc5_shape = visual.ShapeStim(
    win=win, name='loc5_shape',
    size=(2, 2), vertices='triangle',
    ori=45.0, pos=(-200, 0),
    lineWidth=2.0,     colorSpace='rgb',  lineColor='red', fillColor=None,
    opacity=None, depth=-9.0, interpolate=True)
loc5_line = visual.Line(
    win=win, name='loc5_line',
    start=(-(1, 1)[0]/2.0, 0), end=(+(1, 1)[0]/2.0, 0),
    ori=0.0, pos=(-200, 0),
    lineWidth=2.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=None, depth=-10.0, interpolate=True)
loc6_shape = visual.ShapeStim(
    win=win, name='loc6_shape',
    size=(2, 2), vertices='triangle',
    ori=45.0, pos=(-141, -141),
    lineWidth=2.0,     colorSpace='rgb',  lineColor='red', fillColor=None,
    opacity=None, depth=-11.0, interpolate=True)
loc6_line = visual.Line(
    win=win, name='loc6_line',
    start=(-(1, 1)[0]/2.0, 0), end=(+(1, 1)[0]/2.0, 0),
    ori=0.0, pos=(-141, -141),
    lineWidth=2.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=None, depth=-12.0, interpolate=True)
loc7_shape = visual.ShapeStim(
    win=win, name='loc7_shape',
    size=(2, 2), vertices='triangle',
    ori=45.0, pos=(0, -200),
    lineWidth=2.0,     colorSpace='rgb',  lineColor='red', fillColor=None,
    opacity=None, depth=-13.0, interpolate=True)
loc7_line = visual.Line(
    win=win, name='loc7_line',
    start=(-(1, 1)[0]/2.0, 0), end=(+(1, 1)[0]/2.0, 0),
    ori=0.0, pos=(0, -200),
    lineWidth=2.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=None, depth=-14.0, interpolate=True)
loc8_shape = visual.ShapeStim(
    win=win, name='loc8_shape',
    size=(2, 2), vertices='triangle',
    ori=45.0, pos=(141, -141),
    lineWidth=2.0,     colorSpace='rgb',  lineColor='red', fillColor=None,
    opacity=None, depth=-15.0, interpolate=True)
loc8_line = visual.Line(
    win=win, name='loc8_line',
    start=(-(1, 1)[0]/2.0, 0), end=(+(1, 1)[0]/2.0, 0),
    ori=0.0, pos=(141, -141),
    lineWidth=2.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=None, depth=-16.0, interpolate=True)
resp = keyboard.Keyboard()
#import random
#random = Math.random;
block_num=0
circle_vertices = []
theta = []
x=[]
y=[]
green=[-1,0,-1]
red=[1,0,0]
for i in range(100):
    theta = 2 * pi * i / 99
    x = 18 * cos(theta)
    y = 18 * sin(theta)
    circle_vertices.append((x, y))
a=15  
diamond_vertices = [(-a, a), (a, a), (a, -a), (-a, -a)]
#define line direction
b=20
hori_start=[-b,0]
hori_end=[b,0]
vert_start=[0,-b]
vert_end=[0,b]

#define loc
c=200
d=141
loc1=(c,0);loc2=(d,d);loc3=(0,c);loc4=(-d,d);
loc5=(-c,0);loc6=(-d,-d);loc7=(0,-c);loc8=(d,-d)
locs=[loc1,loc2,loc3,loc4,loc5,loc6,loc7,loc8]
#define loc_list
high_prob_loc = locs[int(random() * 8)] 
#high_prob_loc = random.choice(locs)  # 从所有位置中随机选择一个
low_prob_locs = [loc for loc in locs if loc != high_prob_loc]
#define dis loc list
distractor_locs=[]
tar_only_locs=[]
distractor_locs=[high_prob_loc]*24+low_prob_locs*8  # distractor locations
shuffle(distractor_locs)
tar_only_locs = locs*5  # target locations
shuffle(tar_only_locs)
#define parameter list
shape = ['circle', 'diamond']
distractor = ['red', 'green', 'no_dis']
detection  = ['hori','vert']

# 计算基础试次数
base_trial_count = len(shape) * len(distractor) * len(detection)  # 2×3×2=12
repeat_times = 10  # 需要重复的次数

# 显式构建试次列表
trial_list_new = []
trial = []
for _ in range(repeat_times):
    for s in shape:
        for ds in distractor:
            for d in detection:
                # 强制所有元素为字符串类型
                trial = [s,ds,d,
                    'left' if d == 'hori' else 'up'
                ]
                trial_list_new.append(trial)  # 必须创建独立副本

shuffle(trial_list_new)
# Add the distractor locations.
j = 0
k = 0
filtered_locs = []
n=[]
random_index=[]
tar_both_loc=[]
dis_loc_fake=(9999,9999)
for i in range(120):
    if str(trial_list_new[i][1]) == "no_dis":  # [1]指的是第二项
        trial_list_new[i] = trial_list_new[i]+[dis_loc_fake,tar_only_locs[k]]
        k = k + 1
    else:
        filtered_locs = []
        for m in locs:
            if m != distractor_locs[j]:
                filtered_locs.append(m)
        n = len(filtered_locs)
        random_index = int(random() * n)  # 在Python中会调用random模块，在JS中会转为Math.random()
        tar_both_loc = filtered_locs[random_index]
#        tar_both_loc = random.choice([m for m in locs if not m == distractor_locs[j]])
        trial_list_new[i] = trial_list_new[i]+[distractor_locs[j],tar_both_loc]
        j = j + 1
#thisExp.addData('trial_list_new', trial_list_new)
shuffle(trial_list_new)
current_trial = 0




# Initialize components for Routine "feedback"
feedbackClock = core.Clock()
text_4 = visual.TextStim(win=win, name='text_4',
    text='',
    font='Open Sans',
    pos=(0, 0), height=30.0, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "iti"
itiClock = core.Clock()
iti_blank = visual.TextStim(win=win, name='iti_blank',
    text='',
    font='Open Sans',
    pos=(0, 0), height=30.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "formal_cue"
formal_cueClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='练习结束，请按空格开始实验\n\n再次提示，任务为找到独特形状\n（例如圆形中的菱形，或菱形中的圆形）\n\n并判断内部线段朝向',
    font='Open Sans',
    pos=(0, 0), height=30.0, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "fix"
fixClock = core.Clock()
fix_circle = visual.ShapeStim(
    win=win, name='fix_circle', vertices=9999,
    size=(20, 20),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=None, depth=0.0, interpolate=True)

# Initialize components for Routine "trial"
trialClock = core.Clock()
fixation = visual.ShapeStim(
    win=win, name='fixation', vertices=9999,
    size=(20, 20),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=None, depth=0.0, interpolate=True)
loc1_shape = visual.Rect(
    win=win, name='loc1_shape',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=45.0, pos=(200, 0),
    lineWidth=2.0,     colorSpace='rgb',  lineColor='white', fillColor=None,
    opacity=None, depth=-1.0, interpolate=True)
loc1_line = visual.Line(
    win=win, name='loc1_line',
    start=(-(1, 1)[0]/2.0, 0), end=(+(1, 1)[0]/2.0, 0),
    ori=0.0, pos=(200, 0),
    lineWidth=2.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=None, depth=-2.0, interpolate=True)
loc2_shape = visual.ShapeStim(
    win=win, name='loc2_shape',
    size=(2, 2), vertices='triangle',
    ori=45.0, pos=(141, 141),
    lineWidth=2.0,     colorSpace='rgb',  lineColor='red', fillColor=None,
    opacity=None, depth=-3.0, interpolate=True)
loc2_line = visual.Line(
    win=win, name='loc2_line',
    start=(-(1,1)[0]/2.0, 0), end=(+(1,1)[0]/2.0, 0),
    ori=0.0, pos=(141, 141),
    lineWidth=2.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=None, depth=-4.0, interpolate=True)
loc3_shape = visual.ShapeStim(
    win=win, name='loc3_shape',
    size=(2, 2), vertices='triangle',
    ori=45.0, pos=(0, 200),
    lineWidth=2.0,     colorSpace='rgb',  lineColor='red', fillColor=None,
    opacity=None, depth=-5.0, interpolate=True)
loc3_line = visual.Line(
    win=win, name='loc3_line',
    start=(-(1, 1)[0]/2.0, 0), end=(+(1, 1)[0]/2.0, 0),
    ori=0.0, pos=(0, 200),
    lineWidth=2.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=None, depth=-6.0, interpolate=True)
loc4_shape = visual.ShapeStim(
    win=win, name='loc4_shape',
    size=(2,2), vertices='triangle',
    ori=45.0, pos=(-141,141),
    lineWidth=2.0,     colorSpace='rgb',  lineColor='red', fillColor=None,
    opacity=None, depth=-7.0, interpolate=True)
loc4_line = visual.Line(
    win=win, name='loc4_line',
    start=(-(1, 1)[0]/2.0, 0), end=(+(1, 1)[0]/2.0, 0),
    ori=0.0, pos=(-141,141),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=None, depth=-8.0, interpolate=True)
loc5_shape = visual.ShapeStim(
    win=win, name='loc5_shape',
    size=(2, 2), vertices='triangle',
    ori=45.0, pos=(-200, 0),
    lineWidth=2.0,     colorSpace='rgb',  lineColor='red', fillColor=None,
    opacity=None, depth=-9.0, interpolate=True)
loc5_line = visual.Line(
    win=win, name='loc5_line',
    start=(-(1, 1)[0]/2.0, 0), end=(+(1, 1)[0]/2.0, 0),
    ori=0.0, pos=(-200, 0),
    lineWidth=2.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=None, depth=-10.0, interpolate=True)
loc6_shape = visual.ShapeStim(
    win=win, name='loc6_shape',
    size=(2, 2), vertices='triangle',
    ori=45.0, pos=(-141, -141),
    lineWidth=2.0,     colorSpace='rgb',  lineColor='red', fillColor=None,
    opacity=None, depth=-11.0, interpolate=True)
loc6_line = visual.Line(
    win=win, name='loc6_line',
    start=(-(1, 1)[0]/2.0, 0), end=(+(1, 1)[0]/2.0, 0),
    ori=0.0, pos=(-141, -141),
    lineWidth=2.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=None, depth=-12.0, interpolate=True)
loc7_shape = visual.ShapeStim(
    win=win, name='loc7_shape',
    size=(2, 2), vertices='triangle',
    ori=45.0, pos=(0, -200),
    lineWidth=2.0,     colorSpace='rgb',  lineColor='red', fillColor=None,
    opacity=None, depth=-13.0, interpolate=True)
loc7_line = visual.Line(
    win=win, name='loc7_line',
    start=(-(1, 1)[0]/2.0, 0), end=(+(1, 1)[0]/2.0, 0),
    ori=0.0, pos=(0, -200),
    lineWidth=2.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=None, depth=-14.0, interpolate=True)
loc8_shape = visual.ShapeStim(
    win=win, name='loc8_shape',
    size=(2, 2), vertices='triangle',
    ori=45.0, pos=(141, -141),
    lineWidth=2.0,     colorSpace='rgb',  lineColor='red', fillColor=None,
    opacity=None, depth=-15.0, interpolate=True)
loc8_line = visual.Line(
    win=win, name='loc8_line',
    start=(-(1, 1)[0]/2.0, 0), end=(+(1, 1)[0]/2.0, 0),
    ori=0.0, pos=(141, -141),
    lineWidth=2.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=None, depth=-16.0, interpolate=True)
resp = keyboard.Keyboard()
#import random
#random = Math.random;
block_num=0
circle_vertices = []
theta = []
x=[]
y=[]
green=[-1,0,-1]
red=[1,0,0]
for i in range(100):
    theta = 2 * pi * i / 99
    x = 18 * cos(theta)
    y = 18 * sin(theta)
    circle_vertices.append((x, y))
a=15  
diamond_vertices = [(-a, a), (a, a), (a, -a), (-a, -a)]
#define line direction
b=20
hori_start=[-b,0]
hori_end=[b,0]
vert_start=[0,-b]
vert_end=[0,b]

#define loc
c=200
d=141
loc1=(c,0);loc2=(d,d);loc3=(0,c);loc4=(-d,d);
loc5=(-c,0);loc6=(-d,-d);loc7=(0,-c);loc8=(d,-d)
locs=[loc1,loc2,loc3,loc4,loc5,loc6,loc7,loc8]
#define loc_list
high_prob_loc = locs[int(random() * 8)] 
#high_prob_loc = random.choice(locs)  # 从所有位置中随机选择一个
low_prob_locs = [loc for loc in locs if loc != high_prob_loc]
#define dis loc list
distractor_locs=[]
tar_only_locs=[]
distractor_locs=[high_prob_loc]*24+low_prob_locs*8  # distractor locations
shuffle(distractor_locs)
tar_only_locs = locs*5  # target locations
shuffle(tar_only_locs)
#define parameter list
shape = ['circle', 'diamond']
distractor = ['red', 'green', 'no_dis']
detection  = ['hori','vert']

# 计算基础试次数
base_trial_count = len(shape) * len(distractor) * len(detection)  # 2×3×2=12
repeat_times = 10  # 需要重复的次数

# 显式构建试次列表
trial_list_new = []
trial = []
for _ in range(repeat_times):
    for s in shape:
        for ds in distractor:
            for d in detection:
                # 强制所有元素为字符串类型
                trial = [s,ds,d,
                    'left' if d == 'hori' else 'up'
                ]
                trial_list_new.append(trial)  # 必须创建独立副本

shuffle(trial_list_new)
# Add the distractor locations.
j = 0
k = 0
filtered_locs = []
n=[]
random_index=[]
tar_both_loc=[]
dis_loc_fake=(9999,9999)
for i in range(120):
    if str(trial_list_new[i][1]) == "no_dis":  # [1]指的是第二项
        trial_list_new[i] = trial_list_new[i]+[dis_loc_fake,tar_only_locs[k]]
        k = k + 1
    else:
        filtered_locs = []
        for m in locs:
            if m != distractor_locs[j]:
                filtered_locs.append(m)
        n = len(filtered_locs)
        random_index = int(random() * n)  # 在Python中会调用random模块，在JS中会转为Math.random()
        tar_both_loc = filtered_locs[random_index]
#        tar_both_loc = random.choice([m for m in locs if not m == distractor_locs[j]])
        trial_list_new[i] = trial_list_new[i]+[distractor_locs[j],tar_both_loc]
        j = j + 1
#thisExp.addData('trial_list_new', trial_list_new)
shuffle(trial_list_new)
current_trial = 0




# Initialize components for Routine "feedback"
feedbackClock = core.Clock()
text_4 = visual.TextStim(win=win, name='text_4',
    text='',
    font='Open Sans',
    pos=(0, 0), height=30.0, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "iti"
itiClock = core.Clock()
iti_blank = visual.TextStim(win=win, name='iti_blank',
    text='',
    font='Open Sans',
    pos=(0, 0), height=30.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "break_3"
break_3Clock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text='现在可以休息\n\n准备好了按空格键继续',
    font='Open Sans',
    pos=(0, 0), height=30.0, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_3 = keyboard.Keyboard()

# Initialize components for Routine "end"
endClock = core.Clock()
end_2 = visual.TextStim(win=win, name='end_2',
    text='实验结束，谢谢参与',
    font='Open Sans',
    pos=(0, 0), height=30.0, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instr"-------
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
instrComponents = [text, key_resp]
for thisComponent in instrComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instrClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instr"-------
while continueRoutine:
    # get current time
    t = instrClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instrClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    
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
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
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
    for thisComponent in instrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instr"-------
for thisComponent in instrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.addData('key_resp.started', key_resp.tStartRefresh)
thisExp.addData('key_resp.stopped', key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "instr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=10.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "fix"-------
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    fixComponents = [fix_circle]
    for thisComponent in fixComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    fixClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "fix"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = fixClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=fixClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fix_circle* updates
        if fix_circle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fix_circle.frameNStart = frameN  # exact frame index
            fix_circle.tStart = t  # local t and not account for scr refresh
            fix_circle.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix_circle, 'tStartRefresh')  # time at next scr refresh
            fix_circle.setAutoDraw(True)
        if fix_circle.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fix_circle.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                fix_circle.tStop = t  # not accounting for scr refresh
                fix_circle.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fix_circle, 'tStopRefresh')  # time at next scr refresh
                fix_circle.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "fix"-------
    for thisComponent in fixComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('fix_circle.started', fix_circle.tStartRefresh)
    trials.addData('fix_circle.stopped', fix_circle.tStopRefresh)
    
    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    loc1_shape.setLineColor('red')
    resp.keys = []
    resp.rt = []
    _resp_allKeys = []
    trial_info=trial_list_new[current_trial]
    current_trial=current_trial+1
    
    thisExp.addData('trial_para', trial_info)
    
    tar_shape=[]
    dis_color_condi=[]
    tar_line=[]
    cor_resp=[]
    dis_loc=[]
    tar_loc=[]
    #unpacking trial info
    tar_shape=trial_info[0]#目标形状
    dis_color_condi=trial_info[1]#干扰有无和颜色条件
    tar_line=trial_info[2]#目标形状内线段朝向
    cor_resp=trial_info[3]#正确反应按键
    dis_loc = trial_info[4]
    tar_loc = trial_info[5]
    
    print(trial_info)
    print(tar_shape)
    print(dis_color_condi)
    print(tar_line)
    print(cor_resp)
    print(dis_loc)
    print(tar_loc)
    
    thisExp.addData('tar_shape', tar_shape)
    thisExp.addData('dis_color_condi', dis_color_condi)
    thisExp.addData('tar_line', tar_line)
    thisExp.addData('cor_resp', cor_resp)
    thisExp.addData('dis_loc', dis_loc)
    thisExp.addData('tar_loc', tar_loc)
    
    #define maps
    shapes = {
        "loc1_shape": loc1_shape,
        "loc2_shape": loc2_shape,
        "loc3_shape": loc3_shape,
        "loc4_shape": loc4_shape,
        "loc5_shape": loc5_shape,
        "loc6_shape": loc6_shape,
        "loc7_shape": loc7_shape,
        "loc8_shape": loc8_shape
    }
    
    lines = {
        "loc1_shape": loc1_line,
        "loc2_shape": loc2_line,
        "loc3_shape": loc3_line,
        "loc4_shape": loc4_line,
        "loc5_shape": loc5_line,
        "loc6_shape": loc6_line,
        "loc7_shape": loc7_line,
        "loc8_shape": loc8_line
    }
    
    # 定义位置到组件名称的映射
    loc_to_shape_name = { 
        (200, 0): "loc1_shape",
        (141, 141): "loc2_shape",
        (0, 200): "loc3_shape",
        (-141, 141): "loc4_shape",
        (-200, 0): "loc5_shape",
        (-141, -141): "loc6_shape",
        (0, -200): "loc7_shape",
        (141, -141): "loc8_shape"
    }    
    
    # 定义形状和颜色的映射
    shape_map = {
        'circle': circle_vertices,
        'diamond': diamond_vertices
    }
    
    colors=[]
    # 设置其他位置的形状和颜色
    other_shape = 'diamond' if tar_shape == 'circle' else 'circle'
    if dis_color_condi == 'red':
        other_color = green
    elif dis_color_condi== 'green':
        other_color = red
    elif dis_color_condi == 'no_dis':
        colors = [red, green]
        other_color = colors[int(random() * len(colors))]
    
    shuffle(locs)
    loc=[]
    shape_name=[]
    shape=[]
    line=[]
    # 遍历所有位置，设置形状和线条属性
    for i in range(len(locs)):
        loc = locs[i]
        shape_name = loc_to_shape_name[loc]
        shape = shapes[shape_name]
        line = lines[shape_name]
        if loc == tar_loc:
          shape.vertices = shape_map[tar_shape]
          shape.lineColor = other_color
          line.start = hori_start if tar_line == 'hori' else vert_start
          line.end = hori_end if tar_line == 'hori' else vert_end
        elif loc == dis_loc:
           shape.vertices = shape_map[other_shape]
           shape.lineColor = red if dis_color_condi == 'red' else green
    #       dis_line=random.choice(['hori', 'vert'])
           line_dir = ['hori', 'vert']
           dis_line = line_dir[int(random() * len(line_dir))]
           line.start = hori_start if dis_line == 'hori' else vert_start
           line.end = hori_end if dis_line == 'hori' else vert_end
        else:
            # 其他位置：设置相反的形状和颜色
            shape.vertices = shape_map[other_shape]
            shape.lineColor = other_color
            if i % 2 == 0:  # 偶数索引：水平方向
                line.start = hori_start
                line.end = hori_end
            else:  # 奇数索引：竖直方向
                line.start = vert_start
                line.end = vert_end
    
    feedback_text = ""
    # keep track of which components have finished
    trialComponents = [fixation, loc1_shape, loc1_line, loc2_shape, loc2_line, loc3_shape, loc3_line, loc4_shape, loc4_line, loc5_shape, loc5_line, loc6_shape, loc6_line, loc7_shape, loc7_line, loc8_shape, loc8_line, resp]
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
        
        # *fixation* updates
        if fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation.frameNStart = frameN  # exact frame index
            fixation.tStart = t  # local t and not account for scr refresh
            fixation.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation, 'tStartRefresh')  # time at next scr refresh
            fixation.setAutoDraw(True)
        if fixation.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                fixation.tStop = t  # not accounting for scr refresh
                fixation.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fixation, 'tStopRefresh')  # time at next scr refresh
                fixation.setAutoDraw(False)
        
        # *loc1_shape* updates
        if loc1_shape.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            loc1_shape.frameNStart = frameN  # exact frame index
            loc1_shape.tStart = t  # local t and not account for scr refresh
            loc1_shape.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(loc1_shape, 'tStartRefresh')  # time at next scr refresh
            loc1_shape.setAutoDraw(True)
        if loc1_shape.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > loc1_shape.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                loc1_shape.tStop = t  # not accounting for scr refresh
                loc1_shape.frameNStop = frameN  # exact frame index
                win.timeOnFlip(loc1_shape, 'tStopRefresh')  # time at next scr refresh
                loc1_shape.setAutoDraw(False)
        
        # *loc1_line* updates
        if loc1_line.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            loc1_line.frameNStart = frameN  # exact frame index
            loc1_line.tStart = t  # local t and not account for scr refresh
            loc1_line.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(loc1_line, 'tStartRefresh')  # time at next scr refresh
            loc1_line.setAutoDraw(True)
        if loc1_line.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > loc1_line.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                loc1_line.tStop = t  # not accounting for scr refresh
                loc1_line.frameNStop = frameN  # exact frame index
                win.timeOnFlip(loc1_line, 'tStopRefresh')  # time at next scr refresh
                loc1_line.setAutoDraw(False)
        
        # *loc2_shape* updates
        if loc2_shape.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            loc2_shape.frameNStart = frameN  # exact frame index
            loc2_shape.tStart = t  # local t and not account for scr refresh
            loc2_shape.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(loc2_shape, 'tStartRefresh')  # time at next scr refresh
            loc2_shape.setAutoDraw(True)
        if loc2_shape.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > loc2_shape.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                loc2_shape.tStop = t  # not accounting for scr refresh
                loc2_shape.frameNStop = frameN  # exact frame index
                win.timeOnFlip(loc2_shape, 'tStopRefresh')  # time at next scr refresh
                loc2_shape.setAutoDraw(False)
        
        # *loc2_line* updates
        if loc2_line.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            loc2_line.frameNStart = frameN  # exact frame index
            loc2_line.tStart = t  # local t and not account for scr refresh
            loc2_line.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(loc2_line, 'tStartRefresh')  # time at next scr refresh
            loc2_line.setAutoDraw(True)
        if loc2_line.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > loc2_line.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                loc2_line.tStop = t  # not accounting for scr refresh
                loc2_line.frameNStop = frameN  # exact frame index
                win.timeOnFlip(loc2_line, 'tStopRefresh')  # time at next scr refresh
                loc2_line.setAutoDraw(False)
        
        # *loc3_shape* updates
        if loc3_shape.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            loc3_shape.frameNStart = frameN  # exact frame index
            loc3_shape.tStart = t  # local t and not account for scr refresh
            loc3_shape.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(loc3_shape, 'tStartRefresh')  # time at next scr refresh
            loc3_shape.setAutoDraw(True)
        if loc3_shape.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > loc3_shape.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                loc3_shape.tStop = t  # not accounting for scr refresh
                loc3_shape.frameNStop = frameN  # exact frame index
                win.timeOnFlip(loc3_shape, 'tStopRefresh')  # time at next scr refresh
                loc3_shape.setAutoDraw(False)
        
        # *loc3_line* updates
        if loc3_line.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            loc3_line.frameNStart = frameN  # exact frame index
            loc3_line.tStart = t  # local t and not account for scr refresh
            loc3_line.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(loc3_line, 'tStartRefresh')  # time at next scr refresh
            loc3_line.setAutoDraw(True)
        if loc3_line.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > loc3_line.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                loc3_line.tStop = t  # not accounting for scr refresh
                loc3_line.frameNStop = frameN  # exact frame index
                win.timeOnFlip(loc3_line, 'tStopRefresh')  # time at next scr refresh
                loc3_line.setAutoDraw(False)
        
        # *loc4_shape* updates
        if loc4_shape.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            loc4_shape.frameNStart = frameN  # exact frame index
            loc4_shape.tStart = t  # local t and not account for scr refresh
            loc4_shape.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(loc4_shape, 'tStartRefresh')  # time at next scr refresh
            loc4_shape.setAutoDraw(True)
        if loc4_shape.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > loc4_shape.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                loc4_shape.tStop = t  # not accounting for scr refresh
                loc4_shape.frameNStop = frameN  # exact frame index
                win.timeOnFlip(loc4_shape, 'tStopRefresh')  # time at next scr refresh
                loc4_shape.setAutoDraw(False)
        
        # *loc4_line* updates
        if loc4_line.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            loc4_line.frameNStart = frameN  # exact frame index
            loc4_line.tStart = t  # local t and not account for scr refresh
            loc4_line.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(loc4_line, 'tStartRefresh')  # time at next scr refresh
            loc4_line.setAutoDraw(True)
        if loc4_line.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > loc4_line.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                loc4_line.tStop = t  # not accounting for scr refresh
                loc4_line.frameNStop = frameN  # exact frame index
                win.timeOnFlip(loc4_line, 'tStopRefresh')  # time at next scr refresh
                loc4_line.setAutoDraw(False)
        
        # *loc5_shape* updates
        if loc5_shape.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            loc5_shape.frameNStart = frameN  # exact frame index
            loc5_shape.tStart = t  # local t and not account for scr refresh
            loc5_shape.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(loc5_shape, 'tStartRefresh')  # time at next scr refresh
            loc5_shape.setAutoDraw(True)
        if loc5_shape.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > loc5_shape.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                loc5_shape.tStop = t  # not accounting for scr refresh
                loc5_shape.frameNStop = frameN  # exact frame index
                win.timeOnFlip(loc5_shape, 'tStopRefresh')  # time at next scr refresh
                loc5_shape.setAutoDraw(False)
        
        # *loc5_line* updates
        if loc5_line.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            loc5_line.frameNStart = frameN  # exact frame index
            loc5_line.tStart = t  # local t and not account for scr refresh
            loc5_line.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(loc5_line, 'tStartRefresh')  # time at next scr refresh
            loc5_line.setAutoDraw(True)
        if loc5_line.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > loc5_line.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                loc5_line.tStop = t  # not accounting for scr refresh
                loc5_line.frameNStop = frameN  # exact frame index
                win.timeOnFlip(loc5_line, 'tStopRefresh')  # time at next scr refresh
                loc5_line.setAutoDraw(False)
        
        # *loc6_shape* updates
        if loc6_shape.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            loc6_shape.frameNStart = frameN  # exact frame index
            loc6_shape.tStart = t  # local t and not account for scr refresh
            loc6_shape.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(loc6_shape, 'tStartRefresh')  # time at next scr refresh
            loc6_shape.setAutoDraw(True)
        if loc6_shape.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > loc6_shape.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                loc6_shape.tStop = t  # not accounting for scr refresh
                loc6_shape.frameNStop = frameN  # exact frame index
                win.timeOnFlip(loc6_shape, 'tStopRefresh')  # time at next scr refresh
                loc6_shape.setAutoDraw(False)
        
        # *loc6_line* updates
        if loc6_line.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            loc6_line.frameNStart = frameN  # exact frame index
            loc6_line.tStart = t  # local t and not account for scr refresh
            loc6_line.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(loc6_line, 'tStartRefresh')  # time at next scr refresh
            loc6_line.setAutoDraw(True)
        if loc6_line.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > loc6_line.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                loc6_line.tStop = t  # not accounting for scr refresh
                loc6_line.frameNStop = frameN  # exact frame index
                win.timeOnFlip(loc6_line, 'tStopRefresh')  # time at next scr refresh
                loc6_line.setAutoDraw(False)
        
        # *loc7_shape* updates
        if loc7_shape.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            loc7_shape.frameNStart = frameN  # exact frame index
            loc7_shape.tStart = t  # local t and not account for scr refresh
            loc7_shape.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(loc7_shape, 'tStartRefresh')  # time at next scr refresh
            loc7_shape.setAutoDraw(True)
        if loc7_shape.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > loc7_shape.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                loc7_shape.tStop = t  # not accounting for scr refresh
                loc7_shape.frameNStop = frameN  # exact frame index
                win.timeOnFlip(loc7_shape, 'tStopRefresh')  # time at next scr refresh
                loc7_shape.setAutoDraw(False)
        
        # *loc7_line* updates
        if loc7_line.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            loc7_line.frameNStart = frameN  # exact frame index
            loc7_line.tStart = t  # local t and not account for scr refresh
            loc7_line.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(loc7_line, 'tStartRefresh')  # time at next scr refresh
            loc7_line.setAutoDraw(True)
        if loc7_line.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > loc7_line.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                loc7_line.tStop = t  # not accounting for scr refresh
                loc7_line.frameNStop = frameN  # exact frame index
                win.timeOnFlip(loc7_line, 'tStopRefresh')  # time at next scr refresh
                loc7_line.setAutoDraw(False)
        
        # *loc8_shape* updates
        if loc8_shape.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            loc8_shape.frameNStart = frameN  # exact frame index
            loc8_shape.tStart = t  # local t and not account for scr refresh
            loc8_shape.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(loc8_shape, 'tStartRefresh')  # time at next scr refresh
            loc8_shape.setAutoDraw(True)
        if loc8_shape.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > loc8_shape.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                loc8_shape.tStop = t  # not accounting for scr refresh
                loc8_shape.frameNStop = frameN  # exact frame index
                win.timeOnFlip(loc8_shape, 'tStopRefresh')  # time at next scr refresh
                loc8_shape.setAutoDraw(False)
        
        # *loc8_line* updates
        if loc8_line.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            loc8_line.frameNStart = frameN  # exact frame index
            loc8_line.tStart = t  # local t and not account for scr refresh
            loc8_line.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(loc8_line, 'tStartRefresh')  # time at next scr refresh
            loc8_line.setAutoDraw(True)
        if loc8_line.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > loc8_line.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                loc8_line.tStop = t  # not accounting for scr refresh
                loc8_line.frameNStop = frameN  # exact frame index
                win.timeOnFlip(loc8_line, 'tStopRefresh')  # time at next scr refresh
                loc8_line.setAutoDraw(False)
        
        # *resp* updates
        waitOnFlip = False
        if resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            resp.frameNStart = frameN  # exact frame index
            resp.tStart = t  # local t and not account for scr refresh
            resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(resp, 'tStartRefresh')  # time at next scr refresh
            resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > resp.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                resp.tStop = t  # not accounting for scr refresh
                resp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(resp, 'tStopRefresh')  # time at next scr refresh
                resp.status = FINISHED
        if resp.status == STARTED and not waitOnFlip:
            theseKeys = resp.getKeys(keyList=['up', 'left'], waitRelease=False)
            _resp_allKeys.extend(theseKeys)
            if len(_resp_allKeys):
                resp.keys = _resp_allKeys[-1].name  # just the last key pressed
                resp.rt = _resp_allKeys[-1].rt
                # was this correct?
                if (resp.keys == str(cor_resp)) or (resp.keys == cor_resp):
                    resp.corr = 1
                else:
                    resp.corr = 0
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
    trials.addData('fixation.started', fixation.tStartRefresh)
    trials.addData('fixation.stopped', fixation.tStopRefresh)
    trials.addData('loc1_shape.started', loc1_shape.tStartRefresh)
    trials.addData('loc1_shape.stopped', loc1_shape.tStopRefresh)
    trials.addData('loc1_line.started', loc1_line.tStartRefresh)
    trials.addData('loc1_line.stopped', loc1_line.tStopRefresh)
    trials.addData('loc2_shape.started', loc2_shape.tStartRefresh)
    trials.addData('loc2_shape.stopped', loc2_shape.tStopRefresh)
    trials.addData('loc2_line.started', loc2_line.tStartRefresh)
    trials.addData('loc2_line.stopped', loc2_line.tStopRefresh)
    trials.addData('loc3_shape.started', loc3_shape.tStartRefresh)
    trials.addData('loc3_shape.stopped', loc3_shape.tStopRefresh)
    trials.addData('loc3_line.started', loc3_line.tStartRefresh)
    trials.addData('loc3_line.stopped', loc3_line.tStopRefresh)
    trials.addData('loc4_shape.started', loc4_shape.tStartRefresh)
    trials.addData('loc4_shape.stopped', loc4_shape.tStopRefresh)
    trials.addData('loc4_line.started', loc4_line.tStartRefresh)
    trials.addData('loc4_line.stopped', loc4_line.tStopRefresh)
    trials.addData('loc5_shape.started', loc5_shape.tStartRefresh)
    trials.addData('loc5_shape.stopped', loc5_shape.tStopRefresh)
    trials.addData('loc5_line.started', loc5_line.tStartRefresh)
    trials.addData('loc5_line.stopped', loc5_line.tStopRefresh)
    trials.addData('loc6_shape.started', loc6_shape.tStartRefresh)
    trials.addData('loc6_shape.stopped', loc6_shape.tStopRefresh)
    trials.addData('loc6_line.started', loc6_line.tStartRefresh)
    trials.addData('loc6_line.stopped', loc6_line.tStopRefresh)
    trials.addData('loc7_shape.started', loc7_shape.tStartRefresh)
    trials.addData('loc7_shape.stopped', loc7_shape.tStopRefresh)
    trials.addData('loc7_line.started', loc7_line.tStartRefresh)
    trials.addData('loc7_line.stopped', loc7_line.tStopRefresh)
    trials.addData('loc8_shape.started', loc8_shape.tStartRefresh)
    trials.addData('loc8_shape.stopped', loc8_shape.tStopRefresh)
    trials.addData('loc8_line.started', loc8_line.tStartRefresh)
    trials.addData('loc8_line.stopped', loc8_line.tStopRefresh)
    # check responses
    if resp.keys in ['', [], None]:  # No response was made
        resp.keys = None
        # was no response the correct answer?!
        if str(cor_resp).lower() == 'none':
           resp.corr = 1;  # correct non-response
        else:
           resp.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('resp.keys',resp.keys)
    trials.addData('resp.corr', resp.corr)
    if resp.keys != None:  # we had a response
        trials.addData('resp.rt', resp.rt)
    trials.addData('resp.started', resp.tStartRefresh)
    trials.addData('resp.stopped', resp.tStopRefresh)
    # 判断按键是否正确
    if resp.keys is None:  # 没有按键
        feedback_text = "请及时反应，集中注意力！"
    elif resp.keys != cor_resp:  # 按键错误
        feedback_text = "错误！"
    else:  # 按键正确
        feedback_text = ""  # 不显示反馈
        
    
    
    # ------Prepare to start Routine "feedback"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    text_4.setText(feedback_text)
    if feedback_text == "":
        continueRoutine = False
    # keep track of which components have finished
    feedbackComponents = [text_4]
    for thisComponent in feedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    feedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "feedback"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = feedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=feedbackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_4* updates
        if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_4.frameNStart = frameN  # exact frame index
            text_4.tStart = t  # local t and not account for scr refresh
            text_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
            text_4.setAutoDraw(True)
        if text_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_4.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                text_4.tStop = t  # not accounting for scr refresh
                text_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_4, 'tStopRefresh')  # time at next scr refresh
                text_4.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feedback"-------
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('text_4.started', text_4.tStartRefresh)
    trials.addData('text_4.stopped', text_4.tStopRefresh)
    
    # ------Prepare to start Routine "iti"-------
    continueRoutine = True
    # update component parameters for each repeat
    iti_blank.setText(' ')
    # keep track of which components have finished
    itiComponents = [iti_blank]
    for thisComponent in itiComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    itiClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "iti"-------
    while continueRoutine:
        # get current time
        t = itiClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=itiClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *iti_blank* updates
        if iti_blank.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            iti_blank.frameNStart = frameN  # exact frame index
            iti_blank.tStart = t  # local t and not account for scr refresh
            iti_blank.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(iti_blank, 'tStartRefresh')  # time at next scr refresh
            iti_blank.setAutoDraw(True)
        if iti_blank.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > iti_blank.tStartRefresh + 0.5 + random() * 0.25-frameTolerance:
                # keep track of stop time/frame for later
                iti_blank.tStop = t  # not accounting for scr refresh
                iti_blank.frameNStop = frameN  # exact frame index
                win.timeOnFlip(iti_blank, 'tStopRefresh')  # time at next scr refresh
                iti_blank.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in itiComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "iti"-------
    for thisComponent in itiComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('iti_blank.started', iti_blank.tStartRefresh)
    trials.addData('iti_blank.stopped', iti_blank.tStopRefresh)
    # the Routine "iti" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 10.0 repeats of 'trials'

# get names of stimulus parameters
if trials.trialList in ([], [None], None):
    params = []
else:
    params = trials.trialList[0].keys()
# save data for this loop
trials.saveAsExcel(filename + '.xlsx', sheetName='trials',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "formal_cue"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
current_trial = 0
# keep track of which components have finished
formal_cueComponents = [text_2, key_resp_2]
for thisComponent in formal_cueComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
formal_cueClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "formal_cue"-------
while continueRoutine:
    # get current time
    t = formal_cueClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=formal_cueClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    
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
        theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
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
    for thisComponent in formal_cueComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "formal_cue"-------
for thisComponent in formal_cueComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys = None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.addData('key_resp_2.started', key_resp_2.tStartRefresh)
thisExp.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
thisExp.nextEntry()
# the Routine "formal_cue" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_3 = data.TrialHandler(nReps=6.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials_3')
thisExp.addLoop(trials_3)  # add the loop to the experiment
thisTrial_3 = trials_3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
if thisTrial_3 != None:
    for paramName in thisTrial_3:
        exec('{} = thisTrial_3[paramName]'.format(paramName))

for thisTrial_3 in trials_3:
    currentLoop = trials_3
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
    if thisTrial_3 != None:
        for paramName in thisTrial_3:
            exec('{} = thisTrial_3[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    trials_2 = data.TrialHandler(nReps=120.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='trials_2')
    thisExp.addLoop(trials_2)  # add the loop to the experiment
    thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            exec('{} = thisTrial_2[paramName]'.format(paramName))
    
    for thisTrial_2 in trials_2:
        currentLoop = trials_2
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
        if thisTrial_2 != None:
            for paramName in thisTrial_2:
                exec('{} = thisTrial_2[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "fix"-------
        continueRoutine = True
        routineTimer.add(0.500000)
        # update component parameters for each repeat
        # keep track of which components have finished
        fixComponents = [fix_circle]
        for thisComponent in fixComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        fixClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "fix"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = fixClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=fixClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fix_circle* updates
            if fix_circle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fix_circle.frameNStart = frameN  # exact frame index
                fix_circle.tStart = t  # local t and not account for scr refresh
                fix_circle.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fix_circle, 'tStartRefresh')  # time at next scr refresh
                fix_circle.setAutoDraw(True)
            if fix_circle.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fix_circle.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    fix_circle.tStop = t  # not accounting for scr refresh
                    fix_circle.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(fix_circle, 'tStopRefresh')  # time at next scr refresh
                    fix_circle.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in fixComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "fix"-------
        for thisComponent in fixComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials_2.addData('fix_circle.started', fix_circle.tStartRefresh)
        trials_2.addData('fix_circle.stopped', fix_circle.tStopRefresh)
        
        # ------Prepare to start Routine "trial"-------
        continueRoutine = True
        routineTimer.add(3.000000)
        # update component parameters for each repeat
        loc1_shape.setLineColor('red')
        resp.keys = []
        resp.rt = []
        _resp_allKeys = []
        trial_info=trial_list_new[current_trial]
        current_trial=current_trial+1
        
        thisExp.addData('trial_para', trial_info)
        
        tar_shape=[]
        dis_color_condi=[]
        tar_line=[]
        cor_resp=[]
        dis_loc=[]
        tar_loc=[]
        #unpacking trial info
        tar_shape=trial_info[0]#目标形状
        dis_color_condi=trial_info[1]#干扰有无和颜色条件
        tar_line=trial_info[2]#目标形状内线段朝向
        cor_resp=trial_info[3]#正确反应按键
        dis_loc = trial_info[4]
        tar_loc = trial_info[5]
        
        print(trial_info)
        print(tar_shape)
        print(dis_color_condi)
        print(tar_line)
        print(cor_resp)
        print(dis_loc)
        print(tar_loc)
        
        thisExp.addData('tar_shape', tar_shape)
        thisExp.addData('dis_color_condi', dis_color_condi)
        thisExp.addData('tar_line', tar_line)
        thisExp.addData('cor_resp', cor_resp)
        thisExp.addData('dis_loc', dis_loc)
        thisExp.addData('tar_loc', tar_loc)
        
        #define maps
        shapes = {
            "loc1_shape": loc1_shape,
            "loc2_shape": loc2_shape,
            "loc3_shape": loc3_shape,
            "loc4_shape": loc4_shape,
            "loc5_shape": loc5_shape,
            "loc6_shape": loc6_shape,
            "loc7_shape": loc7_shape,
            "loc8_shape": loc8_shape
        }
        
        lines = {
            "loc1_shape": loc1_line,
            "loc2_shape": loc2_line,
            "loc3_shape": loc3_line,
            "loc4_shape": loc4_line,
            "loc5_shape": loc5_line,
            "loc6_shape": loc6_line,
            "loc7_shape": loc7_line,
            "loc8_shape": loc8_line
        }
        
        # 定义位置到组件名称的映射
        loc_to_shape_name = { 
            (200, 0): "loc1_shape",
            (141, 141): "loc2_shape",
            (0, 200): "loc3_shape",
            (-141, 141): "loc4_shape",
            (-200, 0): "loc5_shape",
            (-141, -141): "loc6_shape",
            (0, -200): "loc7_shape",
            (141, -141): "loc8_shape"
        }    
        
        # 定义形状和颜色的映射
        shape_map = {
            'circle': circle_vertices,
            'diamond': diamond_vertices
        }
        
        colors=[]
        # 设置其他位置的形状和颜色
        other_shape = 'diamond' if tar_shape == 'circle' else 'circle'
        if dis_color_condi == 'red':
            other_color = green
        elif dis_color_condi== 'green':
            other_color = red
        elif dis_color_condi == 'no_dis':
            colors = [red, green]
            other_color = colors[int(random() * len(colors))]
        
        shuffle(locs)
        loc=[]
        shape_name=[]
        shape=[]
        line=[]
        # 遍历所有位置，设置形状和线条属性
        for i in range(len(locs)):
            loc = locs[i]
            shape_name = loc_to_shape_name[loc]
            shape = shapes[shape_name]
            line = lines[shape_name]
            if loc == tar_loc:
              shape.vertices = shape_map[tar_shape]
              shape.lineColor = other_color
              line.start = hori_start if tar_line == 'hori' else vert_start
              line.end = hori_end if tar_line == 'hori' else vert_end
            elif loc == dis_loc:
               shape.vertices = shape_map[other_shape]
               shape.lineColor = red if dis_color_condi == 'red' else green
        #       dis_line=random.choice(['hori', 'vert'])
               line_dir = ['hori', 'vert']
               dis_line = line_dir[int(random() * len(line_dir))]
               line.start = hori_start if dis_line == 'hori' else vert_start
               line.end = hori_end if dis_line == 'hori' else vert_end
            else:
                # 其他位置：设置相反的形状和颜色
                shape.vertices = shape_map[other_shape]
                shape.lineColor = other_color
                if i % 2 == 0:  # 偶数索引：水平方向
                    line.start = hori_start
                    line.end = hori_end
                else:  # 奇数索引：竖直方向
                    line.start = vert_start
                    line.end = vert_end
        
        feedback_text = ""
        # keep track of which components have finished
        trialComponents = [fixation, loc1_shape, loc1_line, loc2_shape, loc2_line, loc3_shape, loc3_line, loc4_shape, loc4_line, loc5_shape, loc5_line, loc6_shape, loc6_line, loc7_shape, loc7_line, loc8_shape, loc8_line, resp]
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
            
            # *fixation* updates
            if fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixation.frameNStart = frameN  # exact frame index
                fixation.tStart = t  # local t and not account for scr refresh
                fixation.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation, 'tStartRefresh')  # time at next scr refresh
                fixation.setAutoDraw(True)
            if fixation.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixation.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    fixation.tStop = t  # not accounting for scr refresh
                    fixation.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(fixation, 'tStopRefresh')  # time at next scr refresh
                    fixation.setAutoDraw(False)
            
            # *loc1_shape* updates
            if loc1_shape.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                loc1_shape.frameNStart = frameN  # exact frame index
                loc1_shape.tStart = t  # local t and not account for scr refresh
                loc1_shape.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(loc1_shape, 'tStartRefresh')  # time at next scr refresh
                loc1_shape.setAutoDraw(True)
            if loc1_shape.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > loc1_shape.tStartRefresh + 3.0-frameTolerance:
                    # keep track of stop time/frame for later
                    loc1_shape.tStop = t  # not accounting for scr refresh
                    loc1_shape.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(loc1_shape, 'tStopRefresh')  # time at next scr refresh
                    loc1_shape.setAutoDraw(False)
            
            # *loc1_line* updates
            if loc1_line.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                loc1_line.frameNStart = frameN  # exact frame index
                loc1_line.tStart = t  # local t and not account for scr refresh
                loc1_line.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(loc1_line, 'tStartRefresh')  # time at next scr refresh
                loc1_line.setAutoDraw(True)
            if loc1_line.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > loc1_line.tStartRefresh + 3.0-frameTolerance:
                    # keep track of stop time/frame for later
                    loc1_line.tStop = t  # not accounting for scr refresh
                    loc1_line.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(loc1_line, 'tStopRefresh')  # time at next scr refresh
                    loc1_line.setAutoDraw(False)
            
            # *loc2_shape* updates
            if loc2_shape.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                loc2_shape.frameNStart = frameN  # exact frame index
                loc2_shape.tStart = t  # local t and not account for scr refresh
                loc2_shape.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(loc2_shape, 'tStartRefresh')  # time at next scr refresh
                loc2_shape.setAutoDraw(True)
            if loc2_shape.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > loc2_shape.tStartRefresh + 3.0-frameTolerance:
                    # keep track of stop time/frame for later
                    loc2_shape.tStop = t  # not accounting for scr refresh
                    loc2_shape.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(loc2_shape, 'tStopRefresh')  # time at next scr refresh
                    loc2_shape.setAutoDraw(False)
            
            # *loc2_line* updates
            if loc2_line.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                loc2_line.frameNStart = frameN  # exact frame index
                loc2_line.tStart = t  # local t and not account for scr refresh
                loc2_line.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(loc2_line, 'tStartRefresh')  # time at next scr refresh
                loc2_line.setAutoDraw(True)
            if loc2_line.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > loc2_line.tStartRefresh + 3.0-frameTolerance:
                    # keep track of stop time/frame for later
                    loc2_line.tStop = t  # not accounting for scr refresh
                    loc2_line.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(loc2_line, 'tStopRefresh')  # time at next scr refresh
                    loc2_line.setAutoDraw(False)
            
            # *loc3_shape* updates
            if loc3_shape.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                loc3_shape.frameNStart = frameN  # exact frame index
                loc3_shape.tStart = t  # local t and not account for scr refresh
                loc3_shape.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(loc3_shape, 'tStartRefresh')  # time at next scr refresh
                loc3_shape.setAutoDraw(True)
            if loc3_shape.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > loc3_shape.tStartRefresh + 3.0-frameTolerance:
                    # keep track of stop time/frame for later
                    loc3_shape.tStop = t  # not accounting for scr refresh
                    loc3_shape.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(loc3_shape, 'tStopRefresh')  # time at next scr refresh
                    loc3_shape.setAutoDraw(False)
            
            # *loc3_line* updates
            if loc3_line.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                loc3_line.frameNStart = frameN  # exact frame index
                loc3_line.tStart = t  # local t and not account for scr refresh
                loc3_line.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(loc3_line, 'tStartRefresh')  # time at next scr refresh
                loc3_line.setAutoDraw(True)
            if loc3_line.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > loc3_line.tStartRefresh + 3.0-frameTolerance:
                    # keep track of stop time/frame for later
                    loc3_line.tStop = t  # not accounting for scr refresh
                    loc3_line.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(loc3_line, 'tStopRefresh')  # time at next scr refresh
                    loc3_line.setAutoDraw(False)
            
            # *loc4_shape* updates
            if loc4_shape.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                loc4_shape.frameNStart = frameN  # exact frame index
                loc4_shape.tStart = t  # local t and not account for scr refresh
                loc4_shape.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(loc4_shape, 'tStartRefresh')  # time at next scr refresh
                loc4_shape.setAutoDraw(True)
            if loc4_shape.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > loc4_shape.tStartRefresh + 3.0-frameTolerance:
                    # keep track of stop time/frame for later
                    loc4_shape.tStop = t  # not accounting for scr refresh
                    loc4_shape.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(loc4_shape, 'tStopRefresh')  # time at next scr refresh
                    loc4_shape.setAutoDraw(False)
            
            # *loc4_line* updates
            if loc4_line.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                loc4_line.frameNStart = frameN  # exact frame index
                loc4_line.tStart = t  # local t and not account for scr refresh
                loc4_line.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(loc4_line, 'tStartRefresh')  # time at next scr refresh
                loc4_line.setAutoDraw(True)
            if loc4_line.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > loc4_line.tStartRefresh + 3.0-frameTolerance:
                    # keep track of stop time/frame for later
                    loc4_line.tStop = t  # not accounting for scr refresh
                    loc4_line.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(loc4_line, 'tStopRefresh')  # time at next scr refresh
                    loc4_line.setAutoDraw(False)
            
            # *loc5_shape* updates
            if loc5_shape.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                loc5_shape.frameNStart = frameN  # exact frame index
                loc5_shape.tStart = t  # local t and not account for scr refresh
                loc5_shape.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(loc5_shape, 'tStartRefresh')  # time at next scr refresh
                loc5_shape.setAutoDraw(True)
            if loc5_shape.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > loc5_shape.tStartRefresh + 3.0-frameTolerance:
                    # keep track of stop time/frame for later
                    loc5_shape.tStop = t  # not accounting for scr refresh
                    loc5_shape.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(loc5_shape, 'tStopRefresh')  # time at next scr refresh
                    loc5_shape.setAutoDraw(False)
            
            # *loc5_line* updates
            if loc5_line.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                loc5_line.frameNStart = frameN  # exact frame index
                loc5_line.tStart = t  # local t and not account for scr refresh
                loc5_line.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(loc5_line, 'tStartRefresh')  # time at next scr refresh
                loc5_line.setAutoDraw(True)
            if loc5_line.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > loc5_line.tStartRefresh + 3.0-frameTolerance:
                    # keep track of stop time/frame for later
                    loc5_line.tStop = t  # not accounting for scr refresh
                    loc5_line.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(loc5_line, 'tStopRefresh')  # time at next scr refresh
                    loc5_line.setAutoDraw(False)
            
            # *loc6_shape* updates
            if loc6_shape.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                loc6_shape.frameNStart = frameN  # exact frame index
                loc6_shape.tStart = t  # local t and not account for scr refresh
                loc6_shape.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(loc6_shape, 'tStartRefresh')  # time at next scr refresh
                loc6_shape.setAutoDraw(True)
            if loc6_shape.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > loc6_shape.tStartRefresh + 3.0-frameTolerance:
                    # keep track of stop time/frame for later
                    loc6_shape.tStop = t  # not accounting for scr refresh
                    loc6_shape.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(loc6_shape, 'tStopRefresh')  # time at next scr refresh
                    loc6_shape.setAutoDraw(False)
            
            # *loc6_line* updates
            if loc6_line.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                loc6_line.frameNStart = frameN  # exact frame index
                loc6_line.tStart = t  # local t and not account for scr refresh
                loc6_line.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(loc6_line, 'tStartRefresh')  # time at next scr refresh
                loc6_line.setAutoDraw(True)
            if loc6_line.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > loc6_line.tStartRefresh + 3.0-frameTolerance:
                    # keep track of stop time/frame for later
                    loc6_line.tStop = t  # not accounting for scr refresh
                    loc6_line.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(loc6_line, 'tStopRefresh')  # time at next scr refresh
                    loc6_line.setAutoDraw(False)
            
            # *loc7_shape* updates
            if loc7_shape.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                loc7_shape.frameNStart = frameN  # exact frame index
                loc7_shape.tStart = t  # local t and not account for scr refresh
                loc7_shape.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(loc7_shape, 'tStartRefresh')  # time at next scr refresh
                loc7_shape.setAutoDraw(True)
            if loc7_shape.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > loc7_shape.tStartRefresh + 3.0-frameTolerance:
                    # keep track of stop time/frame for later
                    loc7_shape.tStop = t  # not accounting for scr refresh
                    loc7_shape.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(loc7_shape, 'tStopRefresh')  # time at next scr refresh
                    loc7_shape.setAutoDraw(False)
            
            # *loc7_line* updates
            if loc7_line.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                loc7_line.frameNStart = frameN  # exact frame index
                loc7_line.tStart = t  # local t and not account for scr refresh
                loc7_line.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(loc7_line, 'tStartRefresh')  # time at next scr refresh
                loc7_line.setAutoDraw(True)
            if loc7_line.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > loc7_line.tStartRefresh + 3.0-frameTolerance:
                    # keep track of stop time/frame for later
                    loc7_line.tStop = t  # not accounting for scr refresh
                    loc7_line.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(loc7_line, 'tStopRefresh')  # time at next scr refresh
                    loc7_line.setAutoDraw(False)
            
            # *loc8_shape* updates
            if loc8_shape.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                loc8_shape.frameNStart = frameN  # exact frame index
                loc8_shape.tStart = t  # local t and not account for scr refresh
                loc8_shape.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(loc8_shape, 'tStartRefresh')  # time at next scr refresh
                loc8_shape.setAutoDraw(True)
            if loc8_shape.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > loc8_shape.tStartRefresh + 3.0-frameTolerance:
                    # keep track of stop time/frame for later
                    loc8_shape.tStop = t  # not accounting for scr refresh
                    loc8_shape.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(loc8_shape, 'tStopRefresh')  # time at next scr refresh
                    loc8_shape.setAutoDraw(False)
            
            # *loc8_line* updates
            if loc8_line.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                loc8_line.frameNStart = frameN  # exact frame index
                loc8_line.tStart = t  # local t and not account for scr refresh
                loc8_line.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(loc8_line, 'tStartRefresh')  # time at next scr refresh
                loc8_line.setAutoDraw(True)
            if loc8_line.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > loc8_line.tStartRefresh + 3.0-frameTolerance:
                    # keep track of stop time/frame for later
                    loc8_line.tStop = t  # not accounting for scr refresh
                    loc8_line.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(loc8_line, 'tStopRefresh')  # time at next scr refresh
                    loc8_line.setAutoDraw(False)
            
            # *resp* updates
            waitOnFlip = False
            if resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                resp.frameNStart = frameN  # exact frame index
                resp.tStart = t  # local t and not account for scr refresh
                resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(resp, 'tStartRefresh')  # time at next scr refresh
                resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if resp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > resp.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    resp.tStop = t  # not accounting for scr refresh
                    resp.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(resp, 'tStopRefresh')  # time at next scr refresh
                    resp.status = FINISHED
            if resp.status == STARTED and not waitOnFlip:
                theseKeys = resp.getKeys(keyList=['up', 'left'], waitRelease=False)
                _resp_allKeys.extend(theseKeys)
                if len(_resp_allKeys):
                    resp.keys = _resp_allKeys[-1].name  # just the last key pressed
                    resp.rt = _resp_allKeys[-1].rt
                    # was this correct?
                    if (resp.keys == str(cor_resp)) or (resp.keys == cor_resp):
                        resp.corr = 1
                    else:
                        resp.corr = 0
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
        trials_2.addData('fixation.started', fixation.tStartRefresh)
        trials_2.addData('fixation.stopped', fixation.tStopRefresh)
        trials_2.addData('loc1_shape.started', loc1_shape.tStartRefresh)
        trials_2.addData('loc1_shape.stopped', loc1_shape.tStopRefresh)
        trials_2.addData('loc1_line.started', loc1_line.tStartRefresh)
        trials_2.addData('loc1_line.stopped', loc1_line.tStopRefresh)
        trials_2.addData('loc2_shape.started', loc2_shape.tStartRefresh)
        trials_2.addData('loc2_shape.stopped', loc2_shape.tStopRefresh)
        trials_2.addData('loc2_line.started', loc2_line.tStartRefresh)
        trials_2.addData('loc2_line.stopped', loc2_line.tStopRefresh)
        trials_2.addData('loc3_shape.started', loc3_shape.tStartRefresh)
        trials_2.addData('loc3_shape.stopped', loc3_shape.tStopRefresh)
        trials_2.addData('loc3_line.started', loc3_line.tStartRefresh)
        trials_2.addData('loc3_line.stopped', loc3_line.tStopRefresh)
        trials_2.addData('loc4_shape.started', loc4_shape.tStartRefresh)
        trials_2.addData('loc4_shape.stopped', loc4_shape.tStopRefresh)
        trials_2.addData('loc4_line.started', loc4_line.tStartRefresh)
        trials_2.addData('loc4_line.stopped', loc4_line.tStopRefresh)
        trials_2.addData('loc5_shape.started', loc5_shape.tStartRefresh)
        trials_2.addData('loc5_shape.stopped', loc5_shape.tStopRefresh)
        trials_2.addData('loc5_line.started', loc5_line.tStartRefresh)
        trials_2.addData('loc5_line.stopped', loc5_line.tStopRefresh)
        trials_2.addData('loc6_shape.started', loc6_shape.tStartRefresh)
        trials_2.addData('loc6_shape.stopped', loc6_shape.tStopRefresh)
        trials_2.addData('loc6_line.started', loc6_line.tStartRefresh)
        trials_2.addData('loc6_line.stopped', loc6_line.tStopRefresh)
        trials_2.addData('loc7_shape.started', loc7_shape.tStartRefresh)
        trials_2.addData('loc7_shape.stopped', loc7_shape.tStopRefresh)
        trials_2.addData('loc7_line.started', loc7_line.tStartRefresh)
        trials_2.addData('loc7_line.stopped', loc7_line.tStopRefresh)
        trials_2.addData('loc8_shape.started', loc8_shape.tStartRefresh)
        trials_2.addData('loc8_shape.stopped', loc8_shape.tStopRefresh)
        trials_2.addData('loc8_line.started', loc8_line.tStartRefresh)
        trials_2.addData('loc8_line.stopped', loc8_line.tStopRefresh)
        # check responses
        if resp.keys in ['', [], None]:  # No response was made
            resp.keys = None
            # was no response the correct answer?!
            if str(cor_resp).lower() == 'none':
               resp.corr = 1;  # correct non-response
            else:
               resp.corr = 0;  # failed to respond (incorrectly)
        # store data for trials_2 (TrialHandler)
        trials_2.addData('resp.keys',resp.keys)
        trials_2.addData('resp.corr', resp.corr)
        if resp.keys != None:  # we had a response
            trials_2.addData('resp.rt', resp.rt)
        trials_2.addData('resp.started', resp.tStartRefresh)
        trials_2.addData('resp.stopped', resp.tStopRefresh)
        # 判断按键是否正确
        if resp.keys is None:  # 没有按键
            feedback_text = "请及时反应，集中注意力！"
        elif resp.keys != cor_resp:  # 按键错误
            feedback_text = "错误！"
        else:  # 按键正确
            feedback_text = ""  # 不显示反馈
            
        
        
        # ------Prepare to start Routine "feedback"-------
        continueRoutine = True
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        text_4.setText(feedback_text)
        if feedback_text == "":
            continueRoutine = False
        # keep track of which components have finished
        feedbackComponents = [text_4]
        for thisComponent in feedbackComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        feedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "feedback"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = feedbackClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=feedbackClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_4* updates
            if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_4.frameNStart = frameN  # exact frame index
                text_4.tStart = t  # local t and not account for scr refresh
                text_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
                text_4.setAutoDraw(True)
            if text_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_4.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    text_4.tStop = t  # not accounting for scr refresh
                    text_4.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_4, 'tStopRefresh')  # time at next scr refresh
                    text_4.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in feedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "feedback"-------
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials_2.addData('text_4.started', text_4.tStartRefresh)
        trials_2.addData('text_4.stopped', text_4.tStopRefresh)
        
        # ------Prepare to start Routine "iti"-------
        continueRoutine = True
        # update component parameters for each repeat
        iti_blank.setText(' ')
        # keep track of which components have finished
        itiComponents = [iti_blank]
        for thisComponent in itiComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        itiClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "iti"-------
        while continueRoutine:
            # get current time
            t = itiClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=itiClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *iti_blank* updates
            if iti_blank.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                iti_blank.frameNStart = frameN  # exact frame index
                iti_blank.tStart = t  # local t and not account for scr refresh
                iti_blank.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(iti_blank, 'tStartRefresh')  # time at next scr refresh
                iti_blank.setAutoDraw(True)
            if iti_blank.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > iti_blank.tStartRefresh + 0.5 + random() * 0.25-frameTolerance:
                    # keep track of stop time/frame for later
                    iti_blank.tStop = t  # not accounting for scr refresh
                    iti_blank.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(iti_blank, 'tStopRefresh')  # time at next scr refresh
                    iti_blank.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in itiComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "iti"-------
        for thisComponent in itiComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials_2.addData('iti_blank.started', iti_blank.tStartRefresh)
        trials_2.addData('iti_blank.stopped', iti_blank.tStopRefresh)
        # the Routine "iti" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 120.0 repeats of 'trials_2'
    
    # get names of stimulus parameters
    if trials_2.trialList in ([], [None], None):
        params = []
    else:
        params = trials_2.trialList[0].keys()
    # save data for this loop
    trials_2.saveAsExcel(filename + '.xlsx', sheetName='trials_2',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # ------Prepare to start Routine "break_3"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_3.keys = []
    key_resp_3.rt = []
    _key_resp_3_allKeys = []
    current_trial = 0
    shuffle(trial_list_new)
    block_num=block_num+1
    if block_num == 5:
        continueRoutine = False
        
    thisExp.addData('block_num', block_num)
    # keep track of which components have finished
    break_3Components = [text_3, key_resp_3]
    for thisComponent in break_3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    break_3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "break_3"-------
    while continueRoutine:
        # get current time
        t = break_3Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=break_3Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_3* updates
        if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            text_3.setAutoDraw(True)
        
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
            theseKeys = key_resp_3.getKeys(keyList=['space'], waitRelease=False)
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
        for thisComponent in break_3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "break_3"-------
    for thisComponent in break_3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_3.addData('text_3.started', text_3.tStartRefresh)
    trials_3.addData('text_3.stopped', text_3.tStopRefresh)
    # check responses
    if key_resp_3.keys in ['', [], None]:  # No response was made
        key_resp_3.keys = None
    trials_3.addData('key_resp_3.keys',key_resp_3.keys)
    if key_resp_3.keys != None:  # we had a response
        trials_3.addData('key_resp_3.rt', key_resp_3.rt)
    trials_3.addData('key_resp_3.started', key_resp_3.tStartRefresh)
    trials_3.addData('key_resp_3.stopped', key_resp_3.tStopRefresh)
    # the Routine "break_3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 6.0 repeats of 'trials_3'

# get names of stimulus parameters
if trials_3.trialList in ([], [None], None):
    params = []
else:
    params = trials_3.trialList[0].keys()
# save data for this loop
trials_3.saveAsExcel(filename + '.xlsx', sheetName='trials_3',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "end"-------
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
endComponents = [end_2]
for thisComponent in endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "end"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = endClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=endClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *end_2* updates
    if end_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_2.frameNStart = frameN  # exact frame index
        end_2.tStart = t  # local t and not account for scr refresh
        end_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_2, 'tStartRefresh')  # time at next scr refresh
        end_2.setAutoDraw(True)
    if end_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > end_2.tStartRefresh + 2.0-frameTolerance:
            # keep track of stop time/frame for later
            end_2.tStop = t  # not accounting for scr refresh
            end_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(end_2, 'tStopRefresh')  # time at next scr refresh
            end_2.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('end_2.started', end_2.tStartRefresh)
thisExp.addData('end_2.stopped', end_2.tStopRefresh)

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
