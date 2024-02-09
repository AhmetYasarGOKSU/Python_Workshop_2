from math import floor
import random as r

total_flights, total_take_offs, total_landings = 0, 0, 0


def daily_flight():
    take_offs = r.randint(50, 71)
    landings = r.randint(50, 71)
    bad_conditions = 30 / 100
    takes_offs_miss = 60 / 100
    landings_miss = 40 / 100
    final_take_offs = floor(take_offs - (take_offs * bad_conditions * takes_offs_miss))
    final_landings = floor(landings - (landings * bad_conditions * landings_miss))
    day_total_flight = final_take_offs + final_landings
    return day_total_flight, final_landings, final_take_offs


flights = daily_flight()
print(f"Today was made {flights[1]} landings, and {flights[2]} take offs.\nToday was made {flights[0]} flights.")


def monthly_flights():
    global total_flights, total_landings, total_take_offs
    for i in range(30):
        daily_flight()
        flight = daily_flight()
        total_take_offs += flight[2]
        total_landings += flight[1]
        total_flights += flight[0]
    return total_flights, total_landings, total_take_offs


monthly_flights()
print(f"This month was made {total_landings} landings, and {total_take_offs} take offs.\n"
      f"This month was made {total_flights} flights.")
