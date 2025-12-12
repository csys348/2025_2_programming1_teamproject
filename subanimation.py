from cs1graphics import *
import time
import math
import random

# 애니메이션 컨트롤러 클래스
class AnimationController:
    """장면의 카메라(시점)를 제어하는 클래스"""
    
    def __init__(self, canvas, world_layer):
        self.canvas = canvas
        self.world = world_layer
        self.current_scale = 1.0
        # Layer.getX() 메서드 부재로 인한 위치 수동 추적
        self.current_x = 0
        self.current_y = 0
        
    def set_camera(self, x, y, scale, ref_x, ref_y):
        """카메라 상태를 수동으로 업데이트"""
        self.current_x = x
        self.current_y = y
        self.current_scale = scale
        self.world.adjustReference(ref_x, ref_y)
        self.world.moveTo(x, y)
        # 스케일은 외부에서 처리하거나 추적만 함
        # 실제 스케일 적용이 필요한 경우:
        # self.world.scale(scale / current_actual_scale) ...
        # 여기서는 상태 변수만 수동 변경값에 맞춰 업데이트
        
    def zoom_to(self, target_obj, target_scale, duration=1.0):
        """
        target_obj가 중앙에 오고 확대되도록 카메라를 줌/팬 이동
        """
        # 월드 좌표계 기준 타겟 위치 획득
        ref = target_obj.getReferencePoint()
        tx, ty = ref.getX(), ref.getY()
        
        # 현재 상태
        start_scale = self.current_scale
        steps = int(duration * 30)
        
        cw = self.canvas.getWidth()
        ch = self.canvas.getHeight()
        
        # 현재 월드 기준점 (카메라 포커스)
        start_ref = self.world.getReferencePoint()
        start_rx, start_ry = start_ref.getX(), start_ref.getY()
        
        # 타겟 기준점
        target_rx, target_ry = tx, ty
        
        # 화면상 월드 현재 위치
        start_pos_x = self.current_x
        start_pos_y = self.current_y
        
        # 타겟 위치 (항상 화면 중앙)
        target_pos_x = cw / 2
        target_pos_y = ch / 2
        
        for i in range(steps + 1):
            t = i / steps
            # 부드러운 이동 (Ease in/out)
            t_smooth = t * t * (3 - 2 * t)
            
            # 포커스 포인트 보간 (월드 기준점)
            cur_rx = start_rx + (target_rx - start_rx) * t_smooth
            cur_ry = start_ry + (target_ry - start_ry) * t_smooth
            
            # 위치 보간 (캔버스 좌표)
            cur_px = start_pos_x + (target_pos_x - start_pos_x) * t_smooth
            cur_py = start_pos_y + (target_pos_y - start_pos_y) * t_smooth
            
            # 스케일 보간
            cur_scale_val = start_scale + (target_scale - start_scale) * t_smooth
            
            # 적용
            # 1. 기준점 설정
            self.world.adjustReference(cur_rx, cur_ry) 
            
            # 2. 위치 이동
            self.world.moveTo(cur_px, cur_py)
            self.current_x = cur_px
            self.current_y = cur_py
            
            # 3. 스케일 적용
            scale_factor = cur_scale_val / self.current_scale
            self.world.scale(scale_factor)
            
            self.current_scale = cur_scale_val
            
            time.sleep(duration/steps)

# 달력 클래스
class Calendar(Layer):
    """달력 객체 생성 및 페이지 넘김 애니메이션 처리"""
    
    def __init__(self):
        super().__init__()
        
        # 달력 받침대 (붉은 배경) - 안전한 크기
        self.base = Rectangle(300, 400)
        self.base.setFillColor('darkRed')
        self.base.setBorderColor('black')
        self.base.setBorderWidth(2)
        self.add(self.base)
        
        # 금속 링 (제본) - 안전한 크기
        for i in range(5):
            x = -100 + i * 50
            ring_back = Path(Point(x, -180), Point(x, -200))
            ring_back.setBorderWidth(6)
            ring_back.setBorderColor('lightGray')
            self.add(ring_back)
            
        # 페이지 컨테이너
        self.page_layer = Layer()
        self.add(self.page_layer)
        
        # 25일 페이지 (아래쪽)
        self.page25 = self.create_page("25", "Christmas Day", "red", "santa")
        self.page_layer.add(self.page25)
        
        # 24일 페이지 (위쪽)
        self.page24 = self.create_page("24", "Christmas Eve", "darkGreen", "tree")
        self.page_layer.add(self.page24)
        
        # 앞쪽 링 - 안전한 크기
        for i in range(5):
            x = -100 + i * 50
            ring_front = Circle(5, Point(x, -180))
            ring_front.setFillColor('white')
            ring_front.setBorderColor('gray')
            self.add(ring_front)

    def create_page(self, number, subtitle, theme_color, icon_type):
        """달력 페이지 생성 헬퍼 함수"""
        page = Layer()
        
        # 종이 - 안전한 크기
        paper = Rectangle(260, 320)
        paper.setFillColor('white')
        paper.setBorderColor('lightGray')
        paper.move(0, 20)
        page.add(paper)
        
        # 찢어지는 부분 구멍 - 안전한 크기
        for i in range(5):
            x = -100 + i * 50
            hole = Circle(6, Point(x, -140))
            hole.setFillColor('darkRed') # 배경색과 일치
            hole.setBorderColor('darkRed')
            page.add(hole)
        
        # 헤더 라인 - 안전한 크기
        line = Path(Point(-110, -80), Point(110, -80))
        line.setBorderColor('red')
        line.setBorderWidth(2)
        page.add(line)
        
        # 월 (DECEMBER) - 안전한 크기
        month = Text("DECEMBER", 20)
        month.setFontColor('red')
        month.move(0, -100)
        try:
            month.setFont("Impact")
        except:
            pass # 폰트 없을 시 기본값 사용
        page.add(month)
        
        # 날짜 숫자 - 안전한 크기
        num = Text(number, 100)
        num.setFontColor('black')
        try:
            num.setFont("Arial")
        except:
            pass
        num.setDepth(10)
        num.move(0, 10)
        page.add(num)
        
        # 부제 - 안전한 크기
        sub = Text(subtitle, 16)
        sub.setFontColor(theme_color)
        sub.move(0, 80)
        page.add(sub)
        
        # 아이콘 (트리 또는 산타) - 안전한 크기
        if icon_type == "tree":
            tree = Polygon(Point(0, 110), Point(-20, 140), Point(20, 140))
            tree.setFillColor('forestGreen')
            page.add(tree)
        elif icon_type == "santa":
            # 간단한 산타 얼굴 - 안전한 크기
            face = Circle(15, Point(0, 120))
            face.setFillColor('white')
            page.add(face)
            beard = Polygon(Point(-15, 120), Point(0, 145), Point(15, 120))
            beard.setFillColor('white')
            page.add(beard)
            hat = Polygon(Point(-15, 115), Point(0, 95), Point(15, 115))
            hat.setFillColor('red')
            page.add(hat)
            
        return page

    def tear_page(self):
        """맨 위 페이지가 찢겨 나가는 애니메이션"""
        # self.page24 애니메이션
        # 주의: cs1graphics의 Layer 내부 Text 객체는 회전 불가능
        # 따라서 회전 대신 이동만 사용
        steps = 20
        
        # 찢어지는 효과 (좌우 흔들림)
        for i in range(5):
            self.page24.move(5, 0)
            time.sleep(0.05)
            self.page24.move(-5, 0)
            time.sleep(0.05)
            
        # 떨어지는 애니메이션 (회전 없이 이동)
        for i in range(steps):
            self.page24.move(5, 15) # 아래 오른쪽으로 이동
            time.sleep(0.05)
            
        self.page_layer.remove(self.page24)

# 오두막 클래스
class Cabin(Layer):
    """오두막 생성 및 문 열기 애니메이션 처리"""
    
    def __init__(self):
        super().__init__()
        
        # 고퀄리티 통나무 오두막 벽체
        body = Rectangle(220, 180)
        body.setFillColor('saddleBrown')
        body.setBorderColor('black')
        body.setBorderWidth(3)
        self.add(body)
        
        # 통나무 디테일 라인들
        for i in range(8):
            y = -80 + i * 22
            log_line = Path(Point(-110, y), Point(110, y))
            log_line.setBorderColor('brown')
            log_line.setBorderWidth(3)
            self.add(log_line)
            
            # 통나무 끝부분 원형 디테일
            left_end = Circle(4, Point(-110, y))
            left_end.setFillColor('brown')
            left_end.setBorderColor('darkRed')
            self.add(left_end)
            right_end = Circle(4, Point(110, y))
            right_end.setFillColor('brown')
            right_end.setBorderColor('darkRed')
            self.add(right_end)
        
        # 고퀄리티 지붕 (기와 느낌)
        roof = Polygon(Point(-130, -90), Point(0, -160), Point(130, -90))
        roof.setFillColor('darkRed')
        roof.setBorderColor('black')
        roof.setBorderWidth(3)
        self.add(roof)
        
        # 지붕 기와 디테일
        for i in range(6):
            x = -120 + i * 40
            tile = Path(Point(x, -90), Point(x + 20, -110))
            tile.setBorderColor('red')
            tile.setBorderWidth(2)
            self.add(tile)
        
        # 지붕 위 눈
        snow_roof = Polygon(Point(-130, -90), Point(0, -160), Point(130, -90),
                           Point(120, -85), Point(0, -150), Point(-120, -85))
        snow_roof.setFillColor('white')
        snow_roof.setBorderColor('lightBlue')
        snow_roof.setBorderWidth(1)
        self.add(snow_roof)
        
        # 굴뚝
        chimney = Rectangle(20, 40)
        chimney.setFillColor('gray')
        chimney.setBorderColor('black')
        chimney.setBorderWidth(2)
        chimney.move(60, -130)
        self.add(chimney)
        
        # 굴뚝 연기
        for i in range(3):
            smoke = Circle(6 - i)
            smoke.setFillColor('lightGray')
            smoke.setBorderColor('gray')
            smoke.move(60 + i * 8, -160 - i * 15)
            self.add(smoke)
        
        # 고퀄리티 문 프레임
        door_frame = Rectangle(60, 100)
        door_frame.setFillColor('darkRed')
        door_frame.setBorderColor('black')
        door_frame.setBorderWidth(2)
        door_frame.move(0, 50)
        self.add(door_frame)
        
        # 고퀄리티 문 (나무 패널 디테일)
        self.door = Rectangle(55, 95)
        self.door.setFillColor('orange')
        self.door.setBorderColor('black')
        self.door.setBorderWidth(2)
        self.door.move(0, 50)
        self.add(self.door)
        
        # 문 나무 패널 디테일
        for i in range(4):
            y = 15 + i * 20
            panel = Path(Point(-20, y), Point(20, y))
            panel.setBorderColor('brown')
            panel.setBorderWidth(1)
            self.add(panel)
        
        # 고퀄리티 문 손잡이
        self.knob = Circle(5)
        self.knob.setFillColor('gold')
        self.knob.setBorderColor('orange')
        self.knob.setBorderWidth(2)
        self.knob.move(20, 50)
        self.add(self.knob)
        
        # 고퀄리티 창문들
        # 왼쪽 창문
        win1 = Rectangle(50, 50)
        win1.setFillColor('lightBlue')
        win1.setBorderColor('brown')
        win1.setBorderWidth(3)
        win1.move(-70, -20)
        self.add(win1)
        
        # 창문 십자 프레임
        win1_h = Path(Point(-95, -20), Point(-45, -20))
        win1_h.setBorderColor('brown')
        win1_h.setBorderWidth(2)
        self.add(win1_h)
        win1_v = Path(Point(-70, -45), Point(-70, 5))
        win1_v.setBorderColor('brown')
        win1_v.setBorderWidth(2)
        self.add(win1_v)
        
        # 오른쪽 창문
        win2 = Rectangle(35, 35)
        win2.setFillColor('lightBlue')
        win2.setBorderColor('brown')
        win2.setBorderWidth(3)
        win2.move(70, -40)
        self.add(win2)
        
        # 창문 프레임
        win2_h = Path(Point(52, -40), Point(88, -40))
        win2_h.setBorderColor('brown')
        win2_h.setBorderWidth(2)
        self.add(win2_h)
        win2_v = Path(Point(70, -57), Point(70, -23))
        win2_v.setBorderColor('brown')
        win2_v.setBorderWidth(2)
        self.add(win2_v)
        
        # 창문에 따뜻한 빛
        light1 = Rectangle(45, 45)
        light1.setFillColor('yellow')
        light1.setBorderColor('yellow')
        light1.move(-70, -20)
        light1.setDepth(5)
        self.add(light1)
        
        light2 = Rectangle(30, 30)
        light2.setFillColor('yellow')
        light2.setBorderColor('yellow')
        light2.move(70, -40)
        light2.setDepth(5)
        self.add(light2)

    def open_door(self):
        # 문 열기 애니메이션 제거 - 아무것도 하지 않음
        pass

# 겨울 풍경 배경 클래스
class WinterLandscape(Layer):
    """눈 덮인 언덕과 호수가 있는 겨울 풍경 배경"""
    
    def __init__(self):
        super().__init__()
        
        # 고퀄리티 하늘 그라데이션
        for i in range(25):
            y = -200 + i * 12
            sky_strip = Rectangle(1200, 12)
            if i < 8:
                sky_strip.setFillColor('lightBlue')
            elif i < 15:
                sky_strip.setFillColor('lightCyan')
            else:
                sky_strip.setFillColor('white')
            sky_strip.setBorderColor(sky_strip.getFillColor())
            sky_strip.move(0, y)
            sky_strip.setDepth(50)
            self.add(sky_strip)
        
        # 고퀄리티 원경 산맥 (여러 층)
        # 뒷산맥
        back_mountain = Polygon(Point(-600, 0), Point(-400, -120), Point(-200, -90), 
                               Point(0, -140), Point(200, -100), Point(400, -130), 
                               Point(600, -80), Point(600, 200), Point(-600, 200))
        back_mountain.setFillColor('lightGray')
        back_mountain.setBorderColor('gray')
        back_mountain.setBorderWidth(1)
        back_mountain.setDepth(45)
        self.add(back_mountain)
        
        # 중간 산맥
        mid_mountain = Polygon(Point(-500, 20), Point(-300, -80), Point(-100, -60), 
                              Point(100, -100), Point(300, -70), Point(500, -90), 
                              Point(500, 200), Point(-500, 200))
        mid_mountain.setFillColor('gray')
        mid_mountain.setBorderColor('darkGray')
        mid_mountain.setBorderWidth(2)
        mid_mountain.setDepth(40)
        self.add(mid_mountain)
        
        # 산 위 눈 덮개
        for mountain_x in [-400, -100, 200, 400]:
            snow_cap = Polygon(Point(mountain_x-50, -60), Point(mountain_x, -120), 
                              Point(mountain_x+50, -60), Point(mountain_x+40, -50), 
                              Point(mountain_x, -100), Point(mountain_x-40, -50))
            snow_cap.setFillColor('white')
            snow_cap.setBorderColor('lightBlue')
            snow_cap.setDepth(39)
            self.add(snow_cap)
        
        # 고퀄리티 언덕들 (눈 덮인)
        # 앞쪽 언덕
        front_hill = Polygon(Point(-400, 80), Point(-200, 20), Point(0, 30), 
                            Point(200, 10), Point(400, 40), Point(400, 200), Point(-400, 200))
        front_hill.setFillColor('white')
        front_hill.setBorderColor('lightBlue')
        front_hill.setBorderWidth(2)
        front_hill.setDepth(35)
        self.add(front_hill)
        
        # 뒤쪽 언덕
        back_hill = Polygon(Point(-350, 60), Point(-150, 0), Point(50, 5), 
                           Point(250, -10), Point(350, 20), Point(350, 200), Point(-350, 200))
        back_hill.setFillColor('lightCyan')
        back_hill.setBorderColor('lightBlue')
        back_hill.setBorderWidth(1)
        back_hill.setDepth(36)
        self.add(back_hill)
        
        # 고퀄리티 겨울 나무들
        tree_positions = [(-280, 40), (-120, 25), (80, 35), (220, 20), (350, 45)]
        
        for x, y in tree_positions:
            # 나무 줄기
            trunk = Rectangle(12, 50)
            trunk.setFillColor('saddleBrown')
            trunk.setBorderColor('brown')
            trunk.setBorderWidth(2)
            trunk.move(x, y + 25)
            trunk.setDepth(25)
            self.add(trunk)
            
            # 나무 가지들 (눈 덮인)
            for branch_level in range(4):
                branch_y = y - branch_level * 12
                branch_width = 35 - branch_level * 5
                
                # 왼쪽 가지
                left_branch = Polygon(Point(x, branch_y), Point(x - branch_width, branch_y + 8), 
                                     Point(x - branch_width + 5, branch_y + 12), Point(x, branch_y + 4))
                left_branch.setFillColor('darkGreen')
                left_branch.setBorderColor('green')
                left_branch.setDepth(24)
                self.add(left_branch)
                
                # 오른쪽 가지
                right_branch = Polygon(Point(x, branch_y), Point(x + branch_width, branch_y + 8), 
                                      Point(x + branch_width - 5, branch_y + 12), Point(x, branch_y + 4))
                right_branch.setFillColor('darkGreen')
                right_branch.setBorderColor('green')
                right_branch.setDepth(24)
                self.add(right_branch)
                
                # 가지 위 눈
                snow_left = Ellipse(branch_width//2, 6)
                snow_left.setFillColor('white')
                snow_left.setBorderColor('lightBlue')
                snow_left.move(x - branch_width//2, branch_y + 10)
                snow_left.setDepth(23)
                self.add(snow_left)
                
                snow_right = Ellipse(branch_width//2, 6)
                snow_right.setFillColor('white')
                snow_right.setBorderColor('lightBlue')
                snow_right.move(x + branch_width//2, branch_y + 10)
                snow_right.setDepth(23)
                self.add(snow_right)
        
        # 고퀄리티 얼어붙은 호수
        lake = Ellipse(600, 120)
        lake.setFillColor('lightBlue')
        lake.setBorderColor('blue')
        lake.setBorderWidth(3)
        lake.move(0, 150)
        lake.setDepth(30)
        self.add(lake)
        
        # 호수 얼음 균열 디테일
        for i in range(5):
            crack_x = random.randint(-250, 250)
            crack_y = random.randint(120, 180)
            crack = Path(Point(crack_x - 30, crack_y), Point(crack_x + 30, crack_y + 5))
            crack.setBorderColor('darkBlue')
            crack.setBorderWidth(2)
            crack.setDepth(29)
            self.add(crack)
        
        # 고퀄리티 눈송이들 (다양한 크기)
        for i in range(40):
            size = random.randint(2, 6)
            snow = Circle(size)
            snow.setFillColor('white')
            snow.setBorderColor('lightBlue')
            snow.setBorderWidth(1)
            snow.move(random.randint(-500, 500), random.randint(-150, 100))
            snow.setDepth(20)
            self.add(snow)
        
        # 눈 더미들
        for i in range(8):
            pile_x = random.randint(-400, 400)
            pile_y = random.randint(60, 120)
            pile = Ellipse(random.randint(20, 40), random.randint(8, 15))
            pile.setFillColor('white')
            pile.setBorderColor('lightBlue')
            pile.move(pile_x, pile_y)
            pile.setDepth(22)
            self.add(pile)


# 달력 장면 함수
def show_calendar_scene(world, calendar):
    """달력 장면 표시 및 애니메이션"""
    # 달력 장면 (중앙에 배치)
    world.move(1040, 360)  # 달력(-400)이 화면 중앙(640)에 오도록
    time.sleep(1.5)
    
    # 달력 애니메이션
    calendar.tear_page()
    time.sleep(2)

# 오두막 장면 함수
def show_cabin_scene(world, cabin):
    """오두막 장면으로 이동 - 단순하게"""
    # 오두막으로 즉시 이동
    world.move(-800, 0)
    time.sleep(3)


# 메인 함수
def main():
    # 캔버스 설정
    canvas = Canvas(1280, 720)
    canvas.setBackgroundColor('darkBlue')
    canvas.setTitle("Christmas Animation")
    
    # 월드 레이어 (모든 객체 포함)
    world = Layer()
    canvas.add(world)
    
    # 배경 풍경
    ground = Rectangle(3000, 400)
    ground.setFillColor('white')
    ground.move(0, 400) # 하단 배치
    ground.setDepth(200) # 맨 뒤로 보내기
    world.add(ground)
    
    # 눈 내리는 효과 (입자)
    for i in range(50):
        s = Circle(random.randint(2, 5))
        s.setFillColor('white')
        s.setBorderColor('white')
        s.move(random.randint(-1000, 1000), random.randint(-500, 500))
        s.setDepth(150) # 배경 앞, 다른 객체 뒤
        world.add(s)

    # 1. 장면 요소 배치
    # 달력을 왼쪽 멀리 배치
    calendar = Calendar()
    calendar.move(-400, 0)
    calendar.setDepth(10) # 앞쪽에 배치
    world.add(calendar)
    
    # 오두막을 오른쪽 멀리 배치
    cabin = Cabin()
    cabin.move(400, 100) # 약간 아래쪽
    cabin.setDepth(10) # 앞쪽에 배치
    world.add(cabin)
    
    # 겨울 풍경 배경을 오두막 바로 뒤에 배치
    winter_scene = WinterLandscape()
    winter_scene.move(400, 0) # 오두막 바로 뒤
    winter_scene.setDepth(20) # 오두막보다 뒤쪽에 배치
    world.add(winter_scene)
    
    
    # 컨트롤러 생성
    ctrl = AnimationController(canvas, world)
    
    # --- 간단한 애니메이션 시퀀스 ---
    
    # 1. 달력 장면
    show_calendar_scene(world, calendar)
    
    # 2. 오두막 장면 (뒤에 설산 배경이 보임)
    show_cabin_scene(world, cabin)
    
    canvas.wait()
    canvas.close()

if __name__ == "__main__":
    main()
