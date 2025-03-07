from classes.algoritm_module import Algoritm

class Herm_inter(Algoritm):
    def draw_line(b_crd,e_crd,check):
        v1,v2=(),()
        r1,r2=(v1[0]-b_crd[0],v1[1]-b_crd[1]),(v2[0]-e_crd[0],v2[1]-e_crd[1])
        