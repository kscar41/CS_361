from tkinter import *

def saveInfo():
    bookTitleInfo = bookTitle.get()
    authorNameInfo = authorName.get()
    genreTypeInfo = genreType.get()

    print(bookTitleInfo, authorNameInfo, genreTypeInfo)

    file = open("books.txt", "w")
    file.write("Book Title: " + bookTitleInfo + "\n")
    file.write("Authors Name: " + authorNameInfo + "\n")
    file.write("Book Genre: " + genreTypeInfo + "\n")
    file.close()

app = Tk()

app.geometry("500x500")
app.title("title")

heading = Label(text="Python File Handling",bg="blue", fg="white", font="10", width="500", height="3").pack()

bookTitle_text = Label(text="Book Title: ")
authorName_text = Label(text="Authors Name: ")
genreType_text = Label(text="Books Genre: ")

bookTitle_text.place(x=15,y=70)
authorName_text.place(x=15,y=140)
genreType_text.place(x=15,y=210)

bookTitle = StringVar()
authorName = StringVar()
genreType = StringVar()

bookTitleEntry = Entry(textvariable=bookTitle, width="30")
authorsNameEntry = Entry(textvariable=authorName, width="30")
genreTypeEntry = Entry(textvariable=genreType, width="30")

bookTitleEntry.place(x=15,y=100)
authorsNameEntry.place(x=15,y=180)
genreTypeEntry.place(x=15,y=240)

button = Button(app, text="Add Entry", command=saveInfo, width="30", height="2")
button.place(x=15,y=290)

mainloop()
