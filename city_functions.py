def get_city_country(city, country, population=""):
    """Generate a neatly formatted city and country"""
    if population:
        city_country = f"{city}, {country} - {population}."
    else:
        city_country = f"{city}, {country}"

    return city_country.title()
