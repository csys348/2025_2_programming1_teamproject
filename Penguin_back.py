
from cs1graphics import *

# =================================================================
# [수정됨] 뒷모습 전용 목도리 클래스
# =================================================================
class PenguinScarfBack(Layer):
    def __init__(self):
        super().__init__()
        
        # 색상 정의
        scarf_red = (220, 40, 40)
        stripe_yellow = (255, 215, 0)
        
        # 1. 목 뒤를 감싸는 밴드 부분
        neck_band = Polygon(
            Point(-42, -5), 
            Point(42, -5),
            Point(42, 15),
            Point(-42, 16) 
        )
        neck_band.setFillColor(scarf_red)
        neck_band.setBorderColor(scarf_red)
        neck_band.setBorderWidth(10) 
        neck_band.setDepth(10)
        self.add(neck_band)



# =================================================================
# 펭귄 클래스 - 뒷모습
# =================================================================
class PenguinBack(Layer):
    def __init__(self, scarf_mode='off', scale_factor=1.0):
        super().__init__()
        
        # 색상 정의
        black = 'black'
        orange = (255, 140, 0)

        # ---------------------------------------------------------
        # 1. 발 (Feet)
        # ---------------------------------------------------------
        left_foot = Ellipse(40, 25)
        left_foot.setFillColor(orange)
        left_foot.setBorderColor(orange)
        left_foot.move(-25, 95)
        left_foot.setDepth(60) # 몸통보다 뒤
        self.add(left_foot)

        right_foot = Ellipse(40, 25)
        right_foot.setFillColor(orange)
        right_foot.setBorderColor(orange)
        right_foot.move(25, 95)
        right_foot.setDepth(60) # 몸통보다 뒤
        self.add(right_foot)

        # ---------------------------------------------------------
        # 2. 날개 (Wings)
        # ---------------------------------------------------------
        left_wing = Ellipse(35, 90)
        left_wing.setFillColor(black)
        left_wing.setBorderColor(black)
        left_wing.move(-55, 20)
        left_wing.rotate(20) # 왼쪽으로 약간 회전
        left_wing.setDepth(55) 
        self.add(left_wing)

        right_wing = Ellipse(35, 90)
        right_wing.setFillColor(black)
        right_wing.setBorderColor(black)
        right_wing.move(55, 20)
        right_wing.rotate(-20) # 오른쪽으로 약간 회전
        right_wing.setDepth(55)
        self.add(right_wing)

        # ---------------------------------------------------------
        # 3. 몸통 (Body)
        # ---------------------------------------------------------
        body = Ellipse(130, 160)
        body.setFillColor(black)
        body.setBorderColor(black)
        body.move(0, 20) 
        body.setDepth(50)
        self.add(body)

        # ---------------------------------------------------------
        # 4. 머리 (Head)
        # ---------------------------------------------------------
        head = Circle(52, Point(0, -45))
        head.setFillColor(black)
        head.setBorderColor(black)
        head.setDepth(45)
        self.add(head)

        # ---------------------------------------------------------
        # 5. 목도리 착용 (Back View Scarf)
        # ---------------------------------------------------------
        if scarf_mode == 'on':
            my_scarf = PenguinScarfBack()
            my_scarf.move(0, -10) # 목 위치로 이동
            my_scarf.setDepth(5)  # 가장 앞으로
            self.add(my_scarf)

        # ---------------------------------------------------------
        # 크기 조정
        # ---------------------------------------------------------
        if scale_factor != 1.0:
            self.scale(scale_factor)

"""
# =================================================================
# 메인 실행 코드
# =================================================================
paper = Canvas(600, 400, 'white', 'Back View Penguin')

# 1. 뒷모습 (목도리 X)
p_back_off = PenguinBack('off')
p_back_off.moveTo(200, 200)
paper.add(p_back_off)

# 2. 뒷모습 (목도리 O)
p_back_on = PenguinBack('on')
p_back_on.moveTo(450, 200)
paper.add(p_back_on)
"""
