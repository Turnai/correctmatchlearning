import csv


def parserow(row: list):
    print(row)
    dictionary = {' Private': 0, ' Self-emp-not-inc': 1, ' Self-emp-inc': 2, ' Federal-gov': 3, ' Local-gov': 4,
                  ' State-gov': 5, ' Without-pay': 6, ' Never-worked': 7,
                  ' Bachelors': 0, ' Some-college': 1, ' 11th': 2, ' HS-grad': 3, ' Prof-school': 4, ' Assoc-acdm': 5,
                  ' Assoc-voc': 6, ' 9th': 7, ' 7th-8th': 8, ' 12th': 9, ' Masters': 10, ' 1st-4th': 11, ' 10th': 12,
                  ' Doctorate': 13, ' 5th-6th': 14, ' Preschool': 15
                  }
    parsedrow = [dictionary[i] if i in dictionary else i for i in row[:5]]
    atoirow = [int(i) for i in parsedrow]
    print(atoirow)
    return atoirow


if __name__ == '__main__':
    with open("./test.csv", "r") as f:
        with open("./output.csv", "a+") as outcsv:
            outcsv_writer = csv.writer(outcsv)
            reader = csv.reader(f)
            for row in reader:
                outcsv_writer.writerow(parserow(row))
