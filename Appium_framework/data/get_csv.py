
def get_csv_all(csv_file):
    with open(csv_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    return lines
