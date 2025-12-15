from manim import *
import numpy as np

class A7(Scene):
    def construct(self):
        # tiempo de espera
        wt = 0.1
        self.wait(1)

        # titulo
        text_titulo = Text('Reemplazo Generacional').scale(0.9)
        self.add(text_titulo)
        self.play(AddTextLetterByLetter(text_titulo))
        self.wait(wt)
        
        # subimos titulo
        self.play(text_titulo.animate.shift(3.3*UP))
        self.wait(wt)

        # generamos vectores de poblacion (cada poblacion sera un grupo y luego los grupos se agregan a un layout)
        num_hijos = [[0.80077522, 0.47102848, 0.89772868],
                    [0.81440226, 0.4638381,  0.3193687 ],
                    [0.55776199, 0.54662177, 0.49526766],
                    [0.58572785, 0.51296537, 0.50888413]]
        list_hijos = []
        for row in num_hijos:
            aux_tex = Tex(fr'${row[0]:.3f}\quad {row[1]:.3f}\quad {row[2]:.3f}$').scale(1.0)
            list_hijos.append(aux_tex)

        group_hijos = VGroup(*[list_hijos]).arrange_in_grid(4,1)
        group_hijos.shift(1*DOWN)
        self.play(Create(group_hijos))
        self.wait(wt)

        # dibujamos parentesis y colocamos titulo de hijos        
        p1 = Tex(r'$[$').scale(6).next_to(group_hijos, LEFT)
        p2 = Tex(r'$]$').scale(6).next_to(group_hijos, RIGHT)
        tex_hijos = Text('Hijos').scale(0.9).next_to(group_hijos, UP).shift(0.8*UP)
        tex_hijos.shift(0.1*LEFT)
        group_hijos.add(p1, p2, tex_hijos)
        self.play(Create(tex_hijos), Create(p1), Create(p2))
        self.wait(wt)

        # desplazamos a la derecha
        self.play(group_hijos.animate.shift(3.5*RIGHT))
        self.wait(wt)

        # agregamos padres a la izquierda con la misma tecnica que los hijos
        # ya traemos el titulo y parentesis dibujados
        num_padres = [[0.87414573, 0.1658598,  0.30119253],
                    [0.74103176, 0.82978303, 0.61103652],
                    [0.87414573, 0.1658598,  0.30119253],
                    [0.26934412, 0.89372735, 0.73671414]]
        
        list_padres = []
        for row in num_padres:
            aux_tex = Tex(fr'${row[0]:.3f}\quad {row[1]:.3f}\quad {row[2]:.3f}$').scale(1.0)
            list_padres.append(aux_tex)

        group_padres = VGroup(*[list_padres]).arrange_in_grid(4,1)
        group_padres.shift(1*DOWN)
   
        pp1 = Tex(r'$[$').scale(6).next_to(group_padres, LEFT)
        pp2 = Tex(r'$]$').scale(6).next_to(group_padres, RIGHT)
        tex_padres = Text('Padres').scale(0.9).next_to(group_padres, UP).shift(0.8*UP)
        tex_padres.shift(0.1*LEFT)
        group_padres.add(pp1, pp2, tex_padres)
        group_padres.shift(10*LEFT)
        self.play(group_padres.animate.shift(6.5*RIGHT))
        self.wait(wt)

        # resaltamos en rojo la peor solucion de hijos
        self.play(list_hijos[0].animate.set_color(RED_C))
        self.wait(wt)

        # resaltamos en verde la mejor solucion de padres
        self.play(list_padres[1].animate.set_color(GREEN_C))
        self.wait(wt)

        # creamos una copia del mejor padres y sacamos de pantalla el peor hijos mientras traemos la copia a su posicion
        copy_padre = list_padres[1].copy()
        pos_hijo = list_hijos[0].get_center()
        self.play(copy_padre.animate.set_color(YELLOW_C).move_to(pos_hijo),
                  list_hijos[0].animate.shift(10*RIGHT))
        self.wait(wt)

        # desplazamos la poblacion de padres y centramos hijos
        group_hijos.remove(list_hijos[0]) # removemos pero hijo
        group_hijos.add(copy_padre) # agregamos padre al grupo
        self.play(group_padres.animate.shift(10*LEFT))
        self.play(group_hijos.animate.shift(3.5*LEFT))
        self.play(copy_padre.animate.set_color(WHITE))

        self.wait(2)