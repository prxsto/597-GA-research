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

    try:
        polygon = rs.ObjectsByLayer('polygon')
        for i in pts:
            if rs.IsPointOnSurface(polygon, pts[i]):
                j+=1
        if j == 4:
            polyline = rs.AddPolyline([pt1, pt2, pt3, pt4, pt1])
            area = rs.CurveArea(polyline)[0]
    except:
        area = 0
    rs.Redraw()
    return area

fit_function = fit
fit_type = 'max'
num_var = 8 # num in x
boundaries = [(0, 25) for _ in range(num_var)]
num_bin_dig = [8] * num_var # stops between 0 and 1, in binary digits
output_path = os.path.join(os.path.dirname(__file__), 'output')

ga = ga(fit_function,
        fit_type,
        num_var,
        boundaries,
        num_gen=10,
        num_pop=200,
        num_elite=10,
        mutation_probability=0.08,
        n_cross=3,
        num_bin_dig=num_bin_dig,
        min_fit=None,
        output_path=output_path,
        print_refresh=1)

# x = ga.current_pop['scaled'][ga.best_individual_index]
# fit = arch2(x, drawf=True)
# print('fit', fit)
