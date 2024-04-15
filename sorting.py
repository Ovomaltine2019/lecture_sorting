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


def selection_sort_direction(seznam, direction="V"):
    if direction == "V":
        for i in range(len(seznam)): # teoreticky můžu přidat -1, protože poslední prvek budu mít už ve správným pořadí
            min_idx = i
            for j in range(i + 1, len(seznam)):
                if seznam[min_idx] > seznam[j]:
                    min_idx = j
            seznam[i], seznam[min_idx] = seznam[min_idx], seznam[i]

    if direction == "S":
        for i in range(len(seznam)):
            max_idx = i
            for j in range(i + 1, len(seznam)):
                if seznam[max_idx] < seznam[j]:
                    max_idx = j
            seznam[i], seznam[max_idx] = seznam[max_idx], seznam[i]

    return seznam

# nejlepší scénář: "S": O(n*(n-1)) = O(n^2-n) = O(n^2) "V": O(n^2)
# nejhorší scénář: "S": O(n^2) "V": O(n^2)


def bubble_sort(seznam):
    for i in range(len(seznam)-1):
        for j in range(len(seznam)-1-i):
            if seznam[j] > seznam[j+1]:
                seznam[j], seznam[j+1] = seznam[j+1], seznam[j]

    return seznam


# toto je úplně celý můj nápad :-D
def bubble_sort2(seznam):
    for i in range(len(seznam)-1):
        initial = i
        while seznam[i] > seznam[i + 1]:
            seznam[i], seznam[i + 1] = seznam[i + 1], seznam[i]
            i += 1
        i = initial

    return seznam

# nejlepší scénář: O(n)
# nejhorší scénář: O(n^2)


def insertion_sort(seznam):
    for i in range(1, len(seznam)):
        key = seznam[i]
        j = i - 1
        while j >= 0 and seznam[j] > key:
            seznam[j + 1] = seznam[j]
            j -= 1
        seznam[j + 1] = key
    return seznam


# metoda sort() - meni poradi prvku primo v promenne
my_list = [3, 8, 1, 2, 32]

my_list.sort()
print(my_list)

# funkce sorted() - vytvari novy serazeny seznam
my_list = [3, 8, 1, 2, 32]

sorted_list = sorted(my_list)
print(sorted_list)
reverse_sorted_list = sorted(my_list, reverse=True)
print(reverse_sorted_list)


list_of_words = ["MOO", "meeeoow", "woof", "BZZZZZZ"]
list_of_words = sorted(list_of_words, key=len)
list_of_words2 = sorted(list_of_words, key=str.lower)

print(list_of_words)
print(list_of_words2)

# def main():
#     file_name = 'numbers.csv'
#     data = read_data(file_name)
#     print(data)
#     selection = selection_sort(data['series_1'])
#     print(selection)
#     selection2 = selection_sort_direction(data['series_1'], "S")
#     print(selection2)
#     bubble = bubble_sort(data['series_3'])
#     print(bubble)
#     bubble2 = bubble_sort2(data['series_3'])
#     print(bubble2)
#     insertion = insertion_sort(data['series_2'])
#     print(insertion)
#
#
# if __name__ == '__main__':
#     main()
