import math
import random


def regresion(X, y):
    n = len(X)
    sx = sy = sxy = sx2 = 0
    for i in range(n):
        sx += X[i]
        sy += y[i]
        sxy += X[i] * y[i]
        sx2 += X[i] * X[i]
    m = (n * sxy - sx * sy) / (n * sx2 - sx * sx)
    b = (sy - m * sx) / n
    return (m, b)


def _sigmoide(x):
    return 1 / (1 + math.exp(-x))


def _sigmoide_deriv(x):
    s = _sigmoide(x)
    return s * (1 - s)


def perceptron(X, y, config=None):
    """Entrena un perceptrón multicapa sencillo. X: lista de vectores, y: etiquetas 0/1."""
    capas = None
    epocas = 1500
    lr = 0.3
    if config is not None:
        if isinstance(config, dict):
            capas = config.get("capas")
            epocas = config.get("epocas", epocas)
            lr = config.get("lr", lr)
        elif isinstance(config, list):
            capas = config
        elif isinstance(config, (int, float)):
            epocas = int(config)
    if capas is None:
        capas = [len(X[0]), 4, 1]
    elif capas[-1] != 1:
        capas = list(capas) + [1]

    # Inicializar pesos pequeños
    pesos = []
    for i in range(len(capas) - 1):
        fan_in = capas[i] + 1  # + bias
        fan_out = capas[i + 1]
        capa = [[(random.random() - 0.5) * 2 / fan_in for _ in range(fan_in)] for _ in range(fan_out)]
        pesos.append(capa)

    def _forward(x):
        activaciones = []
        entrada = x
        for capa in pesos:
            z = []
            salida = []
            for neuron in capa:
                s = sum(w * v for w, v in zip(neuron[:-1], entrada)) + neuron[-1]
                z.append(s)
                salida.append(_sigmoide(s))
            activaciones.append((entrada, z, salida))
            entrada = salida
        return activaciones, salida

    # Entrenamiento
    for _ in range(epocas):
        for xi, yi in zip(X, y):
            activaciones, salida = _forward(xi)
            # backward
            error = [salida[0] - yi]
            deltas = [ [error[0] * _sigmoide_deriv(activaciones[-1][1][0])] ]
            # capas ocultas
            for l in range(len(pesos) - 2, -1, -1):
                capa = pesos[l]
                sig = activaciones[l][1]
                siguiente = deltas[0]
                delta_capa = []
                for j in range(len(capa)):
                    suma = sum(pesos[l + 1][k][j] * siguiente[k] for k in range(len(pesos[l + 1])))
                    delta_capa.append(_sigmoide_deriv(sig[j]) * suma)
                deltas.insert(0, delta_capa)
            # Actualizar pesos
            for l, capa in enumerate(pesos):
                entrada, _, salida = activaciones[l]
                for j, neuron in enumerate(capa):
                    for k in range(len(entrada)):
                        neuron[k] -= lr * deltas[l][j] * entrada[k]
                    neuron[-1] -= lr * deltas[l][j]  # bias

    return {"tipo": "perceptron", "capas": capas, "pesos": pesos}


def _forward_perceptron(modelo, x):
    pesos = modelo["pesos"]
    entrada = x
    for capa in pesos:
        salida = []
        for neuron in capa:
            s = sum(w * v for w, v in zip(neuron[:-1], entrada)) + neuron[-1]
            salida.append(_sigmoide(s))
        entrada = salida
    return entrada


def kmeans(X, k, iteraciones=20):
    """Clustering k-means sencillo; devuelve ('kmeans', {'centroides': ..., 'etiquetas': ...})."""
    if not X:
        return {"tipo": "kmeans", "centroides": [], "etiquetas": []}
    dim = len(X[0])
    centroides = random.sample(X, min(k, len(X)))
    etiquetas = [0] * len(X)
    for _ in range(iteraciones):
        # asignar
        for i, x in enumerate(X):
            dist_min = None
            c_min = 0
            for idx, c in enumerate(centroides):
                d = sum((xi - ci) ** 2 for xi, ci in zip(x, c))
                if dist_min is None or d < dist_min:
                    dist_min = d
                    c_min = idx
            etiquetas[i] = c_min
        # recalcular
        nuevos = [[0.0] * dim for _ in centroides]
        cont = [0] * len(centroides)
        for etiqueta, x in zip(etiquetas, X):
            cont[etiqueta] += 1
            for j, v in enumerate(x):
                nuevos[etiqueta][j] += v
        for i in range(len(centroides)):
            if cont[i]:
                centroides[i] = [v / cont[i] for v in nuevos[i]]
    return {"tipo": "kmeans", "centroides": centroides, "etiquetas": etiquetas}


def predecir(modelo, x):
    # Regresión lineal (tupla de dos números)
    if (
        isinstance(modelo, tuple)
        and len(modelo) == 2
        and all(isinstance(v, (int, float)) for v in modelo)
    ):
        m, b = modelo
        return m * x + b
    if isinstance(modelo, dict):
        tipo = modelo.get("tipo")
        if tipo == "perceptron":
            salida = _forward_perceptron(modelo, x)[0]
            return 1 if salida >= 0.5 else 0
        if tipo == "kmeans":
            centroides = modelo.get("centroides", [])
            if not centroides:
                return -1
            dist_min = None
            c_min = 0
            for idx, c in enumerate(centroides):
                d = sum((xi - ci) ** 2 for xi, ci in zip(x, c))
                if dist_min is None or d < dist_min:
                    dist_min = d
                    c_min = idx
            return c_min
    raise ValueError("Modelo no soportado")
