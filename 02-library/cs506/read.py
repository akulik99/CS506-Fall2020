def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    matrix = []
    with open(csv_file_path, "r") as f:
        file = f.readlines()
        for row in file:
            row_strip = row.rstrip("\n")
            split_rows = row_strip.split(",")
            rows = []
            for p in split_rows:
                if p.isdigit():
                    rows.append(int(p))
                else:
                    p_strip = p.strip("")
                    rows.append(p_stripped)
            matrix.append(rows)
    return matrix