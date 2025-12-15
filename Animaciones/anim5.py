from manim import *


class A5(Scene):
    def construct(self):
        # tiempo de espera
        wt = 0.1
        self.wait(1)

        # titulo
        text_titulo = Text('Crossover').scale(0.9)
        self.add(text_titulo)
        self.play(AddTextLetterByLetter(text_titulo))
        self.wait(wt)
        
        # subimos titulo
        self.play(text_titulo.animate.shift(3.3*UP))
        self.wait(wt)

        # escribimos la ecuacion 
        # dados un par de padres p1, p2 y alpha en 0,1,  (separamos dados)
        text_dados = Tex('Dados').scale(0.8)
        text_aux = Tex(r'un par de padres $\vec{p_1}$ y $\vec{p_2}$ y $\alpha\in[0,1]$, sus hijos se definen como:').scale(0.8).next_to(text_dados, RIGHT).shift(0.04*DOWN).shift(0.05*LEFT)
        
        # agregamos a un grupo y centramos
        group_def = VGroup(text_dados, text_aux).move_to((0,0.5,0))
        self.play(Create(group_def))
        self.wait(wt)

        # escribimos las ecuaciones h1 y h2 una por una (separando hi= y el resto)
        tex_h1 = Tex(r'$\vec{h_1}=$').scale(0.9)
        tex_h2 = Tex(r'$\vec{h_2}=$').scale(0.9).next_to(tex_h1, DOWN)
        text_eq1 = Tex(r'$\alpha\cdot \vec{p_1} + (1-\alpha)\cdot \vec{p_2}$').scale(0.9).next_to(tex_h1, RIGHT)
        text_eq2 = Tex(r'$\alpha\cdot \vec{p_2} + (1-\alpha)\cdot \vec{p_1}$').scale(0.9).next_to(tex_h2, RIGHT)
        group_eq_hijos = VGroup(tex_h1, tex_h2, text_eq1, text_eq2).move_to((0, -0.75, 0))
        self.play(Create(group_eq_hijos))
        self.wait(wt)


        # subimnos todo
        self.play(group_def.animate.shift(2*UP), group_eq_hijos.animate.shift(2*UP))
        self.wait(wt)


        # traemos la poblacion anterior (en blanco)
        poblacion = [[0.87414573, 0.1658598,  0.30119253],
                    [0.74103176, 0.82978303, 0.61103652],
                    [0.87414573, 0.1658598,  0.30119253],
                    [0.26934412, 0.89372735, 0.73671414]]
        
        list_vec_nums = []
        for i, vs in zip((range(4)), poblacion):
            # creamos vector numerico
            aux_num_vec = Tex(fr'${vs[0]:.3f}\quad{vs[1]:.3f}\quad{vs[2]:.3f}$').scale(0.9)
            
            # acomodamos en pantalla
            if i > 0:
                aux_num_vec.next_to(list_vec_nums[i-1], DOWN)
            
            # agregamos tex a la lista
            list_vec_nums.append(aux_num_vec)
        
        # agregamos al grupo y centramos
        group_pob = VGroup(*list_vec_nums).move_to((0, -1.5, 0))
        
        # agregamos parentesis
        p1 = Tex(r'$[$').scale(5).next_to(group_pob, LEFT)
        p2 = Tex(r'$]$').scale(5).next_to(group_pob, RIGHT)
        group_pob.add(*[p1, p2]).shift(15*LEFT)
        self.add(group_pob)

        # animamos slide del grupo
        self.play(group_pob.animate.shift(15*RIGHT))
        self.wait(wt)

        # coloreamos por aprejas continuas
        self.play(list_vec_nums[0].animate.set_color(BLUE_C),
                  list_vec_nums[1].animate.set_color(BLUE_C),
                  list_vec_nums[2].animate.set_color(GREEN_D),
                  list_vec_nums[3].animate.set_color(GREEN_D))
        self.wait(wt)

        ########### GRUPO DE ANIMACIONES ###########
        list_anims = []

        # sacamos objetos extra de pantalla
        list_anims += [group_pob.animate.shift(15*LEFT),
                       text_aux.animate.shift(15*RIGHT),
                       group_eq_hijos.animate.shift(10*DOWN)]
        
        # # bajamos el texto de dados
        list_anims.append(text_dados.animate.shift(0.5*DOWN))

        # creamos vectores p1 y p2
        text_p1 = Tex(r'$\cdot$ $\vec{p_1}=$').scale(0.9).next_to(text_dados, DOWN).shift(1*RIGHT)
        text_p1.shift(0.7*DOWN)
        text_p2 = Tex(r'$\cdot$ $\vec{p_2}=$').scale(0.9). next_to(text_p1, DOWN)
        list_anims += [Create(text_p1), Create(text_p2)]
        
        # copia de los primer vectores pero en blanco y posicionados correctamente
        copy_vec1 = list_vec_nums[0].copy()
        copy_vec2 = list_vec_nums[1].copy()
        copy_vec1.set_color(WHITE)
        copy_vec2.set_color(WHITE)
        copy_vec1.next_to(text_p1, RIGHT).shift(0.25*RIGHT).shift(0.04*DOWN)
        copy_vec2.next_to(text_p2, RIGHT).shift(0.25*RIGHT).shift(0.04*DOWN)

        list_anims += [ReplacementTransform(list_vec_nums[0], copy_vec1),
                       ReplacementTransform(list_vec_nums[1], copy_vec2)]
        
        # agregamos parentesis a los costados de vectores y creamos grupo
        p1_pl = Tex(r'$($').scale(0.9).next_to(copy_vec1, LEFT)
        p1_pr = Tex(r'$)$').scale(0.9).next_to(copy_vec1, RIGHT)
        p2_pl = Tex(r'$($').scale(0.9).next_to(copy_vec2, LEFT)
        p2_pr = Tex(r'$)$').scale(0.9).next_to(copy_vec2, RIGHT)
        group_vec1 = VGroup(text_p1, p1_pl, copy_vec1, p1_pr)
        group_vec2 = VGroup(text_p2, p2_pl, copy_vec2, p2_pr)

        list_anims += [Create(mo) for mo in [p1_pl, p1_pr, p2_pl, p2_pr]]

        self.play(*list_anims)
        self.wait(wt)

        # seleccionamos alpha con una animacion de 0 a 1 y a 0.3
        tex_alpha = Tex(r'$\cdot$ $\alpha=$').scale(0.9).next_to(text_p2, DOWN).shift(0.05*LEFT).shift(0.1*DOWN)
        num_vt = ValueTracker(0.0)
        tex_alpha_num = always_redraw(lambda: Tex(fr'${num_vt.get_value():.2f}$').scale(0.9).next_to(tex_alpha, RIGHT))
        self.play(Create(tex_alpha), Create(tex_alpha_num))
        self.wait(wt)

        self.play(num_vt.animate.set_value(1.0))
        self.play(num_vt.animate.set_value(0.44))
        self.wait(wt)

        # escribimos las ecuacions h1 y h2 con el valor de alpha seleccionado y en terminos de p1 y p2 (ubicadas horizontalmente)
        # lo haremos por partes (h, = , ...) para centrar el =
        tex_h1 = Tex(r'$\vec{h_1}$').scale(0.9)
        tex_h1_eq = Tex(r'$=$').scale(0.9).next_to(tex_h1, RIGHT)
        tex_h1_r = Tex(r'$0.44\cdot\vec{p_1}+(1-0.44)\cdot\vec{p_2}$').scale(0.9).next_to(tex_h1_eq, RIGHT).shift(0.05*DOWN)
        group_h1 = VGroup(tex_h1, tex_h1_eq, tex_h1_r).move_to((-3.5,-1,0))

        tex_h2 = Tex(r'$\vec{h_2}$').scale(0.9)
        tex_h2_eq = Tex(r'$=$').scale(0.9).next_to(tex_h2, RIGHT)
        tex_h2_r = Tex(r'$0.44\cdot\vec{p_2}+(1-0.44)\cdot\vec{p_1}$').scale(0.9).next_to(tex_h2_eq, RIGHT).shift(0.05*DOWN)
        group_h2 = VGroup(tex_h2, tex_h2_eq, tex_h2_r).move_to((3.5,-1,0))

        self.play(Create(group_h1), Create(group_h2))
        self.wait(wt)


        #(array([0.38462412, 0.07297831, 0.13252471]),
        #array([0.67394603, 0.63489547, 0.73114393]))
        # escribimos debajo la ecuacion en un vector sumando los resultados por componentes (=, ...)
        tex_h1_eq2 = Tex(r'$=$').scale(0.9).next_to(tex_h1_eq, DOWN).shift(0.5*DOWN)
        vec_h1 = Tex(r'$(0.800 \quad 0.531 \quad 0.471)$').scale(0.9).next_to(tex_h1_eq2, RIGHT).shift(0.05*DOWN)
        tex_h2_eq2 = Tex(r'$=$').scale(0.9).next_to(tex_h2_eq, DOWN).shift(0.5*DOWN)
        vec_h2 = Tex(r'$(0.814 \quad 0.463 \quad 0.440)$').scale(0.9).next_to(tex_h2_eq2, RIGHT).shift(0.05*DOWN)
        self.play(*[Create(mo) for mo in [tex_h1_eq2, vec_h1, tex_h2_eq2, vec_h2]])
        self.wait(wt)

        # quitamos todo de escena excepto vectores
        list_anims = [text_dados.animate.shift(10*LEFT),
                      group_vec1.animate.shift(15*LEFT),
                      group_vec2.animate.shift(15*LEFT),
                      tex_alpha.animate.shift(15*LEFT),
                      tex_alpha_num.animate.shift(15*LEFT),
                      group_h1.animate.shift(15*LEFT),
                      group_h2.animate.shift(15*RIGHT),
                      tex_h1_eq2.animate.shift(15*LEFT),
                      tex_h2_eq2.animate.shift(15*RIGHT)]
        
        # transformamos vectores quitando parentesis
        new_vec_h1 = Tex(r'$0.800 \quad 0.531 \quad 0.471$').scale(0.9).move_to(vec_h1.get_center())
        new_vec_h2 = Tex(r'$0.814 \quad 0.463 \quad 0.440$').scale(0.9).move_to(vec_h2.get_center())
        list_anims += [ReplacementTransform(vec_h1, new_vec_h1),
                       ReplacementTransform(vec_h2, new_vec_h2)]
        
        self.play(*list_anims)
        self.wait(wt)

        # los subimos y dibujamos parentesis y escribimos hijos
        self.play(new_vec_h1.animate.move_to((0,0.0,0)))
        #self.wait(wt)

        self.play(new_vec_h2.animate.next_to(new_vec_h1, DOWN))
        self.wait(wt)
        
        # luego traemos el resultado de la otra pareja
        vec_h3 = Tex(r'$0.558 \quad 0.547 \quad 0.529$').scale(0.9).next_to(new_vec_h2, DOWN)
        vec_h4 = Tex(r'$0.586 \quad 0.513 \quad 0.509$').scale(0.9).next_to(vec_h3, DOWN)
        self.play(Create(vec_h3), Create(vec_h4))
        self.wait(wt)
        group_vec_h = VGroup(new_vec_h1, new_vec_h2, vec_h3, vec_h4)

        # creamos parentesis y titulo de hijos
        p1 = Tex(r'$[$').scale(5).next_to(group_vec_h, LEFT)
        p2 = Tex(r'$]$').scale(5).next_to(group_vec_h, RIGHT)
        text_hijos = Text('Hijos').scale(0.8).next_to(group_vec_h, UP).shift(0.7*UP)
        self.play(Create(p1), Create(p2), AddTextLetterByLetter(text_hijos))



        self.wait(2)

