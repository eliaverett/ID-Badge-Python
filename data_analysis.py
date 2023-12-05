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
    
    for entry in data:
        life_expectancy = float(entry['Life expectancy (years)'])
        min_value = min(min_value, life_expectancy)
        max_value = max(max_value, life_expectancy)
    
    return min_value, max_value

def filter_by_year(data, year):
    return [entry for entry in data if entry['Year'] == year]

def calculate_average(data):
    total_life_expectancy = sum(float(entry['Life expectancy (years)']) for entry in data)
    return total_life_expectancy / len(data)

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

def main():
    file_path = 'life-expectancy.csv'
    dataset = load_dataset(file_path)

    overall_min, overall_max = find_min_max_life_expectancy(dataset)
    print(f"The overall min life expectancy is: {overall_min}")
    print(f"The overall max life expectancy is: {overall_max}")


    year_of_interest = input("Enter the year of interest: ")


    data_for_year = filter_by_year(dataset, year_of_interest)

    min_value, min_country, max_value, max_country = find_min_max_for_year(data_for_year)

    print(f"\nFor the year {year_of_interest}:")
    print(f"The average life expectancy across all countries was: {calculate_average(data_for_year)}")
    print(f"The min life expectancy was in {min_country} with {min_value}")
    print(f"The max life expectancy was in {max_country} with {max_value}")

if __name__ == "__main__":
    main()
