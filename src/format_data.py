import csv
import ast
import os
import json
from src import get_location_from_iso3

# Load the CSV file without headers
file_path = os.getenv("FILE_PATH", "./data/Elastic_JSON.csv")  # Default file path

def process_csv_to_object():
    facets_list = []

    with open(file_path, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)  # Read as a dictionary per row

        if "Facets" not in reader.fieldnames:
            print("Facets column not found in the CSV file.")
            return None

        for row in reader:
            item = row.get("Facets")
            if not item:
                continue  # Skip empty rows

            try:
                item_list = json.loads(item)  # load JSON

                # Convert "fake" arrays (strings that look like lists) to real lists
                for key in list(item_list.keys()):  # Use list() to avoid mutation issues
                    value = item_list.pop(key)  # Remove old key

                    # Convert key to lowercase and replace spaces with underscores
                    new_key = key.lower().replace(" ", "_")

                    # Convert JSON strings like "[\"value\"]" into actual lists
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

                    # Convert null to no for meta resolvers
                    if (new_key == "metaresovers"):
                        if value == None:
                            value = "No"

                    # Normalise persistent values
                    if (new_key == "persistent"):
                        if value == "Implicit,Yes" or value == "Yes,Implicit":
                            value = "Yes, Implicit"
                        elif value == "No,Implcit" or value == "Implicit,No":
                            value = "No, Implicit"
                        elif value == "Yes,Explicit" or value == "Explicit,Yes":
                            value = "Yes, Explicit"
                        elif value == "No,Explicit" or value == "Explicit,No":
                            value = "No, Explicit"

                    # Convert certain string numbers to integers (handle " " as null)
                    if new_key in {"count", "managers", "start_date", "recommended_by", "number_of_resolvers"}:
                        if value == " ":
                            value = None
                        else:
                            try:
                                value = int(value)
                            except (ValueError, TypeError):
                                pass  # Ignore if it's not a valid number

                    # Add updated key-value pair
                    item_list[new_key] = value

                # Merge Countries & ISO into one array of objects
                countries = item_list.get("countries", [])
                iso_codes = item_list.get("iso", [])

                # Ensure 'countries' field is an object or empty list, never null
                if isinstance(countries, list) and isinstance(iso_codes, list):
                    item_list["countries"] = [
                        {
                            "name": countries[i] if i < len(countries) else None,
                            "iso": iso_codes[i] if i < len(iso_codes) else None,
                            "location": get_location_from_iso3(iso_codes[i]) if i < len(iso_codes) and iso_codes[i] else None
                        }
                        for i in range(max(len(countries), len(iso_codes)))
                    ]
                
                item_list.pop("iso", None)  # Remove the original 'ISO' field

                facets_list.append(item_list)

            except Exception as e:
                print("Error processing row:", e)
                continue  # Skip invalid JSON entries or other errors

        return facets_list  # Return the list of parsed dictionaries