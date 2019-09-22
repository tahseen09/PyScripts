import yagmail
import csv

subject = "Email subject"
yag = yagmail.SMTP("email", "password")

with open("filename.csv") as file:
    reader = csv.reader(file)
    next(reader)  # Skip header row
    for column1, column2, column3 in reader:				#add as much columns as per your csv file and in the same order
        body = "This is the body of the email"
        yag.send(to=email, subject=subject, contents=body)
