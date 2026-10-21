import math
import requests

def obtener_datos():
    respuesta = requests.get(
        "https://open.er-api.com/v6/latest/USD",
        timeout=(3, 5),
    )
    respuesta.raise_for_status()
    return respuesta.json()


def extraer_tasa(datos: dict, moneda: str = "CLP"):
    if not isinstance(datos, dict):
        raise ValueError("Respuesta inesperada.")

    rates = datos.get("rates")
    if not isinstance(rates, dict) or moneda not in rates:
        raise ValueError(f"No se encontró el valor de la moneda '{moneda}'.")

    valor = rates[moneda]

    if (
        type(valor) not in (int, float)
        or not math.isfinite(valor)
        or valor <= 0
    ):
        raise ValueError("Valor del indicador inválido.")

    fecha = datos.get("time_last_update_utc", "Fecha no disponible")

    return fecha, valor


# --- Bloque principal con control de excepciones ---
try:
    # Consultar la API y obtener los datos.
    datos = obtener_datos()

    # Extraer y validar la fecha y el valor del CLP.
    fecha, valor = extraer_tasa(datos, "CLP")

    # Mostrar el valor con dos decimales y su unidad.
    print(f"Dólar observado: {valor:.2f} CLP por USD")

    # Mostrar la fecha a la que corresponde el dato.
    print(f"Fecha del registro: {fecha}")

except requests.exceptions.RequestException:
    # Controlar fallos de conexión, espera, HTTP o decodificación JSON.
    print("No pudimos consultar el servicio. Reintente.")

except (ValueError, KeyError, TypeError):
    # Controlar valores inválidos, claves ausentes o tipos incorrectos.
    print("La respuesta no contiene un indicador válido.")