# coding=utf-8

import hand as h
import armpoint as ap
from collections import namedtuple
import numpy as np

#몸을 담는 튜플 혹은 클래스 제작이 필요함
#임의로 일단 namedTupel을 이용하여 저장하겠음-> 손만 들어 있을 예정

#bodyp = namedtuple("bodyp", "my_hand")


class bodyp:
    my_hand=0
    my_armpit=0


def GetBodyPosition(Dst):

    #몸에 대한 point를 담는 class
    body=bodyp

    #아직 해당 인자가 어디서 사용되는지 파악을 하지 못했음
    # rowNumber=Dst.rows
    # colNumber=Dst.cols

    print("|--- in GetBodyPosition ---------|")
    # hand_tmp=h.hand
    print("|--- 손에 대한 알고리즘 입니다. ---------|")


    hand_tmp=h.GetHand(Dst)
    body.my_hand=hand_tmp

    #다리에 대한 알고리즘이 작성되어야한다.
    print("|--- 겨드랑이에 대한 알고리즘 입니다. ---------|")
    start_line=ap.find_armpit_start_line(0,0)















