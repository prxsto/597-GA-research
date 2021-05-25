import os
import rhinoscriptsyntax as rs
from genetic_algo import ga
for i in range(50): print('')

def fit(x):
    rs.DeleteObjects(rs.ObjectsByLayer('default'))
    pt1 = x[0], x[1]
    pt2 = x[2], x[3]
    pt3 = x[4], x[5]
    pt4 = x[6], x[7]
    pts = [pt1, pt2, pt3, pt4]

    # try:
    polygon = rs.ObjectsByLayer('polygon')
    j = 0
    for i in range(len(pts)):
        if rs.IsPointOnSurface(polygon, pts[i]):
            j+=1
            print(j)
    if j == 4:
        polyline = rs.AddPolyline([pt1, pt2, pt3, pt4, pt1])
        area = rs.CurveArea(polyline)[0]
        rs.Redraw()
        return area
    else:
        return 0
    # except:
    #     area = 0
    #     # print('oopsies')
    rs.Redraw()
    return 0

pt1 = rs.ObjectsByLayer('pt1')[0]
pt1 = rs.PointCoordinates(pt1)
pt2 = rs.ObjectsByLayer('pt2')[0]
pt2 = rs.PointCoordinates(pt2)
pt3 = rs.ObjectsByLayer('pt3')[0]
pt3 = rs.PointCoordinates(pt3)
pt4 = rs.ObjectsByLayer('pt4')[0]
pt4 = rs.PointCoordinates(pt4)

x = [pt1[0], pt1[1], pt2[0], pt2[1], pt3[0], pt3[1], pt4[0], pt4[1]]

a = fit(x)
print(a)
