import correctmatch

correctmatch.precompile()
import csv
import numpy as np
import pandas as pd


# def parserow(row: list):
#     print(row)
#     dictionary = {' Private': 0, ' Self-emp-not-inc': 1, ' Self-emp-inc': 2, ' Federal-gov': 3, ' Local-gov': 4,
#                   ' State-gov': 5, ' Without-pay': 6, ' Never-worked': 7,
#                   ' Bachelors': 0, ' Some-college': 1, ' 11th': 2, ' HS-grad': 3, ' Prof-school': 4, ' Assoc-acdm': 5,
#                   ' Assoc-voc': 6, ' 9th': 7, ' 7th-8th': 8, ' 12th': 9, ' Masters': 10, ' 1st-4th': 11, ' 10th': 12,
#                   ' Doctorate': 13, ' 5th-6th': 14, ' Preschool': 15
#                   }
#     parsedrow = [dictionary[i] if i in dictionary else i for i in row[:5]]
#     atoirow = [int(i) for i in parsedrow]
#     print(atoirow)
#     return atoirow


# if __name__ == '__main__':
#     with open("./StudentsPerformance.csv", "r") as f:
#         with open("./output.csv", "a+") as outcsv:
#             outcsv_writer = csv.writer(outcsv)
#             reader = csv.reader(f)
#             for row in reader:
#                 outcsv_writer.writerow(parserow(row))

def test_students():
    students = pd.read_csv("StudentsPerformance.csv")
    print(students.head())
    print(len(students))
    print(type(students))
    students_values = students.values[5:]
    print(correctmatch.uniqueness(students_values))
    fitted_model = correctmatch.fit_model(students_values)
    fitted_students = correctmatch.sample_model(fitted_model, students_values.shape[0])
    print(correctmatch.uniqueness(fitted_students))


def test_pillow():
    Pillows = pd.read_csv("SaYoPillow.csv")
    ParsedPillows = pd.DataFrame(columns=['sr', 'rr', 't', 'lm', 'bo', 'rem', 'sr.1', 'hr', 'sl'], dtype=int)
    print(Pillows.head())
    print(len(Pillows))
    for Pillow in Pillows.values:
        ParsedPillow = np.array([int(i) for i in Pillow])
        # pd.concat([ParsedPillows, ParsedPillow])
        ParsedPillows.loc[len(ParsedPillows)] = ParsedPillow
    print(ParsedPillows.head())

    print(correctmatch.uniqueness(ParsedPillows.values))
    fitted_model = correctmatch.fit_model(ParsedPillows.values)
    fitted_ParsedPillows = correctmatch.sample_model(fitted_model, ParsedPillows.shape[0])
    print(correctmatch.uniqueness(fitted_ParsedPillows))


def test_adults():
    adults = pd.read_csv('adults.csv')
    adults.head()

    print(correctmatch.uniqueness(adults.values))
    fitted_model = correctmatch.fit_model(adults.values)
    fitted_adults = correctmatch.sample_model(fitted_model, adults.shape[0])
    print(correctmatch.uniqueness(fitted_adults))


if __name__ == '__main__':
    test_pillow()
