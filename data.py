import csv

def load_dataset(file_path):
    data = []
    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        print(f"CSV Header: {reader.fieldnames}")
        for row in reader:
            data.append(row)
    return data

def find_min_max_life_expectancy(data):
    min_value = float('inf')
    max_value = float('-inf')
    min_country = ''
    max_country = ''
    year_min = ''
    year_max = ''

    for entry in data:
        life_expectancy = float(entry['Life expectancy (years)'])
        if life_expectancy < min_value:
            min_value = life_expectancy
            min_country = entry['Entity']
            year_min = entry['Year']
        if life_expectancy > max_value:
            max_value = life_expectancy
            max_country = entry['Entity']
            year_max = entry['Year']

    return min_value, min_country, year_min, max_value, max_country, year_max

def filter_by_year(data, year):
    return [entry for entry in data if entry['Year'] == year]

def calculate_average(data):
    total_life_expectancy = sum(float(entry['Life expectancy (years)']) for entry in data)
    return total_life_expectancy / len(data) if len(data) > 0 else 0

def find_min_max_for_year(data):
    min_value = float('inf')
    max_value = float('-inf')
    min_country = ''
    max_country = ''
    for entry in data:
        life_expectancy = float(entry['Life expectancy (years)'])
        if life_expectancy < min_value:
            min_value = life_expectancy
            min_country = entry['Entity']
        if life_expectancy > max_value:
            max_value = life_expectancy
            max_country = entry['Entity']
    return min_value, min_country, max_value, max_country

def find_largest_drop(data):
    largest_drop = 0
    year_with_largest_drop = ''
    country_with_largest_drop = ''

    for i in range(1, len(data)):
        current_life_expectancy = float(data[i]['Life expectancy (years)'])
        previous_life_expectancy = float(data[i - 1]['Life expectancy (years)'])
        drop = previous_life_expectancy - current_life_expectancy

        if drop > largest_drop:
            largest_drop = drop
            year_with_largest_drop = data[i]['Year']
            country_with_largest_drop = data[i]['Entity']

    return largest_drop, year_with_largest_drop, country_with_largest_drop

def main():
    file_path = 'life-expectancy.csv'
    dataset = load_dataset(file_path)

    overall_min, min_country, year_min, overall_max, max_country, year_max = find_min_max_life_expectancy(dataset)
    print(f"The overall min life expectancy is: {overall_min} from {min_country} in {year_min}")
    print(f"The overall max life expectancy is: {overall_max} from {max_country} in {year_max}")

    year_of_interest = input("Enter the year of interest: ")

    data_for_year = filter_by_year(dataset, year_of_interest)

    if data_for_year:
        min_value, min_country, max_value, max_country = find_min_max_for_year(data_for_year)

        print(f"\nFor the year {year_of_interest}:")
        print(f"The average life expectancy across all countries was: {calculate_average(data_for_year)}")
        print(f"The min life expectancy was in {min_country} with {min_value}")
        print(f"The max life expectancy was in {max_country} with {max_value}")
    else:
        print(f"No data available for the year {year_of_interest}")

    largest_drop, year_with_largest_drop, country_with_largest_drop = find_largest_drop(dataset)
    print(f"\nThe largest drop in life expectancy occurred in {year_with_largest_drop} in {country_with_largest_drop} with a drop of {largest_drop} years.")

if __name__ == "__main__":
    main()
