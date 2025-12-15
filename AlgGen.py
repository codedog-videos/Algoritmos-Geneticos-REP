import numpy as np
import pandas as pd

########################## POBLACION INICIAL Y FUNCION FITNESS ##########################
# generacion de una poblacion aleatoria de tamano (n_ind, n_var)
# con valores en el rango (r_inicial, r_final)
def generador_poblacion(n_var, n_indv=10, r_inicial = -10.0, r_final=10.0):
    # poblacion con numeros aleatorios en el rango indicado
    poblacion = np.random.uniform(r_inicial, r_final, (n_indv, n_var))
    return poblacion

# definicion de function fitness
def test_f(xs):
    return xs[:,0]**2 + xs[:,1]**2 + xs[:,2]**2


########################## TORNEO BINARIO ##########################
# torneo binario para seleccionar los padres mas aptos
def torneo_binario(padres, fit_padres):
    ganadores = [] # lista de ganadores del torneo binario
    fit_ganadores = [] # lista de fitness de los ganadores
    for i in range(len(padres)):
        # se eligen dos invidivuos aleatorios para participar
        ind_contrincante_1 = np.random.randint(0, len(padres)) # primer contrincante
        ind_contrincante_2 = np.random.randint(0, len(padres)) # segundo contrincante

        # se consulta su fitness
        fitness_1 = fit_padres[ind_contrincante_1]
        fitness_2 = fit_padres[ind_contrincante_2]
        
        # conservamos al ganador y su fitness
        if fitness_1 < fitness_2:
            ganadores.append(padres[ind_contrincante_1])
            fit_ganadores.append(fitness_1)
        else:
            ganadores.append(padres[ind_contrincante_2])
            fit_ganadores.append(fitness_2)

    # regresamos los padres mas aptos para continuar con la evolucion y su fitness
    return np.array(ganadores), np.array(fit_ganadores)


########################## CROSSOVER ##########################
# generacion de hijos cruzando los genes de los padres bajo cierta probabilidad
def crossover(padres, p_cross=0.9):
    # lista de hijos resultantes del crossover
    hijos = []
    
    # iteramos individuos por parejas
    for i in range(0, len(padres), 2):
        # el crossover se realiza con probabilidad p_cross
        if np.random.choice([True, False], p=[p_cross, 1-p_cross]):
            # seleccionamos un valor entre 0 y 1
            alpha = np.random.rand()
            
            # generamos nuevos hijos
            hijo1 = alpha*padres[i] + (1-alpha)*padres[i+1]
            hijo2 = alpha*padres[i+1] + (1-alpha)*padres[i]
            
            # agregamos hijos a la lista
            hijos += [hijo1, hijo2]
        
        # se agregan los padres originales si no se cumple la probabilidad
        else:
            hijos += [padres[i].copy(), padres[i+1].copy()]
    
    # regresamos la lista de hijos
    return np.array(hijos)


########################## MUTACION ##########################
# mutacion sobre los genes de los hijos con valores en cierto rango y probabilidad
def mutacion(hijos, r_inicial, r_final, p_mut=0.2):
    # iteramos sobre los hijos
    for hi in range(len(hijos)):
        # iteramos sobre cada variable del hijo actual
        for vi in range(len(hijos[0])):
            # verificamos si se cumple la probabilidad de mutacion
            if np.random.choice(a=[True, False], p=[p_mut, 1-p_mut]):
                # si se cumple la probabilidad entonces se elige un nuevo valor en el rango especificado
                hijos[hi,vi] = np.random.uniform(r_inicial, r_final)

    # regresamos los hijos con genes mutados
    return np.array(hijos)


########################## REEMPLAZO GENERACIONAL ##########################
# generacion de poblacion final intercambiando los peores hijos por los mejores padres de la generacion actual (elitismo)
def reemplazo_generacional(padres, hijos, fit_padres, fit_hijos, elitismo=0):
    # en caso de aplicarse elitismo
    if elitismo > 0:
        # ordenamos los padres de mejor a peor
        ind_padres = np.argsort(fit_padres)
        padres = padres[ind_padres]
        fit_padres = fit_padres[ind_padres]

        # ordenamos los hijos de mejor a peor
        ind_hijos = np.argsort(fit_hijos)
        hijos = hijos[ind_hijos]
        fit_hijos = fit_hijos[ind_hijos]

        # reemplazamos los peores hijos por los mejores padres (elitismo)
        hijos = np.concatenate([hijos[:-elitismo], padres[:elitismo]])
        fit_hijos = np.concatenate([fit_hijos[:-elitismo], fit_padres[:elitismo]])
        
        # regresamos los hijos y su fitness
        return hijos, fit_hijos

    # si no hay elitismo entonces regresamos a la poblacion inicial de hijos y su fitnes
    else: 
        return hijos, fit_hijos


########################## ESCRITURA DE RESULTADOS ##########################
def info_generacion(generacion, poblacion, fit_poblacion):
    # agregamos indice de generacion
    aux_dicc = {'GENERACION': [generacion]*len(poblacion)}

    # agregamos informacion de cada variable
    for i in range(poblacion.shape[1]):
        aux_dicc[f'V{i+1}'] = poblacion[:,i]

    # agregamos fitness de la poblacion
    aux_dicc['FITNESS'] = fit_poblacion

    # regresamos dataframe con la informacion
    return pd.DataFrame(aux_dicc)


########################## DEFINICION DE VARIABLES DEL ALGORITMO ##########################
n_indv = 20 # numero de individuos en la poblacion
n_var = 3 # tamano de cada individuo (numero de variables)
r_inicial = -5.0 # rango inicial
r_final = 5.0 # rango final
elitismo = 5 # numero de padres a conservar en la poblacion final (reemplazando los peores hijos)
n_gen = 15 # numero de generaciones a ejecutar
p_cross = 0.8
p_mut = 0.03

# lista de la informacion de cada generacion
list_info = []

# generacion de poblacion inicial
padres = generador_poblacion(n_var, n_indv, r_inicial, r_final)

# fitness de la poblacion
fit_padres = test_f(padres)

# agregamos informacion a la lista
list_info.append(info_generacion(generacion=0, poblacion=padres, fit_poblacion=fit_padres))

# ejecucion de generaciones
for i in range(n_gen):
    # torneo binario
    padres, fit_padres = torneo_binario(padres, fit_padres)

    # crossover
    hijos = crossover(padres, p_cross=p_cross)

    # mutacion
    hijos = mutacion(hijos, r_inicial, r_final, p_mut=p_mut)

    # evaluacion del fitness de los hijos
    fit_hijos = test_f(hijos)

    # reemplazo generacional
    hijos, fit_hijos = reemplazo_generacional(padres, hijos, fit_padres, fit_hijos, elitismo)

    # los hijos se convierten en la proxima generacion depadres
    padres = hijos.copy()
    fit_padres = fit_hijos.copy()

    # agregamos informacion a la lista
    list_info.append(info_generacion(generacion=i+1, poblacion=padres, fit_poblacion=fit_padres))

# escritura de resultados
final_info = pd.concat(list_info)
final_info.to_csv('test_gen.csv', index=False)