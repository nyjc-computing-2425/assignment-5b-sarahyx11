def read_csv(filename):
  '''
  take in string filename which is name of CSV file
  read CSV data stored in file name
  returns list of headers and nested list containing the data
  '''
  data = []
  with open(filename, "r") as file:
    header = file.readline()
    header = header.split(",")
    for line in file:
      line = line.split(",")
      line[0] = int(line[0])
      line[3] = int(line[3])
      data.append(line)

  return header, data


def filter_gender(enrolment_by_age, sex):
  '''
  takes in list of records (enrolment_by_age) and string (sex)
  returns a list of records where value in the sex colum matches string sex
  sex column is excluded in returned records
  '''
  records = []
  for each in enrolment_by_age:
    hold = each[::]
    if hold[2] == sex:
      hold.remove(hold[2])
      records.append(hold)
  return records

def sum_by_year(enrolment_data):
  '''
  takes in list of records (enrolment_data)
  return result as a list of lists
  each inner list comprises of two integers, year and total_enrolment that year
  '''
  year_data = []
  data = enrolment_data
  for each in data:
    year = [each[0]]
    if year not in year_data:
      year_data.append(year)
    else:
      continue

  year_sum = []
  count = 0
  for year in year_data:
    years = year[::]
    years.append(0)
    for index in range(len(data) - count):
      if data[count][0] == int(years[0]):
        years[1] = years[1] + data[count][2]
        count += 1
        
      else:
        break
    year_sum.append(years)
  return year_sum

def write_csv(filename, header, data):
  '''
  take in filename, header and data
  writes header and data into file with filename
  return number of lines written
  '''
  with open(filename, "w") as file:
    file.writelines(header)
    count = 1
    for list in data:
      list = map(str, list)
      file.writelines(list)
      count += 1

  return (count)



