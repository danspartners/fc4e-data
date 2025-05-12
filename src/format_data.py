import csv
import ast
import os
import json
from src import get_location_from_iso3

file_path = os.getenv("FILE_PATH", "./data/data.csv")  # Default file path

persistent_map = {
    "Explicit": "Explicit",
    "Implicit,No": "Implicit, No",
    "Implicit, No": "Implicit, No",
    "Implicit,Yes": "Implicit, Yes",
    "No": "No",
}

def process_csv_to_object():
    facets_list = []

    with open(file_path, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)  # Read as a dictionary per row

        for row in reader:
            item_dict = {}  # Initialize as a dictionary
            for column_name, value in row.items():
                new_key = column_name.lower().replace(" ", "_")
                if isinstance(value, str) and value.startswith("[") and value.endswith("]"):
                    try:
                        value = ast.literal_eval(value)
                    except (ValueError, SyntaxError):
                        pass

                # Convert specific values to an array (even if there's only one value)
                if (new_key == "iso" or new_key == "entity") and isinstance(value, str):
                    value = value.split(",")

                if (new_key == "globally_unique"):
                    if value == "Yes":
                        value = True
                    elif value == "No":
                        value = False
                    else:
                        value = None

                # Normalise persistent values
                if (new_key == "persistent"):
                    value = persistent_map.get(value, value)

                # Convert certain string numbers to integers (handle " " as null)
                if new_key in {"count", "managers", "start_date", "recommended_by", "number_of_resolvers"}:
                    if value == " ":
                        value = None
                    else:
                        try:
                            value = int(value)
                        except (ValueError, TypeError):
                            pass  # Ignore if it's not a valid number

                # Convert null to no for meta resolvers
                if (new_key == "metaresolvers"):
                    if value == None:
                        value = "No"

                item_dict[new_key] = value

            # Merge Countries & ISO into one array of objects
            countries = item_dict.get("countries", [])
            iso_codes = item_dict.get("iso", [])

            if isinstance(countries, list) and isinstance(iso_codes, list):
                item_dict["countries"] = [
                    {
                        "name": countries[i] if i < len(countries) else None,
                        "iso": iso_codes[i] if i < len(iso_codes) else None,
                        "location": get_location_from_iso3(iso_codes[i]) if i < len(iso_codes) and iso_codes[i] else None
                    }
                    for i in range(max(len(countries), len(iso_codes)))
                ]

            item_dict.pop("iso", None)

            facets_list.append(item_dict)

    return facets_list  # Return the list of parsed dictionaries