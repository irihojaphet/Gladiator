def main():
    spacecraft = {"name": "Voyager 1", "distance": 163}
    spacecraft.update({"country": "USA", "orbit": "Sun"}) # adding keys to dictionary
    print(create_report(spacecraft))  



def create_report(spacecraft):
    return f"""
    =========REPORT=========

    Name:{spacecraft.get("name", "Unknown")}
    Distance:{spacecraft.get("distance", "Unkown")} AU
    Country:{spacecraft.get("country", "Unknown")}
    Orbit:{spacecraft.get("orbit", "Unknown")}

    ========================
    """

main()