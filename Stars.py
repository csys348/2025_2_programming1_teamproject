
from cs1graphics import *
import math

# =================================================================
# 1. 단일 별 모양 클래스 (변경 없음)
# =================================================================
class Star(Polygon):
    def __init__(self, radius=20, color='gold'):
        """
        radius: 별의 반지름 (크기)
        color: 채우기 색상
        """
        points = []
        inner_radius = radius * 0.4
        angle_step = 36 * (math.pi / 180) 
        current_angle = -math.pi / 2 
        
        # 별의 10개 꼭짓점 계산
        for i in range(10):
            r = radius if i % 2 == 0 else inner_radius
            x = r * math.cos(current_angle)
            y = r * math.sin(current_angle)
            points.append(Point(x, y))
            current_angle += angle_step
            
        super().__init__(*points) 
        self.setFillColor(color)
        self.setBorderColor('orange')
        self.setBorderWidth(1)

# =================================================================
# 2. 별들의 고리 클래스 
# =================================================================
class StarBurst(Layer):
    def __init__(self):
        super().__init__()
        
        # 회전할 레이어 생성 
        self.outer_layer = Layer()
        self.add(self.outer_layer)

        # ---------------------------------------------------------
        # [핵심 Fix] 중심축 고정용 투명 앵커 (Invisible Anchor)
        # ---------------------------------------------------------
        # (0,0) 위치에 투명한 점을 박아두어 회전축을 강제로 고정합니다.
        anchor_outer = Circle(1, Point(0,0))
        anchor_outer.setBorderWidth(0) # 투명
        self.outer_layer.add(anchor_outer)
        
        # ---------------------------------------------------------
        # A. 바깥쪽 큰 별들 생성 (Outer Ring)
        # ---------------------------------------------------------
        num_outer = 12
        radius_outer = 180
        
        for i in range(num_outer):
            angle = (360 / num_outer) * i
            rad = math.radians(angle)
            
            x = radius_outer * math.cos(rad)
            y = radius_outer * math.sin(rad)
            
            star = Star(radius=25, color='gold')
            star.move(x, y)
            star.rotate(angle + 90) 
            self.outer_layer.add(star)

    # =============================================================
    # 별 회전시키기 메서드
    # =============================================================
    def rotate_star(self,scarf ):
        for n in range(360):
            self.outer_layer.rotate(3)
            


