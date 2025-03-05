import mysql.connector

def load(data):
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='SQL@Learn123',
        database='api_data'
    )
    cursor = conn.cursor()

    sql = """
    INSERT INTO weather_data (city, temperature, humidity, weather_description) VALUES
    (%s, %s, %s, %s)
    """
    values = (data['city'], data['temperature'], data['humidity'], data['weather_description'])
    cursor.execute(sql, values)
    conn.commit()
    cursor.close()
    conn.close()
