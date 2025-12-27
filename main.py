from manim import *

# config.background_color = "#1c0d1a"

class AngleFunc(Scene):
    def construct(self):
        self.create()
    
    def create(self):
        # 绘制坐标系
        nbp = NumberPlane(
            x_range=[-2.5, 2.5, 1],
            y_range=[-1.5, 1.5, 1],
            axis_config={
                "stroke_width" : 0,
            },
            background_line_style={
                "stroke_width": 2,
                "stroke_opacity": 0.8,
            }
        ).scale(2)
        angleValueTracker = ValueTracker(1/4)
        # 绘制角两边
        line1 = Line(
            start=[0,0,0],
            end=[3,0,0],
            color="#fffef8",
        )
        line2 = Line(
            start=[0,0,0],
            end=[3,0,0],
            color="#fffef8",
        ).rotate_about_origin(PI/4)
        angle = Angle(
                line1, line2,
                radius=0.5,
                other_angle=False if angleValueTracker.get_value() > 0 else True,
                color="#fcd217"
            )
         # 保证角度值在-180到180之间,使旋转不易错乱
        def getPI(x):
            if abs(x) > 2  and int(abs(x)) % 2 == 1:
                return x + (int(abs(x)) - 1)
            elif abs(x) <= 2:
                return x
            elif abs(x) > 2 and int(abs(x)) % 2 == 0:
                return x + (int(abs(x)))
            
            
        # 绘制角度标记
        angle_text = MathTex(
            r"\theta",
        ).move_to( Point([ 1.5*np.cos(PI/2 * getPI(angleValueTracker.get_value())),
                        1.5*np.sin(PI/2 * getPI(angleValueTracker.get_value())),
                        0]))
        
        # 角度值和角度值文字
        angle_value_text = MathTex(r"\theta = ").align_on_border(LEFT).shift(UP*0.5+RIGHT)
        angle_value = DecimalNumber(angle.get_value(degrees=True), unit="^{\circ}").next_to(angle_value_text, RIGHT, buff=0.1)
        self.play(
            Create(nbp),
            Create(line1),
            Create(line2),
            Create(angle),
            Write(angle_text),
            Write(angle_value_text),
            Write(angle_value),
            run_time = 2,
        )
        self.wait()
        # 添加更新
        line2.add_updater(
            lambda x: x.become(
              Line(
                start=[0,0,0],
                end=[3*np.cos(angleValueTracker.get_value() * PI),3*np.sin(angleValueTracker.get_value() * PI),0],
                color="#fffef8",
              )   
            )
        )
        angle.add_updater(
            lambda x: x.become(
                Angle(
                    line1, line2,
                    radius=0.5,
                    other_angle= False if angleValueTracker.get_value() > 0 else True,
                    color="#fcd217"
                )
            )
        )
        angle_text.add_updater(
            lambda x: x.move_to(
                Point([ 1.5*np.cos(PI/2 * getPI(angleValueTracker.get_value())),
                        1.5*np.sin(PI/2 * getPI(angleValueTracker.get_value())),
                        0])
            )
        )
        angle_value.add_updater(
            lambda x: x.become(
                DecimalNumber(
                    number=angleValueTracker.get_value() * 180,
                    unit="^{\circ}"
                ).next_to(angle_value_text, RIGHT, buff=0.1)
            )
        )
        self.play(
            angleValueTracker.animate.set_value(-3),
            run_time=5,
            rate_functions = smooth,
        )
        self.wait(0.5)
        angleValueTracker.clear_updaters()
        self.play(
            angleValueTracker.animate.set_value(2),
            run_time=5,
            rate_functions = smooth,
        )
        self.wait(0.5)

class CircleFunc(Scene):
    def construct(self):
        # 创建坐标系
        nbp = NumberPlane(
            x_range=[-1.5, 1.5, 1],
            y_range=[-1.5, 1.5, 1],
            x_length=3,
            y_length=3,
        )
        nbp.scale(2)
        # 创建一个单位圆
        circle = Circle(radius=2)
        # 创建一个点，用于旋转
        dotRotate = Dot(
            point=circle.point_from_proportion(0),
            fill_opacity= 1,
        )
        # 创建一个旋转值的跟踪器
        RotValueTracker = ValueTracker(0)
        dotRotate.add_updater(
            lambda x: x.move_to(circle.point_from_proportion(RotValueTracker.get_value()%1))
        )
        # 添加点的横坐标直线,纵坐标直线
        xLine = Line(
            # FIXME : 初始位置鬼畜,原因不清
            start= nbp.c2p(0,0),
            end= [dotRotate.get_x(),0,0],
            color = GREEN
        ).add_updater(
            lambda x: x.put_start_and_end_on(
                nbp.c2p(0,0),[dotRotate.get_x(),0,0]
            )
        )
        yLine = Line(
            start= [dotRotate.get_x(),0,0],
            end= dotRotate.get_center(),
            color = YELLOW
        ).add_updater(
            lambda y: y.become(
                Line( 
                    start= [dotRotate.get_x(),0,0],
                    end= dotRotate.get_center(),
                    color = YELLOW
                )
            )
        )
        # 添加斜边
        hypotenuse = Line(
            start= nbp.c2p(0,0),
            end= dotRotate.get_center(),
            color = "#FFFFFF"
        ).add_updater(
            lambda x: x.become(
                Line(
                    start= nbp.c2p(0,0),
                    end=  dotRotate.get_center(),
                    color = "#FFFFFF"
                )
            )
        )
        
        self.add(dotRotate)
        # 保存原始状态
        circleGroup = VGroup(
            nbp,
            circle,
            xLine,
            yLine,
            hypotenuse,
            dotRotate
        )
        circleGroup.save_state()
        self.play(
            Create(nbp),
            Create(circle , introducer=True),
            run_time=2
        )
        self.wait()
        # 这里必须后画线,否则线的位置会出现问题
        self.play(
            FadeIn(hypotenuse),
            FadeIn(xLine),
            FadeIn(yLine),
            run_time = 0.5
        )
        self.wait()
        
        # 线性运动速度
        self.play(
            ChangeSpeed(
                RotValueTracker.animate.set_value(0.999999),
                speedinfo={0.25:0.5 , 0.5:0.5 ,0.6:0.4, 0.75:0.4 , 1:1}
            ),
            run_time=5
        )
        self.wait()
        
        # 添加坐标轴
        axe = Axes(
            x_range = [0,10,1],
            y_range = [-2,2,1],
            y_length = 4/0.75,
            axis_config={
                "include_numbers": True,
            },
        ).scale(0.75).align_on_border(RIGHT)
        # 将圆和nbp放在一起,移到左边
        self.play(
            circleGroup.animate.scale(0.5).align_on_border(LEFT),
            run_time = 1
        )
        # 添加角度
        angle = Angle(
            Line(nbp.c2p(0,0),nbp.c2p(1,0),color=GREEN),
            hypotenuse
        )
        angle.add_updater(
            lambda x: x.become(
                Angle(
                Line(nbp.c2p(0,0),nbp.c2p(1,0),color=GREEN),
                hypotenuse)
            )
        )
        self.play(
            Create(axe),
            run_time = 2
        )
        self.wait()
        # 将RotValueTracker的值设置为0
        RotValueTracker.set_value(0.00000001)
        # 添加正弦函数的点
        dot_sin =  Dot(
                axe.c2p(angle.get_value() /180 * PI,np.sin(angle.get_value()/180 * PI)),
        )
        # 为该点设置单独的更新器
        dot_sin_tracker = ValueTracker(0.00000001)
        dot_sin.add_updater(
            lambda x: x.move_to(
                axe.c2p(
                    dot_sin_tracker.get_value(),
                    np.sin(dot_sin_tracker.get_value())
                )
            )
        )
        # 添加正弦函数的路径
        sin_path = TracedPath(dot_sin.get_center , color=YELLOW_A)
        # 将旋转点和正弦函数的点作连线,并添加到场景
        linkLine = DashedLine(
            dotRotate.get_center(),
            dot_sin.get_center(),
            color=WHITE
        ).add_updater(
            lambda x: x.become(
                DashedLine(
                    dotRotate.get_center(),
                    dot_sin.get_center(),
                    color=WHITE
                )
            )
        )
        self.add(sin_path)
        self.play(
            Create(dot_sin),
            Create(linkLine),
            run_time = 1
        )
        self.play(
             ChangeSpeed(
                AnimationGroup(
                    RotValueTracker.animate.set_value(1.5),
                    dot_sin_tracker.animate.set_value(3 * PI),
                ),
                speedinfo={0.25:0.5 , 0.5:0.5 ,0.6:0.4, 0.75:0.4 , 1:1}
            ),
           run_time = 8
        )