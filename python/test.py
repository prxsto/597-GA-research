import os
import rhinoscriptsyntax as rs
from genetic_algo import ga
for i in range(50): print('')

polygon = rs.ObjectsByLayer('polygon')
rs.MoveObject(polygon, [1,2,3])
