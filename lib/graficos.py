puntos_datos = []
lineas = []


def puntos(X, y, color="rojo"):
    """Acumula puntos a graficar."""
    global puntos_datos
    colores = {"rojo": (255, 0, 0), "azul": (0, 0, 255), "verde": (0, 255, 0)}
    c = colores.get(color.lower(), (255, 0, 0))
    for x, yy in zip(X, y):
        puntos_datos.append((float(x), float(yy), c))


def linea(modelo):
    """Añade una línea (m, b) a graficar."""
    global lineas
    lineas.append(modelo)


def _ajustar_rango(valores, extra=0.1):
    """Devuelve (min, max) con un padding configurable."""
    vmin = min(valores)
    vmax = max(valores)
    if vmin == vmax:
        delta = abs(vmin) if vmin else 1.0
        vmin -= delta * extra
        vmax += delta * extra
    else:
        margen = (vmax - vmin) * extra
        vmin -= margen
        vmax += margen
    return vmin, vmax


def _a_pixel(x, y, x1, x2, y1, y2, w, h):
    """Convierte coordenadas reales a coordenadas de pixel."""
    px = int((x - x1) / (x2 - x1) * (w - 1))
    py = int((y2 - y) / (y2 - y1) * (h - 1))
    return px, py


def _guardar_ppm(nombre, ancho, alto, pixels):
    with open(nombre, "wb") as f:
        f.write(f"P6\n{ancho} {alto}\n255\n".encode())
        f.write(pixels)


def graficar(nombre="resultado.png", ancho=800, alto=600, limpiar=True):
    if not puntos_datos:
        print("No hay datos")
        return

    xs = [p[0] for p in puntos_datos]
    ys = [p[1] for p in puntos_datos]
    x1, x2 = _ajustar_rango(xs)
    y1, y2 = _ajustar_rango(ys)

    fondo = 255
    pixels = bytearray([fondo] * (ancho * alto * 3))

    def dibujar(px, py, color):
        if 0 <= px < ancho and 0 <= py < alto:
            idx = (py * ancho + px) * 3
            pixels[idx : idx + 3] = bytes(color)

    # Ejes si entran en el rango
    gris = (200, 200, 200)
    if x1 <= 0 <= x2:
        px0, _ = _a_pixel(0, y1, x1, x2, y1, y2, ancho, alto)
        for py in range(alto):
            dibujar(px0, py, gris)
    if y1 <= 0 <= y2:
        _, py0 = _a_pixel(x1, 0, x1, x2, y1, y2, ancho, alto)
        for px in range(ancho):
            dibujar(px, py0, gris)

    # Líneas de regresión (azul)
    for m, b in lineas:
        for px in range(ancho):
            x = x1 + (px / (ancho - 1)) * (x2 - x1)
            y = m * x + b
            py = int((y2 - y) / (y2 - y1) * (alto - 1))
            dibujar(px, py, (0, 0, 255))

    # Puntos (pequeño cuadrado 3x3)
    for x, y, color in puntos_datos:
        cx, cy = _a_pixel(x, y, x1, x2, y1, y2, ancho, alto)
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                dibujar(cx + dx, cy + dy, color)

    ext = nombre.lower().rsplit(".", 1)[-1] if "." in nombre else ""
    if ext == "ppm" or not ext:
        _guardar_ppm(nombre, ancho, alto, pixels)
    else:
        try:
            from PIL import Image

            img = Image.frombytes("RGB", (ancho, alto), bytes(pixels))
            img.save(nombre)
        except Exception as exc:  # Pillow no instalado o error al guardar
            fallback = "resultado.ppm"
            _guardar_ppm(fallback, ancho, alto, pixels)
            print(
                f"No se pudo guardar {nombre} ({exc}); se guardó PPM como {fallback}"
            )
            nombre = fallback

    if limpiar:
        puntos_datos.clear()
        lineas.clear()

    print(f"Gráfica generada: {nombre}")
