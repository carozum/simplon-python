"""
Écrire un programme qui convertit en mètres par seconde et en km/h une vitesse fournie par l'utilisateur en miles/heure (1 mile = 1609 mètres). Afficher le résultat avec uniquement 2 chiffres après la virgule.
"""

print(
    f"""*****************************
    \nEXERCICE 5 - conversion
    \r
    \r*****************************""")


def convert_time(total_seconds):
    one_year = 36525 * 24 * 36
    one_month = 3043.7 * 24 * 36
    one_day = 24 * 3600
    one_hour = 3600
    one_minute = 60

    years = total_seconds // one_year
    years_remainder = total_seconds - years * one_year

    months = years_remainder // one_month
    months_remainder = years_remainder % one_month

    days = months_remainder // one_day
    days_remainder = months_remainder % one_day

    hours = days_remainder // one_hour
    hours_remainder = days_remainder % one_hour

    minutes = hours_remainder // one_minute
    minutes_remainder = hours_remainder % one_minute

    return f"""
        \n{total_seconds} secondes correspondent à :
        \r{years} années {months} mois {days} jours
        \r{hours} heures {minutes} minutes {minutes_remainder} secondes
        """


print("Conversion seconds to year/month/day/hour/minute/seconds")
print(convert_time(3430061596791935255))


def speed_km_h(speed):
    return round(speed * 1609 / 1000, 2)


def speed_m_s(speed):
    return round(speed * 1609 / 3600, 2)


speed = 120
print("***********************")
print("Conversion miles per hour to km per hour")
print(f"\n{speed} mile(s) per hour are about {speed_km_h(speed)} km per hour")

print("\n***********************")
print("Conversion miles per hour to meter per second")
print(f"\n{speed} mile(s) per hour are about {speed_m_s(speed)} meter(s) per hour")
print("\n***********************")
