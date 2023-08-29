import json


def parsing_json_airoport(json_file):

    info = 'Airport information:\n' + 'Code IATA: ' + json_file.get('iata', '') + '\nName: ' + json_file.get('shortName', '') \
           + '\nFull name: ' + json_file.get('fullName', '') + '\nContinent: ' + json_file.get('continent').get('name', '') \
           + '\nCountry: ' + json_file.get('country').get('name', '') + '\nCity: ' + json_file.get('municipalityName', '')\
           + '\nСoordinates: ' + str(json_file.get('location').get('lat', '')) + ', ' + str(json_file.get('location').get('lon', '')) \
           + '\nWebsite: ' + json_file.get('urls').get('webSite', '') + '\nWikipedia: ' + json_file.get('urls').get('wikipedia', '') \
           + '\nTwitter: ' + json_file.get('urls').get('twitter', '') + '\nGoogle Maps: ' + json_file.get('urls').get('googleMaps', '') \
           + '\nFlight Radar: ' + json_file.get('urls').get('flightRadar', '') + '\n'

    return info

def parsing_json_flight(json_file):

    info = 'Flight information:\n' +'Number: '+ json_file['number'] + '\nAirline: ' + json_file['airline']['name'] + '\nAircraft: '+ json_file['aircraft']['model'] \
             + '\nStatus: '+ json_file['status'] + '\nDeparture:\n' + '   Airport: ' + '\n      Code IATA: ' + str(json_file['departure']['airport']['iata']) \
             + '\n      Name: ' + json_file['departure']['airport']['name'] + '\n      Сoordinates: ' + str(json_file['departure']['airport']['location']['lat'])  + ', ' \
             + str(json_file['departure']['airport']['location']['lon']) + '\n   Scheduled time(local): ' + json_file['departure']['scheduledTimeLocal'] \
             + '\nArrival:\n' + '   Airport: ' + '\n      Code IATA: ' + str(json_file['arrival']['airport']['iata']) \
             + '\n      Name: ' + json_file['arrival']['airport']['name'] + '\n      Сoordinates: ' + str(json_file['arrival']['airport']['location']['lat'])  + ', ' \
             + str(json_file['arrival']['airport']['location']['lon']) + '\n   Scheduled time(local): ' + json_file['arrival']['scheduledTimeLocal'] \
             + '\n   Actual time(local): ' + json_file['arrival']['actualTimeLocal']  + '\n   Terminal: ' + json_file['arrival']['terminal'] \
             + '\n   Baggage belt: ' + json_file['arrival']['baggageBelt']

    return info


def parsing_json_distance_time_information(json_file):

    info = '\nDeparture airport:\n' + '   Code IATA: ' + str(json_file['from']['iata']) + '\n   Name: ' + json_file['from']['name'] \
            + '\n   Сoordinates: ' + str(json_file['from']['location']['lat']) + ', ' + str(json_file['from']['location']['lon']) \
            + '\nArrival airport:\n' + '   Code IATA: ' + str(json_file['to']['iata']) + '\n   Name: ' + json_file['to']['name'] \
            + '\n   Сoordinates: ' + str(json_file['to']['location']['lat']) + ', ' + str(json_file['to']['location']['lon']) \
            + '\nDistance:' + '\n   Meter: ' + str(json_file['greatCircleDistance']['meter']) + '\n   Km: ' + str(json_file['greatCircleDistance']['km']) \
            + '\n   Mile: ' + str(json_file['greatCircleDistance']['mile']) + '\nApprox flight time: ' + str(json_file['approxFlightTime'])

    return info


def parsing_json_airoport_schedule(json_file, ArrivalDeparture):
    #print(json.dumps(json_file, indent=4))
    info = list()
    info.append('Flight schedule:')
    if ArrivalDeparture == 'arrival':
        for flight in json_file['arrivals']:
            info.append('\n\nFlight: ' + str(flight['number']) + '\n   Scheduled time: ' + str(flight['movement']['scheduledTimeLocal']) \
                    + '\n   Actual time: ' + str(flight['movement']['actualTimeLocal']) + '\n   Runway time: ' + str(flight['movement'].get('runwayTimeLocal', '')) \
                    + '\n   Departure airport: ' + str(flight['movement']['airport']['iata']) + ' ' + str(flight['movement']['airport']['name']) \
                    + '\n   Airline: ' + str(flight['airline']['name']) + '\n   Aircraft: ' + str(flight['aircraft']['model']) \
                    + '\n   Status: ' + str(flight['status']) + '\n   Terminal: ' + str(flight['movement']['terminal']) \
                    + '\n   Baggage belt: ' + str(flight['movement'].get('baggageBelt', '')))
    elif ArrivalDeparture == 'departure':
        for flight in json_file['departures']:
            info.append('\n\nFlight: ' + str(flight['number']) + '\n   Scheduled time: ' + str(flight['movement']['scheduledTimeLocal']) \
                    + '\n   Actual time: ' + str(flight['movement']['actualTimeLocal']) + '\n   Runway time: ' + str(flight['movement'].get('runwayTimeLocal', '')) \
                    + '\n   Arrival airport: ' + str(flight['movement']['airport']['iata']) + ' ' + str(flight['movement']['airport']['name']) \
                    + '\n   Airline: ' + str(flight['airline']['name']) + '\n   Aircraft: ' + str(flight['aircraft']['model']) \
                    + '\n   Status: ' + str(flight['status']) + '\n   Terminal: ' + str(flight['movement']['terminal']) \
                    + '\n   Check in desk: ' + str(flight['movement'].get('checkInDesk', '')) + '\n   Gate: ' + str(flight['movement'].get('gate', '')))

    return info
