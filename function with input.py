import math

def paint_calc(height,width,coverage):
    total_paint = (height * width)/coverage
    round_up_paint = math.ceil(total_paint)
    print(f"You will need {round_up_paint} cans of paint")

h = int(input("enter wall height"))
w = int(input("enter the width of wall"))
c = int(input("coverage per can"))
paint_calc(height=h,width=w,coverage=c)