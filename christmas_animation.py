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

# 달력 장면 함수
def show_calendar_scene(world, calendar):
    """달력 장면 표시 및 애니메이션"""
    # 달력이 화면 중앙에 오도록 조정
    time.sleep(1)
    
    # 달력 애니메이션
    calendar.tear_page()
    time.sleep(2)

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
    # 달력을 중앙에 배치
    calendar = Calendar()
    calendar.move(0, 0)
    calendar.setDepth(10)
    world.add(calendar)
    
    
    # 컨트롤러 생성
    ctrl = AnimationController(canvas, world)
    
    # --- 달력 애니메이션 ---
    
    # 달력 장면 실행
    show_calendar_scene(world, calendar)
    
    canvas.wait()
    canvas.close()

if __name__ == "__main__":
    main()
