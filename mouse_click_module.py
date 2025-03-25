from menu_var_module import buttons
import var_module

def mouse_click(mouse_pos):
    for menu_num in var_module.menu_nums:
        for num in range(len(buttons[menu_num])):
            if buttons[menu_num][num].begin_crd[0]<=mouse_pos[0]<=buttons[menu_num][num].get_end_crd(0) and\
               buttons[menu_num][num].begin_crd[1]<=mouse_pos[1]<=buttons[menu_num][num].get_end_crd(1):

                var_module.press_button=num+1
                buttons[menu_num][num].click()
                return True