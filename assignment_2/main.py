import requests
from datetime import datetime
import enum_data

# BILM464, Assignment #2
# OpenSky REST API, provides ADS-B info of the live 
# flights when requested, response can be narrowed down by
# geographic coordinates or ICAO24 Transponder Code

# LIMITATIONS: 100 requests per day for unauthorized clients.
# Documentation and more info at: https://openskynetwork.github.io/opensky-api/rest.html 

URL = "https://opensky-network.org/api/states/all"

## Params ##

#-- Geographic constraints:
    # lamin: Minimum latitude (enlem), fp32
    # lamax: Maximum latitude, fp32

    # lomin: Minimum longitude (boylam), fp32
    # lomax: Maximum longitude, fp32

#-- Flight specific query:
    # icao24:  Transponder code of the plane in hex, string

turkey_lamin = 35.4618
turkey_lamax = 42.0643
turkey_lomax = 44.5753
turkey_lomin = 26.0905

params = {
    'lamin': turkey_lamin,
    'lomin': turkey_lomin,
    'lamax': turkey_lamax,
    'lomax': turkey_lomax
}

def main():
    response = requests.get(url=URL, params=params)
    if response.status_code == 200:
        print( parse_response(response.json()) )
    else:
        print(response.status_code)

def parse_response(json: dict) -> str:
    out = ""
    for flight in json['states']:
        out += f"""
        Transponder Kodu: {flight[0]}
        Cagri Kodu (Callsign): {flight[1]}
        Ulke: {flight[2]}
        Son Konum Guncellemesi: {datetime.utcfromtimestamp(flight[3]).strftime('%Y-%m-%d %H:%M:%S')} (UTC)
        Son Transponder Mesaji: {datetime.utcfromtimestamp(flight[4]).strftime('%Y-%m-%d %H:%M:%S')} (UTC)
        Boylam: {flight[5]}
        Enlem: {flight[6]}
        Barometrik Irtifa: {flight[7]}
        Yerde: {flight[8]}
        Hiz (Ground Speed): {flight[9]}
        Yon Derecesi (N = 0°, Saat Yonu): {flight[10]}
        Dikey Hiz Degisimi: {flight[11]}
        Geometrik Irtifa: {flight[13]}
        Squawk Kodu (7700 = Acil Durum): {flight[14]}
        Konum Bilgisi Kaynagi: {enum_data.data_source_map[ flight[16] ]}
        """
        out += "--------------------------------------\n"
    return out
            

if __name__ == "__main__":
    main()