from manim import *
import pandas as pd

class anim8(ThreeDScene):
    def construct(self):
        wt = 1.0

        # numero de generaciones
        ngen = 10

        # definicion de ejes
        axes = ThreeDAxes(x_range=(-5,5,1), y_range=(-5,5,1), z_range=(-5,5,1))
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
        
        # definicion de texto estatico (no refleja cambios 3d)
        text_titulo = Text("Experimentos").scale(0.9).to_corner(UL)
        text_cross = Tex(r"$p_{crossover}=0.5$").scale(0.7).next_to(text_titulo, DOWN).shift(0.5*LEFT)
        text_mut = Tex(r"$p_{mutacion}=0.01$").scale(0.7).next_to(text_cross, DOWN)
        text_eli = Tex(r"$elitismo=0$").scale(0.7).next_to(text_mut, DOWN)

        self.add_fixed_in_frame_mobjects(text_titulo, text_cross, text_mut, text_eli)

        self.play(*[Write(mo) for mo in [text_titulo, text_cross, text_mut, text_eli]], Create(axes))
        self.wait(wt)
        
        # leemos data de experimento
        data = pd.read_csv('Data/conervadora1.csv')

        gen = 0
        pob = data.loc[data['GENERACION']==0][['V1', 'V2', 'V3']].values
        
        # lista de puntos
        colors = [BLUE_C, BLUE_E, GOLD, GRAY_A, GREEN, GREEN_E, LIGHT_PINK, LOGO_BLUE, MAROON, PINK, PURE_GREEN,
                  PURE_BLUE, PURE_RED, TEAL, YELLOW, YELLOW_C]
        list_points = []
        for  point in pob:
            # elegimos color de maner aleatoria
            aux_ind = np.random. randint(0, len(colors))

            # dibujamos punto del color elegido
            aux_points = Sphere(radius=0.035).move_to(axes.p2c(point)).set_color(colors[aux_ind])
            list_points.append(aux_points)
        
        # creamos grupo con los puntos
        group_points = VGroup(*list_points)
        self.play(Create(group_points))

        # animamos la creacion de gen = num (value tracker)
        tex_gen = Tex(r'gen=').scale(0.9).to_corner(DR).shift(1.2*LEFT)
        num_vt = ValueTracker(ngen)
        tex_alpha_num = always_redraw(lambda: Tex(fr'${int(num_vt.get_value())}$').scale(0.9).next_to(tex_gen, RIGHT).shift(0.05*UP))
        num_vt.set_value(0)

        
        self.add_fixed_in_frame_mobjects(tex_gen, tex_alpha_num)
        self.play(Write(tex_gen), Write(tex_alpha_num))
        self.wait(wt)

        # animacion para el resto de generaciones
        for gen in range(1, 11):
            pob = data.loc[data['GENERACION']==gen][['V1', 'V2', 'V3']].values
        
            # itera sobre lista de puntos y nueva posicion
            aux_anims = []
            for point, new_pos in zip(list_points, pob):
                aux_anims.append(point.animate.move_to(axes.p2c(new_pos)))

            # animamos los puntos y el cambio de generacion
            self.play(*aux_anims, num_vt.animate.set_value(gen))
            self.wait(0.5)
        
    
        
        
        self.wait(2)
