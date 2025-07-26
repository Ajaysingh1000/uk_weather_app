def parse_climate_text(text):
    lines = text.strip().splitlines()

    # Extract metadata
    metadata = {"description": ""}
    metadata["description"] = lines[:5]

    data_lines = [
        line for line in lines if line.strip() and line.strip()[0:4].isdigit()
    ]
    parsed_entries = []

    for line in data_lines:
        parts = line.strip().split()
        if len(parts) != 18:
            continue
        year = int(parts[0])
        values = [None if val == "---" else float(val) for val in parts[1:]]
        parsed_entries.append(
            {
                "year": year,
                "jan": values[0],
                "feb": values[1],
                "mar": values[2],
                "apr": values[3],
                "may": values[4],
                "jun": values[5],
                "jul": values[6],
                "aug": values[7],
                "sep": values[8],
                "oct": values[9],
                "nov": values[10],
                "dec": values[11],
                "win": values[12],
                "spr": values[13],
                "sum": values[14],
                "aut": values[15],
                "ann": values[16],
            }
        )

    return {"data": parsed_entries, "metadata": metadata}
