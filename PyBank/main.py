import csv

# This function by passing the path to the data
# will read the records and store them in a dictionary
# and return the dictionary
def load_data(path):

    # This dictionary will contain the records from the csv file
    data_dict = {}

    with open(f'{path}', 'r') as file:

        # read the content of the csv file
        csvreader = csv.reader(file)

        # read the header of the data
        header = next(csvreader)

        # looping over the records in the data
        # and add the records to the dictionary
        for index, record in enumerate(csvreader):

            # giving an index to the records in the file
            # and store them in the dictionary
            data_dict[index] = dict(zip(header, record))

    # return the dictionary containing the records in the .csv file
    return data_dict

# This function given the dictionary of the records
# will return the number of month in the records
def get_number_of_month(data_dict):

    # return the number of the records in the dictionary
    return len(data_dict)

# This function given the dictionary of the data
# summing up the profits of the records
# and return the total net profit amount
def net_total_amount(data_dict):

    # stores the net total amount
    net_amount = 0

    # Looping over the records
    for record_index in data_dict:

        # summing up the profit/loss for that month
        net_amount += int(data_dict[record_index]['Profit/Losses'])

    # return the net profit of the records over the period
    return net_amount

# This function given the dictionary of the records
# will return the average change over the period
def average_change(data_dict):

    # Get the first and last record index
    record_indexes = list(data_dict.keys())
    first_index, last_index = record_indexes[0], record_indexes[-1]

    # compute the change in this period
    total_change = int(data_dict[last_index]['Profit/Losses']) - int(data_dict[first_index]['Profit/Losses'])

    # return the average change
    return total_change / (len(data_dict) - 1)

# This function given the records will find the month
# that we had the highest increase in the profit
# with respect to its previous month
def greatest_increase(data_dict):

    # storing the record index and the value of the highest increase
    # with respect to the previous month
    max_increase_index, max_increase_value = 0, float('-inf')

    # getting the record indexes
    record_indexes = list(data_dict.keys())

    # looping over the records and compute the increase
    # for one month with respect to the previous month
    for i in range(1, len(record_indexes)):

        # get the profit of the current month and the previous one
        current_profit = int(data_dict[record_indexes[i]]['Profit/Losses'])
        previous_profit = int(data_dict[record_indexes[i - 1]]['Profit/Losses'])

        # compare the increase in the profit with respect to the highest increase
        # that we have found so far
        if (current_profit - previous_profit) > max_increase_value:

            # if this increase is higher, update the values
            max_increase_value = current_profit - previous_profit
            max_increase_index = i

    # return the month and the value of the
    # highest increase in the profit
    return (data_dict[record_indexes[max_increase_index]]['Date'], max_increase_value)

# This function given the records will find the month
# that we had the highest increase in the profit
# with respect to its previous month
def greatest_decrease(data_dict):

    # storing the record index and the value of the highest decrease
    # with respect to the previous month
    max_decrease_index, max_decrease_value = 0, float('inf')

    # getting the record indexes
    record_indexes = list(data_dict.keys())

    # looping over the records and compute the decrease
    # for one month with respect to the previous month
    for i in range(1, len(record_indexes)):

        # get the profit of the current month and the previous one
        current_profit = int(data_dict[record_indexes[i]]['Profit/Losses'])
        previous_profit = int(data_dict[record_indexes[i - 1]]['Profit/Losses'])

        # compare the decrease in the profit with respect to the highest decrease
        # that we have found so far
        if (current_profit - previous_profit) < max_decrease_value:

            # if this decrease is higher, update the values
            max_decrease_value = current_profit - previous_profit
            max_decrease_index = i

    # return the month and the value of the
    # highest decrease in the profit
    return (data_dict[record_indexes[max_decrease_index]]['Date'], max_decrease_value)


if __name__ == '__main__':

    with open('analysis/PyBank.txt', 'w') as out_file:
        # Reading the data by passing the path to the data
        Bank_dict = load_data('Resources/budget_data.csv')
        out_file.write('Financial Analysis\n')
        out_file.write('-' * 30 + '\n')
        out_file.write(f'Total Months: {get_number_of_month(Bank_dict)}\n')
        out_file.write(f'Total: ${net_total_amount(Bank_dict)}\n')
        out_file.write(f'Average Change: ${round(average_change(Bank_dict), 2)}\n')

        # get the month of the highest increase and the value
        month, value = greatest_increase(Bank_dict)
        out_file.write(f'Greatest Increase in Profits: {month} (${value})\n')

        # get the month of the highest decrease and the value
        month, value = greatest_decrease(Bank_dict)
        out_file.write(f'Greatest Decrease in Profits: {month} (${value})\n')
