import csv

def read_csv(file_path):
    try:
        with open(file_path, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = [row for row in csv_reader]
            return data
    except FileNotFoundError:
        print("CSV file not found.")
    except Exception as e:
        print(f"Error reading CSV: {str(e)}")

def read_user_data(file_path):
    try:
        with open(file_path, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = [row for row in csv_reader]
            return data
    except FileNotFoundError:
        print("CSV file not found.")
    except Exception as e:
        print(f"Error reading CSV: {str(e)}")

def conduct_exam(questions, user_data):
    score = 0
    for question in questions:
        print(question['question'])
        user_answer = input("Your answer: ").strip()

        if user_answer.lower() == question['correct_answer'].lower():
            score += 1

    return score

if __name__ == "__main__":

    questions = read_csv('/media/raj/Doom/iLearn/python_tasks/task6/questions.csv')
    users = read_user_data('/media/raj/Doom/iLearn/python_tasks/task6/users.csv')

    if questions and users:
        print("Welcome to the Exam!")
        username = input("Enter your username: ").strip()
        user_data = next((user for user in users if user['username'] == username), None)
        if user_data:
            print(f"Hello, {username}!")
            user_score = conduct_exam(questions, user_data)
            print(f"Your score: {user_score}/{len(questions)}")
        else:
            print("User not found.")