
from services.geocoding_service import (
    buscar_cidades,
    GeocodingError
)

try:
    cidades = buscar_cidades("Manaus")

    if not cidades:
        print("Nenhum resultado encontrado.")

    for cidade in cidades:
        print(f"Cidade: {cidade['nome']}")
        print(f"Estado: {cidade['estado']}")
        print(f"Latitude: {cidade['latitude']}")
        print(f"Longitude: {cidade['longitude']}")
        print()

except (GeocodingError, ValueError) as erro:
    print("Não foi possível consultar:", erro)
