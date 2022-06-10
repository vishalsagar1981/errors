file = open("user_data.csv","r")
lines = file.readlines()
file.close()
lines = [line.strip() for line in lines[1:]]
file_to_write = open("students_uni.txt","w")
for line in lines:
    #print(line)
    person_data = line.split(',')
    #print(person_data)
    name = person_data[0]
    age = person_data[1]
    degree = person_data[2]
    uni = person_data[3]
    print(f"{name} is {age} years Old and studying {degree} at {uni} ")
    sample_csv_value = ','.join([name,age,degree,uni])
    print(sample_csv_value)
    file_to_write.write(sample_csv_value)
    file_to_write.write("\n")

file_to_write.close()