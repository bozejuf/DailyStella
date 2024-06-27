from datetime import datetime
from flask import Flask, render_template, request

app = Flask(__name__)

def change_numbers():
    file = open("pic_number.txt", "r")
    pic_number = int(file.read())
    if date_is_different():
        pic_number += 1
        file.close()
        file = open("pic_number.txt", "w")
        file.write(str(pic_number))
        file.close()
        file = open("last_update.txt", "w")
        file.write(datetime.now().strftime("%d-%m-%Y"))
        file.close()

@app.route("/")
def index():
    change_numbers()
    file = open("pic_number.txt", "r")
    pic_number = f"Stella{file.read()}"
    return render_template("index.html", pic_number=pic_number)

# checks if the date of today is different than the date in last_update.txt
def date_is_different():
    # read late update-date in last_update (dd-mm-yyy format)
    file = open("last_update.txt", "r")
    last_update = file.read()

    # save current date in current_date (dd-mm-yyyy format)
    current_date = datetime.now().strftime("%d-%m-%Y")

    if current_date == last_update:
        return False
    else:
        return True


if __name__ == '__main__':
    app.run(debug=True)