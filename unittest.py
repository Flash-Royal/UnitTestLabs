#import sys
# sys.path.append('E:/всякое/new')

import elevator as elevator
import pytest
from unittest.mock import create_autospec

def testCleanGrain():
    assert elevator.cleanGrain() == -1000

def testDispatchGrain():
    elevator.goodGrain = 1000
    elevator.grainKgCost = 10
    elevator.currentExpense = 0
    elevator.currentProfit = 0
    assert elevator.dispatchGrain() == 5000

def testDesinfectGrain():
    elevator.taxeGrain = 1000
    elevator.taxes = 500
    elevator.flag = 1
    elevator.currentProfit = 0
    assert elevator.desinfectGrain() == -11500

def testProgress():
    elevator.currentProfit = 0
    elevator.iters = 3
    elevator.flag = 1
    elevator.taxeGrain = 1000
    elevator.grainKgCost = 20
    assert elevator.progress() == 0

def testRecieveGrain():
    elevator.flag = 2
    elevator.taxes = 5000
    assert elevator.recieveGrain() == -15000

def testDrawGraph():
    coords = [[1,2],[3,4],[1.4,5.2],[2.5,1.2],[1,5.6]]
    assert elevator.drawGraph(coords) == [[1,3,1.4,2.5],[2,4,5.2,1.2]]

def testSysError():
    assert elevator.syserror() == 2

def testArrowMove():
    mass = [100,200,500,350,250,50]
    assert elevator.arrowMove(mass, 50, 30) == [150,230,550,380,300,80]

mockFunc = create_autospec(elevator.getStage, return_value = "Cleaning")
def testGetStage():
    assert mockFunc() == "Cleaning"
