import pyttsx3
import PyPDF2

# Open the PDF file
book = open('SE principle.pdf', 'rb')

pdfReader = PyPDF2.PdfReader(book)
pages= len(pdfReader.pages)
print(pages)
friend = pyttsx3.init()
for num in range(0,pages):

    read = pdfReader.pages[num]
    text = read.extract_text()
    friend.say(text)
    friend.runAndWait()

# Close the book

