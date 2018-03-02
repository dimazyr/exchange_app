def read_file(filepath: str):
    """
    function to extract data from input file
    :param filepath: path to input text file
    :return: dataset/ two-dimensional array of each change per row
    """
    with open(filepath, "r") as f:
        lines = f.read().splitlines()
    data = []
    exchange_classes = []
    for line in lines:
        data.append(line.split(","))
        if line[-1] not in exchange_classes:
            exchange_classes.append(line[-1])
    return data, exchange_classes

