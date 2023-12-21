import random


def langSelec():
  print("Please select a language to begin.")
  print("1. French")
  print("2. Haitian Creole")

  language = input("Enter the number of the language you want to select: ")
  while language != "1" and language != "2":
    print("Please enter a valid number. "
          "Please enter 1 for french and 2 for Haitian Creole.")
    language = input("Enter the number of the language you want to select: ")
  print("")
  return language


def diffLevel():
  print("Please select a difficulty level.")
  print("1. Word level")
  print("2. Sentence level")
  print("3. Paragraph level")
  DiffLevel = input("Enter the level of difficulty you want to select: ")
  while DiffLevel != "1" and DiffLevel != "2" and DiffLevel != "3":
    print("Please enter a valid number.")
    DiffLevel = input("Enter the level of difficulty you want to select: ")
  print("")
  return DiffLevel


def numQuest():
  while True:  #loop for continuous prompting
    try:
      numQ = input("Enter how many questions you would like to do (1-53): ")
      numQ = int(numQ)
      if 1 <= numQ <= 53:
        print("")
        return numQ
      else:
        print("Please enter a number between 1 and 53.")
    except ValueError:
      print("Invalid input. Please enter a number between 1 and 53.")

      
def wordTranslation(testLanguage, englishTranslate, numQuestions):
  try:
    print("You have selected Word level.")
    print("")
    print(
        "Word Vocabulary Quiz: Test your knowledge of individual words.\n "
        "You will be given a word and you have to guess the English "
        "translation. "
        "You will have 3 attempts. "
        "Each question is worth 3 points. A point will be deducted per attempt. "
        "Good luck!")
    print("")
    with open(testLanguage, "r", encoding='utf-8') as f, open(englishTranslate, "r", encoding='utf-8') as p:
      testWords = [line.strip() for line in f.readlines()]
      englishTrans = [line.strip() for line in p.readlines()]
      quizDict = dict(zip(testWords, englishTrans))

      score = 0
      wordList = list(quizDict.keys())  # Create a list of all words

      for i in range(numQuestions):
        # Check if there are enough words left to continue the quiz
        if len(wordList) == 0:
          print("Ran out of words for the quiz.")
          break

        # Randomly select a word and remove it from the list
        testPhrase = random.choice(wordList)
        wordList.remove(testPhrase)

        attempts = 3
        questionScore = 3
        while attempts > 0:
          userInput = input(
              f"Question {i + 1} What is the English translation of "
              f"'{testPhrase}'? "
              f"You have {attempts} attempts.\n")
          attempts -= 1

          if userInput.lower() == quizDict[testPhrase].lower():
            score += questionScore
            print(f"Correct! Your score is {score}.")
            print("")
            break
          else:
            questionScore -= 1
            if attempts > 0:
              print("Incorrect. Please try again.")
              print("")
            else:
              print(
                  f"Incorrect. The correct answer is '{quizDict[testPhrase]}'."
              )
              print("")

      finalScorePerc = (score / (numQuestions * 3)) * 100
      print(
          f"Your final score is {score}/{numQuestions*3} or {finalScorePerc}%."
      )
      print("")

      if finalScorePerc >= 80:
        print("Congratulations! You have passed the quiz. "
              "Thank you for playing the Word Vocabulary Quiz.")
      else:
        print("Keep trying, you need an 80% to pass! You'll get there. "
              "Thank you for playing the Word Vocabulary Quiz.")
  except FileNotFoundError:
    raise ValueError("File not found") from FileNotFoundError


def sentenceTranslation(testLanguage, englishTranslate, numQuestions):
    print("You have selected sentence level.")
    print("")
    print(
        "Sentence Vocabulary Quiz: Test your knowledge of sentences.\n "
        "You will be given a sentence and you have to guess the English "
        "translation. " 
        "You will be scored based on how many words you get correct. " 
        "You will have 3 attempts. "
        "Each question is worth 3 points. A point will be deducted per attempt. "
        "Good luck!")
    print("")
    with open(testLanguage, "r", encoding='utf-8') as f, open(englishTranslate, "r", encoding='utf-8') as p:
      testSentence = [line.strip() for line in f.readlines()]
      englishTrans = [line.strip() for line in p.readlines()]
      quizDict = dict(zip(testSentence, englishTrans))

      score = 0
      sentenceList = list(quizDict.keys())  # Create a list of all sentences

      for i in range(numQuestions):
        # Check if there are enough sentences left to continue the quiz
        if len(sentenceList) == 0:
          print("Ran out of sentences for the quiz.")
          break

        # Randomly select a word and remove it from the list
        testPhrase = random.choice(sentenceList)
        sentenceList.remove(testPhrase)

        attempts = 3
        questionScore = 3
        commonWordScore = 0
        while attempts > 0:
          userInput = input(
              f"Question {i + 1} What is the English translation of "
              f"'{testPhrase}'? "
              f"You have {attempts} attempts.\n")
          attempts -= 1
          
          correctWords = set(quizDict[testPhrase].lower().split())
          userWords = set(userInput.lower().split())

          commonWords = correctWords.intersection(userWords)
          commonWordScore = len(commonWords) / len(correctWords)
          
          if commonWordScore >= 0.8:
            score += questionScore
            print(f"Mostly Correct! Your score is {score}.")
            print("")
            print(f"The full correct answer is '{quizDict[testPhrase]}'")
            print("")
          else:
            questionScore -= 1
            if attempts > 0:
              print("Incorrect. Please try again.")
              print("")
            else:
              print(f"Incorrect. The correct answer is '{quizDict[testPhrase]}'")
              print("")

      finalScorePerc = (score / (numQuestions * 3)) * 100
      print(
          f"Your final score is {score}/{numQuestions*3} or {finalScorePerc}%.")
      print("")

      if finalScorePerc >= 80:
        print("Congratulations! You have passed the quiz. "
              "Thank you for playing the sentence Vocabulary Quiz.")
      else:
        print("Keep trying, you need an 80% to pass! You'll get there. "
              "Thank you for playing the sentence Vocabulary Quiz.")


def paragraphTranslation(testLanguage, englishTranslate, numQuestions):
  print("You have selected paragraph level. You are brave!!!")
  print("")
  print(
      "Paragraph Vocabulary Quiz: Test your knowledge of paragraphs.\n "
      "You will be given a paragraph and you have to guess the English "
      "translation. " 
      "You will be scored based on how many words you get correct per sentence translated. " 
      "You will have only 1 attempts. "
      "Each sentence is worth 3 points. Make sure you have the same number of sentences "
      "as the original prompt. If not, you will get a 0. "
      "Seperate your sentences using a PERIOD. "
      "Good luck!")
  print("")
  with open(testLanguage, "r", encoding='utf-8') as f, open(englishTranslate, "r", encoding='utf-8') as p:
    testParag = [line.strip() for line in f.readlines()]
    englishTrans = [line.strip() for line in p.readlines()]
    quizDict = dict(zip(testParag, englishTrans))

    score = 0
    numParag = 0
    paragList = list(quizDict.keys())  # Create a list of all paragraphs

  for i in range(numQuestions):
    # Check if there are enough paragraphs left to continue the quiz
    if len(paragList) == 0:
      print("Ran out of paragraphs for the quiz.")
      break
    
    # Randomly select a paragraph and remove it from the list
    testParag = random.choice(paragList)
    paragList.remove(testParag)
   
    userInput = input(f"Question {i + 1} What is the English translation of '{testParag}'?\n ")
    userSentences = userInput.lower().split(". ")
    correctSentences = quizDict[testParag].lower().split(". ")
    numParag = len(correctSentences)  # Total number of sentences in the correct paragraph

    if len(userSentences) == len(correctSentences):
      for userSentence, correctSentence in zip(userSentences, correctSentences):
        commonWords = set(userSentence.split()).intersection(set(correctSentence.split()))
        commonWordScore = len(commonWords) / len(set(correctSentence.split()))

        if commonWordScore >= 0.8:
            score += 3
        
      print(f"Mostly Correct! Your score is {score}.")
      print("")
      print(f"The correct answer is '{quizDict[testParag]}'")
      print("")
    else:
      score = 0
      print("Incorrect number of sentences for the paragraph.")
      print("")
      print(f"The correct answer is '{quizDict[testParag]}'")
      print("")      

  finalScorePerc = (score / (numParag * 3)) * 100
  print(f"Your final score is {score}/{numParag*3} or {finalScorePerc}%.")
  print("")

  if finalScorePerc >= 80:
    print("Congratulations! You have passed the quiz. "
          "Thank you for playing the paragraph Vocabulary Quiz.")
  else:
    print("Keep trying, you need an 80% to pass! You'll get there. "
          "Thank you for playing the paragraph Vocabulary Quiz.")


  
print("Welcome to the language quiz, where you can test your knowledge in "
      "french, and Haitian Creole.")
print("")
selectedLanguage = langSelec()  # Store the selected language

if selectedLanguage == "1":
  print("\nYou have selected French!!")
  print("")
  print(
      "French is a Romance Language. Since it French comes from Latin, "
      "it’s considered a Romance language. "
      "But did you know that the type of Latin French descended "
      "from is not the same as traditional Latin? "
      "It’s called Vulgar (nonstandard) Latin. Vulgar Latin was essentially "
      "informal Latin, "
      "whereas traditional Latin is what scholars and academics tend to study. "
      "All of the Romance languages are descended from Vulgar Latin.")
  print("")

if selectedLanguage == "2":
  print("\nYou have selected Haitian Creole!!")
  print("")
  print(
      "Haitian Creole is a French-based Creole language "
      "spoken by over 10 million people worldwide. "
      "Haitian Creole became one of the official languages of Haiti in 1987, "
      "with over 95% of Haitians speaking it. "
      "There are also Haitian Creole speakers in other Caribbean islands, "
      "French Guiana, France, Canada, and the United States.")
  print("")

# Difficulty Level Selection
difficultyLevel = diffLevel()  # Store the selected difficulty level

# Number of Questions Selection
numQ = numQuest()  # Store the number of questions

if selectedLanguage == "1" and difficultyLevel == "1":
  try:
      wordTranslation("FrenchWords.txt", "EnglishWords.txt", numQ)
  except FileNotFoundError:
      print("Error: The required file for the French word quiz is not found.")

elif selectedLanguage == "1" and difficultyLevel == "2":
  try:
      sentenceTranslation("FrenchSentences.txt", "EnglishSentences.txt", numQ)
  except FileNotFoundError:
      print("Error: The required file for the French sentence quiz is not found.")

elif selectedLanguage == "1" and difficultyLevel == "3":
  try:
      paragraphTranslation("FrenchParagraphs.txt", "EnglishParagraphs.txt", numQ)
  except FileNotFoundError:
      print("Error: The required file for the French sentence quiz is not found.")
  
elif selectedLanguage == "2" and difficultyLevel == "1":
  try:
      wordTranslation("HaitianCreoleWords.txt", "EnglishWords.txt", numQ)
  except FileNotFoundError:
      print("Error: The required file for the Haitian Creole word quiz is not found.")
    
elif selectedLanguage == "2" and difficultyLevel == "2":
  try:
      sentenceTranslation("HaitianCreoleSentences.txt", "EnglishSentences.txt", numQ)
  except FileNotFoundError:
      print("Error: The required file for the Haitian Creole sentence quiz is not found.")

elif selectedLanguage == "2" and difficultyLevel == "3":
  try:
      paragraphTranslation("HaitianCreoleParagraphs.txt", "EnglishParagraphs.txt", numQ)
  except FileNotFoundError:
      print("Error: The required file for the French sentence quiz is not found.")

