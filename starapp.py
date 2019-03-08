
# coding: utf-8


import tkinter as tk
import celestials as c
from random import randint



star = c.Star()



def max_Coord(star, lcx, lcy, rcx, rcy):
    left = True
    up = 1
    for item in star.celestials:
        if left == True:
            lcx = lcx - item.radius
            left = False
            if up == 1:

                lcy = lcy + item.radius*4
                up = randint(0,1)
                lcx = lcx - star.radius/2
                lcy = lcy + star.radius/2

            else:

                lcy = lcy - item.radius*4
                lcx = lcx - star.radius/2
                lcy = lcy - star.radius/2
        else:
            rcx = rcx + item.radius*4
            left = True
            if up == 1:
                rcy = rcy + item.radius*4
                up = randint(0,1)
                rcx = rcx + star.radius/2
                rcy = rcy + star.radius/2
            else:

                rcy = rcy - item.radius*4
                up = randint(0,1)
                rcx = rcx + star.radius/2
                rcy = rcy - star.radius/2
    return lcx, lcy, rcx, rcy
    



for item in star.celestials:
    print(item.category, item.radius)



master = tk.Tk()
x = 600
y = 600
cx = x/2
cy = y/2
def get_pixels(cel, x):
    return (cel.radius*x)
w = tk.Canvas(master, width=x, height=y)

def get_max(cel, x):
    m = 0.0
    for item in cel.celestials:
        if item.radius > m:
            m = item.radius
    return (m*x)
w.pack()
orbital = get_pixels(star, x)/1.5
star_image = w.create_oval(cx - get_pixels(star, x), cy - get_pixels(star, x), cx + get_pixels(star, x), cy + get_pixels(star, x))

left = True
up = 0
m = get_max(star, x)/1.5
lcx = cx - orbital
lcy = cy - orbital
rcx = cx + orbital
rcy = cy + orbital



for item in star.celestials:
    cel_radius = get_pixels(item, x)
    if left == True:
        lcx = lcx - m
        
        left = False
        if up == 1:
            print("initializing planet")
            print(star.celestials.index(item))
            lcy = lcy - cel_radius
            w.create_oval(lcx, lcy, lcx - cel_radius, lcy - cel_radius)
            up = 0
            lcx = lcx - m
            lcy = lcy - m
            rcx = rcx + m
            rcy = rcy + m
            
        else:
            print("initializing planet")
            print(star.celestials.index(item))
            lcy = lcy - cel_radius
            w.create_oval(lcx, lcy, lcx - cel_radius, lcy - cel_radius)
            lcx = lcx - m
            lcy = lcy - m
            rcx = rcx + m
            rcy = rcy + m
            up = 1
    else:
        rcx = rcx + cel_radius
        left = True
        if up == 1:
            print("initializing planet")
            print(star.celestials.index(item))
            rcy = rcy + cel_radius
            
            w.create_oval(rcx, rcy, rcx + cel_radius, rcy + cel_radius)
            up = 0
            lcx = lcx - m
            lcy = lcy - m
            rcx = rcx + m
            rcy = rcy + m
        else:
            print("initializing planet")
            print(star.celestials.index(item))
            rcy = rcy + cel_radius
            w.create_oval(rcx, rcy, rcx + cel_radius, rcy + cel_radius)
            up = 1
            lcx = lcx - m
            lcy = lcy - m
            rcx = rcx + m
            rcy = rcy + m

w.pack()
tk.mainloop()




star.category





tcx = cx - star.radius
tcy = cy - star.radius
trcx = cx + star.radius
trcy = cy + star.radius

def determineRadius(cel, w, h, whitespace):
    '''
    given a celestial return the number of pixels for the objects radius
    '''
    r = 0
    if category == 'main_sequence':
    elif category == 'blackhole':
    elif category == 'dwarf':
    elif category == 'neutron':
    elif category == ''


    

