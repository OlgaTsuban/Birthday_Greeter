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
    for user in users:
        birthday = user['birthday']
        name = user['name']
        if birthday.year > current_data.year:
            print(f"The birth year {birthday.year} is immposible")
            continue
        if birthday.month == current_data.month:
            if birthday.day <= current_data.day + 7 and birthday.day >= (current_data).day:
                try_day = datetime.datetime(current_data.year,birthday.month,birthday.day)
                week_day = try_day.strftime('%A') if try_day.strftime('%A') not in ('Sunday' ,'Saturday') else 'Monday'
                birthday_dict[week_day].append(name)
                
        if birthday.month - current_data.month == 1:
            if birthday.day <= (current_data + datetime.timedelta(days=7)).day:
                try_day = datetime.datetime(current_data.year,birthday.month,birthday.day)
                week_day = try_day.strftime('%A') if try_day.strftime('%A') not in ('Sunday' ,'Saturday') else 'Monday'
                birthday_dict[week_day].append(name)
                
    #print the day and name(names)
    print_result(birthday_dict)

    return birthday_dict


#print the result (days and name)
def print_result(birthday_dict):
    for day, names in birthday_dict.items():
        if names:
            print(f"{day}: {', '.join(names)}")

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
