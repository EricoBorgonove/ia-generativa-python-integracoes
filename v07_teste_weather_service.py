
import json

from services.weather_service import (
    consultar_clima,
    WeatherServiceError
)
from services.geocoding_service import GeocodingError

cidade = input("Qual cidade deseja consultar? ").strip()

try:
    resultado = consultar_clima(cidade, dias=5)

    print("\n=== RESULTADO DA API ===")

    print(
        json.dumps(
            resultado,
            indent=4,
            ensure_ascii=False
        )
    )

except (
    WeatherServiceError,
    GeocodingError,
    ValueError
) as erro:
    print("Erro:", erro)
