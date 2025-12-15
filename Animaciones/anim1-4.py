from manim import *

class A1(Scene):
    def construct(self):
        #self.next_section(skip_animations=True)

        # tiempo de espera
        wt = 0.1
        self.wait(1)

        # escribir algoritmos geneticos
        text_alg_gen = Text('Algoritmos\nGeneticos').scale(1.2)
        self.add(text_alg_gen)
        self.play(AddTextLetterByLetter(text_alg_gen))
        self.wait(wt)

        # encerrar el texto en circulo
        circle = Circle(2.8)
        self.add(circle)
        self.play(Create(circle))
        self.wait(wt)

        # creamos grupo y bajamos objetos
        group_alg_evol = VGroup(circle, text_alg_gen)
        self.play(group_alg_evol.animate.shift(0.7*DOWN))
        self.wait(wt)

        # escribimos algoritmos evolutivos
        text_alg_evol = Text('Algoritmos Evolutivos').scale(1.2).shift(3.1*UP)
        self.add(text_alg_evol)
        group_alg_evol.add(text_alg_evol) # agregamos texto al grupo
        self.play(AddTextLetterByLetter(text_alg_evol))
        self.wait(wt)

        # hacer pequena la letra
        self.play(text_alg_gen.animate.scale(0.5))
        self.wait(wt)

        # agregamos mas tecnicas
        tecnicas = ['Differential\nEvolution', 'Particle Swarm\nOptimization', 'Ant Colony\nOptimization', 'Cuckoo\nSearch']
        coordenadas = [[1,0.5,0], [1,-1.8,0], [-1,0.5,0], [-1.3,-1.8,0]]
        for tecnica, coordenada in zip(tecnicas, coordenadas):
            aux_text = Text(tecnica).move_to(coordenada).scale(0.5)
            self.add(aux_text)
            group_alg_evol.add(aux_text) # add text to group
            self.play(Create(aux_text))
        self.wait(wt)

        # desplazamos todos los elementos fuera de la pantalla (excepto el titulo)
        group_alg_evol.remove(text_alg_evol) # eliminamos el titulo del grupo para evitar moverlo
        self.play(group_alg_evol.animate.shift(15*LEFT))
        self.wait(wt)

        # agregamos fitness (latex)
        tex_fitness = Tex('fitness').scale(1.0)
        tex_f = Tex(r'$f$').scale(1.0)
        tex_fx = Tex(r'$f(x)$').scale(1.0)
        self.add(tex_fitness)
        self.play(Create(tex_fitness))
        self.wait(wt)

        # convertimos a f y luego f(x)
        #self.add(tex_f)
        self.play(ReplacementTransform(tex_fitness, tex_f))
        self.wait(wt)

        #self.add(tex_fx)
        self.play(ReplacementTransform(tex_f, tex_fx))
        self.wait(wt)

        # creamos axis y desplazamos f(x) al eje vertical y creamos x en el eje horizontal
        # definimos un axis para graficar en el
        ax = Axes(x_range=[-2, 2], y_range=[-2, 5], axis_config={"include_tip": False},
                  x_length=12, y_length=5.5).shift(1*DOWN)
        tex_x = Tex(r'$x$').scale(1.0).next_to(ax, RIGHT).shift(1.2*DOWN)
        self.play(Create(ax), tex_fx.animate.next_to(ax, UP), Create(tex_x))
        self.wait(wt)

        # funcion a graficar
        def func(x):
            return x**2 + np.sin(5*x)

        # graficamos funcion en el plot
        graph = ax.plot(func, color=MAROON)
        self.add(graph)
        self.play(Create(graph))
        self.wait(wt)

        # creamos un conjunto de puntos
        colors = [BLUE_A, GOLD_B, GREEN, PURPLE_E] # colores
        value_ts = [ValueTracker(i) for i in [-1.8, -1.0, 1.1, 1.9]]
        dots = [Dot(point=ax.coords_to_point(vt.get_value(), func(vt.get_value())), color=ci) for vt, ci in zip(value_ts, colors)]
        self.add(*value_ts, *dots)
        self.play(*[Create(di) for di in dots])
        self.wait(wt)

        # ENCONTRAR UNA FORMA MAS EFICIENTE DE DEFINIR MULTIPLES LAMBDAS (O LA MISMA FUNCION PERO CON PARAMETROS)
        # definimos updater s para cada punto asociados a un value tracker
        # for dot, vt in zip(dots, value_ts):
        #     dot.add_updater(lambda d: d.move_to(ax.coords_to_point(vt.get_value(), func(vt.get_value()))))
        dots[0].add_updater(lambda d0: d0.move_to(ax.coords_to_point(value_ts[0].get_value(), func(value_ts[0].get_value()))))
        dots[1].add_updater(lambda d1: d1.move_to(ax.coords_to_point(value_ts[1].get_value(), func(value_ts[1].get_value()))))
        dots[2].add_updater(lambda d2: d2.move_to(ax.coords_to_point(value_ts[2].get_value(), func(value_ts[2].get_value()))))
        dots[3].add_updater(lambda d3: d3.move_to(ax.coords_to_point(value_ts[3].get_value(), func(value_ts[3].get_value()))))

        # actualizamos su evolucion por generaciones
        gen_values = [[-1.6, -0.7, 0.6, 1.2],
                      [-1.0,-0.4, 0.1, 0.5],
                      [-0.7,-0.32, -0.1, 0.0],
                      [-0.4,-0.29, -0.25, -0.2]]
        for i in range(len(gen_values)):
            # valores de la generacion actual
            act_values = gen_values[i]
            
            # # actualizacion de los puntos a esos valores con los value tracker
            self.play(*[vt.animate.set_value(val) for vt, val in zip(value_ts, act_values)])
            self.wait(wt)
        
        # dibujamos flecha y texto de minimo absoluto
        flecha = Arrow(start=ax.coords_to_point(-0.45, 2.0), end=ax.coords_to_point(-0.29, -0.85))
        text_flecha = Text('optimo\nabsoluto').scale(0.5).next_to(flecha, UP).shift(0.5*LEFT)
        self.add(flecha, text_flecha)
        self.play(*[Create(mo) for mo in [flecha, text_flecha]])
        self.wait(wt)

        self.wait(2)



class A2(Scene):
    def construct(self):
        # tiempo de espera
        wt = 0.1
        self.wait(1)

        # escribimos pregunta
        text_pregunta = Text('¿Como funcionan los Algoritmos Geneticos?').scale(0.9)
        self.add(text_pregunta)
        self.play(AddTextLetterByLetter(text_pregunta))
        self.wait(wt)
        
        # subimos pregunta y respondemos
        text_re = Text('RE: Selección Natural').scale(0.9).shift(0.5*DOWN)
        self.add(text_re)
        self.play(text_pregunta.animate.shift(0.6*UP), AddTextLetterByLetter(text_re))
        self.wait(wt)

        # eliminamos respues y subimos pregunta como titulo
        self.play(text_pregunta.animate.shift(2.2*UP), text_re.animate.shift(15*LEFT))
        self.wait(wt)

        # creamos poblaciones de puntos con cada individuo con colores del mismo color
        points = []
        colors = [BLUE_D, GREEN, ORANGE, PURPLE_E]
        aux_start = [-2.0, 0.5, 0.0]
        radio = 0.33
        for i in range(4):
            #aux_points = []
            for j in range(6):
                if i==0 and j==0:
                    points.append(Dot(radius=radio, color=colors[i]).move_to(aux_start))
                elif j>0:
                    points.append(Dot(radius=radio, color=colors[i]).next_to(points[6*i+j-1], RIGHT))
                elif j==0 and i>0:
                    points.append(Dot(radius=radio, color=colors[i]).next_to(points[6*(i-1)], DOWN))
        
        # creamos grupo y agregamos puntos
        group_points = VGroup(*points)

        # centramos
        group_points.move_to([0, group_points.get_y(), 0])

        # creamos label Exploracion y colocamos arriba de puntos
        text_exp = Text('Exploración').scale(0.8)
        text_exp.next_to(group_points, UP)

        # agregamos texto al grupo
        group_points.add(text_exp)

        self.add(group_points)
        self.play(Create(group_points))
        self.wait(wt)

        # intercambiamos genes por parejas
        # fila 0 y 1
        animaciones = []
        for ind in [3,4,5]:
            aux_up = [points[ind].get_x(), points[ind].get_y(), 0]
            aux_down = [points[6+ind].get_x(), points[6+ind].get_y(), 0]
            animaciones += [points[ind].animate.move_to(aux_down), points[6+ind].animate.move_to(aux_up)]

        # fila 2 y 3
        for ind in [0,1]:
            aux_up = [points[12+ind].get_x(), points[12+ind].get_y(), 0]
            aux_down = [points[18+ind].get_x(), points[18+ind].get_y(), 0]
            animaciones += [points[12+ind].animate.move_to(aux_down), points[18+ind].animate.move_to(aux_up)]
        
        self.play(*animaciones)
        self.wait(wt)

        # cambiamos a rojo algunos puntos para representar mutaciones
        animaciones = []
        self.play(*[points[i].animate.set_color(PURE_RED) for i in [2, 15, 22]])
        self.wait(wt)

        # desplazamos a izquierda
        self.play(group_points.animate.shift(1.8*LEFT))

        # anadimos flechas y numeros al lado de cada fila
        mobjects = []
        for ind, val, color in zip([11, 5, 17, 23], [7,0,6,4], [PURE_RED, GREEN, ORANGE, ORANGE]):
            # add arrow pointing to the right
            aux_arrow = Arrow(start=[points[ind].get_x()+0.4, points[ind].get_y(), 0], end=[points[ind].get_x()+1.9, points[ind].get_y(), 0])
            
            # add fintess text
            aux_tex = Tex(fr'$f(x)={val}$').set_color(color).scale(1)
            aux_tex.next_to(aux_arrow, RIGHT)
            mobjects += [aux_arrow, aux_tex]

        # creamos group
        group_fit = VGroup(*mobjects)

        # creamos texto seleccion
        text_sel = Text('Selección').scale(0.8)
        text_sel.next_to(group_fit, UP).shift(0.15*UP).shift(0.65*RIGHT)

        # anadimos texto al group
        group_fit.add(text_sel)

        # anadimos objetos y los creamos
        self.add(group_fit)
        self.play(Create(group_fit))
        self.wait(wt)

        self.wait(2)




class A3(Scene):
    def construct(self):
        # tiempo de espera
        wt = 0.1
        self.wait(1)

        # titulo
        text_titulo = Text('Definicion del Problema e Inicializacion').scale(0.9)
        self.add(text_titulo)
        self.play(AddTextLetterByLetter(text_titulo))
        self.wait(wt)
        
        # subimos titulo
        self.play(text_titulo.animate.shift(3.3*UP))
        self.wait(wt)

        # escribimos f
        tex_f = Tex(r'$f$').scale(1.5)
        self.add(tex_f)
        self.play(Create(tex_f))
        self.wait(wt)

        # escribimos f(x vector)
        tex_fx = Tex(r'$f(\vec{w})$').scale(1.5)
        self.play(ReplacementTransform(tex_f, tex_fx))
        self.wait(wt)

        # escribimos f(x)= y agregamos numero
        tex_fx_eq = Tex(r'$f(\vec{w})=$').scale(1.5)
        num_vt = ValueTracker(10)
        #tex_num = Tex(fr'${num_vt.get_value()}$').scale(1.5).next_to(tex_fx_eq, RIGHT)
        tex_num = always_redraw(lambda: Tex(fr'${num_vt.get_value():.2f}$').scale(1.5).next_to(tex_fx_eq, RIGHT) )
        
        # creamos grupo de ecuaciones
        group_eq = VGroup(tex_fx_eq, tex_num)
        group_eq.move_to([0, group_eq.get_y(), 0]) # centramos la ecuacion

        # animamos transformacion de ecuacion y numero
        self.play(ReplacementTransform(tex_fx, tex_fx_eq), Create(tex_num))
        self.wait(wt)

        # resaltamos en rojo el 10 y vuelve a blanco
        #tex_num_red = Tex(fr'${num_vt.get_value()}$', color=PURE_RED).scale(1.5)
        self.play(tex_num.animate.set_color(PURE_RED))
        self.play(tex_num.animate.set_color(WHITE))
        self.wait(wt)

        # animamos cambio de 10 a 0
        self.play(num_vt.animate.set_value(0.0))
        self.wait(wt)

        # resaltamos 0 en verde y vuelve a blanco
        self.play(tex_num.animate.set_color(GREEN))
        self.play(tex_num.animate.set_color(WHITE))
        self.wait(wt)

        # desplazamos a arriba la ecuacion
        self.play(group_eq.animate.shift(2*UP))
        self.wait(wt)

        # creamos lista de vectores
        list_vectors = []
        for v, color in zip(['w', 'x', 'y', 'z'], [BLUE_C, GREEN, LOGO_BLUE, TEAL]):
            list_vectors.append(Tex(fr'${v}_1, {v}_2, \dots, {v}_n$', color=color).scale(1.8))

        # escribimos w = w1,...
        self.play(Create(list_vectors[0]))
        self.wait(wt)

        # desplazamos vector w arriba y creamos iterativamente los otros vectores
        self.play(list_vectors[0].animate.shift(0.5*UP))
        for i in range(1,4):
            # acomodar vector debajo del anterior
            list_vectors[i].next_to(list_vectors[i-1], DOWN)
            self.play(Create(list_vectors[i]))
        self.wait(wt)

        # creamos grupo con los vectores
        group_vec = VGroup(*list_vectors)
        
        # anadimos corchetes al grupo
        p1 = Tex(r'$[$').scale(7).next_to(group_vec, LEFT)
        p2 = Tex(r'$]$').scale(7).next_to(group_vec, RIGHT)
        self.play(Create(p1), Create(p2))
        self.wait(wt)

        # desplegamos la ecuacion del ejemplo
        tex_num_prob = Tex(fr'$w^2_1+w^2_2+w^2_3$').scale(1.5).next_to(tex_fx_eq, RIGHT)
        self.play(ReplacementTransform(tex_num, tex_num_prob))
        
        # actualizamos la parte derecha de la ecuacion y centramos
        group_eq.remove(tex_num)
        group_eq.add(tex_num_prob)
        self.play(group_eq.animate.move_to((0, group_eq.get_y(), 0)))
        self.wait(wt)

        # creamos lista con numeros
        aux_poblacion = [[0.76176705, 0.9561041,  0.88792681],
                        [0.87414573, 0.1658598,  0.30119253],
                        [0.26934412, 0.89372735, 0.73671414],
                        [0.74103176, 0.82978303, 0.61103652]]
        
        
        list_vec_nums = []
        for i, vs, color in zip((range(4)), aux_poblacion, [BLUE_C, GREEN, LOGO_BLUE, TEAL]):
            # creamos vector numerico
            aux_num_vec = Tex(fr'${vs[0]:.3f}\quad{vs[1]:.3f}\quad{vs[2]:.3f}$', color=color).scale(1.3)
            
            # acomodamos en pantalla
            if i > 0:
                aux_num_vec.next_to(list_vec_nums[i-1], DOWN)
            
            # agregamos tex a la lista
            list_vec_nums.append(aux_num_vec)

        # creamos grupo con vectores numericos
        group_vec_num = VGroup(*list_vec_nums)

        # colocamos en la misma posicion de que el grupo de vectores anterior
        group_vec_num.move_to((group_vec.get_x(), group_vec.get_y(), 0))

        # animamos la transformacion delos vectores normales a el grupo numerico
        self.play(ReplacementTransform(group_vec, group_vec_num))
        self.wait(wt)
        
        self.wait(2)




class A4(Scene):
    def construct(self):
        # tiempo de espera
        wt = 0.1
        self.wait(1)

        # titulo
        text_titulo = Text('Torneo Binario').scale(0.9)
        self.add(text_titulo)
        self.play(AddTextLetterByLetter(text_titulo))
        self.wait(wt)
        
        # subimos titulo
        self.play(text_titulo.animate.shift(3.3*UP))
        self.wait(wt)

        # creamos la misma poblacion de numeros y la movemos a la izquierda fuera de pantalla
        aux_poblacion = [[0.76176705, 0.9561041,  0.88792681],
                        [0.87414573, 0.1658598,  0.30119253],
                        [0.26934412, 0.89372735, 0.73671414],
                        [0.74103176, 0.82978303, 0.61103652]]
        
        
        list_vec_nums = []
        for i, vs, color in zip((range(4)), aux_poblacion, [BLUE_C, GREEN, LOGO_BLUE, TEAL]):
            # creamos vector numerico
            aux_num_vec = Tex(fr'${vs[0]:.3f}\quad{vs[1]:.3f}\quad{vs[2]:.3f}$', color=color).scale(1.3)
            
            # acomodamos en pantalla
            if i > 0:
                aux_num_vec.next_to(list_vec_nums[i-1], DOWN)
            
            # agregamos tex a la lista
            list_vec_nums.append(aux_num_vec)

        # creamos grupo con vectores numericos
        group_vec_num = VGroup(*list_vec_nums)

        # centramos vectores
        group_vec_num.move_to((0, -0.2, 0))

        # agregamos parentesis
        # anadimos corchetes al grupo
        p1 = Tex(r'$[$').scale(7).next_to(group_vec_num, LEFT)
        p2 = Tex(r'$]$').scale(7).next_to(group_vec_num, RIGHT)
        group_vec_num.add(*[p1, p2])
        self.add(group_vec_num)

        # desplazamos grupo fuera de pantalla
        group_vec_num.shift(15*LEFT)

        # animamos su desplazamiento al centro
        self.play(group_vec_num.animate.shift(15*RIGHT))
        self.wait(wt)

        # creamos un par de flechas apuntando al primer y ultimo individuo
        flecha1 = Arrow(start=LEFT, end=RIGHT).next_to(group_vec_num[0], LEFT).shift(0.65*LEFT)
        flecha2 = Arrow(start=LEFT, end=RIGHT).next_to(group_vec_num[3], LEFT).shift(0.65*LEFT)
        self.play(*[Create(fi) for fi in [flecha1, flecha2]])
        self.wait(wt)

        # animamos el cambio de posicion contraria hasta seleccionar un par
        self.play(flecha1.animate.move_to((flecha2.get_x(), flecha2.get_y(), 0)),
                  flecha2.animate.move_to((flecha1.get_x(), flecha1.get_y(), 0)))
        self.play(flecha1.animate.move_to((flecha1.get_x(), group_vec_num[1].get_y(), 0)),
                  flecha2.animate.move_to((flecha2.get_x(), group_vec_num[2].get_y(), 0)))
        self.wait(wt)

        # creamos copia de los vectores y quitamos vectores del grupo
        vec1 = list_vec_nums[1].copy()
        vec2 = list_vec_nums[2].copy()
        self.add(vec1, vec2)
        group_vec_num.remove(list_vec_nums[1])
        group_vec_num.remove(list_vec_nums[2])

        # desplazar flechas y grupo fuera de pantalla, y separar vectores
        self.play(*[mo.animate.shift(10*DOWN) for mo in [flecha1, flecha2, group_vec_num]],
                  vec1.animate.shift(0.25*UP), vec2.animate.shift(0.25*DOWN))
        self.wait(wt)

        # convertimos a f(x) = v,... = 
        copy_vec1 = vec1.copy() #copia
        copy_vec2 = vec2.copy() #copia
        tex_eq1 = Tex(r'$f(0.874, 0.166, 0.301)=0.882$', color=GREEN).scale(1.3).move_to(vec1.get_center())
        tex_eq2 = Tex(r'$f(0.269, 0.894, 0.737)=1.414$', color=LOGO_BLUE).scale(1.3).move_to(vec2.get_center())
        self.play(*[ReplacementTransform(vi, eqi) for vi, eqi in zip([vec1, vec2], [tex_eq1, tex_eq2])])
        self.wait(wt)

        # resltamos la primera ecuacion
        self.play(ApplyWave(tex_eq1))
        self.wait(wt)

        # desplazamos segunda ecuacion fuera de la pantalla
        self.play(tex_eq2.animate.shift(15*DOWN))
        self.wait(wt)

        # convertimos primera ecuacion en vector
        #self.add(copy_vec1)
        self.play(ReplacementTransform(tex_eq1, copy_vec1))
        self.wait(wt)

        # quitamos corchetes del grupo anterior, los traemos arriba y creamos texto de ganadores
        group_vec_num.remove(p1)
        group_vec_num.remove(p2)
        text_ganadores = Text('Ganadores').scale(0.8).next_to(copy_vec1, UP).shift(1.0*UP)
        self.play(*[pi.animate.shift(9.5*UP) for pi in [p1, p2]], AddTextLetterByLetter(text_ganadores))
        self.wait(wt)

        # traemos el resto de vectores hacia arriba uno por uno (3, 1, 2)
        copy_vec2.shift(10*DOWN)
        self.play(list_vec_nums[3].animate.next_to(copy_vec1, DOWN))

        # copia de la copia
        copy_copy_vec1 = copy_vec1.copy()
        copy_copy_vec1.shift(15*DOWN)

        self.play(copy_copy_vec1.animate.next_to(list_vec_nums[3], DOWN))
        list_vec_nums[2].shift(10*DOWN)
        self.play(list_vec_nums[2].animate.next_to(copy_copy_vec1, DOWN))
        self.wait(wt)

        # convertimos texto de ganadores en padres
        text_padres = Text('Padres').scale(0.8).move_to(text_ganadores.get_center())
        self.play(ReplacementTransform(text_ganadores, text_padres))
        self.wait(wt)

        # resaltamos padres repetidos
        self.play(ApplyWave(copy_vec1), ApplyWave(copy_copy_vec1))
        self.wait(wt)
        

        self.wait(2)

