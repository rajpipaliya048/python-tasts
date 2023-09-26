import datetime

def get_time_from_user():
    try:
        time_str = input("Enter a time in HH:MM:SS format: ")
        time_parts = time_str.split(":")
        
        if len(time_parts) != 3:
            raise ValueError("Invalid input. Use HH:MM:SS format.")
        
        hours, minutes, seconds = map(int, time_parts)
        return datetime.timedelta(hours=hours, minutes=minutes, seconds=seconds)
    except ValueError as e:
        print(f"Error: {e}")

def increase_time(time, unit, value):
    if unit == "seconds":
        return time + datetime.timedelta(seconds=value)
    elif unit == "minutes":
        return time + datetime.timedelta(minutes=value)
    elif unit == "hours":
        return time + datetime.timedelta(hours=value)
    else:
        raise ValueError("Invalid unit. Use 'seconds', 'minutes', or 'hours'.")

def main():
    time1 = get_time_from_user()
    if time1 is None:
        return
    
    operation = input("Choose operation\n 1. increase \n 2. add \n 3. difference: ").strip()
    
    if operation == "1":
        unit = input("Enter unit (seconds/minutes/hours): ").strip().lower()
        value = int(input("Enter value: "))
        result = increase_time(time1, unit, value)
        print(f"Result: {result}")
    
    elif operation == "2":
        time2 = get_time_from_user()
        if time2 is not None:
            result = time1 + time2
            print(f"Result: {result}")
    
    elif operation == "3":
        time2 = get_time_from_user()
        if time2 is not None:
            result = time1 - time2
            print(f"Result: {result}")
    
    else:
        print("Invalid operation. Use '1', '2', or '3'.")

main()
