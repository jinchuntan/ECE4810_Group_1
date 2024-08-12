import requests

# Define the channel ID and API key
channel_id_1 = '2614232' #mine
channel_id_2 = '2614230' #jw
channel_id_3 = '2614224' #yuchen
channel_id_4     = '2614220'#nigel
api_key_1 = 'IG9E4CJY8MNFRZTM'  # mine
api_key_2 = 'F9MCAETDMGOH7T9W' #jw
api_key_3 = '1HWF4MSNPCXA57QT' #yuchen
api_key_4 = '7GGTGRKDWUULIGGZ' #nigel
field_numbers = [1]  # List of field numbers
results = 1
flag_velocity_13 = 0
flag_velocity_24 = 0

# Define Parameter
Distance13 = 16.5 #in cm
Distance24 = 16.5 # in cm, subjected to changes

Threshold1 = 25
Threshold2 = 25
Threshold3 = 25
Threshold4 = 25

# Construct the URLs for each field
url1 = [f"https://api.thingspeak.com/channels/{channel_id_1}/fields/{field_number}.json?api_key={api_key_1}&results={results}" for field_number in field_numbers]
url2 = [f"https://api.thingspeak.com/channels/{channel_id_2}/fields/{field_number}.json?api_key={api_key_2}&results={results}" for field_number in field_numbers]
url3 = [f"https://api.thingspeak.com/channels/{channel_id_3}/fields/{field_number}.json?api_key={api_key_3}&results={results}" for field_number in field_numbers]
url4 = [f"https://api.thingspeak.com/channels/{channel_id_4}/fields/{field_number}.json?api_key={api_key_4}&results={results}" for field_number in field_numbers]

# Send the GET requests for each field
while True:
    response1 = requests.get(url1[0])
    response2 = requests.get(url2[0])
    response3 = requests.get(url3[0])
    response4 = requests.get(url4[0])

    # Parse the JSON responses for each field
    data1 = response1.json()
    data2 = response2.json()
    data3 = response3.json()
    data4 = response4.json()

    # Extract the time and distance data for channel 1
    time_data1 = [entry['created_at'] for entry in data1['feeds']]
    distance_data_1 = [entry[f'field1'] for entry in data1['feeds']]
    minutes1 = [int(entry.split(':')[1]) for entry in time_data1 if entry.split(':')[1].isdigit()]
    seconds1 = [int(entry.split(':')[2][:-1]) for entry in time_data1 if entry.split(':')[2][:-1].isdigit()]
    time_in_seconds1 = [minutes1[i] * 60 + seconds1[i] for i in range(len(minutes1))]
    time_in_seconds_1 = time_in_seconds1[-1]
    distance_1 = float(distance_data_1[-1])

    # Extract the time and distance data for channel 2
    time_data2 = [entry['created_at'] for entry in data2['feeds']]
    distance_data_2 = [entry[f'field1'] for entry in data2['feeds']]
    minutes2 = [int(entry.split(':')[1]) for entry in time_data2 if entry.split(':')[1].isdigit()]
    seconds2 = [int(entry.split(':')[2][:-1]) for entry in time_data2 if entry.split(':')[2][:-1].isdigit()]
    time_in_seconds2 = [minutes2[i] * 60 + seconds2[i] for i in range(len(minutes2))]
    time_in_seconds_2 = time_in_seconds2[-1]
    distance_2 = float(distance_data_2[-1])

    # Extract the time and distance data for channel 3
    time_data3 = [entry['created_at'] for entry in data3['feeds']]
    distance_data_3 = [entry[f'field1'] for entry in data3['feeds']]
    minutes3 = [int(entry.split(':')[1]) for entry in time_data3 if entry.split(':')[1].isdigit()]
    seconds3 = [int(entry.split(':')[2][:-1]) for entry in time_data3 if entry.split(':')[2][:-1].isdigit()]
    time_in_seconds3 = [minutes3[i] * 60 + seconds3[i] for i in range(len(minutes3))]
    time_in_seconds_3 = time_in_seconds3[-1]
    distance_3 = float(distance_data_3[-1])

    # Extract the time and distance data for channel 4
    time_data4 = [entry['created_at'] for entry in data4['feeds']]
    distance_data_4 = [entry[f'field1'] for entry in data4['feeds']]
    minutes4 = [int(entry.split(':')[1]) for entry in time_data4 if entry.split(':')[1].isdigit()]
    seconds4 = [int(entry.split(':')[2][:-1]) for entry in time_data4 if entry.split(':')[2][:-1].isdigit()]
    time_in_seconds4 = [minutes4[i] * 60 + seconds4[i] for i in range(len(minutes4))]
    time_in_seconds_4 = time_in_seconds4[-1]
    distance_4 = float(distance_data_4[-1])

    # Loop through distance_1, distance_2, distance_3, and distance_4
    for i in range(len(distance_data_1)):
        # Check if the entry is None
        if distance_data_1[i] is None:
            distance_data_1[i] = 100
        else:
            distance_data_1[i] = float(distance_data_1[i])

        if distance_data_2[i] is None:
            distance_data_2[i] = 100
        else:
            distance_data_2[i] = float(distance_data_2[i])

        if distance_data_3[i] is None:
            distance_data_3[i] = 100
        else:
            distance_data_3[i] = float(distance_data_3[i])

        if distance_data_4[i] is None:
            distance_data_4[i] = 100
        else:
            distance_data_4[i] = float(distance_data_4[i])

    if distance_1 > 0 and distance_3 > 0:
        flag_velocity_13 = 1


    # Calculating Velocity12
    if flag_velocity_13 == 1:
        try:
            # Calculate the difference in time between time_in_seconds_1 and time_in_seconds_3
            time_difference13 = abs(time_in_seconds_1 - time_in_seconds_3)
            # Calculate the velocity using the formula velocity = distance / time
            velocity13 = Distance13 / time_difference13
            # Print the calculated velocity
            print("Velocity between UDM 1 and 3:", velocity13 ,"cm/s")
            # upload velocity to thingspeak!!!!!!!!!!!
            flag_velocity_13 = 0

        except:
            if time_in_seconds_1 is None:
                print("Entry 1 not found")
            elif time_in_seconds_3 is None:
                print("Entry 3 not found")
            else:
                print("No entry found")

    # Calculating Velocity24
    if flag_velocity_24 == 1:
        try:
            # Calculate the difference in time between time_in_seconds_2 and time_in_seconds_4
            time_difference24 = abs(time_in_seconds_2 - time_in_seconds_4)
            # Calculate the velocity using the formula velocity = distance / time
            velocity24 = Distance24 / time_difference24
            # Print the calculated velocity
            print("Velocity between UDM 2 and 4:", velocity24 ,"cm/s")
            # upload velocity to thingspeak!!!!!!!!!!!
            flag_velocity_24 = 0

        except:
            if time_in_seconds_2 is None:
                print("Entry 2 not found")
            elif time_in_seconds_4 is None:
                print("Entry 4 not found")
            else:
                print("No entry found")

    threshold_steer = 5
    # Determine if the vehicle is going straight or steering left/right
    if distance_data_1[0] > distance_data_3[0] and distance_data_1[0] - distance_data_3[0] > threshold_steer:
        print("Vehicle is steering left")
    elif distance_data_1[0] < distance_data_3[0] and distance_data_3[0] - distance_data_1[0] > threshold_steer:
        print("Vehicle is steering right")
    else:
        print("Vehicle is going straight")