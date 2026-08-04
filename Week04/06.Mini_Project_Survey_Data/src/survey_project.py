def run_survey():
    city = input('What is your favourite Australian city? ')
    with open('survey_results.txt', 'a') as file:
        file.write(city + '\n')

if __name__ == '__main__':
    pass # run_survey()
