import csv
import random

def create_sets_of_question(capitals_csv, number_of_sets, number_of_questions_per_set):
    # Read capitals dict
    capitals = {}
    with open(capitals_csv, encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        next(reader)
        for row in reader:
            capitals[row[0]] = row[1]
    
    # Check no country will be repeated.
    if number_of_sets * number_of_questions_per_set > len(capitals):
        raise ValueError
    
    # Start with all capitals available.
    available_countries = list(capitals.keys())
    
    # Create `number_of_sets` files.
    for questin_set_number in range(1, number_of_sets + 1):

        # Open specific file for writing, eq. `zestaw1.csv`
        with open(f'zestaw{questin_set_number}.csv', 'w') as csvfile:

            # Start-up csv writer, by opening it and writing heading line.
            writer = csv.writer(csvfile, delimiter=';')
            writer.writerow(('Państwo','A','B','C','D'))

            # We need `number_of_questions_per_set` questions.
            for _ in range(number_of_questions_per_set):

                # Chose country from the list of available countries.
                current_country = random.choice(available_countries)
                available_countries.remove(current_country)

                # Take current country capital as a first answer.
                answers = [capitals[current_country]]

                # Extend the answers list by chosing 3 other cities.
                answers.extend(
                    random.sample(
                    # Remember to omit current capital, as it is already in the answers list
                        [capital for country, capital in capitals.items()
                         if country != current_country], 
                        3
                    )
                )

                # Shuffle answers.
                random.shuffle(answers)

                # Output the data to resulting csv file.
                writer.writerow((current_country, *answers))

if '__main__' == __name__:
    create_sets_of_question('stolice.csv', 1, 48)