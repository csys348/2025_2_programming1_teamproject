
from cs1graphics import *
import time
import math

# =================================================================
# 옆모습 전용 목도리 클래스 (변경 없음)
# =================================================================
class PenguinScarfSide(Layer):
    def __init__(self):
        super().__init__()
        
        # 색상 정의
        scarf_red = (220, 40, 40)
        stripe_yellow = (255, 215, 0)
        
        # 1. 목을 감싸는 부분
        neck_wrap = Polygon(
            Point(-45, -5), 
            Point(35, 0), 
            Point(40, 25), 
            Point(-40, 20) 
        )
        neck_wrap.setFillColor(scarf_red)
        neck_wrap.setBorderColor(scarf_red)
        neck_wrap.setDepth(5)
        
        self.add(neck_wrap)

        # 2. 꼬리 부분
        tail = Polygon(
            Point(20, 20), Point(45, 20),
            Point(50, 85), Point(20, 85)
        )
        tail.setFillColor(scarf_red)
        tail.setBorderColor(scarf_red)
        tail.setDepth(4)
        tail.move(-5, -7)
        self.add(tail)

        # 3. 줄무늬
        s1 = Path(Point(22, 70), Point(49, 70))
        s1.setBorderColor(stripe_yellow)
        s1.setBorderWidth(4)
        s1.setDepth(3)
        s1.move(-5, -7)
        self.add(s1)

        s2 = Path(Point(21, 78), Point(50, 78))
        s2.setBorderColor(stripe_yellow)
        s2.setBorderWidth(4)
        s2.setDepth(3)
        s2.move(-5, -7)
        self.add(s2)

        # 4. 술
        start_x = 22
        y_pos = 85
        for i in range(5):
            x = start_x + (i * 6)
            fringe = Path(Point(x, y_pos), Point(x, y_pos + 8))
            fringe.setBorderColor(scarf_red)
            fringe.setBorderWidth(2)
            fringe.setDepth(3)
            fringe.move(-5, -7)
            self.add(fringe)


# =================================================================
# 펭귄 클래스 (Side View)
# =================================================================
class PenguinSide(Layer):
    def __init__(self, scarf_mode='off', direction='right', scale_factor=1.0):
        super().__init__()
        
        self.direction = direction
        
        # 0. 색상 정의
        black = 'black'
        white = 'white'
        orange = (255, 140, 0)
        
        if scarf_mode == 'on':
            cheek_color = (255, 180, 200) # 분홍
        else:
            cheek_color = (100, 200, 255) # 파랑

        # ---------------------------------------------------------
        # 1. 발 (Feet)
        # ---------------------------------------------------------
        # 초기 위치: 왼발 -10, 오른발 +10 (간격 20)
        self.left_foot = Ellipse(30, 20)
        self.left_foot.setFillColor(orange)
        self.left_foot.setBorderColor(orange)
        self.left_foot.move(-10, 125)
        self.left_foot.setDepth(60)
        self.add(self.left_foot)

        self.right_foot = Ellipse(35, 25)
        self.right_foot.setFillColor(orange)
        self.right_foot.setBorderColor(orange)
        self.right_foot.move(10, 128)
        self.right_foot.setDepth(55)
        self.right_foot.move(0, -3)
        self.add(self.right_foot)

        # ---------------------------------------------------------
        # 2. 꼬리 (Tail)
        # ---------------------------------------------------------
        tail = Polygon(Point(-40, 100), Point(-70, 130), Point(-30, 120))
        tail.setFillColor(black)
        tail.setBorderColor(black)
        tail.setDepth(52)
        tail.move(8, -5)
        self.add(tail)

        # ---------------------------------------------------------
        # 3. 몸통 (Body)
        # ---------------------------------------------------------
        body = Ellipse(110, 150)
        body.setFillColor(black)
        body.setBorderColor(black)
        body.move(-10, 45)
        body.setDepth(50)
        self.add(body)

        # ---------------------------------------------------------
        # 4. 배 (Belly)
        # ---------------------------------------------------------
        belly = Ellipse(60, 110)
        belly.setFillColor(white)
        belly.setBorderColor(white)
        belly.move(15, 55)
        belly.setDepth(40)
        belly.move(-10, 0)
        belly.rotate(10)
        self.add(belly)

        # ---------------------------------------------------------
        # 6. 날개 (Wing)
        # ---------------------------------------------------------
        wing = Ellipse(35, 90)
        wing.setFillColor(black)
        wing.setBorderColor(black)
        wing.move(-15, 50)
        wing.rotate(-15)
        wing.setDepth(35)
        self.add(wing)

        # ---------------------------------------------------------
        # 5. 머리와 얼굴 요소
        # ---------------------------------------------------------
        head = Circle(48, Point(-5, -40))
        head.setFillColor(black)
        head.setBorderColor(black)
        head.setDepth(30)
        self.add(head)

        eye_bg = Circle(12, Point(15, -50))
        eye_bg.setFillColor(white)
        eye_bg.setBorderWidth(0)
        eye_bg.setDepth(20)
        self.add(eye_bg)
        
        pupil = Circle(4, Point(19, -50))
        pupil.setFillColor(black)
        pupil.setDepth(10)
        self.add(pupil)

        beak = Polygon(Point(35, -40), Point(65, -33), Point(35, -25))
        beak.setFillColor(orange)
        beak.setBorderColor(orange)
        beak.setDepth(15)
        self.add(beak)

        cheek = Circle(9, Point(3, -35))
        cheek.setFillColor(cheek_color)
        cheek.setBorderColor(cheek_color)
        cheek.setDepth(25)
        cheek.move(-6, 6) 
        self.add(cheek)

        # ---------------------------------------------------------
        # 8. 목도리 착용
        # ---------------------------------------------------------
        if scarf_mode == 'on':
            my_scarf = PenguinScarfSide()
            my_scarf.setDepth(5)
            self.add(my_scarf)

        # ---------------------------------------------------------
        # 크기 조정 (Scale)
        # ---------------------------------------------------------
        if scale_factor != 1.0:
            self.scale(scale_factor)

        # ---------------------------------------------------------
        # 방향 전환 (Direction)
        # ---------------------------------------------------------
        if direction == 'left':
            self.flip(0)

    # =============================================================
    # 걷기 애니메이션 메서드
    # =============================================================
    def move_to(self, distance):
        step_size = 3        
        steps = int(distance / step_size)
        
        direction_sign = 1
        if self.direction == 'left':
            direction_sign = -1

        # 진폭을 크게 주어 다리가 시원하게 교차하도록 설정 (30픽셀)
        amplitude = 30       
        frequency = 0.3      
        
        # 현재 이동량을 추적하여 마지막에 리셋하기 위함
        current_offset_left = 0
        current_offset_right = 0

        for i in range(steps):
            # 1. 몸체 전진
            self.move(step_size * direction_sign, 0)

            # 2. 발 흔들기
            val = math.sin(i * frequency) * amplitude

            target_offset_left = val + 10
            target_offset_right = -val - 10

            # 이번 프레임 이동량 계산
            delta_left = target_offset_left - current_offset_left
            delta_right = target_offset_right - current_offset_right

            # 이동 실행
            self.left_foot.move(delta_left, 0)
            self.right_foot.move(delta_right, 0)

            # 오프셋 업데이트
            current_offset_left = target_offset_left
            current_offset_right = target_offset_right
            
            time.sleep(0.02)

        # 3. 애니메이션 종료 후 발 위치 초기화
        # 움직인 만큼 반대로 되돌려 원래의 가지런한(-10, +10) 상태로 복귀
        self.left_foot.move(-current_offset_left, 0)
        self.right_foot.move(-current_offset_right, 0)
"""

# =================================================================
# 메인 실행 코드
# =================================================================
paper = Canvas(800, 600, 'white', 'Perfect Walking Penguin')

# 1. 오른쪽 펭귄
p_right = PenguinSide('on', 'right')
p_right.moveTo(150, 250)
paper.add(p_right)

# 2. 왼쪽 펭귄
p_left = PenguinSide('off', 'left')
p_left.moveTo(650, 450)
paper.add(p_left)

time.sleep(1)

# [테스트] 
# 이제 갈 때나 올 때나 발이 똑같은 간격으로 시원하게 교차할 것입니다.
p_right.move_to(300)
p_left.move_to(300)
"""
