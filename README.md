# Lenguaje_Deep_Learning
# Igris

Interprete sencillo de un mini lenguaje enfocado en ejercicios de algebra lineal, estadistica basica y algoritmos pequeños de aprendizaje automatico. Incluye ejemplos listos para ejecutar y utilidades para graficar resultados en una imagen PNG/PPM.

## Requisitos
- Python 3.9+.
- Dependencias de Python: `antlr4-python3-runtime`. Para guardar graficos en PNG se recomienda ademas `Pillow` (si no esta, se generara un archivo PPM).
- No se necesita regenerar el parser: los archivos producidos por ANTLR ya estan incluidos.

Instalacion rapida de dependencias (en un entorno virtual o global):
```bash
pip install antlr4-python3-runtime pillow
```

## Ejecutar un programa Igris
Cada programa termina con extension `.igris`. Para ejecutarlo use `igris.py` indicando la ruta del archivo:
```bash
python3 igris.py ejemplos/02_regresion.igris
```

El interprete informara `IGRIS -> '<archivo>' ejecutado con exito` al finalizar. Las graficas se guardan como `resultado.png` (o `resultado.ppm` si no hay Pillow) en el directorio actual.

## Datos de ejemplo
- `datos/altura_peso.csv`: pares altura-peso para regresion lineal.
- `datos/iris.csv`: dataset simplificado para pruebas varias.

## Ejemplos incluidos
- `ejemplos/01_basico.igris`: operaciones aritmeticas, vectores y funciones matematicas (`raiz`, `seno`).
- `ejemplos/02_regresion.igris`: regresion lineal sobre `altura_peso.csv`, prediccion y grafica.
- `ejemplos/03_control.igris`: condicionales `si`/`sino` y bucles `mientras`.
- `ejemplos/04_perceptron.igris`: perceptron multicapa para OR.
- `ejemplos/05_kmeans.igris`: clustering k-means y prediccion de etiquetas.
- `ejemplos/06_sen.igris`: generacion de la curva seno muestreada y graficada.
- `ejemplos/07_multi_capa.igris`: perceptron entrenado muchas epocas para resolver XOR.

Puede ejecutar cualquiera cambiando el archivo en el comando de ejecucion:
```bash
python3 igris.py ejemplos/06_sen.igris
```

## Sintaxis rapida del lenguaje
- **Asignacion:** `variable => expresion`
- **Impresion:** `ver "texto", expresion, ...`
- **Bloques:** `{ ... }`
- **Condicional:** `si (condicion) { ... } sino { ... }`
- **Bucle:** `mientras (condicion) { ... }`
- **Vectores y acceso:** `v => [1,2,3]`, `v[0]`
- **Literales:** numeros enteros o decimales, `verdadero`, `falso`, cadenas entre comillas.

### Funciones incorporadas
- **Archivos y datos:** `cargar("archivo.csv")` lee desde `datos/`; `col(matriz, i)` toma la columna `i`.
- **Algebra basica:** `sumar`, `restar`, `multiplicar`, `dividir`, `potencia`, `raiz`, `seno`.
- **Matrices:** `mat_suma(A,B)`, `mat_resta(A,B)`, `mat_mult(A,B)`, `mat_trans(A)`, `mat_inv(A)`.
- **Modelos:** `regresion(X,y)` devuelve `(m,b)`; `perceptron(X,y[,config])` retorna un diccionario de red; `kmeans(X,k[,iter])`.
- **Prediccion:** `predecir(modelo, x)` funciona con regresion, perceptron y kmeans.
- **Graficos:** `puntos(X,y[,color])`, `linea(modelo)` y `graficar()` genera la imagen. Colores soportados: `rojo`, `azul`, `verde`.

### Operadores
- Aritmeticos: `+ - * / % ^`
- Comparacion: `< <= > >= == !=`
- Logicos: `&& ||`
- Precedencias estandar; use parentesis para agrupar.

## Crear y correr tu propio ejemplo
1) Escribe tu programa en un archivo `.igris` dentro de `ejemplos/` o en cualquier ruta.
2) Si necesitas cargar datos, pon el CSV en `datos/` y llama `cargar("archivo.csv")`.
3) Ejecuta `python3 igris.py ruta/al/archivo.igris`.
4) Si usas `puntos`, `linea` o `graficar`, revisa la imagen generada (por defecto `resultado.png`).

## Problemas comunes
- **Modulo antlr4 no encontrado:** instala `antlr4-python3-runtime`.
- **Imagen no se guarda en PNG:** instala `Pillow` o usa el archivo PPM generado.
- **Errores de dimensiones en matrices:** revisa que las listas anidadas tengan tamanos compatibles para la operacion.
