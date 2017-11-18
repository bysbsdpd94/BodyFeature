# coding=utf-8
import copy

#허리는 왼쪽 허리점과 오른쪽 허리 점을 찾아 반환하면 된다.
#해당 알고리즘은 겨드랑이를 찾은 이후에 진행될 예정임

class waistpoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def GetWaist(edge):

    #이미지를 복사한다.
    outImage = copy.copy(edge)  # 객체 복사하기

    rowNumber = 840L
    colNumber = 641L


