import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime


engine = pyttsx3.init('espeak')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', "english-us")

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("Thank you for visiting here.")


def write_data():
    import mysql.connector
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="ian297",
        database="test",
    )

    # Creating the cursor
    mycursor = mydb.cursor()

    # Taking input from the user
    n = int(input("ENTER THE NUMBER OF PERSONS TO BE VACCINATED : "))
    for i in range(n):
        print("ENTER THE DETAILS OF THE PERSON",i+1)
        Adhar_Number = input("Enter the adhar number: ")
        Name = input("Enter the name: ")
        Age = input("Enter the email: ")
        Vaccine_Type = input("Enter the vaccine type: ")

        # Creating the query using string operations
        query = "INSERT INTO persons (Adhar_Number, Name, Age, Vaccine_Type) VALUES ('{}', '{}', '{}', '{}')".format(Adhar_Number , Name, Age, Vaccine_Type)

        # Executing the query
        mycursor.execute(query)

        # Commiting the changes
        mydb.commit()

        print("Data has been inserted!!")

def display():

    # Creating a DB connection
    import mysql.connector
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="ian",
        database="test",
    )

    # Creating the cursor
    mycursor = mydb.cursor()

    # Creating the query
    query = "SELECT * FROM persons"

    # Executed the query
    mycursor.execute(query)

    # Fetched the data
    records = mycursor.fetchall()

    for record in records:
        print("\n--------------------------------")
        print(record)
        print("--------------------------------\n")

def search():
    # Creating a DB connection
    import mysql.connector
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="ian297",
        database="test",
    )

# Creating the cursor
mycursor = mydb.cursor()

# Creating the query
# query = "SELECT * FROM persons"

# Executed the query
mycursor.execute(query)

# Fetched the data
records = mycursor.fetchall()

a = input("enter adhar number to be searched ")

for record in records:
    if record[0] == a:
        print(record)




def update():
    pass


def delete():
    pass


if __name__ == "__main__":

    wishMe()
    speak("kindly type your desired option")

    while True:
        
        print("MENU  \n 1-REGISTER YOURSELF   \n 2-DISPLAY EXISING RECORDS  \n 3-SEARCH FOR A RECORD  \n 4-UPDATE OLD RECORD   \n 5-DELETE AN EXISTING RECORD  \n 6-EXIT")
        ch  = int(input("Enter Your Choice : "))
        
        if ch == 1:
            speak("alright")
            write_data()
        elif ch == 2:
            speak("Sure")
            display()
        elif ch == 3:
            speak("Okay")
            search()
        elif ch == 4:
            speak("fine")
            update()
        elif ch == 5:
            speak("done")
            delete()
        elif ch == 6:
            print("!! THANK YOU , HAVE A NICE DAY !!")
            speak("!! THANK YOU , HAVE A NICE DAY !!")
        
            break
