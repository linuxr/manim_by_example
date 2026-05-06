# 1. 🔲 基础对象：几何图形: 05-贝塞尔曲线
from manim import (
    BLUE,
    BLUE_A,
    BLUE_C,
    BLUE_D,
    BLUE_E,
    DOWN,
    GREEN,
    GREEN_C,
    GREEN_D,
    GREEN_E,
    LEFT,
    PINK,
    RED,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Create,
    CubicBezier,
    DashedLine,
    Dot,
    Line,
    Scene,
    Text,
    VGroup,
    Write,
)


class CubicBezierExample(Scene):
    def construct(self):
        # 定义四个控制点
        start_anchor = LEFT * 4 + DOWN * 2
        start_handle = LEFT * 2 + UP * 2
        end_handle = RIGHT * 2 + UP * 2
        end_anchor = RIGHT * 4 + DOWN * 2

        # 创建贝塞尔曲线
        bezier = CubicBezier(
            start_anchor,  # 起点
            start_handle,  # 第一个控制点
            end_handle,  # 第二个控制点
            end_anchor,  # 终点
            color=YELLOW,
            stroke_width=4,
        )

        # 可视化控制点
        dots = VGroup(
            *[
                Dot(start_anchor, color=WHITE),
                Dot(start_handle, color=BLUE),
                Dot(end_handle, color=BLUE),
                Dot(end_anchor, color=WHITE),
            ]
        )

        # 添加控制点标签
        labels = VGroup(
            Text("起点", font_size=24).next_to(start_anchor, DOWN),
            Text("控制点1", font_size=24, color=BLUE).next_to(start_handle, UP),
            Text("控制点2", font_size=24, color=BLUE).next_to(end_handle, UP),
            Text("终点", font_size=24).next_to(end_anchor, DOWN),
        )

        # 绘制辅助线（连接起点到控制点，控制点到终点）
        guide_lines = VGroup(
            DashedLine(start_anchor, start_handle, color=BLUE_A, stroke_opacity=0.5),
            DashedLine(start_handle, end_handle, color=BLUE_A, stroke_opacity=0.5),
            DashedLine(end_handle, end_anchor, color=BLUE_A, stroke_opacity=0.5),
        )

        # 动画展示
        self.play(Create(guide_lines), Create(dots), Write(labels), run_time=1.5)

        self.play(Create(bezier), run_time=2)
        self.wait()


class HeartShape(Scene):
    def construct(self):
        # 左半边爱心的四个控制点
        left_points = [
            DOWN * 2.5,  # 起点（底部尖端）
            LEFT * 3 + DOWN,  # 控制点1
            LEFT * 2 + UP * 2,  # 控制点2
            UP * 0.5,  # 终点（顶部凹陷处）
        ]

        # 右半边爱心的四个控制点
        right_points = [
            DOWN * 2.5,  # 起点（底部尖端，与左半边共用）
            RIGHT * 3 + DOWN,  # 控制点1
            RIGHT * 2 + UP * 2,  # 控制点2
            UP * 0.5,  # 终点（顶部凹陷处，与左半边共用）
        ]

        # 绘制左半边（红色）
        left_heart = CubicBezier(
            left_points[0],
            left_points[1],
            left_points[2],
            left_points[3],
            color=RED,
            stroke_width=6,
        )

        # 绘制右半边（粉色）
        right_heart = CubicBezier(
            right_points[0],
            right_points[1],
            right_points[2],
            right_points[3],
            color=PINK,
            stroke_width=6,
        )

        # 组合成完整爱心
        heart = VGroup(left_heart, right_heart)

        # 添加标题
        title = Text("❤️ 贝塞尔曲线绘制爱心", font_size=36, color=RED)
        title.to_edge(UP)

        self.play(Write(title))
        self.wait(0.5)
        self.play(Create(heart), run_time=3)
        self.wait()


class WaterDrop(Scene):
    def construct(self):
        # 水滴的四个控制点
        drop_points = [
            DOWN * 3,  # 起点（底部尖端）
            LEFT * 2 + DOWN,  # 控制点1（向左拉）
            LEFT * 1.5 + UP,  # 控制点2（向上并向左）
            UP * 2,  # 终点（顶部圆润处）
        ]

        # 左侧曲线
        left_curve = CubicBezier(
            drop_points[0],
            drop_points[1],
            drop_points[2],
            drop_points[3],
            color=BLUE_C,
            stroke_width=6,
        )

        # 右侧曲线（镜像）
        right_curve = CubicBezier(
            DOWN * 3,  # 起点（与左侧共用）
            RIGHT * 2 + DOWN,  # 控制点1（向右拉）
            RIGHT * 1.5 + UP,  # 控制点2（向上并向右）
            UP * 2,  # 终点（与左侧共用）
            color=BLUE_D,
            stroke_width=6,
        )

        # 顶部连接弧
        top_arc = CubicBezier(
            UP * 2,
            RIGHT * 0.5 + UP * 2.5,
            LEFT * 0.5 + UP * 2.5,
            UP * 2,
            color=BLUE_E,
            stroke_width=6,
        )

        water_drop = VGroup(left_curve, right_curve, top_arc)

        # 添加标题
        title = Text("💧 水滴", font_size=36, color=BLUE)
        title.to_edge(UP)

        self.play(Write(title))
        self.wait(0.5)
        self.play(Create(water_drop), run_time=3)
        self.wait()


class LeafShape(Scene):
    def construct(self):
        # 叶子的四个控制点
        leaf_points = [
            LEFT * 3,  # 起点（叶柄）
            LEFT * 1 + UP * 2,  # 控制点1（向上弯曲）
            RIGHT * 1 + UP * 2,  # 控制点2（向上弯曲）
            RIGHT * 3,  # 终点（叶尖）
        ]

        # 上半部分
        top_leaf = CubicBezier(
            leaf_points[0],
            leaf_points[1],
            leaf_points[2],
            leaf_points[3],
            color=GREEN_C,
            stroke_width=6,
        )

        # 下半部分（镜像）
        bottom_leaf = CubicBezier(
            LEFT * 3,  # 起点（与上半部分共用）
            LEFT * 1 + DOWN * 2,  # 控制点1（向下弯曲）
            RIGHT * 1 + DOWN * 2,  # 控制点2（向下弯曲）
            RIGHT * 3,  # 终点（与上半部分共用）
            color=GREEN_D,
            stroke_width=6,
        )

        # 添加叶脉
        mid_vein = Line(LEFT * 3, RIGHT * 3, color=GREEN_E, stroke_width=3)

        leaf = VGroup(top_leaf, bottom_leaf, mid_vein)

        # 添加标题
        title = Text("🌿 叶子", font_size=36, color=GREEN)
        title.to_edge(UP)

        self.play(Write(title))
        self.wait(0.5)
        self.play(Create(leaf), run_time=3)
        self.wait()
