from manim import *
import numpy as np

class A6(Scene):
    def construct(self):
        # tiempo de espera
        wt = 0.1
        self.wait(1)

        # titulo
        text_titulo = Text('Mutacion').scale(0.9)
        self.add(text_titulo)
        self.play(AddTextLetterByLetter(text_titulo))
        self.wait(wt)
        
        # subimos titulo
        self.play(text_titulo.animate.shift(3.3*UP))
        self.wait(wt)

        # dibujamos poblacion resultante del crossover (pero elemento por elemento)
        pob = [ [0.80077522, 0.53180472, 0.47197408],
                [0.81440226, 0.4638381,  0.44025497],
                [0.55776199, 0.54662177, 0.52902254],
                [0.58572785, 0.51296537, 0.50888413]]
        
        aux_nums = []
        for v in np.array(pob).flatten():
            aux_nums.append(Tex(fr'$ {v:.3f} $').scale(1.3))

        # creamos grupo y organisamos en grid
        group_nums = VGroup(*aux_nums).arrange_in_grid(rows=4, cols=3, buff=(0.6, 0.3))
        group_nums.move_to((0,0,0))
        self.play(Create(group_nums))

        # traemos parantesis 
        p1 = Tex(r'$[$').scale(7).next_to(group_nums, LEFT)
        p2 = Tex(r'$]$').scale(7).next_to(group_nums, RIGHT)
        group_nums.add(*[p1, p2])
        self.play(Create(p1), Create(p2))
        self.wait(wt)

        # iteramos sobre todos los numeros y comparamos con la mutacion
        pob_mut =  [[0.80077522, 0.47102848, 0.89772868],
                    [0.81440226, 0.4638381,  0.44025497 ],
                    [0.55776199, 0.54662177, 0.49526766],
                    [0.58572785, 0.51296537, 0.50888413],]
        for mo, pi, pm in zip(aux_nums, np.array(pob).flatten(), np.array(pob_mut).flatten()):
            # animamos resltado a amarillo cuando no hay mutacion
            if pi == pm:
                self.play(mo.animate.set_color(YELLOW), run_time=0.5)
                self.play(mo.animate.set_color(WHITE), run_time=0.5)
            else:
                aux_mo = Tex(fr'$ {pm:.3f} $', color=RED).scale(1.3).move_to(mo.get_center())
                self.play(ReplacementTransform(mo, aux_mo))
        self.wait(wt)

        


        self.wait(2)