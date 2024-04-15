import os
import csv


def read_data(file_name):
    """
    Reads csv file and returns numeric data.

    :param file_name: (str), name of CSV file
    :return: (dict), dictionary with numeric data, keys - csv column names, values - numbers in each column
    """
    cwd_path = os.getcwd()
    file_path = os.path.join(cwd_path, file_name)

    data = {}
    with open(file_path, mode="r", newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        headers = next(csv_reader)

        # pro každý sloupec prázdný seznam v datovém slovníku
        for header in headers:
            data[header] = []

        for row in csv_reader:
            for i, value in enumerate(row):
                data[headers[i]].append(float(value))

    return data


def selection_sort(seznam):
    for i in range(len(seznam)):
        min_idx = i
        for j in range(i+1, len(seznam)):
            if seznam[min_idx] > seznam[j]:
                min_idx = j
        seznam[i], seznam[min_idx] = seznam[min_idx], seznam[i]

    return seznam


def main():
    file_name = 'numbers.csv'
    data = read_data(file_name)
    print(data)
    selection = selection_sort(data['series_1'])
    print(selection)


if __name__ == '__main__':
    main()
