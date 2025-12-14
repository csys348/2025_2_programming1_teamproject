
from cs1graphics import *
import time

# =================================================================
# 목도리 클래스 
# =================================================================
class PenguinScarf(Layer):
    def __init__(self):
        super().__init__()
        
        # 색상 정의
        scarf_red = (220, 40, 40)
        stripe_yellow = (255, 215, 0)
        
        # -----------------------------------------------------
        # 1. 목을 감싸는 부분 (Neck Wrap) 
        # -----------------------------------------------------
        neck_wrap = Polygon(
            Point(-45, -5), Point(45, -5),  # 위쪽 
            Point(50, 20), Point(-50, 20)   # 아래쪽 
        )
        neck_wrap.setFillColor(scarf_red)
        neck_wrap.setBorderColor(scarf_red)
        neck_wrap.setDepth(5)
        self.add(neck_wrap)

        # -----------------------------------------------------
        # 2. 꼬리 부분 (Long Tail) 
        # -----------------------------------------------------
        tail = Polygon(
            Point(20, 15), Point(50, 15),   # 연결 부위 
            Point(58, 80), Point(28, 80)    # 아래 끝단 
        )
        tail.setFillColor(scarf_red)
        tail.setBorderColor(scarf_red)
        tail.setDepth(4)
        self.add(tail)

        # -----------------------------------------------------
        # 3. 줄무늬 (Stripes) - [위치/크기 조정]
        # -----------------------------------------------------
        s1 = Path(Point(26, 65), Point(56, 65))
        s1.setBorderColor(stripe_yellow)
        s1.setBorderWidth(4) # 두께
        s1.setDepth(3)
        self.add(s1)

        s2 = Path(Point(27, 73), Point(57, 73))
        s2.setBorderColor(stripe_yellow)
        s2.setBorderWidth(4)
        s2.setDepth(3)
        self.add(s2)

        # -----------------------------------------------------
        # 4. 술 (Fringes) 
        # -----------------------------------------------------
        start_x = 28
        y_pos = 80 
        for i in range(6): # 개수 6개
            x = start_x + (i * 6)
            fringe = Path(Point(x, y_pos), Point(x, y_pos + 8)) # 길이 
            fringe.setBorderColor(scarf_red)
            fringe.setBorderWidth(2)
            fringe.setDepth(3)
            self.add(fringe)


# =================================================================
# 펭귄 클래스 
# =================================================================
class Penguin(Layer):
    def __init__(self, scarf_mode='off', scale_factor=1.0):
        super().__init__()
        
        black = 'black'
        white = 'white'
        orange = (255, 140, 0)
        
        # 볼 색상 결정
        if scarf_mode == 'on':
            cheek_color = (255, 180, 200) # 분홍
        else:
            cheek_color = (100, 200, 255) # 파랑
        self.left_foot = Ellipse(45, 30)
        self.left_foot.setFillColor(orange)
        self.left_foot.setBorderColor(orange)
        self.left_foot.move(-25, 125) 
        self.left_foot.setDepth(60)
        self.add(self.left_foot)

        self.right_foot = Ellipse(45, 30)
        self.right_foot.setFillColor(orange)
        self.right_foot.setBorderColor(orange)
        self.right_foot.move(25, 125)
        self.right_foot.setDepth(60)
        self.add(self.right_foot)

        # 2. 날개 (Layer로 감싸서 회전 중심점을 어깨로 설정)
        
        # Layer의 (0,0)이 Ellipse의 상단 끝(어깨)이 되도록 Ellipse를 아래로 45 이동
        wing_height_half = 90 / 2 # 45

        # --- 왼쪽 날개 그룹 ---
        self.left_wing_group = Layer()
        self.left_wing = Ellipse(30, 90)
        self.left_wing.setFillColor(black)
        self.left_wing.setBorderColor(black)
        self.left_wing.move(0, wing_height_half) # Layer 기준: 중심점(0, 45) -> Layer의 (0,0)이 어깨
        self.left_wing_group.add(self.left_wing)

        # 펭귄의 몸통 옆으로 Layer 배치 및 초기 각도 설정
        self.left_wing_group.rotate(20) # 초기 회전 각도
        self.left_wing_group.move(-65, -5) # 펭귄 Layer 내에서의 최종 위치
        self.left_wing_group.setDepth(55)
        self.left_wing_group.move(15, 10)
        self.add(self.left_wing_group) # Penguin Layer에 날개 Layer 추가
        
        # --- 오른쪽 날개 그룹 ---
        self.right_wing_group = Layer()
        self.right_wing = Ellipse(30, 90)
        self.right_wing.setFillColor(black)
        self.right_wing.setBorderColor(black)
        self.right_wing.move(0, wing_height_half) # Layer 기준: 중심점(0, 45)
        self.right_wing_group.add(self.right_wing)

        # 펭귄의 몸통 옆으로 Layer 배치 및 초기 각도 설정
        self.right_wing_group.rotate(-20) # 초기 회전 각도
        self.right_wing_group.move(65, -5)
        self.right_wing_group.setDepth(55)
        self.right_wing_group.move(-15, 10)
        self.add(self.right_wing_group) 
        

        # 3. 몸통 
        body = Ellipse(130, 150)
        body.setFillColor(black)
        body.setBorderColor(black)
        body.move(0, 45)
        body.setDepth(50)
        self.add(body)

        # 4. 배 
        belly = Ellipse(90, 120)
        belly.setFillColor(white)
        belly.setBorderColor(white)
        belly.move(0, 55)
        belly.setDepth(40)
        self.add(belly)

        # 5. 머리
        head = Circle(50, Point(0, -30))
        head.setFillColor(black)
        head.setBorderColor(black)
        head.setDepth(30)
        self.add(head)

        # 6. 얼굴 요소
        left_eye_bg = Circle(12, Point(-20, -40))
        left_eye_bg.setFillColor(white)
        left_eye_bg.setBorderWidth(0)
        left_eye_bg.setDepth(20)
        self.add(left_eye_bg)

        right_eye_bg = Circle(12, Point(20, -40))
        right_eye_bg.setFillColor(white)
        right_eye_bg.setBorderWidth(0)
        right_eye_bg.setDepth(20)
        self.add(right_eye_bg)
        
        left_pupil = Circle(5, Point(-20, -40))
        left_pupil.setFillColor(black)
        left_pupil.setDepth(10)
        self.add(left_pupil)

        right_pupil = Circle(5, Point(20, -40))
        right_pupil.setFillColor(black)
        right_pupil.setDepth(10)
        self.add(right_pupil)

        beak = Polygon(Point(-10, -25), Point(10, -25), Point(0, -5))
        beak.setFillColor(orange)
        beak.setBorderColor(orange)
        beak.setDepth(15)
        self.add(beak)

        left_cheek = Circle(8, Point(-35, -25))
        left_cheek.setFillColor(cheek_color)
        left_cheek.setBorderColor(cheek_color)
        left_cheek.setDepth(25)
        left_cheek.move(0,5)
        self.add(left_cheek)

        right_cheek = Circle(8, Point(35, -25))
        right_cheek.setFillColor(cheek_color)
        right_cheek.setBorderColor(cheek_color)
        right_cheek.setDepth(25)
        right_cheek.move(0,5)
        self.add(right_cheek)

        # 7. 목도리 착용 여부
        if scarf_mode == 'on':
            my_scarf = PenguinScarf()
            my_scarf.setDepth(5) 
            self.add(my_scarf)

        if scale_factor != 1.0:
            self.scale(scale_factor)
            
        # 애니메이션을 위한 초기 각도 저장 
        self.initial_left_angle = 20
        self.initial_right_angle = -20


    def arms_up(self):
        """
        펭귄의 팔을 위로 올리면서 회전시키는 애니메이션.
        """
        rotation_angle = 100 # 총 회전할 각도
        move_distance = 15   # 총 위로 올릴 거리 (픽셀)
        steps = 50           # 애니메이션 단계 수
        step_angle = rotation_angle / steps
        step_move = move_distance / steps # 단계별 이동 거리

        for _ in range(steps):
            # 1. 팔 Layer 회전 (어깨 기준)
            self.left_wing_group.rotate(step_angle)
            self.right_wing_group.rotate(-step_angle) 
            
            # 2. 팔 Layer 전체를 위로 이동 (y축 음의 방향)
            self.left_wing_group.move(0, -step_move)
            self.right_wing_group.move(0, -step_move)
            
            time.sleep(0.005)

    def arms_down(self):
        """
        펭귄의 팔을 원래 위치로 내리면서 회전시키는 애니메이션.
        """
        rotation_angle = 100 # 총 회전할 각도
        move_distance = 15   # 총 아래로 내릴 거리 (픽셀)
        steps = 50           # 애니메이션 단계 수
        step_angle = rotation_angle / steps
        step_move = move_distance / steps # 단계별 이동 거리

        for _ in range(steps):
            # 1. 팔 Layer 회전 (원래 각도로 복귀)
            self.left_wing_group.rotate(-step_angle)
            self.right_wing_group.rotate(step_angle) 
            
            # 2. 팔 Layer 전체를 아래로 이동 (y축 양의 방향)
            self.left_wing_group.move(0, step_move)
            self.right_wing_group.move(0, step_move)
            
            time.sleep(0.001)

    def hurray(self):
        #팔을 들고 회전시킨 후 (arms_up), 잠시 멈췄다가, 팔을 내리고 회전시킵니다 (arms_down).
        self.arms_up()
        time.sleep(0.5) # 잠시 만세 상태 유지
        self.arms_down()

"""
# =================================================================
# 메인 실행 코드
# =================================================================
paper = Canvas(600, 400, 'white', 'Slim Scarf Penguin')

on = 'on'
off = 'off'

# 1. 목도리 안 한 펭귄 (파란 볼)
pingu_cold = Penguin(off)
pingu_cold.moveTo(150, 200)
paper.add(pingu_cold)

# 2. 목도리 한 펭귄 (분홍 볼 + 슬림해진 목도리)
pingu_warm = Penguin(on)
pingu_warm.moveTo(450, 200)
paper.add(pingu_warm)

# paper.wait()
# paper.close()
"""
