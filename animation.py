from cs1graphics import *
import time
from Penguin_front import *
from Penguin_back import *
from Penguin_side import *
from BoxNscarf import *
from Stars import *
from Text_object import *
from Scene10 import *

#선물 상자에서 목도리가 나오고 뒤에 별들이 돌아가며 선물을 강조하는 애니메이션 구현 함수 
def show_present(canvas, x, y):
    gift = GiftBox()
    gift.scale(1.8)
    gift.moveTo(x,y)
    canvas.add(gift)
    gift.open()

    scarf = Scarf(scale_factor=2)
    scarf.moveTo(x,y)
    scarf.setDepth(55)
    canvas.add(scarf)

    star = StarBurst()
    star.moveTo(650, 375)
    star.scale(2)

    for i in range(150):
        scarf.move(0,-3)
        if i < 50:
            gift.move(0 ,7)

    canvas.add(star)
    star.rotate_star(scarf)

    canvas.remove(gift)
    canvas.remove(scarf)
    canvas.remove(star)

#펭귄이 점프하고 회전하는 함수 
def penguin_dance(canvas, x, y):
    p_f = Penguin('on')
    p_r = PenguinSide('on','right')
    p_b = PenguinBack('on')
    p_l = PenguinSide('on','left')
    p_all_dir = [p_f, p_r, p_b, p_l, p_f]
    p_f.moveTo(x,y)
    canvas.add(p_f)

    for i in range(50):
        if i < 25:
            p_f.move(0,-4)
        else:
            p_f.move(0,-2)
    canvas.remove(p_f)
    
    for dirs in p_all_dir:
        showNrm(canvas, dirs, 0.05, x, y-100)
    canvas.add(p_f)

    for i in range(50):
        if i < 25:
            p_f.move(0,2)
        else:
            p_f.move(0,4)
    canvas.remove(p_f)
    
    
#텍스트 보여주는 함수==============================================
def showNrm(canvas, obj, delay,x, y):
    obj.moveTo(x,y)
    canvas.add(obj)
    time.sleep(delay)
    canvas.remove(obj)


def show_script(canvas, full_sentence, delay, font_size, x, y):
    s_each = full_sentence.split('/')
    obj_each = []
    for n in s_each:
        t_obj = mytext(n, font_size)
        obj_each.append(t_obj)

    for i in obj_each:
        showNrm(canvas, i, delay, x, y)

#==============================================================


# =================================================================
#  메인 함수 (설정 및 초기화 담당)
# =================================================================
def main():
    # 1. 캔버스 설정 (1280 x 720), 배경 완성 되면 교
    width, height = 1280, 720
    og_pingu_x = 200
    og_pingu_y = 550
    paper = Canvas(width, height, 'skyblue', 'Gift Reveal Animation')
    
    
# =================================================================
# 달력이 뜯기는 장면  
# =================================================================

# =================================================================
# 산타가 오두막집에서 나와 썰매를 타고 날아가는 장면  
# =================================================================

# =================================================================
# 산타가 왼쪽에서 나와서 선물을 떨어트리는 장면 
# =================================================================

    pingu = Penguin('off')
    pingu.moveTo(og_pingu_x, og_pingu_y)
    paper.add(pingu)
    
    show_script(paper, 'Hello, my name is Pingu! / I am freezing now / I wish I had winter clothing brr...',2, 20 ,200, 450)
# =================================================================
# 산타가 와서 선물 떨어트리는 장면 , 선물 상자 포지션은 1000, 650 포지션은 로 설정 (바꿀 수 있음), 스케일은 0.5로 설정.  
# =================================================================

# =================================================================
# 선물 상자가 흔들리면서 떨어지는 장면 : 선물 상자 확대하여 보여주기  
# =================================================================

# =================================================================
# 펭귄이 떨어진 선물 상자를 보고 말을 한다 --> 선물 상자로 걸어간다 --> 선물상자가 열리고 목도리가 나온다 --> 목도리를 차고 신나한다 --> 산타에게 감사인
    gift = GiftBox()
    gift.scale(0.5)
    gift.moveTo(1000, 650)
    paper.add(gift)
    
    show_script(paper, "Wait! did I just saw santa claus? / Maybe that is my christmas gift!! / let's go check it out!",3, 20 ,200, 450)

    paper.remove(pingu)
    
    p_right = PenguinSide('off', 'right')
    p_right.moveTo(og_pingu_x,og_pingu_y)
    paper.add(p_right)
    p_right.move_to(600)


    paper.remove(p_right)
    paper.remove(gift)
    
    show_present(paper, width//2, 600)

    pingu_scarf = Penguin('on')
    pingu_scarf.moveTo(og_pingu_x+600, og_pingu_y)
    paper.add(pingu_scarf)

    script3 = "Now I have scarf! / I am not cold anymore! / I am very happy!! / I want to jump!"
    show_script(paper, script3,3, 20 ,800, 450)

    paper.remove(pingu_scarf)

    penguin_dance (paper, 800, 450)
    penguin_dance (paper, 800, 450)
    penguin_dance (paper, 800, 450)

    paper.add(pingu_scarf)
    script4 = "Wait I have to say thank you!"
    show_script(paper, script4,3, 20 ,800, 450)
    paper.remove(pingu_scarf)
    pingu_scarf.scale(2.2)
    pingu_scarf.move(-200, 0)
    paper.add(pingu_scarf)
    pingu_scarf.arms_up()
    script5 = 'Thank you Santa! / and \n Merry christmas!!!'
    show_script(paper, script5,3, 45 ,620, 300)
    
    
# ================================================================= 
    

    

# =================================================================
# 산타가 확대되어 보여지고 말풍선 나오고 따봉하고 The End! 하는 장면 
# =================================================================
    run_santa_ending(paper)

main()
