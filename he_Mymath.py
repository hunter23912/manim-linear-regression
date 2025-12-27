import math
from manim import *
from manim.opengl import *
# from manim_slides import Slide
from manim_play_timeline import play_timeline
from manim_fonts import *
from manim import X11
from manim import XKCD
from manim import BS381
import numpy as np
from colour import Color

# manim plugins -l


config.cairo_renderer_settings = {
    "SCALE_FACTOR": 3
}

config.quality = "high_quality"
config.background_color = X11.GRAY1

# class Math(Scene):
#     def construct(self):
#         self.add(NumberPlane())
#         c = Circle(radius=2, color=WHITE , fill_opacity=0.1)
#         dots = VGroup(
#             *[Dot().move_to(c.point_from_proportion(i)) 
#               for i in np.linspace(0,1,200)]
#         )
#         lines = VGroup(*[Line(dots[i],dots[100+i]).set_color( color=Color(hsl=(i/100, 0.99, 0.5))) for i in range(100)]
#         )
#         self.play(Create(lines),Create(c))
#         self.wait()
#         self.play(c.animate.shift(LEFT*2).rotate(-PI/2),lines.animate.shift(RIGHT*2).rotate(PI/2))
#         self.wait()
#         self.play(FadeOut(c),FadeOut(lines))
#         lines.add_updater(
#             lambda mob ,dt: mob.rotate(PI*dt).scale(1-dt)
#         )
#         self.play(Create(lines))
#         self.wait(2)
        
        
# class AXES(Scene):
#     def construct(self):
#         axes = Axes(
#             x_range=[-8,8,1],
#             y_range=[-8,8,1],
#             x_length=8,
#             y_length=8
#         )
#         cur = axes.plot(lambda x: x).set_color(BLUE)
#         Vt = ValueTracker(1)
#         cur.add_updater(
#             lambda mob: mob.become(
#                 axes.plot(lambda x: x*(Vt.get_value()),color=BLUE)
#             )
#         )
#         # num1 = MathTex(r"\alpha=").shift(2*(2*LEFT+UP)-UP) 
#         cur_name = DecimalNumber(
#             Vt.get_value(),
#             num_decimal_places=2,
#             # show_ellipsis=True,
#             color=WHITE
#         )
#         num = MathTex(r"y=\alpha x").shift(2*(2*LEFT+UP))
#         cur_name.add_updater(
#             lambda mob: mob.set_value(Vt.get_value()).next_to(num,RIGHT)
#         )
#         Gr = VGroup(axes,cur,num)
#         self.Vt = Vt
#         self.play(Create(Gr))
#         self.interactive_embed()
        
#     def on_key_press(self, symbol, modifiers):
#         from pyglet.window import key as pyglet_key
#         if symbol == pyglet_key.UP:
#             self.play(self.Vt.animate.increment_value(1))
#         elif symbol == pyglet_key.DOWN:
#             self.play(self.Vt.animate.increment_value(-1))
#         super().on_key_press(symbol, modifiers)       
        
# class Col(Scene):
#     def construct(self):
#         X11_colors =[
#             color for color_name , color in
#             inspect.getmembers(X11, lambda obj: isinstance(obj, ManimColor))
#         ]
#         X11_colors_mob = VMobject()
#         for color in X11_colors:
#             dot = Dot(color=color,radius=0.05)
#             X11_colors_mob.add(dot)
#         # X11_colors_mob.sort()
#         X11_colors_mob.arrange_in_grid(23,41,buff=0.2)
#         self.play(FadeIn(X11_colors_mob,lag_ratio=0.01),run_time=2)
#         self.wait()
        
# class RandomDot(Scene):
#     def construct(self):
#         axe = Axes(
#             tips=False,
#             x_range=[-10,10,1],
#             y_range=[-5.7,5.7,1],
#             x_length=10,
#             y_length=5.7
#         )
#         cur = axe.plot(
#             lambda x: x,
#             x_range=[-7,7,1],
#             use_smoothing=True
#         ).set_color(YELLOW)
#         dots = VGroup()
#         for i in range(-25,26):
#             dot = Dot(
#                 radius=0.05,
#                 color=BLUE,
#                 point=[random.gauss(i/10,0.5),random.gauss(i/10,0.5),0]
#             )
#             dots.add(dot)
#         Lines = VMobject()
#         for dot in dots:
#             Lines.add(Line(
#                 color=X11.GHOSTWHITE,
#                 start=dot.get_center(),
#                 end=[dot.get_center()[0],dot.get_center()[0],0]
#             ))
#         tex = MathTex(r"y=x").set_color(WHITE).shift(3*LEFT+2*UP).scale(1.5)
#         allVg = VGroup(axe,dots,Lines,cur,tex)
#         self.play(Create(axe),FadeIn(dots,lag_ratio=0.01),run_time=2)
#         self.play(Create(cur),run_time=1)
#         self.play(Create(Lines),run_time=1)
#         self.wait()
#         # self.play(allVg.animate.shift(3*LEFT+2*UP).scale(0.5),run_time=1)
#         # self.wait()


class Math(Scene):
    def construct(self):
        
        ax = Axes(
            x_range=[-5,5.1,1],
            y_range=[-5,5.1,1],
            x_length=9,
            y_length=5.5,
            tips=False,
            axis_config={
                "numbers_to_include": np.arange(-5, 5.1, 1),
                'font_size': 24,
                # 'numbers_with_elongated_ticks': [-4,4],
                }
        ).scale(1.12)
        
        vt = ValueTracker(0)
        mat = Tex("$ y = x ^{0} + {0}x$" , color=GOLD_A).scale(1.12).shift(3*RIGHT+2*DOWN)
        cur = ax.plot(lambda x : x**vt.get_value() + x*vt.get_value() , x_range=[-5,5.1],color=BLUE)
        # cur.add_updater(
        #     lambda mob :mob.become(ax.plot(lambda x : x + vt.get_value() , color=BLUE))
        # )
        def transTex(mob):
            mob.become(Tex("$y = x^{%.2f} + {%.2f}x$"%(vt.get_value(), vt.get_value()) , color=GOLD_A).scale(1.12).shift(3*RIGHT+2*DOWN))
            return mob
        def transCur(mob):
            mob.become(ax.plot(lambda x : x**vt.get_value() + x*vt.get_value(), x_range=[-5,5.1], color=BLUE))
            return mob
        
        cur_with_tex = AnimationGroup(ApplyFunction(transTex, mat) ,ApplyFunction(transCur , cur) , lag_ratio=0.2 )
        
        self.play(Create(ax),Create(cur),run_time=2)
        self.add(mat)
        self.wait()
        for i in np.arange(1, 7 ,1):
            vt.set_value(i)
            self.play(cur_with_tex,run_time = 1)
            self.wait()
        self.wait()
        vt.set_value(1)
        self.play(cur_with_tex , run_time=1)
        self.wait()        


class Gauss(Scene):
    def construct(self): 
        v = ValueTracker(0)
        sigm = ValueTracker(0.2)
        ax = Axes(
            x_range=[-8,8,1],
            y_range=[-8,8,1],
            x_length=10,
            y_length=8,
            tips=False
        )
        cur = ax.plot(lambda x : (1/(math.sqrt(2*PI)*sigm.get_value()))*math.exp(-(x-v.get_value())**2)/(2*sigm.get_value())).set_color(ORANGE)
        self.play(Create(ax),Create(cur),run_time=2)
        self.wait()
        cur.add_updater(
            lambda mob : mob.become(ax.plot(lambda x : (1/(math.sqrt(2*PI)*sigm.get_value()))*math.exp(-(x-v.get_value())**2)/(2*sigm.get_value())).set_color(ORANGE))
        )
        self.play(v.animate.set_value(2),run_time=2)
        self.wait()
        self.play(sigm.animate.set_value(0.4),run_time=2)
        self.wait()
        self.play(v.animate.set_value(-2),run_time=2)
        self.wait()
        self.play(sigm.animate.set_value(0.24),run_time=2)
        self.wait()
        
class Tables(Scene):
    def construct(self):
        aver_chi = 1.75
        sigm_chi = 0.05
        data_arr_chi = np.random.normal(aver_chi,sigm_chi,100)
        
        # 删除data_arr_chi中的数据小于 1.5 的数据
        data_arr_chi = data_arr_chi[data_arr_chi > 1.5]
        data_arr_chi = np.round(data_arr_chi,2)
        data_arr_par = 0.97*data_arr_chi + np.random.normal(0,0.05,len(data_arr_chi))
        data_arr_par = np.round(data_arr_par,2)
        
        # 线性回归模型
        par = np.polyfit(data_arr_chi , data_arr_par , 1)
        par = np.around(par,2)
        
        # 数据入表
        data_table = []
        for i in range(100):
            data_table.append([str(data_arr_par[i]),str(data_arr_chi[i])])
        
        # 插入省略符
        data_table[8] = ["..." , "..."]
        data_table = Table(
                table=data_table[0:10],
            col_labels=[Text("y=父辈身高" , font='Microsoft YaHei'), Text("x=子辈身高",font='Microsoft YaHei')],
            include_outer_lines=True
        ).scale(0.4)
        
        # 绘制图表
        self.play(data_table.create())
        self.wait()
        self.play(data_table.animate.shift(4.5*LEFT).scale(0.95))
        self.wait()
        
        # 绘制坐标轴
        ax_table = Axes(
            x_range=[1.4,2.1,0.1],
            y_range=[1.4,2.1,0.1],
            x_length=7,
            y_length=7,
            tips=False,
            axis_config={"include_numbers": True}
        ).scale(0.75).shift(RIGHT*1.2)
        
        # 定义坐标轴标签
        ax_label = ax_table.get_axis_labels(
            y_label=Text(r"父辈身高",font='Microsoft YaHei').scale(0.35),
            x_label=Text(r"子辈身高",font='Microsoft YaHei').scale(0.35)
        )
        
        # 绘制直线
        line = ax_table.plot(
            lambda x: par[0]*x + par[1] ,
            color=BLUE ,
            x_range=[1.4,2.1]
        ).set_color(YELLOW).scale(0.75)
        
        # 绘制直线方程
        if par[1] > 0:
            line_func = MathTex(r"y=%.2lf\codt{x}+%.2lf"%(par[0],par[1]))
        else :
            line_func = MathTex(r"y=%.2lf\cdot{x}%.2lf"%(par[0],par[1]))
        line_func.next_to(line,RIGHT).shift(LEFT*0.5).scale(0.75)
        
        # 绘制散点
        dots = VGroup()
        for i in range(100):
            dot = np.around(ax_table.coords_to_point(data_arr_chi[i],data_arr_par[i] + 0.01),2)
            dots.add(Dot(point=[dot[0] , dot[1] ,0],radius=0.05,color=BLUE))
        
        self.play(
            FadeIn(ax_table),
            FadeIn(ax_label),
            Create(dots),
            run_time = 2,
            lag_ratio = 0.01
        )
        self.wait()
        self.play(
            Create(line),
            Write(line_func),
            run_time = 2,
            lag_ratio = 0.01
        )
        self.wait()
        
        
class Open(Scene):
    def construct(self):
        with RegisterFont("ZCOOL XiaoWei") as fonts:
            openText = VGroup()
            opentext_hello = Text(
                "线性回归",
                font="快看世界体",
                color=BS381.BS381_172
            )
            opentext_hello1 =  Text(
                "——预测的艺术",
                font=fonts[0],
            ).next_to(opentext_hello,DOWN)
            opentext_hello2 = Text(
                'Linear Regression',
                font='Afacad',
            ).align_on_border(RIGHT+DOWN).set_color_by_gradient('#5D9FFF', '#B8DCFF','#6BBBFF')
            openText.add(opentext_hello,opentext_hello1 , opentext_hello2)
            
            
            axe_open = Axes(
                tips=False,
                x_range=[-10,10,1],
                y_range=[-5.7,5.7,1],
                x_length=10,
                y_length=5.7
            )
            cur_open = axe_open.plot(
                lambda x: x,
                x_range=[-7,7,1],
                use_smoothing=True
            ).set_color(YELLOW)
            dots_open = VGroup()
            for i in range(-50,51):
                dot = Dot(
                    radius=0.05,
                    color=BLUE,
                    point=[random.gauss(i/15,0.5),random.gauss(i/15,0.5),0]
                )
                dots_open.add(dot)
            openDotGroup = VGroup(axe_open,dots_open,cur_open)

            openText.scale(1.5).shift(2*LEFT+1.5*UP)
            self.play(Create(openDotGroup ,lag_ratio=0.02),run_time=2)
            self.play(openDotGroup.animate.shift(RIGHT).scale(0.5),run_time = 1)
            self.play(Write(openText),run_time = 2)            
            self.wait()
        

# class BasicExample(Slide):
#     def construct(self):
#         circle = Circle(radius=3, color=BLUE)
#         dot = Dot()

#         self.play(GrowFromCenter(circle))
#         self.wait()  # Waits user to press continue to go to the next slide

#         self.next_slide(loop=True)  # Start loop
#         self.play(MoveAlongPath(dot, circle), run_time=2, rate_func=linear)
#         self.wait()  # This will start a new non-looping slide

#         self.play(dot.animate.move_to(ORIGIN))
        
        
# class SlidesTables(Slide):
#     def construct(self):
#         aver_chi = 1.75
#         sigm_chi = 0.05
#         data_arr_chi = np.random.normal(aver_chi,sigm_chi,100)
        
#         # 删除data_arr_chi中的数据小于 1.5 的数据
#         data_arr_chi = data_arr_chi[data_arr_chi > 1.5]
#         data_arr_chi = np.round(data_arr_chi,2)
#         data_arr_par = 0.97*data_arr_chi + np.random.normal(0,0.05,len(data_arr_chi))
#         data_arr_par = np.round(data_arr_par,2)
        
#         # 线性回归模型
#         par = np.polyfit(data_arr_chi , data_arr_par , 1)
#         par = np.around(par,2)
        
#         # 数据入表
#         data_table = []
#         for i in range(100):
#             data_table.append([str(data_arr_par[i]),str(data_arr_chi[i])])
        
#         # 插入省略符
#         data_table[8] = ["..." , "..."]
#         data_table = Table(
#                 table=data_table[0:10],
#             col_labels=[Text("y=父辈身高" , font='Microsoft YaHei'), Text("x=子辈身高",font='Microsoft YaHei')],
#             include_outer_lines=True
#         ).scale(0.4)
        
#         # 绘制图表
#         self.play(data_table.create())
#         self.wait()
#         self.play(data_table.animate.shift(4.5*LEFT).scale(0.95))
#         self.wait()
        
#         # 绘制坐标轴
#         ax_table = Axes(
#             x_range=[1.4,2.1,0.1],
#             y_range=[1.4,2.1,0.1],
#             x_length=7,
#             y_length=7,
#             tips=False,
#             axis_config={"include_numbers": True}
#         ).scale(0.75).shift(RIGHT*1.2)
        
#         # 定义坐标轴标签
#         ax_label = ax_table.get_axis_labels(
#             y_label=Text(r"父辈身高",font='Microsoft YaHei').scale(0.35),
#             x_label=Text(r"子辈身高",font='Microsoft YaHei').scale(0.35)
#         )
        
#         # 绘制直线
#         line = ax_table.plot(
#             lambda x: par[0]*x + par[1] ,
#             color=BLUE ,
#             x_range=[1.4,2.1]
#         ).set_color(YELLOW).scale(0.75)
        
#         # 绘制直线方程
#         if par[1] > 0:
#             line_func = MathTex(r"y=%.2lf\codt{x}+%.2lf"%(par[0],par[1]))
#         else :
#             line_func = MathTex(r"y=%.2lf\cdot{x}%.2lf"%(par[0],par[1]))
#         line_func.next_to(line,RIGHT).shift(LEFT*0.5).scale(0.75)
        
#         # 绘制散点
#         dots = VGroup()
#         for i in range(100):
#             dot = np.around(ax_table.coords_to_point(data_arr_chi[i],data_arr_par[i] + 0.01),2)
#             dots.add(Dot(point=[dot[0] , dot[1] ,0],radius=0.05,color=BLUE))
        
#         self.play(
#             FadeIn(ax_table),
#             FadeIn(ax_label),
#             Create(dots),
#             run_time = 2,
#             lag_ratio = 0.01
#         )
#         self.wait()
#         self.play(
#             Create(line),
#             Write(line_func),
#             run_time = 2,
#             lag_ratio = 0.01
#         )
        
class DescribeMath(Scene):
    def construct(self):
        axe = Axes(
            x_range=[1.4,2.1,0.1],
            y_range=[1.4,2.1,0.1],
            x_length=9,
            y_length=5.5
        )
        y_axe_label = axe.get_y_axis_label("y" , edge=LEFT , direction=LEFT , buff=0)
        x_axe_label = axe.get_x_axis_label("x")
        axe_cur = axe.plot(
            lambda x: 1.06*x - 0.1, 
            color=YELLOW,
            x_range=[1.45,2.05,0.1]
        )
        axe_blue_dash = axe.get_lines_to_point(axe.c2p(2.1,2.1) , color=BLUE)
        dots = VGroup()
        dots.add(
            Dot(point=axe.c2p(1.5,1.64),radius=0.075),
            Dot(point=axe.c2p(1.63,1.60),radius=0.075),
            Dot(point=axe.c2p(1.72,1.76),radius=0.075),
            Dot(point=axe.c2p(1.8,1.91),radius=0.075),
            Dot(point=axe.c2p(1.95,1.8),radius=0.075),
            Dot(point=axe.c2p(1.77,1.64),radius=0.075),
        )
        dots.set_color(X11.HOTPINK1)
        position_cur = axe.input_to_graph_point(1.77 , axe_cur)
        line_pos_dot = Line(
            start=position_cur,
            end=dots[5].get_center(),
            color=WHITE
        )
        text_dots = VGroup()
        text_dots.add(MathTex(
                r"(x_{i} ,y_{i})"
            ).next_to(dots[5],DOWN).scale(0.65).set_color(WHITE)       
        )
        brace_line = Brace(line_pos_dot , direction=line_pos_dot.copy().rotate(PI/2).get_unit_vector() , buff=0.1)
        text_dots.add(
            MathTex(r"S_{i} = (y_{i} - \hat{y}_{i})^{2}").next_to(brace_line,RIGHT).scale(0.8).set_color(WHITE).shift(LEFT*0.3)
        )
        
        
        Left_mob = VGroup(
            axe , axe_blue_dash, x_axe_label,
            y_axe_label, text_dots , brace_line ,
            axe_cur , line_pos_dot,
            dots
        )
        Left_mob.save_state()
        math_tex = MathTex(
            r"S = (y_{1}-\hat{y}_{1})^2 +(y_{2}-\hat{y}_{2})^2 \cdots+(y_{n}-\hat{y}_{n})^2"
        ).shift(DOWN)
        math_tex1_sigma = MathTex(
            r"{ S=\sum_{i=1}^{n} }","(","{{y_i}}","-","{{\hat{y_i}}})^2"
        ).next_to(math_tex , DOWN)
        math_tex2_haty = MathTex(
            r"\hat{y}_{i} = b x_{i} + a"
        ).next_to(math_tex1_sigma , RIGHT).shift(LEFT)
        
        math_tex2_sigma_all = MathTex(
            r"S = \sum_{i=1}^{n}",r"(",r"{y_i}",r"-",r"(bx_{i}+a))^2",
        ).shift(DOWN*2)
        math_tex2_sigma_all[4][1].set_color_by_gradient(['#84fab0', '#8fd3f4'])
        math_tex2_sigma_all[4][5].set_color_by_gradient(['#84fab0', '#8fd3f4'])
        self.play(
            FadeIn(axe), 
            Write(y_axe_label), 
            Write(x_axe_label),
            Create(axe_blue_dash), 
            run_time=2
        )
        self.wait()
        self.play(Create(dots),run_time=1.5 , rate_func=lambda t: smooth(t, 3))
        self.wait()
        self.play(
            Create(axe_cur),
            Write(text_dots[0]),
            Create(line_pos_dot),
            FadeIn(brace_line),
            Write(text_dots[1]),
            run_time=2
        )
        self.play(
                dots[0:5].animate.set_fill(opacity=0.5),
                run_time = 0.3
        )
        self.play(
            FocusOn(dots[5], opacity=0.25 , color=color_gradient(['#fdcbf1','#fdcbf1','#e6dee9'],3)),
            run_time = 1
        )
        self.play(Indicate(VGroup(text_dots[1],text_dots[0])))
        self.wait()
        self.play(
            Left_mob.animate.align_on_border(UP).scale(0.7).shift(UP),
        )
        self.play(TransformFromCopy(dots , math_tex), run_time = 1)
        self.wait()
        self.play(TransformFromCopy(math_tex, math_tex1_sigma), run_time = 1)
        self.wait()
        self.play(Indicate(math_tex1_sigma[4]) , run_time = 1)
        self.play(math_tex1_sigma.animate.shift(LEFT*2),TransformFromCopy(math_tex1_sigma[4] , math_tex2_haty) , run_time = 1)
        self.wait()
        self.play(ReplacementTransform(VGroup(math_tex2_haty , math_tex1_sigma) , math_tex2_sigma_all),run_time=1.5)
        self.wait()
        self.play(FadeOut(VGroup(Left_mob, math_tex1_sigma,math_tex2_haty,math_tex)),run_time=1)
        self.wait()    
        
        # 开始求导讲解 Derivative
        math_tex2_sigma_all.save_state()
        self.play(math_tex2_sigma_all.animate.center().shift(UP))
        desText = VGroup()
        desText.add(Text(
                "可以发现，S是一个关于b和a的二次函数",
                font="快看世界体",
                t2g={
                    'a':('#84fab0', '#8fd3f4'),
                    'b':('#84fab0', '#8fd3f4')
                }
            ).next_to(math_tex2_sigma_all,DOWN*1.2)
        )
        desText.add(Text(
                "求导? S关于b,a的最小值? ",
                font="快看世界体",
                t2g={
                    'a':('#84fab0', '#8fd3f4'),
                    'b':('#84fab0', '#8fd3f4')
                }
            ).next_to(desText[0],DOWN)
        )
        desText.add(Text(
            "求导取得二次函数最小值",
                font="快看世界体",
            color = XKCD.CANARYYELLOW
            ).next_to(math_tex2_sigma_all,UP).shift(UP*0.7).scale(1.2)
        )
        desText.scale(0.75)
        self.play(Write(desText[0:2]), run_time = 2)
        self.wait()
        self.play(Circumscribe(desText[1][0:2]),
                  Circumscribe(desText[0][-4:]),
                  Circumscribe(desText[1][-4:-1]),
                  desText[0][-4:].animate.set_color(XKCD.CANARYYELLOW),
                  desText[1][0:2].animate.set_color(XKCD.CANARYYELLOW),
                  desText[1][-4:-1].animate.set_color(XKCD.CANARYYELLOW),
                  run_time=1.5)
        self.wait()
        desText_d = VGroup(
            desText[0][-4:].copy(),
            desText[1][0:2].copy(),
            desText[1][-4:-1].copy()
        )
        
        self.play(
            TransformFromCopy(desText_d , desText[2]),
            run_time = 1.5
        )
        self.wait()
        self.play(FadeOut(desText),run_time=1)
        self.play(math_tex2_sigma_all.animate.shift(DOWN*2) , run_time =1)
        
        desText.add(Text(
                "分别单独考虑a对S和b对S的影响\n\n若只考虑a",
                font="快看世界体",
                t2g={
                    'a':('#84fab0', '#8fd3f4'),
                    'b':('#84fab0', '#8fd3f4')
                }
            ).shift(UP*0.7)
        )
        
        math_tex2_sigma_all_da = MathTex(
            r"\frac{\mathrm{d}S}{\mathrm{d}a} = \sum_{i=1}^{n}{-2}\cdot(y_{i}", "-", "b","x_{i} -", "a",")",
        ).next_to(desText[-1],DOWN*0.4)
        
        math_tex2_sigma_all_da[2].set_color_by_gradient('#84fab0', '#8fd3f4')
        math_tex2_sigma_all_da[4].set_color_by_gradient('#84fab0', '#8fd3f4')
        self.play(Write(desText[-1]), run_time = 2)
        self.wait()
        self.play(ReplacementTransform(math_tex2_sigma_all,math_tex2_sigma_all_da),run_time=1.5)
        self.wait()
        self.play(FadeOut(desText[-1]),run_time=1)
        self.wait()
        
        Vt_a = ValueTracker(1.4)
        dots[0:5].set_fill(opacity=1)
        axe_cur = axe.plot(
            lambda x : 1.06*x + 1.65-1.4,
            color = YELLOW,
            x_range=[1.45,2.05,0.1]
        )
        Left_mob = VGroup(
            axe , axe_blue_dash, x_axe_label,
            y_axe_label, axe_cur ,dots
        ).align_on_border(LEFT).shift(DOWN*2).scale(0.8)
        
        tex2_haty = Text(
            r"假令b不变，改变a",
            font="Microsoft Sans Serif",
            font_size=40,
            t2f={
                'b':'Times New Roman',
                'a':'Times New Roman'
            }
        ).align_on_border(UL).shift(RIGHT*0.2 + DOWN*0.2)
        
        tex2_haty[2].set_color_by_gradient(['#84fab0', '#8fd3f4'])
        tex2_haty[-1].set_color_by_gradient(['#84fab0', '#8fd3f4'])
        math_tex2_haty = MathTex(
            r"\hat{y} =bx+a"
        ).next_to(Left_mob , DOWN)
        
        
        # 右边的轴
        axe_right = axe.copy()
        raxe_blue_dash = axe_right.get_lines_to_point(axe_right.c2p(2.1,2.1) , color=BLUE)
        rx_axe_label = axe_right.get_x_axis_label("a").scale(0.6)
        ry_axe_label = axe_right.get_y_axis_label("S",edge=LEFT,direction=LEFT,buff=0).scale(0.6)
        
        # 二次曲线
        def fun_cur(x):
            return 8*(x-1.75)**2  + 1.5
        
        cur_x_2 = axe_right.plot(
            fun_cur,
            x_range=[1.4,2.1],
            color = BLUE
        )
        slope_cur_x = np.linspace(1.4,1.75,100)
        slope_cur_x[-1] = 1.75
        slope_cur = axe_right.get_secant_slope_group(
            x = slope_cur_x[0], 
            graph = cur_x_2,
            dx = 0.0001, 
            secant_line_length = 5,
            secant_line_color = RED_D,
        )
        
        Right_mob = VGroup(
            axe_right ,raxe_blue_dash,
            rx_axe_label,ry_axe_label,
            cur_x_2,slope_cur
        ).align_on_border(RIGHT)
    
        
        self.play(math_tex2_sigma_all_da.animate.next_to(Right_mob, DOWN).scale(0.75))
        self.wait()
        for i,j in zip(Left_mob, Right_mob):
            self.play(Create(i), Create(j),run_time = 0.75)
        self.wait()
        
        self.play(
            Write(tex2_haty),
            Write(math_tex2_haty),
            run_time = 1.5
        )
        
        slope_dot =Dot(
                point=[axe_right.c2p(slope_cur_x[0] , fun_cur(slope_cur_x[0]))],
                fill_opacity=1
            )
        h_line =  axe_right.get_lines_to_point(slope_dot.get_center())
        
        self.play(Create(h_line))
        h_line.add_updater(
            lambda mob : mob.become(axe_right.get_lines_to_point(axe_right.c2p(Vt_a.get_value() , fun_cur(Vt_a.get_value()))))
        )
        slope_dot.add_updater(
            lambda mob : mob.become(Dot(
                    point=[axe_right.c2p(Vt_a.get_value() , fun_cur(Vt_a.get_value()))],
                    fill_opacity=1
                )
            )
        )
        slope_cur.add_updater(
            lambda mob : mob.become(axe_right.get_secant_slope_group(
                    x = Vt_a.get_value(), 
                    graph = cur_x_2,
                    dx = 0.0001, 
                    secant_line_length = 5,
                    secant_line_color = RED_D,
                )
            )
        )
        
        axe_cur.add_updater( 
            lambda mob: mob.become(axe.plot(
                    lambda x : 1.06 *x -Vt_a.get_value() + 1.65,
                    color = YELLOW,
                    x_range=[1.45,2.05,0.1]
                )
            )
        )
        self.play(Vt_a.animate.set_value(1.75),run_time=4)
        self.wait()
        self.play(FadeOut(Left_mob), 
                  FadeOut(axe_cur),
                  FadeOut(math_tex2_haty),
                  run_time = 1)
        
        # math_tex2_sigma_all_da
        explain_text = Text(
            "当a取得二次函数对称轴\n\nS取得最小值，此时",
                font_size=25,
                font="快看世界体",
                t2g={
                    'a':('#84fab0', '#8fd3f4'),
                },
                t2c={
                    '二次函数对称轴': XKCD.CANARYYELLOW
                }
        ).next_to(tex2_haty,DOWN)
        explain_Math = MathTex(
            r"&\frac{\mathrm{d}S}{\mathrm{d}a}=0",r"\\&\sum_{i=1}^{n}{y_i}=",r"b",r"\sum_{i=1}^{n}{x_i}+n",r"a"
        )
        explain_Math_help = Text(
            "即"
        ).next_to(explain_Math[0],RIGHT)
        
        explain_Math[2].set_color_by_gradient(['#84fab0', '#8fd3f4'])
        explain_Math[4].set_color_by_gradient(['#84fab0', '#8fd3f4'])
        
        explain_MathAll = VGroup(
            explain_Math_help , 
            explain_Math
        ).next_to(explain_text , DOWN).scale(0.75)
        
        self.play(
            Write(explain_MathAll[0]),
            Write(explain_MathAll[1][0]),
            Write(explain_text),
            run_time = 2
        )
        self.play(
            math_tex2_sigma_all_da.animate.next_to(explain_Math[0],DOWN).shift(RIGHT*2),
            run_time = 1.5
        )
        self.play(
            Circumscribe(math_tex2_sigma_all_da),
            run_time = 2
        )
        self.play(
            Transform(math_tex2_sigma_all_da,explain_MathAll[1][1:]),
            run_time = 2
        )
        self.wait(2)
        self.play(
            FadeOut(explain_MathAll), 
            FadeOut(explain_text) , 
            FadeOut(tex2_haty),
            FadeOut(Right_mob),
            FadeOut(h_line),
            FadeOut(slope_cur),
            FadeOut(math_tex2_sigma_all_da),
            run_time = 1)
        
class Der_b(Scene):
    def construct(self):
        
        text_des = VGroup()
        text_des.add(Text(
                "b对S的影响与a类似",
                font="快看世界体",
                t2g={
                    'a':('#84fab0', '#8fd3f4'),
                    'b':('#84fab0', '#8fd3f4'),
                },
                fill_opacity=0.8
            ).shift(UP*2)
        )
        
        text_des.add(Text(
                "对b求导后取二次函数的对称轴",
                font="快看世界体",
                fill_opacity=0.8,
                t2g={
                    'b':('#84fab0', '#8fd3f4'),
                },
                t2c={
                    '二次函数的对称轴': XKCD.CANARYYELLOW
                }
            ).next_to(text_des[0],DOWN)
        )
        
        math_tex2_sigma_all = MathTex(
            r"S = \sum_{i=1}^{n}",r"(",r"{y_i}",r"-",r"(bx_{i}+a))^2",
        ).next_to(text_des[-1], DOWN).shift(DOWN*0.2)
        
        math_tex2_sigma_all_db = MathTex(
            r"\frac{\mathrm{d}S}{\mathrm{d}b} = -2[(\sum_{i=1}^{n}x_{i}y_{i})-" ,r"b",r"(\sum_{i=1}^{n}{x^{2}}_{i}) -", r"a",r"\sum_{i=1}^{n}x_i] ",
        ).next_to(text_des[-1], DOWN).shift(DOWN*0.2)
        math_tex2_sigma_all_db[1].set_color_by_gradient('#84fab0', '#8fd3f4')
        math_tex2_sigma_all_db[3].set_color_by_gradient('#84fab0', '#8fd3f4')
        
        self.play(
            LaggedStart(
                Write(text_des),
                Write(math_tex2_sigma_all),      
                run_time=2,
                lag_ratio=0.5
            )
        )
        self.wait()
        self.play(
            ReplacementTransform(math_tex2_sigma_all,math_tex2_sigma_all_db),
            run_time=1.5
        )
        self.wait()
        
        self.play(
            FadeOut(text_des),
            run_time=1
        )
        
        # 散点 + 坐标轴
        axe = Axes(
            x_range=[0,0.7,0.1],
            y_range=[0,0.7,0.1],
            x_length=9,
            y_length=5.5
        )
        y_axe_label = axe.get_y_axis_label("y" , edge=LEFT , direction=LEFT , buff=0)
        x_axe_label = axe.get_x_axis_label("x")
        
        # 直线
        axe_cur = axe.plot(
            lambda x: 1.06*x + 0.01, 
            color=YELLOW,
            x_range=[0.05,0.7,0.1]
        )
        axe_blue_dash = axe.get_lines_to_point(axe.c2p(0.7,0.7) , color=BLUE)
        dots = VGroup()
        dots.add(
            Dot(point=axe.c2p(0.1,0.24),radius=0.075),
            Dot(point=axe.c2p(0.23,0.20),radius=0.075),
            Dot(point=axe.c2p(0.32,0.36),radius=0.075),
            Dot(point=axe.c2p(0.4,0.51),radius=0.075),
            Dot(point=axe.c2p(0.55,0.4),radius=0.075),
            Dot(point=axe.c2p(0.37,0.24),radius=0.075),
        )
        dots.set_color(X11.HOTPINK1)
        
        
        # 添加 ValueTracker
        Vt_b = ValueTracker(3)
        Vt_x = ValueTracker(0.7)
        
        left_mob = VGroup(
            axe , axe_blue_dash, x_axe_label,
            y_axe_label, axe_cur ,dots
        ).align_on_border(LEFT).scale(0.65).shift(LEFT*1.5)
        
        # 拟合直线 描述方程
        math_tex2_haty = MathTex(
            r"\hat{y} =", r"b", r"x+",r"a"
        ).next_to(left_mob , DOWN)
        math_tex2_haty[1].set_color_by_gradient(['#84fab0', '#8fd3f4'])
        math_tex2_haty[3].set_color_by_gradient(['#84fab0', '#8fd3f4'])
        
        axe_right =  axe.copy()
        raxe_blue_dash = axe_right.get_lines_to_point(axe_right.c2p(0.7,0.7) , color=BLUE)
        raxe_x_label = axe_right.get_x_axis_label("b").scale(0.6)
        raxe_y_label = axe_right.get_y_axis_label("S",edge=LEFT,direction=LEFT,buff=0).scale(0.6)
        
        raxe_cur = axe_right.plot(
            lambda x: 8*(x-0.35)**2 + 0.15,
            x_range=[0,0.7],
            color = XKCD.PALECYAN
        )
        
        
        # 二次曲线
        def fun_cur(x):
            return 8*(x-0.35)**2 + 0.15
        
        cur_x_2 = axe_right.plot(
            fun_cur,
            x_range=[0,0.7],
            color = BLUE
        )
        slope_cur_x = np.linspace(0.7,0,100)
        slope_cur_x[-1] = 0
        slope_cur = axe_right.get_secant_slope_group(
            x = slope_cur_x[0], 
            graph = cur_x_2,
            dx = 0.0001, 
            secant_line_length = 5,
            secant_line_color = RED_D,
        )
        
        right_mob = VGroup(
            axe_right ,raxe_blue_dash,
            raxe_x_label,raxe_y_label,
            raxe_cur,slope_cur
        ).align_on_border(RIGHT).shift(RIGHT*0.5)
        
        slope_dot =Dot(
                point=[axe_right.c2p(slope_cur_x[0] , fun_cur(slope_cur_x[0]))],
                fill_opacity=1
        )
        
        # 切点和切线
        slope_dot.add_updater(
            lambda mob : mob.become(Dot(
                    point=[axe_right.c2p(Vt_x.get_value() , fun_cur(Vt_x.get_value()))],
                    fill_opacity=1
                )
            )
        )
        slope_cur.add_updater(
            lambda mob : mob.become(axe_right.get_secant_slope_group(
                    x = Vt_x.get_value(), 
                    graph = cur_x_2,
                    dx = 0.0001, 
                    secant_line_length = 5,
                    secant_line_color = RED_D,
                )
            )
        )
        
        # 左边的线
        axe_cur.add_updater( 
            lambda mob: mob.become(axe.plot(
                    lambda x : Vt_b.get_value() *x + 0.01,
                    color = YELLOW,
                    x_range=[0.05,0.65,0.1]
                )
            )
        )
        text2_des = Text(
            "假令a不变，改变b",
            t2g={
                'a':('#84fab0', '#8fd3f4'),
                'b':('#84fab0', '#8fd3f4'),
            },
            t2f={
                'a':'Times New Roman',
                'b':'Times New Roman',
            },
            t2s={
                'a': ITALIC,
                'b': ITALIC,
            }
        ).align_on_border(UL).shift(RIGHT*0.2 + DOWN*0.2)
        self.play(math_tex2_sigma_all_db.animate.next_to(right_mob, DOWN).scale(0.65))
        self.play(
            Create(math_tex2_haty),
            Write(text2_des),
            run_time = 1.5
        )
        
        for i,j in zip(left_mob, right_mob):
            self.play(Create(i), Create(j), run_time = 0.75)
        self.wait()
        h_line = axe_right.get_lines_to_point(slope_dot.get_center())
        
        self.play(Create(h_line))
        h_line.add_updater(
            lambda mob : mob.become(axe_right.get_lines_to_point(axe_right.c2p(Vt_x.get_value() , fun_cur(Vt_x.get_value()))))
        )
        self.play(Vt_b.animate.set_value(1.06),Vt_x.animate.set_value(0.35),run_time=4)
        self.wait(2)
        
        self.play(
            FadeOut(left_mob),
            FadeOut(math_tex2_haty),
            FadeOut(axe_cur),
            run_time = 1.5
        )
        
        explain_text = Text(
            "当b取得二次函数对称轴\n\nS取得最小值，此时",
                font="快看世界体",
                font_size=25,
                t2g={
                    'b':('#84fab0', '#8fd3f4'),
                },
                t2c={
                    '二次函数对称轴': XKCD.CANARYYELLOW
                }
        ).next_to(text2_des,DOWN)
        
        explain_Math = MathTex(
            r"&\frac{\mathrm{d}S}{\mathrm{d}b}=0",r"\\&\sum_{i=1}^{n}x_{i}y_{i}=", r"b",r"\sum_{i=1}^{n}{x_{i}}^2+",r"a",r"n\bar{x}"
        )
        explain_Math_help = Text(
            "即"
        ).next_to(explain_Math[0],RIGHT)
        
        explain_Math[2].set_color_by_gradient(['#84fab0', '#8fd3f4'])
        explain_Math[4].set_color_by_gradient(['#84fab0', '#8fd3f4'])
        
        explain_MathAll = VGroup(
            explain_Math_help , 
            explain_Math
        ).next_to(explain_text , DOWN).scale(0.75)
        
        self.play(
            Write(explain_MathAll[0]),
            Write(explain_MathAll[1][0]),
            Write(explain_text),
            run_time = 2
        )
        self.play(
            math_tex2_sigma_all_db.animate.next_to(explain_Math[0] , DOWN).shift(RIGHT*2),
            run_time = 2
        )
        self.play(
            Circumscribe(math_tex2_sigma_all_db),
            run_time = 2
        )
        self.play(
            Transform(math_tex2_sigma_all_db,explain_MathAll[1][1:]),
            run_time = 1.5
        )
        self.wait()
        self.play(FadeOut(h_line))
        
        self.play(
            FadeOut(explain_MathAll), 
            FadeOut(explain_text) , 
            FadeOut(text2_des),
            FadeOut(right_mob),
            FadeOut(slope_cur),
            FadeOut(math_tex2_sigma_all_db),
            run_time = 1
        )
        
        sum_up_text = VGroup()
        # 0
        sum_up_text.add(Text(
                "综合上述两个方程",
                font="快看世界体",
                fill_opacity=0.8
            ).shift(UP*2)
        )
        # 1
        sum_up_text.add(MathTex(
                r"\\&\sum_{i=1}^{n}x_{i}y_{i}=", r"b",r"\sum_{i=1}^{n}{x_{i}}^2+",r"a",r"n\bar{x}"
            ).next_to(sum_up_text[0],DOWN)
        )
        sum_up_text[-1][1].set_color_by_gradient(['#84fab0', '#8fd3f4'])
        sum_up_text[-1][3].set_color_by_gradient(['#84fab0', '#8fd3f4'])
        
        # 2
        sum_up_text.add(MathTex(
                r"\\&\sum_{i=1}^{n}{y_i}=",r"b",r"\sum_{i=1}^{n}{x_i}+n",r"a"
            ).next_to(sum_up_text[1],DOWN)
        )
        sum_up_text[-1][1].set_color_by_gradient(['#84fab0', '#8fd3f4'])
        sum_up_text[-1][3].set_color_by_gradient(['#84fab0', '#8fd3f4'])
        
        self.play(
            Write(sum_up_text[0:3]),
            run_time = 2
        )
        self.wait()
        
        # 3
        sum_up_text.add(Text(
                "整理后得到",
                font="快看世界体",
            ).next_to(sum_up_text[0],DOWN).shift(UP)
        ).set_color_by_gradient('#FFFEFF','#D7FFFE')
        
        # 4
        sum_up_text.add(MathTex(
                r"b", r"=\frac{\sum_{i=1}^{n}x_{i}y_{i}}{\sum_{i=1}^{n}{x_i}^2-n\bar{x}^2}"
            ).next_to(sum_up_text[0],DOWN).shift(DOWN*0.4)
        )
        sum_up_text[-1][0].set_color_by_gradient(['#84fab0', '#8fd3f4'])
        
        # 5
        sum_up_text.add(MathTex(
                r"a", r"=\bar{y}-",r"b",r"\bar{x}"
            ).next_to(sum_up_text[-1],DOWN).shift(DOWN*0.4).scale(1.2)
        )
        sum_up_text[-1][0].set_color_by_gradient(['#84fab0', '#8fd3f4'])
        sum_up_text[-1][2].set_color_by_gradient(['#84fab0', '#8fd3f4'])

        self.play(
            ReplacementTransform(sum_up_text[0],sum_up_text[3]),
            run_time = 2
        )

        self.play(
            ReplacementTransform(sum_up_text[1],sum_up_text[-2]),
            ReplacementTransform(sum_up_text[2],sum_up_text[-1]),
            run_time = 2
        )
        self.wait(2)