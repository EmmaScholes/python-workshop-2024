import pandas

#Convert CSV file to Dataframe
csvFile = pandas.read_csv('./data/timesheet_data.csv')

#Rename CSV file columns
csvFile.rename(columns={'Original Entry Date': 'DATE'}, inplace=True)
csvFile.rename(columns={'Cost Reg': 'COST'}, inplace=True)
csvFile.rename(columns={'Quantity Reg': 'HOURS'}, inplace=True)

#Cut columns
results_csv = csvFile[['DATE', 'Employee Name', 'COST', 'HOURS']]


#filter hours under 8
results_csv = results_csv[csvFile['HOURS'] < 8]


#Saving to CSV file
results_csv.to_csv('Results.csv')


print(results_csv.head())
