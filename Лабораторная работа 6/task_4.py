import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename: str, delimiter=",", new_line="\n") -> list[dict]:
    with open(filename) as f:
        headers_list = f.readline().rstrip(new_line).split(delimiter)
        data = [line.rstrip(new_line).split(delimiter) for line in f.readlines()]

        list_json = []
        for k in range(len(data)):
            list_json.append({headers_list[i]: data[k][i] for i in range(len(headers_list))})

        return list_json

print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
