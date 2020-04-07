def get_report(path):
    """
    Creates a report of the file specified as argument.

    :param path: path to file from which the report should be created (string)
    :return: the report (string)
    """
    missing_count , numbers , words  = _read_file(path)

    report = _make_report(missing_count, numbers, words)
    return report

def _read_file(path):
    """
    Reads and returns the data from the file specified as argument.

    :param path: path to the file to be read.
    :return: a tuple containing
    1. the number of empty lines (int)
    2. numeric values (list of floats)
    3. non-numeric values (list of strings)

    """
    with open(path, 'r') as data_file:
        lines = data_file.readlines()

    empty_lines = 0
    words = []
    numbers = []
    for line in lines :
        line = line.strip()
        if line == '':
            empty_lines = empty_lines + 1
        else:
            is_number = False
            try:
                number = float(line)
                is_number = True
            except Exception:
                pass

            if is_number:
                numbers.append(number)
            else:
                words.append(line)
    return empty_lines, numbers, words

def _make_report(missing_values, numbers, words):
    """
    Creates and a report based on data given as arguments.

    :param missing_values: number of empty lines (int)
    :param numbers: numeric values (list of floats)
    :param words: non numeric values (list of strings)
    :return: the generated report (string)
    """
    max_value = _get_max_value(numbers)
    lower_case_words = _words_to_lowercase(words)
    most_common_info = _get_most_common_words(lower_case_words)
    most_common_words , most_common_count = most_common_info

    most_common_str = ', '.join(most_common_words)

    report = ('missing values: {}\n'
              'highest number: {}\n'
              'most common words: {}\n'
              'occurrences of most common: {}\n'
              '#####\n'
              'numbers: {}\n'
              'words: {}').format(missing_values, max_value, most_common_str,
                                  most_common_count, numbers, lower_case_words)

    return report

def _words_to_lowercase(words):
    """
    :param words: words to be converted (list of strings)
    :return: lowercased words (list of strings)
    """
    lowercased = []
    for word in words :
        lowercased.append(word.lower())
    return lowercased

def _get_max_value(numbers):
    """
    Returns the greatest value of the list given as argument.

    :param numbers: numbers (list of numeric values)
    :return: greatest value of numbers, None if numbers is an empty list
    """
    if not len(numbers):
        max_value = None
    else :
        max_value = max(numbers)
    return max_value



def _get_most_common_words(words):
    """
    Finds the most common words in a list of words.
    If there are multiple different words with the same amount of occurrences,
    they are all included in the return value sorted alphabetically.
    In addition to returning the most common words, the return value
    includes also the count of occurrences of the most common words.

    :param words: list of words (list of strings)
    :return: a tuple containing:
    1. most common words (list of strings)
    2. the count of occurrences of the most common words (int)
    """
    word_counts = {}
    for valeur in words:
        if valeur not in word_counts.keys():
            word_counts[valeur] = 1
        else:
            word_counts[valeur] += 1

    max_count = max(word_counts.values())

    most_common_words =[word for word in word_counts.keys() if word_counts[word] == max_count]

    return most_common_words, max_count









