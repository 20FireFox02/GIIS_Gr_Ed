from wind_init_module import display
from constant_module import WHITE
from drawing.draw_menu_module import draw_menu

from frst_lines_alg.brezen_alg_module import Brz_alg
from frst_lines_alg.dig_dif_an_module import Dda
from frst_lines_alg.wu_alg_module import Wu_alg

from sec_lines_alg.brezen_circle_alg_module import Brz_circle_alg
from sec_lines_alg.ellipse_alg_module import Ellipse_alg
from sec_lines_alg.giperb_alg_module import Giperb_alg
from sec_lines_alg.parab_alg_module import Parab_alg

from curve_alg.hermit_inter_module import Herm_inter
from curve_alg.bezier_forms_module import Bez_form
from curve_alg.b_spline_module import B_spl

from classes.line_module import Line
lines=[]

#Line([[29,29],[29,48],[53,29],[79,29]],7)
DRAWING_ALG=[Dda(),Brz_alg(),Wu_alg(),Brz_circle_alg(),Ellipse_alg(),Giperb_alg(),Parab_alg(),Herm_inter(),Bez_form(),B_spl()]
"""pg.font.init()
smallfont = pg.font.SysFont('Corbel',25) 
dda_t=smallfont.render('dda',True,BLACK)
brz_t=smallfont.render('brezen',True,BLACK)
wu_t=smallfont.render('wu',True,BLACK)

text=dda_t
"""
def draw(check):
    display.fill(WHITE)
    #draw_menu(display,menu_click)
    draw_menu()
    
    for line in  lines[:-1]:
        DRAWING_ALG[line.draw_alg].draw_line(line.points,lambda:True)
    #DRAWING_ALG[lines[-1].draw_alg].draw_line(lines[-1].points,check)
    try:
        DRAWING_ALG[lines[-1].draw_alg].draw_line(lines[-1].points,check)
    except:
        print("Error last line drawing")
    draw_menu()