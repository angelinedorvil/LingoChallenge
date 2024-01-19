import LingoChallengeFunctions

def main():
    print("Welcome to the language quiz, where you can test your knowledge in selected languages")
    print("")
    selected_language = LingoChallengeFunctions.langSelec()  # Store the selected language

    LingoChallengeFunctions.langInfo(selected_language)  # display information of language selected

    # Difficulty Level Selection
    difficultyLevel = LingoChallengeFunctions.diffLevel()  # Store the selected difficulty level

    # Number of Questions Selection
    numQ = LingoChallengeFunctions.numQuest()  # Store the number of questions

    # getting test items based on user selection
    LingoChallengeFunctions.testSelec(selected_language, difficultyLevel, numQ)

if __name__ == "__main__":
    main()
