
def parsing_json_airport(json_file):
    """Функция для вывода информации об аэропорте"""
    info = ('Airport information:\n' + 'Code IATA: ' + json_file.get('iata', '') + '\nName: '
            + json_file.get('shortName', '') + '\nFull name: ' + json_file.get('fullName', '') + '\nContinent: '
            + json_file.get('continent').get('name', '') + '\nCountry: ' + json_file.get('country').get('name', '')
            + '\nCity: ' + json_file.get('municipalityName', '') + '\nСoordinates: '
            + str(json_file.get('location').get('lat', '')) + ', ' + str(json_file.get('location').get('lon', ''))
            + '\nWebsite: ' + json_file.get('urls').get('webSite', '') + '\nWikipedia: '
            + json_file.get('urls').get('wikipedia', '') + '\nTwitter: ' + json_file.get('urls').get('twitter', '')
            + '\nGoogle Maps: ' + json_file.get('urls').get('googleMaps', '') + '\nFlight Radar: '
            + json_file.get('urls').get('flightRadar', '') + '\n')

    return info


def parsing_json_flight(json_file):
    """Функция для вывода информации о рейсе"""
    info = ('Flight information:\n' + 'Number: ' + json_file.get('number', '') + '\nAirline: '
            + json_file['airline'].get('name', '') + '\nAircraft: ' + json_file['aircraft'].get('model', '')
            + '\nStatus: ' + json_file.get('status', '') + '\nDeparture:\n' + '   Airport: ' + '\n      Code IATA: '
            + str(json_file['departure']['airport'].get('iata', '')) + '\n      Name: '
            + json_file['departure']['airport'].get('name', '') + '\n      Сoordinates: '
            + str(json_file['departure']['airport']['location'].get('lat', '')) + ', '
            + str(json_file['departure']['airport']['location'].get('lon', '')) + '\n   Scheduled time(local): '
            + str(json_file['departure'].get('scheduledTimeLocal', '')) + '\nArrival:\n' + '   Airport: '
            + '\n      Code IATA: ' + str(json_file['arrival']['airport'].get('iata', '')) + '\n      Name: '
            + json_file['arrival']['airport'].get('name') + '\n      Сoordinates: '
            + str(json_file['arrival']['airport']['location'].get('lat', '')) + ', '
            + str(json_file['arrival']['airport']['location'].get('lon', '')) + '\n   Scheduled time(local): '
            + json_file['arrival'].get('scheduledTimeLocal', '') + '\n   Actual time(local): '
            + json_file['arrival'].get('actualTimeLocal', '') + '\n   Terminal: '
            + json_file['arrival'].get('terminal', '') + '\n   Baggage belt: '
            + json_file['arrival'].get('baggageBelt', ''))

    return info


def parsing_json_distance_time_information(json_file):
    """Функция для вывода информации о дистанции и времени полета"""
    info = ('Distance/flight time between airports:' + '\nDeparture airport:\n' + '   Code IATA: ' + str(json_file['from'].get('iata', '')) + '\n   Name: '
            + json_file['from'].get('name', '') + '\n   Сoordinates: '
            + str(json_file['from']['location'].get('lat', '')) + ', '
            + str(json_file['from']['location'].get('lon', '')) + '\nArrival airport:\n' + '   Code IATA: '
            + str(json_file['to'].get('iata', '')) + '\n   Name: ' + json_file['to'].get('name', '')
            + '\n   Сoordinates: ' + str(json_file['to']['location'].get('lat', '')) + ', '
            + str(json_file['to']['location'].get('lon', '')) + '\nDistance:' + '\n   Meter: '
            + str(json_file['greatCircleDistance'].get('meter', '')) + '\n   Km: '
            + str(json_file['greatCircleDistance'].get('km', '')) + '\n   Mile: '
            + str(json_file['greatCircleDistance'].get('mile', '')) + '\nApprox flight time: '
            + str(json_file['approxFlightTime']))

    return info


def parsing_json_airport_schedule(json_file, arrival_departure):
    """Функция для вывода информации о расписании"""
    info = list()
    info.append('Flight schedule:')
    if arrival_departure == 'arrival':
        for flight in json_file['arrivals']:
            info.append('\n\nFlight: ' + str(flight.get('number', '')) + '\n   Scheduled time: '
                        + str(flight['movement'].get('scheduledTimeLocal', '')) + '\n   Actual time: '
                        + str(flight['movement'].get('actualTimeLocal', '')) + '\n   Runway time: '
                        + str(flight['movement'].get('runwayTimeLocal', '')) + '\n   Departure airport: '
                        + str(flight['movement']['airport'].get('iata', '')) + ' '
                        + str(flight['movement']['airport'].get('name', '')) + '\n   Airline: '
                        + str(flight['airline'].get('name', '')) + '\n   Aircraft: '
                        + str(flight['aircraft'].get('model', '')) + '\n   Status: ' + str(flight.get('status', ''))
                        + '\n   Terminal: ' + str(flight['movement'].get('terminal', '')) + '\n   Baggage belt: '
                        + str(flight['movement'].get('baggageBelt', '')))
    elif arrival_departure == 'departure':
        for flight in json_file['departures']:
            info.append('\n\nFlight: ' + str(flight.get('number', '')) + '\n   Scheduled time: '
                        + str(flight['movement'].get('scheduledTimeLocal', '')) + '\n   Actual time: '
                        + str(flight['movement'].get('actualTimeLocal', '')) + '\n   Runway time: '
                        + str(flight['movement'].get('runwayTimeLocal', '')) + '\n   Arrival airport: '
                        + str(flight['movement']['airport'].get('iata', '')) + ' '
                        + str(flight['movement']['airport'].get('name', '')) + '\n   Airline: '
                        + str(flight['airline'].get('name', '')) + '\n   Aircraft: '
                        + str(flight['aircraft'].get('model', '')) + '\n   Status: ' + str(flight.get('status', ''))
                        + '\n   Terminal: ' + str(flight['movement'].get('terminal', '')) + '\n   Check in desk: '
                        + str(flight['movement'].get('checkInDesk', '')) + '\n   Gate: '
                        + str(flight['movement'].get('gate', '')))

    return info
