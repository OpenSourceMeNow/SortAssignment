'''
=================================================================
written by..: Bryan Munera
=================================================================
'''


def main():
    examScores = []

    # Infinite loop to display menu and take user input
    while True:
        displayMenu()
        choice = input("Please select an option: ")

        # Option 1: Get one exam score
        if choice == "1":
            score = getOneExamScore()
            examScores.append(score)
            print("Score added:", score)

        # Option 2: Get exam scores until user enters -999
        elif choice == "2":
            getExamScoresUntilStop(examScores)

        # Option 3: Display all exam scores entered
        elif choice == "3":
            sub_choice = input("Choose an option (a/b): ")
            if sub_choice.lower() == "a":
                displayExamScores(examScores, reverse=True)
            elif sub_choice.lower() == "b":
                displayExamScores(examScores)
            else:
                print("Invalid option. Please choose 'a' or 'b'.")

        # Option 4: Display exam statistics
        elif choice == "4":
            displayExamStatistics(examScores)

        # Option 5: Adjust all exam scores
        elif choice == "5":
            adjustAllExamScores(examScores)
            print("All exam scores adjusted.")

        # Option 6: Remove all F grades from the list
        elif choice == "6":
            removeAllFGrades(examScores)
            print("All F grades removed.")

        # Option 7: Quit the program
        elif choice == "7":
            print("Quitting the program.")
            break
        else:
            print("Invalid option. Please choose a valid number from the menu.")


# Function to display the main menu
def displayMenu():
    print("                  MAIN MENU")
    print("1. Get one Exam Score")
    print("2. Get exam scores until the user enters -999")
    print("3. Display All Exam Scores Entered")
    print("                  a. From Highest to Lowest")
    print("                  b. From Lowest to Highest")
    print("4. Display Exam Statistics")
    print("5. Adjust all Exam Scores")
    print("6. Remove all F grades from the list")
    print("7. Quit the Program")

# Function to get one exam score from the user
def getOneExamScore():
    while True:
        try:
            score = float(input("Enter an exam score between 0 and 100: "))
            if 0 <= score <= 100:
                return score
            else:
                print("Invalid input. Please enter a number between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 100.")

# Function to get exam scores from the user until they enter -999
def getExamScoresUntilStop(examScores):
    while True:
        try:
            score = float(input("Enter an exam score between 0 and 100 (-999 to stop): "))
            if 0 <= score <= 100:
                examScores.append(score)
            elif score == -999:
                break
            else:
                print("Invalid input. Please enter a number between 0 and 100 or -999 to stop.")
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 100 or -999 to stop.")

# Function to get letter grade based on a score
def getLetterGrade(score):
    if 90 <= score <= 100:
        return 'A'
    elif 80 <= score <= 89:
        return 'B'
    elif 70 <= score <= 79:
        return 'C'
    elif 60 <= score <= 69:
        return 'D'
    else:
        return 'F'

# Function to display exam scores in either ascending or descending order
def displayExamScores(examScores, reverse=False):
    sortedScores = sorted(examScores, reverse=reverse)
    for score in sortedScores:
        print(f"Score: {score} - Grade: {getLetterGrade(score)}")

# Function to display exam statistics
def displayExamStatistics(examScores):
    if len(examScores) == 0:
        print("No exam scores entered yet.")
        return

    highestScore = max(examScores)
    lowestScore = min(examScores)
    averageScore = sum(examScores) / len(examScores)

    gradeCount = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}
    for score in examScores:
        grade = getLetterGrade(score)
        gradeCount[grade] += 1

    print("Number of scores entered:", len(examScores))
    print(f"Highest score: {highestScore} - Grade: {getLetterGrade(highestScore)}")
    print(f"Lowest score: {lowestScore} - Grade: {getLetterGrade(lowestScore)}")
    print("Average score:", round(averageScore, 2))
    print("Grade count:")
    for grade, count in gradeCount.items():
        print(f"{grade}: {count}")

# Function to adjust all exam scores
def adjustAllExamScores(examScores):
    for i, score in enumerate(examScores):
        examScores[i] = max(0, score - 5)

# Function to remove a F grades
def removeAllFGrades(examScores):
    examScores[:] = [score for score in examScores if getLetterGrade(score) != 'F']

main()

