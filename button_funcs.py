import var_module as vm
import work_envir.var_work as vw
def set_menu():
    if len(vm.menu_nums)==1:
        vm.menu_nums.append(vm.press_button)
    else:vm.menu_nums.pop()

def dda_btn():
    vm.menu_nums.pop()
    print(vm.menu_nums)
    vw.work_env=vw.WE_2D
    vw.work_env.alg_num=0

def brz_btn():
    vm.menu_nums.pop()
    vw.work_env=vw.WE_2D
    vw.work_env.alg_num=1

def wu_btn():
    vm.menu_nums.pop()
    vw.work_env=vw.WE_2D
    vw.work_env.alg_num=2

def brz_crcl_btn():
    vm.menu_nums.pop()
    vw.work_env=vw.WE_2D
    vw.work_env.alg_num=3

def ell_btn():
    vm.menu_nums.pop()
    vw.work_env=vw.WE_2D
    vw.work_env.alg_num=4

def gprbl_btn():
    vm.menu_nums.pop()
    vw.work_env=vw.WE_2D
    vw.work_env.alg_num=5

def prbl_btn():
    vm.menu_nums.pop()
    vw.work_env=vw.WE_2D
    vw.work_env.alg_num=6

def hrmin_btn():
    vm.menu_nums.pop()
    vw.work_env=vw.WE_2D
    vw.work_env.alg_num=7

def bzfrm_btn():
    vm.menu_nums.pop()
    vw.work_env=vw.WE_2D
    vw.work_env.alg_num=8

def bspl_btn():
    vm.menu_nums.pop()
    vw.work_env=vw.WE_2D
    vw.work_env.alg_num=9

def we_3d_btn():
    vw.work_env=vw.WE_3D

def pol_btn():
    vm.menu_nums.pop()
    vw.work_env=vw.WE_PL
    vw.work_env.alg_num=0

def greh_btn():
    vm.menu_nums.pop()
    vw.work_env=vw.WE_PL
    vw.work_env.alg_num=1

def djarw_btn():
    vm.menu_nums.pop()
    vw.work_env=vw.WE_PL
    vw.work_env.alg_num=2
