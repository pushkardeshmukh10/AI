import re
# Imports the re module.
# re is used for Regular Expressions (RegEx).


def chatbot_response(user_input):
    # Defines a function that accepts user input.

    # Convert input to lowercase
    text = user_input.lower().strip()
    # lower() converts text into lowercase.
    # strip() removes extra spaces from beginning and end.

    # ---------- GREETINGS ----------
    if re.search(r"\b(hi|hello|hey|good morning|good afternoon)\b", text):
        # Searches for greeting words in user input.
        return "Hello! How can I help you?"
        # Returns greeting response.

    # ---------- NAME ----------
    elif re.search(r"\b(your name|who are you|what are you)\b", text):
        # Checks whether user asks about chatbot identity.
        return "I am a Rule-Based Chatbot created using Python."

    # ---------- HOW ARE YOU ----------
    elif re.search(r"\b(how are you|how do you feel)\b", text):
        # Checks how are you questions.
        return "I am fine. Thank you for asking!"

    # ---------- PYTHON ----------
    elif re.search(r"\b(python|python language)\b", text):
        # Searches for Python keyword.
        return "Python is a high-level, interpreted and easy-to-learn programming language."

    # ---------- JAVA ----------
    elif re.search(r"\b(java|java language)\b", text):
        # Searches for Java keyword.
        return "Java is a popular object-oriented programming language."

    # ---------- C / C++ ----------
    elif re.search(r"\b(c language|c programming|c\+\+|cpp)\b", text):
        # Checks for C or C++ keywords.
        return "C and C++ are widely used programming languages for system and application development."

    # ---------- DBMS ----------
    elif re.search(r"\b(dbms|database|sql)\b", text):
        # Searches for database-related keywords.
        return "DBMS is software used to create, manage and organize databases."

    # ---------- DATA STRUCTURES ----------
    elif re.search(r"\b(data structure|stack|queue|linked list|tree|graph)\b", text):
        # Checks for data structure-related keywords.
        return "Data structures are ways of organizing and storing data efficiently."

    # ---------- OPERATING SYSTEM ----------
    elif re.search(r"\b(operating system|os|linux|windows)\b", text):
        # Searches for operating system keywords.
        return "An operating system manages computer hardware, software and system resources."

    # ---------- COMPUTER NETWORK ----------
    elif re.search(r"\b(network|computer network|tcp|ip|internet)\b", text):
        # Checks networking-related keywords.
        return "A computer network connects devices so that they can communicate and share resources."

    # ---------- ARTIFICIAL INTELLIGENCE ----------
    elif re.search(r"\b(ai|artificial intelligence)\b", text):
        # Searches for Artificial Intelligence keywords.
        return "Artificial Intelligence enables computers to perform tasks that normally require human intelligence."

    # ---------- MACHINE LEARNING ----------
    elif re.search(r"\b(machine learning|ml)\b", text):
        # Checks for Machine Learning keywords.
        return "Machine Learning allows computers to learn patterns from data."

    # ---------- COLLEGE ----------
    elif re.search(r"\b(college|university|campus)\b", text):
        # Searches for college-related keywords.
        return "College is an important place for learning, practical work and developing technical skills."

    # ---------- EXAM ----------
    elif re.search(r"\b(exam|examination|test)\b", text):
        # Checks for exam-related words.
        return "Prepare a study schedule, revise important concepts and practice previous questions."

    # ---------- STUDY ----------
    elif re.search(r"\b(study|studying|learn|learning)\b", text):
        # Searches for study-related keywords.
        return "Regular practice and revision are good ways to improve your technical knowledge."

    # ---------- THANKS ----------
    elif re.search(r"\b(thanks|thank you|thankyou)\b", text):
        # Checks for thank-you messages.
        return "You're welcome!"

    # ---------- HELP ----------
    elif re.search(r"\b(help|help me|can you help)\b", text):
        # Checks whether user needs help.
        return "Sure! You can ask me about Python, Java, DBMS, OS, AI, ML or Data Structures."

    # ---------- GOODBYE ----------
    elif re.search(r"\b(bye|goodbye|exit|quit)\b", text):
        # Checks for goodbye keywords.
        return "Goodbye! Have a nice day."

    # ---------- UNKNOWN INPUT ----------
    else:
        # Executes when no rule matches.
        return "Sorry, I don't understand your question."


# Main program
print("=" * 50)
print("RULE-BASED CHATBOT")
print("=" * 50)
print("Chatbot: Hello! I am a simple chatbot.")
print("Chatbot: Type 'bye' to end the conversation.")
print()
# Prints an empty line.


while True:
    # Starts an infinite loop.
    # Chatbot continues until break is executed.
    user_input = input("You: ")
    # Accepts message from user.

    response = chatbot_response(user_input)
    # Calls chatbot_response() function.
    # Stores the returned response.

    print("Chatbot:", response)
    # Displays chatbot response.

    # Exit condition
    if re.search(r"\b(bye|goodbye|exit|quit)\b", user_input.lower()):
        # Checks whether user entered an exit keyword.
        break
        # Terminates the while loop.
