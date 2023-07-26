import datetime

def get_birthdays_per_week(users):
    #define the current date
    current_data = datetime.datetime.now()
    
    #this dictionary will contain the result of the program
    birthday_dict = {
    "Monday": [],
    "Tuesday": [],
    "Wednesday": [],
    "Thursday": [],
    "Friday": []
    }

    #check each birthday of the list users
    for i in users:
        if i["birthday"].year > current_data.year:
            print(f"The birth year {i['birthday'].year} is immposible") 
        else:
            if i["birthday"].month == current_data.month:
                if i["birthday"].day <= current_data.day + 7 and i["birthday"].day >= (current_data).day:
                    if i["birthday"].strftime('%A') == "Sunday" or i["birthday"].strftime('%A') == "Saturday":
                        birthday_dict["Monday"].append(i["name"])
                    else:
                        birthday_dict[i["birthday"].strftime('%A')].append(i["name"])
            if i["birthday"].month - current_data.month == 1:
                if i["birthday"].day <= (current_data + datetime.timedelta(days=7)).day:
                    if datetime.datetime(current_data.year,i["birthday"].month,i["birthday"].day) .strftime('%A') in ["Sunday" ,"Saturday"]:
                        birthday_dict["Monday"].append(i["name"])
                    else:
                        birthday_dict[datetime.datetime(current_data.year, i["birthday"].month,i["birthday"].day).strftime('%A')].append(i["name"])
    #print the day and name(names)
    for day, names in birthday_dict.items():
        if names:
            print(f"{day}: {', '.join(names)}")
    return birthday_dict

if __name__ == '__main__':
    #list with name and birthday
    users = [
    {"name": "John", "birthday": datetime.datetime(3990, 8, 1)},
    {"name": "Alice", "birthday": datetime.datetime(1985, 8, 2)},
    {"name": "Bob", "birthday": datetime.datetime(1995, 9, 30)},
    {"name": "Emma", "birthday": datetime.datetime(1998, 7, 30)},
    {"name": "Michael", "birthday": datetime.datetime(1982, 6, 28)},
    ]

    #call the function to get the result
    get_birthdays_per_week(users)