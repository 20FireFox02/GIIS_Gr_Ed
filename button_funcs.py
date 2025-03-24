import var_module
def set_menu():
    if len(var_module.menu_nums)==1:
        var_module.menu_nums.append(var_module.press_button)
    else:var_module.menu_nums.pop()

def dda_btn():
    var_module.menu_nums.pop()
    var_module.alg_num=0

def brz_btn():
    var_module.menu_nums.pop()
    var_module.alg_num=1

def wu_btn():
    var_module.menu_nums.pop()
    var_module.alg_num=2

def brz_crcl_btn():
    var_module.menu_nums.pop()
    var_module.alg_num=3

def ell_btn():
    var_module.menu_nums.pop()
    var_module.alg_num=4

def gprbl_btn():
    var_module.menu_nums.pop()
    var_module.alg_num=5

def prbl_btn():
    var_module.menu_nums.pop()
    var_module.alg_num=6

def hrmin_btn():
    var_module.menu_nums.pop()
    var_module.alg_num=7

def bzfrm_btn():
    var_module.menu_nums.pop()
    var_module.alg_num=8

def bspl_btn():
    var_module.menu_nums.pop()
    var_module.alg_num=9