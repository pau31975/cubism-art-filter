import cv2 as cv
import numpy as np
import math
from random import randrange
from matplotlib import pyplot as plt

def show(cimg, numc):
    def centroid(k, cimg):
        c = []
        x = 0
        while len(c) < k:
            i = randrange(cimg.shape[0])
            j = randrange(cimg.shape[1])
            if (i,j) not in c:
                c += [(i,j)]
        return c

    def assign(c, cimg):
        d = {}
        for i in range(cimg.shape[0]):
            for j in range(cimg.shape[1]):
                lisl = []
                for x in c:
                    l = (((x[0]-i)**2)+((x[1]-j)**2))**(0.5)
                    lisl += [l]
                    if l == min(lisl):
                        xc = x
                if xc not in d:
                    d[xc] = [(i,j)]
                if xc in d:
                    d[xc] += [(i,j)]
        return d

    def avcolor(d, cimg):
        nd = {}
        for i in d:
            c = 0
            r = 0
            g = 0
            b = 0
            for j in d[i]:
                r += cimg[j[0],j[1],0]
                g += cimg[j[0],j[1],1]
                b += cimg[j[0],j[1],2]
                c += 1
            avr = r/c
            avg = g/c
            avb = b/c
            for k in d[i]:
                if (avr,avg,avb) not in nd:
                    nd[(avr,avg,avb)] = [k]
                if (avr,avg,avb) in nd:
                    nd[(avr,avg,avb)] += [k]
        return nd

    def update(nd, cimg):
        for i in nd:
            for j in nd[i]:
                cimg.itemset((j[0],j[1],0),i[0])
                cimg.itemset((j[0],j[1],1),i[1])
                cimg.itemset((j[0],j[1],2),i[2])
    c = centroid(numc, cimg)
    d = assign(c, cimg)
    nd = avcolor(d, cimg)
    update(nd, cimg)
    plt.imshow(cimg)
    plt.axis('off')
    plt.show()

def compare(cimg, imgo, numc):
    def centroid(k, cimg):
        c = []
        x = 0
        while len(c) < k:
            i = randrange(cimg.shape[0])
            j = randrange(cimg.shape[1])
            if (i,j) not in c:
                c += [(i,j)]
        return c

    def assign(c, cimg):
        d = {}
        for i in range(cimg.shape[0]):
            for j in range(cimg.shape[1]):
                lisl = []
                for x in c:
                    l = (((x[0]-i)**2)+((x[1]-j)**2))**(0.5)
                    lisl += [l]
                    if l == min(lisl):
                        xc = x
                if xc not in d:
                    d[xc] = [(i,j)]
                if xc in d:
                    d[xc] += [(i,j)]
        return d

    def avcolor(d, cimg):
        nd = {}
        for i in d:
            c = 0
            r = 0
            g = 0
            b = 0
            for j in d[i]:
                r += cimg[j[0],j[1],0]
                g += cimg[j[0],j[1],1]
                b += cimg[j[0],j[1],2]
                c += 1
            avr = r/c
            avg = g/c
            avb = b/c
            for k in d[i]:
                if (avr,avg,avb) not in nd:
                    nd[(avr,avg,avb)] = [k]
                if (avr,avg,avb) in nd:
                    nd[(avr,avg,avb)] += [k]
        return nd

    def update(nd, cimg):
        for i in nd:
            for j in nd[i]:
                cimg.itemset((j[0],j[1],0),i[0])
                cimg.itemset((j[0],j[1],1),i[1])
                cimg.itemset((j[0],j[1],2),i[2])
    
    c = centroid(numc, cimg)
    d = assign(c, cimg)
    nd = avcolor(d, cimg)
    update(nd, cimg)

    plt.subplot(1,2,1)
    plt.imshow(imgo)
    plt.axis('off')
    plt.title('original')

    plt.subplot(1,2,2)
    plt.imshow(cimg)
    plt.axis('off')
    plt.title('cubism')

    plt.show()