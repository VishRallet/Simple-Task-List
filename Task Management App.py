import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import random

def save_tasks():
    tasks.to_csv('tasks.csv', index=False)

try:
    tasks = pd.read_csv('tasks.csv')
except FileNotFoundError:
    tasks = pd.DataFrame(columns=['description', 'priority'])
    save_tasks()

def add_task(description, priority):
    global tasks
    new_task = pd.DataFrame({'description': [description], 'priority': [priority]})
    tasks = pd.concat([tasks, new_task], ignore_index=True)
    save_tasks()
    train_model()

def remove_task(description):
    global tasks
    if description in tasks['description'].values:
        tasks = tasks[tasks['description'] != description]
        save_tasks()
        print("Task removed successfully.")
        train_model()
    else:
        print(f"No task found with description '{description}'.")

def list_tasks():
    if tasks.empty:
        print("No tasks available.")
    else:
        print("Tasks:")
        print("{:<5} {:<30} {:<10}".format("Sl No", "Description", "Priority"))
        print("="*46)
        for index, row in tasks.iterrows():
            print("{:<5} {:<30} {:<10}".format(index + 1, row['description'], row['priority']))

def train_model():
    global model
    if tasks.empty or tasks['description'].str.strip().eq('').all():
        return
    valid_tasks = tasks[tasks['description'].str.strip() != '']
    if valid_tasks.shape[0] < 2:
        return
    try:
        vectorizer = CountVectorizer(stop_words='english')
        clf = MultinomialNB()
        model = make_pipeline(vectorizer, clf)
        model.fit(valid_tasks['description'], valid_tasks['priority'])
    except ValueError as e:
        print(f"Error training model: {e}")

def recommend_task():
    global model
    if 'model' not in globals():
        print("Please add tasks and train the model first.")
        return
    if not tasks.empty:
        predicted_priorities = model.predict(tasks['description'])
        tasks['predicted_priority'] = predicted_priorities
        high_priority_tasks = tasks[tasks['predicted_priority'] == 'High']
        if not high_priority_tasks.empty:
            random_task = random.choice(high_priority_tasks['description'].values)
            print(f"Recommended task: {random_task} - Predicted Priority: High")
        else:
            print("No high-priority tasks available for recommendation.")
    else:
        print("No tasks available for recommendations.")

train_model()

while True:
    print("\nTask Management App")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. List Tasks")
    print("4. Recommend Task")
    print("5. Exit")
    choice = input("Select an option: ")
    if choice == "1":
        description = input("Enter task description: ")
        while True:
            priority = input("Enter task priority (Low/Medium/High): ").capitalize()
            if priority in ["High", "Medium", "Low"]:
                break
            else:
                print("Invalid priority! Please enter High, Medium, or Low.")
        add_task(description, priority)
        print("Task added successfully.")
    elif choice == "2":
        description = input("Enter task description to remove: ")
        remove_task(description)
    elif choice == "3":
        list_tasks()
    elif choice == "4":
        recommend_task()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid option. Please select a valid option.")
