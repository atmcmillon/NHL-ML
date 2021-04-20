#NHL Season Prediction Machine
#Austin McMillon
#This single-layer algorithm analyzes game outcome patterns from
#NHL teams, with the current example being the Vegas Golden Knights.
#It can take an entire team's history to generate 1 of 3 possible
#outcomes for 82 regular season games(Win, Loss, OverTime Loss),
#based solely on the record alone.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

record = pd.read_csv('vgk_record_1718.csv')
#print(record1718)

recordshape = record.shape
recordindex = record.index
#R: 82, C: 2
#So the number of transitions from item to item
#in a list of size n will be n - 1 transitions

wlhist = record["Vegas Golden Knights W/L History"]
wlhist = wlhist.to_numpy()
#print(wlhist)

wlbi = record["W/L as Binary"]
wlbi = wlbi.to_numpy()

wfork = {'W': 0, 'L': 0, 'OTL': 0}
lfork = {'W': 0, 'L': 0, 'OTL': 0}
ofork = {'W': 0, 'L': 0, 'OTL': 0}

w = 0
l = 0
otl = 0

tm = np.zeros((3, 3))
x0 = np.zeros(3)
#Preallocating my matrices

for i in wlhist:
    if i is 'W':
        w += 1
    elif i is 'L':
        l += 1
    else:
        otl += 1

x0 = [(w / len(wlhist)), (l / len(wlhist)), (otl / len(wlhist))]
#print(x0)

for i in range(1, len(wlhist)):
    if wlhist[i - 1] is 'W':
        if wlhist[i] is 'W':
            wfork['W'] += 1
        elif wlhist[i] is 'L':
            wfork['L'] += 1
        else:
            wfork['OTL'] += 1
    #Checks for win -> new state
    elif wlhist[i - 1] is 'L':
        if wlhist[i] is 'W':
            lfork['W'] += 1
        elif wlhist[i] is 'L':
            lfork['L'] += 1
        else:
            lfork['OTL'] += 1
    #Checks for lose -> new state
    else:
        if wlhist[i] is 'W':
            ofork['W'] += 1
        elif wlhist[i] is 'L':
            ofork['L'] += 1
        else:
            ofork['OTL'] += 1
    #Checks for overtime loss -> new state
#print(wfork, lfork, ofork)

ww = wfork['W'] / (wfork['W'] + wfork['L'] + wfork['OTL'])
wl = wfork['L'] / (wfork['W'] + wfork['L'] + wfork['OTL'])
wo = wfork['OTL'] / (wfork['W'] + wfork['L'] + wfork['OTL'])
lw = lfork['W'] / (lfork['W'] + lfork['L'] + lfork['OTL'])
ll = lfork['L'] / (lfork['W'] + lfork['L'] + lfork['OTL'])
lo = lfork['OTL'] / (lfork['W'] + lfork['L'] + lfork['OTL'])
ow = ofork['W'] / ((ofork['W'] + ofork['L'] + ofork['OTL']))
ol = ofork['L'] / ((ofork['W'] + ofork['L'] + ofork['OTL']))
oo = ofork['OTL'] / ((ofork['W'] + ofork['L'] + ofork['OTL']))

tm[0][0] = ww
tm[0][1] = wl
tm[0][2] = wo
tm[1][0] = lw
tm[1][1] = ll
tm[1][2] = lo
tm[2][0] = ow
tm[2][1] = ol
tm[2][2] = oo
#print(tm)

wlhist2 = []

a = np.zeros((82, 3))
#Gives me a list of state matrices for an 82-game NHL regular season

rando = np.random.rand(82)
wdif = np.zeros(82)
ldif = np.zeros(82)
odif = np.zeros(82)
#Gives me 82 random numbers between 0 and 1, so I can find the closest
#probability to each number to print out a matching result in the next
#NHL season. The computer essentially makes a 'guess.'

a[0] = np.matmul(x0, tm)

for i in range(1, 82):
    a[i] = np.matmul(a[i - 1], tm)

    wdif[i] = abs(rando[i] - a[i][0])
    ldif[i] = abs(rando[i] - a[i][1])
    odif[i] = abs(rando[i] - a[i][2])

    if wdif[i] < ldif[i] and wdif[i] < odif[i]:
        wlhist2.append('W')
    elif ldif[i] < wdif[i] and ldif[i] < odif[i]:
        wlhist2.append('L')
    else:
        wlhist2.append('OTL')

print(wlhist2)
    