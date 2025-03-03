import pandas as pd
import json
import ast

# Load the CSV file without headers
file_path = "Elastic_JSON.csv"  # Update with your actual file path
df = pd.read_csv(file_path)

if "Facets" in df.columns:
    facets_list = []

    for item in df["Facets"].dropna():  # Drop empty rows
        try:
            parsed_json = json.loads(item)

            # Convert "fake" arrays (strings that look like lists) to real lists
            for key in list(parsed_json.keys()):  # Use list() to avoid mutation issues
                value = parsed_json.pop(key)  # Remove old key
                
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

                # Normalise persistent values
                if (new_key == "persistent"):
                    if value == "Implicit,Yes":
                        value = "Yes, Implicit"
                    elif value == "Yes,Implicit":
                        value = "Yes, Implicit"
                    elif value == "No,Implcit":
                        value = "No, Implicit"
                    elif value == "Implicit,No":
                        value = "No, Implicit"
                    elif value == "Yes,Explicit":
                        value = "Yes, Explicit"
                    elif value == "Explicit,Yes":
                        value = "Yes, Explicit"
                    elif value == "No,Explicit":
                        value = "No, Explicit"
                    elif value == "Explicit,No":
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
                parsed_json[new_key] = value

            # Merge Countries & ISO into one array of objects
            countries = parsed_json.get("countries", [])
            iso_codes = parsed_json.get("iso", [])

            if isinstance(countries, list) and isinstance(iso_codes, list):
                parsed_json["countries"] = [
                    {"name": countries[i] if i < len(countries) else None, "iso": iso_codes[i] if i < len(iso_codes) else None}
                    for i in range(max(len(countries), len(iso_codes)))
                ]
            
            parsed_json.pop("iso", None)  # Remove the original 'ISO' field

            facets_list.append(parsed_json)

        except json.JSONDecodeError:
            pass  # Skip invalid JSON entries

        # Save the cleaned data to a JSON file
        output_path = "data.json"
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(facets_list, f, indent=4, ensure_ascii=False)

    print(f"Processed JSON saved to {output_path}")
else:
    print("Facets column not found in the CSV file.")
