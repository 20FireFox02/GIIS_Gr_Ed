from classes.button_module import Button
from classes.menu_module import Menu
from button_funcs import *

EQUPM_BUTTON_SIZE=(40,40)
ALG_BUTTON_SIZE=(90,20)

buttons=[[Button((5,5),EQUPM_BUTTON_SIZE,lambda:set_menu()),\
          Button((5,50),EQUPM_BUTTON_SIZE,lambda:set_menu()),\
          Button((5,95),EQUPM_BUTTON_SIZE,lambda:set_menu()),\
          Button((5,140),EQUPM_BUTTON_SIZE,lambda:we_3d_btn()),\
          Button((5,185),EQUPM_BUTTON_SIZE,lambda:set_menu()),\
          Button((5,230),EQUPM_BUTTON_SIZE,lambda:set_menu()),\
          Button((5,750),EQUPM_BUTTON_SIZE,lambda:True)],\
          
          [Button((50,5),ALG_BUTTON_SIZE,lambda:dda_btn()),\
          Button((50,30),ALG_BUTTON_SIZE,lambda:brz_btn()),\
          Button((50,55),ALG_BUTTON_SIZE,lambda:wu_btn())],\
          
          [Button((50,50),ALG_BUTTON_SIZE,lambda:brz_crcl_btn()),\
          Button((50,75),ALG_BUTTON_SIZE,lambda:ell_btn()),\
          Button((50,100),ALG_BUTTON_SIZE,lambda:gprbl_btn()),\
          Button((50,125),ALG_BUTTON_SIZE,lambda:prbl_btn())],\
          
          [Button((50,95),ALG_BUTTON_SIZE,lambda:hrmin_btn()),\
          Button((50,120),ALG_BUTTON_SIZE,lambda:bzfrm_btn()),\
          Button((50,145),ALG_BUTTON_SIZE,lambda:bspl_btn())],\
            
          [],\
          
          [Button((50,185),ALG_BUTTON_SIZE,lambda:pol_btn()),\
          Button((50,210),ALG_BUTTON_SIZE,lambda:greh_btn()),\
          Button((50,235),ALG_BUTTON_SIZE,lambda:djarw_btn())],\
          
          [Button((50,230),ALG_BUTTON_SIZE,lambda:brz_crcl_btn()),\
          Button((50,255),ALG_BUTTON_SIZE,lambda:ell_btn()),\
          Button((50,280),ALG_BUTTON_SIZE,lambda:gprbl_btn()),\
          Button((50,305),ALG_BUTTON_SIZE,lambda:prbl_btn())]]


menus=[Menu((0,0),(50,800)),Menu((45,0),(100,80)),Menu((45,45),(100,105)),Menu((45,90),(100,80)),Menu(),\
       Menu((45,180),(100,80)),Menu((45,225),(100,105))]