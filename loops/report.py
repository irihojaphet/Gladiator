def main():
    spacecraft = {"name": "Voyager 1", "distance": 163}
    spacecraft["country"] = "USA" # adding key to dictionary
    print(create_report(spacecraft))  



def create_report(spacecraft):
    return f"""
    =========REPORT=========

    Name:{spacecraft["name"]}
    Distance:{spacecraft["distance"]} AU
    Country:{spacecraft["country"]}

    ========================
    """

main()