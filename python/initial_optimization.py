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
            # print(j)
    if j == 4:
        polyline = rs.AddPolyline([pt1, pt2, pt3, pt4, pt1])
        area = rs.CurveArea(polyline)[0]
        rs.Redraw()
        return area
    # except:
    #     area = 0
    #     # print('oopsies')
    rs.Redraw()
    return 0

fit_function = fit
fit_type = 'max'
num_var = 8 # num in x
boundaries = [(0, 12.5), (0,12.5), (12.5, 25), (0, 12.5), (12.5, 25), (12.5, 25), (0, 12.5), (12.5, 25)]
num_bin_dig = [6] * num_var # stops between 0 and 1, in binary digits
output_path = os.path.join(os.path.dirname(__file__), 'output')

ga = ga(fit_function,
        fit_type,
        num_var,
        boundaries,
        num_gen=20,
        num_pop=50,
        num_elite=10,
        mutation_probability=0.01,
        n_cross=1,
        num_bin_dig=num_bin_dig,
        min_fit=None,
        output_path=output_path,
        print_refresh=1)

# x = ga.current_pop['scaled'][ga.best_individual_index]
# fit = arch2(x, drawf=True)
# print('fit', fit)
