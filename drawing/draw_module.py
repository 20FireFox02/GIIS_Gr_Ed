from frst_lines_alg.brezen_alg_module import *
from frst_lines_alg.dig_dif_an_module import *
from frst_lines_alg.wu_alg_module import *

from sec_lines_alg.brezen_circle_alg_module import *
from sec_lines_alg.ellipse_alg_module import *
from sec_lines_alg.giperb_alg_module import *
from sec_lines_alg.parab_alg_module import *

from wind_init_module import display
from drawing.draw_menu_module import draw_menu
from constant_module import WHITE

lines=[]

drawing_alg=[Dda(),Brz_alg(),Wu_alg(),Brz_circle_alg(),Ellipse_alg(),Giperb_alg(),Parab_alg()]
"""pg.font.init()
smallfont = pg.font.SysFont('Corbel',25) 
dda_t=smallfont.render('dda',True,BLACK)
brz_t=smallfont.render('brezen',True,BLACK)
wu_t=smallfont.render('wu',True,BLACK)

text=dda_t
"""
def draw(check):
    display.fill(WHITE)
    draw_menu()
    for line in  lines[:-1]:
        drawing_alg[line.draw_alg].draw_line(line.points,lambda:True)
    try:
        drawing_alg[lines[-1].draw_alg].draw_line(lines[-1].points,check)
    except:
        print("Error last line drawing")
    draw_menu()