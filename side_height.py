# coding=utf-8
import copy

def GetRatio(edge,height):
    outImage = copy.copy(edge)  # 객체 복사하기

    #사진의 픽셀 수
    rowNumber = 840L
    colNumber = 641L

    count=0

    print("|--- in GetRatio ---------|")

    up=0 #인체의 흑색과 백색 바이너리에대한 머리 좌표 값을 받아온다.
    down=0 # 인체의 바닥 부분의 좌표값을 받아온다.

    for i in range(0,rowNumber):
        data=outImage[i] # 행의 첫번째 주소를 가져온다.

        for j in range(0,colNumber):
            if 255 in data[j]:
                up=i
                break
        if up>0:
            break

    #아래에서 부터 쭉 올라온다.
    for i in range(rowNumber-1,0,-1):
        data=outImage[i]
        for j in range(0,colNumber):
            if 255 in data[j]:
                down=i
                break
        if down>0:
            break



    Pix_Ratio= height*1.0/(down-up+1)

    print("|------- Side  ---------|")
    print("head position: %d"+up)
    print("foot position: %d"+down)




