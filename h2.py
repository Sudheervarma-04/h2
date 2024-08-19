import random

# Complete dictionary with all Indian states and union territories
states_and_capitals = {
    'Andhra Pradesh': 'Amaravati',
    'Arunachal Pradesh': 'Itanagar',
    'Assam': 'Dispur',
    'Bihar': 'Patna',
    'Chhattisgarh': 'Raipur',
    'Goa': 'Panaji',
    'Gujarat': 'Gandhinagar',
    'Haryana': 'Chandigarh',
    'Himachal Pradesh': 'Shimla',
    'Jharkhand': 'Ranchi',
    'Karnataka': 'Bengaluru',
    'Kerala': 'Thiruvananthapuram',
    'Madhya Pradesh': 'Bhopal',
    'Maharashtra': 'Mumbai',
    'Manipur': 'Imphal',
    'Meghalaya': 'Shillong',
    'Mizoram': 'Aizawl',
    'Nagaland': 'Kohima',
    'Odisha': 'Bhubaneswar',
    'Punjab': 'Chandigarh',
    'Rajasthan': 'Jaipur',
    'Sikkim': 'Gangtok',
    'Tamil Nadu': 'Chennai',
    'Telangana': 'Hyderabad',
    'Tripura': 'Agartala',
    'Uttar Pradesh': 'Lucknow',
    'Uttarakhand': 'Dehradun',
    'West Bengal': 'Kolkata',
    'Andaman and Nicobar Islands': 'Port Blair',
    'Chandigarh (Union Territory)': 'Chandigarh',
    'Dadra and Nagar Haveli and Daman and Diu': 'Daman',
    'Lakshadweep': 'Kavaratti',
    'Delhi': 'New Delhi',
    'Puducherry': 'Puducherry',
    'Ladakh': 'Leh',
    'Jammu and Kashmir': 'Srinagar (summer), Jammu (winter)'
}

def conduct_quiz(num_questions):
    # Shuffle the states and union territories
    states = list(states_and_capitals.keys())
    random.shuffle(states)

    score = 0

    # Conduct the quiz
    for i in range(num_questions):
        state = states[i]
        print(f"Question {i+1}: What is the capital of {state}?")
        answer = input("Your answer: ").strip()

        if answer.lower() == states_and_capitals[state].lower():
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {states_and_capitals[state]}.\n")

    # Calculate grade based on score
    grade = calculate_grade(score, num_questions)
    print(f"Quiz finished! Your total score is {score} out of {num_questions}.")
    print(f"Your grade is: {grade}")

def calculate_grade(score, total_questions):
    percentage = (score / total_questions) * 100

    if percentage >= 90:
        return 'A'
    elif percentage >= 75:
        return 'B'
    elif percentage >= 50:
        return 'C'
    else:
        return 'D'

if __name__ == "__main__":
    print("Welcome to the States and Capitals Quiz!")
    num_questions = int(input("Enter the number of questions you want in the quiz: "))

    if num_questions > len(states_and_capitals):
        print(f"Only {len(states_and_capitals)} questions are available. The quiz will contain {len(states_and_capitals)} questions.")
        num_questions = len(states_and_capitals)

    conduct_quiz(num_questions)
