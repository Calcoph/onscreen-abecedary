defaults = {
    "size": [200, 50],
    "initial position": [1000, 50],
    "font size": [25],
    "font family": ["Cascadia code"],
    "text": ["ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"],
    "color mode": ["dark"]
}

configuration = dict()

# Read the file
section = "nosection"
with open("config.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        if len(line) > 0:
            if line[0:2] == "[#":
                section = line[2:-2]
            elif line != "\n":
                value = line.split("#")[0]
                if value[-1] == "\n":
                    value = value[:-1]

                if section in configuration:
                    configuration[section].append(value)
                else:
                    configuration[section] = [value]

# Verify data
verification = [
    ("size", 2, ("int", "int")),
    ("initial position", 2, ("int", "int")),
    ("font size", 1, ("float",)),
    ("font family", 1, ("string",)),
    ("text", 1, ("string",)),
    ("color mode", 1, ("string",))
]
for i in verification:
    section_name, item_amount, types = i
    if section_name in configuration:
        section = configuration[section_name]
        if len(section) != item_amount:
            configuration[section_name] = defaults[section_name]
            print("not the exact amount of options")
        else:
            result = []
            for jndex, j in enumerate(section):
                if types[jndex] == "string":
                    result.append(j)
                elif types[jndex] == "int":
                    try:
                        result.append(int(j))
                    except ValueError:
                        configuration[section_name] = defaults[section_name]
                        print("that is not an int")
                        break
                elif types[jndex] == "float":
                    try:
                        result.append(float(j))
                    except ValueError:
                        configuration[section_name] = defaults[section_name]
                        print("that is not a float")
                        break
            configuration[section_name] = result
    else:
        configuration[section_name] = defaults[section_name]
        print("that key is not in configuration")
        print(section_name)

styles = {
    "dark": "QLabel { background-color: #000000; color: #FFFFFF }",
    "light": "QLabel { background-color: #FFFFFF; color: #000000 }",
}

if __name__ == "__main__":
    for key, value in configuration.items():
        print(f'"{key}": {value}')
