
def parsing_json_airoport(json_file):
    info = 'Airport information:\n' + 'Code IATA: ' + json_file.get('iata', '') + '\nName: ' + json_file.get('shortName', '') \
           + '\nFull name: ' + json_file.get('fullName', '') + '\nContinent: ' + json_file.get('continent').get('name', '') \
           + '\nCountry: ' + json_file.get('country').get('name', '') + '\nCity: ' + json_file.get('municipalityName', '')\
           + '\nСoordinates: ' + str(json_file.get('location').get('lat', '')) + ', ' + str(json_file.get('location').get('lon', '')) \
           + '\nWebsite: ' + json_file.get('urls').get('webSite', '') + '\nWikipedia: ' + json_file.get('urls').get('wikipedia', '') \
           + '\nTwitter: ' + json_file.get('urls').get('twitter', '') + '\nGoogle Maps: ' + json_file.get('urls').get('googleMaps', '') \
           + '\nFlight Radar: ' + json_file.get('urls').get('flightRadar', '') + '\n'

    return info

def parsing_json_airoport_schedule(json_file):
    print(json_file)
    info = 'Flight schedule:\n'

    return info
