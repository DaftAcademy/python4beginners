import os
import shutil
import tempfile
from functools import wraps

from homework_checker.base import Assignment

# # Chcemy napisać sprawdzarkę do testu znajomości stolic europejskich.
# # Format listy stolic taki jak w pliku stolice.csv
# # Format pytań taki jak w pliku pytania.csv
# # Format odpowiedzi taki jak w pliku odpowiedzi.csv
#
# # Napisz funkcję check_homework, która przyjmuje trzy argumenty:
# # - capitals_csv to ścieżka do pliku, który zawiera listę stolic europejskich
# # - questions_csv to ścieżka pliku csv, który zawiera pytania
# # - answers_csv to ścieżka pliku, który zawiera odpowiedzi
# # Funkcja zwraca liczbę poprawnych odpowiedzi
#
# def check_homework(capitals_csv, questions_csv, answers_csv):
#     # Tu wpisz swoje rozwiązanie (i skasuj raise NotImplementedError() :)
#     raise NotImplementedError()
#
# assert check_homework('stolice.csv', 'pytania.csv', 'odpowiedzi.csv') == 5
#
import csv

def check_homework(capitals_file_name, questions_file_name, answers_file_name):

    capitals_data = {}
    with open('stolice.csv', 'r') as capitals:
        reader = csv.reader(capitals, delimiter=';')
        next(reader)
        for row in reader:
            country, capital = row
            capitals_data[country] = capital

    good_answers = []
    with open('pytania.csv', 'r') as questions:
        reader = csv.reader(questions, delimiter=';')
        next(reader)
        for row in reader:
            country, a, b, c, d = row
            if capitals_data[country] == a:
                good_answers.append('A')
            elif capitals_data[country] == b:
                good_answers.append('B')
            elif capitals_data[country] == c:
                good_answers.append('C')
            elif capitals_data[country] == d:
                good_answers.append('D')

    points = 0
    with open('odpowiedzi.csv', 'r') as answers_file:
        reader = csv.reader(answers_file, delimiter=';')
        next(reader)
        for idx, row in enumerate(reader):
            answer = row[0]
            if answer == good_answers[idx]:
                points += 1

    return points


def run_in_clean_directory(src):

    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            cwd = os.getcwd()
            with tempfile.TemporaryDirectory() as tmpdirname:
                src_files = os.listdir(src)
                for file_name in src_files:
                    full_file_name = os.path.join(src, file_name)
                    if (os.path.isfile(full_file_name)):
                        shutil.copy(full_file_name, tmpdirname)
                try:
                    os.chdir(tmpdirname)
                    func(*args, **kwargs)
                finally:
                    os.chdir(cwd)

        return wrapper

    return decorator


@run_in_clean_directory('../homework4/2a')
def test_basic(func, module, attr_name):
    assert 5 ==  func('stolice.csv', 'pytania.csv', 'odpowiedzi.csv')

@run_in_clean_directory('../homework4/2b')
def test_basic_2(func, module, attr_name):
    assert 4 ==  func('stolice.csv', 'pytania.csv', 'odpowiedzi.csv')

@run_in_clean_directory('../homework4/2c')
def test_everyting_bad(func, module, attr_name):
    assert 0 ==  func('stolice.csv', 'pytania.csv', 'odpowiedzi.csv')

assignment = Assignment('zadanie2', 'zadanie2.py', 'check_homework', (test_basic, test_basic_2,
                                                                      test_everyting_bad))
