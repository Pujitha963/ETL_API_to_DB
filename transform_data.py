def transform(data):
    if not data:
        return None

    transformed_data = {
        "city": data['name'],
        "temperature": data['main']['temp'],
        "humidity": data['main']['humidity'],
        "weather_description": data['weather'][0]['description']
    }
    return transformed_data