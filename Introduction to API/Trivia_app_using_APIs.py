import requests
import random
import html

EDUCATION_CATEGORY_ID = 9
API_URL = f"https://opentdb.com/api.php?amount=10&category={EDUCATION_CATEGORY_ID}&type=multiple"
def get_education_questions():
    responce = requests.get(API_URL)
    if responce.status_code == 200:
        data = responce.json()
        if data['response_code'] == 0 and data['results']:
            return data['results']
        return None
    
def run_quiz():
    questions = get_education_questions()
    if not questions:
        print("Failed to fetch educational questions")
        return
    score = 0
    print("Welcome to the Education Quiz!\n")
    for i, q in enumerate(questions, 1):
        questions = html.unescape(q['question'])
        correct = html.unescape(q['correct_answer'])
        incorrects = [html.unescape(a) for a in q['incorrect_answers']]
        options = incorrects +[correct]
        random.shuffle(options)
        print(f"Question {i}:\n{questions}")
        for idx, options in enumerate(options, 1):
            print(f"    {idx}. {options}")

        while True:
            try:
                choice = int(input("\nYour answer (1-4): "))
                if 1 <= choice <=4:
                    break
            except ValueError:
                pass
            print("Invalid input. Please enter a number between 1 and 4 to answer the question")
        
        if options[choice-1] == correct:
            print("✅Correct! Plus 1 point!\n")
            score += 1
        else:
            print(f"❌ Incorrect!!! Correct answer: {correct}\n")

    print(f"Final Scaore: {score}/{len(questions)}")
    print(f"Percentage: {score/len(questions)*100:.1f}%")
if __name__ == "__main__":
    run_quiz()