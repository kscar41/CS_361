from tkinter import *
from tkinter import messagebox

def saveInfo():
    bookTitleInfo = bookTitle.get()
    authorNameInfo = authorName.get()
    genreTypeInfo = genreType.get()

    print(bookTitleInfo, authorNameInfo, genreTypeInfo)

    file = open("books.txt", "a+")
    file.write("Book Title: " + bookTitleInfo + "\n")
    file.write("Authors Name: " + authorNameInfo + "\n")
    file.write("Book Genre: " + genreTypeInfo + "\n")
    file.write("\n")
    file.close()

def clear():
    bookTitleEntry.delete(0, 'end')
    authorsNameEntry.delete(0, 'end')
    genreTypeEntry.delete(0, 'end')

def helpWindow():
    newWindow = Toplevel(app)
    newWindow.title("Help Window")
    newWindow.geometry("400x200")
    Label(newWindow, text="enter the books you have read along with the author and genre").pack()
    Label(newWindow, text="and have all your books in one spot.").pack()
    Label(newWindow, text="For more help email us at booktracker@email.com").pack()

    backButton = Button(newWindow, text="Go Back Home", command=newWindow.destroy)
    backButton.place(x=110,y=110)

def reviewWindow():
    def saveReview():
        reviewInfo = reviewEntry.get('1.0', 'end-1c')

        print(reviewInfo)

        file = open("reviews.txt", "a+")
        file.write("Book review: " + reviewInfo + "\n")
        file.write("\n")
        file.close()

    def clear():
        reviewEntry.delete('1.0', 'end-1c')
        
    newWindow = Toplevel(app)
    newWindow.title("Review Window")
    newWindow.geometry("500x500")

    review_text = Label(newWindow, text="Leave a review on your latest reads!!")

    review_text.place(x=10,y=35)

    reviewEntry = Text(newWindow, width=65, height=20)

    reviewEntry.place(x=10,y=55)

    clearButton = Button(newWindow, text="Clear", command=clear, width="25", height ="3")
    clearButton.place(x=150,y=325)

    button = Button(newWindow, text="Add Review", command=saveReview, width="10", height="2")
    button.place(x=300,y=400)        

    backButton = Button(newWindow, text="Go Back", command=newWindow.destroy,  width="10", height="2")
    backButton.place(x=110,y=400)

def reviewWindowHelp():
    window = Toplevel(app)
    window.title("About Review Feature")
    window.geometry("500x300")

    featureInfo = Label(window, text="You can now leave reviews about your latest reads!!")
    info = Label(window, text="Just type out your thought, Hit Add Review")
    info2 = Label(window, text="And presto, you know have all your reviews together")
    featureInfo.place(x=15,y=10)
    info.place(x=15,y=35)
    info2.place(x=15,y=60)
    
    prompt = Label(window, text="Would you like to use this feature today?")
    prompt.place(x=15,y=100)

    button = Button(window, text="Yes", command=reviewWindow, width="10", height="2")
    button.place(x=15,y=125)

    button2 = Button(window, text="No", command=window.destroy, width="10", height="2")
    button2.place(x=150,y=125)

app = Tk()

app.geometry("500x500")
app.title("Book Tracker")

heading = Label(text="All your books on one shelf!!",bg="blue", fg="white", font="10", width="500", height="3").pack()

bookTitle_text = Label(text="Book Title: ")
authorName_text = Label(text="Authors Name: ")
genreType_text = Label(text="Books Genre: ")

bookTitle_text.place(x=15,y=70)
authorName_text.place(x=15,y=140)
genreType_text.place(x=15,y=200)

bookTitle = StringVar()
authorName = StringVar()
genreType = StringVar()

bookTitleEntry = Entry(textvariable=bookTitle, width="30")
authorsNameEntry = Entry(textvariable=authorName, width="30")
genreTypeEntry = Entry(textvariable=genreType, width="30")

bookTitleEntry.place(x=15,y=90)
authorsNameEntry.place(x=15,y=160)
genreTypeEntry.place(x=15,y=220)

button = Button(app, text="Add Entry", command=saveInfo, width="10", height="2")
button.place(x=15,y=250)

clearButton = Button(app, text="Clear", command=clear, width="10", height ="2")
clearButton.place(x=150,y=250)

helpButton = Button(app, text="?", command=helpWindow, width="3", height="3")
helpButton.place(x=440,y=1)

feature = Label(app, text="** New Feature Available **", font="30")
feature.place(x=15, y=300)

feature1 = Label(app, text="would you like to know more?")
feature1.place(x=15,y=320)

r = IntVar()
r.get()
bttn1 = Radiobutton(app, text="yes", variable=r, value=1, command=reviewWindowHelp)
bttn1.place(x=205,y=320)

bttnQuit = Button(app, text="Exit Book Tracker", command=app.quit)
bttnQuit.place(x=360, y=455)

mainloop()
