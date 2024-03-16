from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPixmap, QIcon
from random import randint, shuffle


questions = [
    ['What is the chemical symbol for gold?', 'Au', 'Ag', 'Pt', 'Fe'],
    ['Which planet is known as the Red Planet?', 'Mars', 'Venus', 'Jupiter', 'Saturn'],
    ['What is the largest mammal on Earth?', 'Elephant', 'Blue Whale', 'Giraffe', 'Hippopotamus']
]

correct_answer = 0

is_correct = False

def check_answer():
    global options, correct_answer, is_correct
    if options[0].isChecked():
        correct_answer += 1
        is_correct = True
    else:
        is_correct = False

def show_answer():
    global options
    options_box.setTitle('Your result')
    rb.hide()
    rb2.hide()
    rb3.hide()
    rb4.hide()

    is_correct_label.setText('Incorrect answer')
    is_correct_label.setStyleSheet() # Red
    if is_correct:
        is_correct_label.setText('Correct answer')
        is_correct_label.setStyleSheet() # Green

    correct_option.setText(options[0].text())

    btn.setText('Next question')

    is_correct_label.show()
    correct_option.show()

def next_question():
    current_question = randint(0, len(questions) - 1)
    label.setText(questions[current_question][0])
    shuffle(options)
    options[0].setText(questions[current_question][1])
    options[1].setText(questions[current_question][2])
    options[2].setText(questions[current_question][3])
    options[3].setText(questions[current_question][4])

    button_box = QButtonGroup()
    button_box.addButton(options[0])
    button_box.addButton(options[1])
    button_box.addButton(options[2])
    button_box.addButton(options[3])

    button_box.setExclusive(False)
    options[0].setChecked(False)
    options[1].setChecked(False)
    options[2].setChecked(False)
    options[3].setChecked(False)
    button_box.setExclusive(True)

    del questions[current_question]

    rb.show()
    rb2.show()
    rb3.show()
    rb4.show()
    btn.setText('Answer')
    options_box.setTitle('Answer options')

    is_correct_label.hide()
    correct_option.hide()

def handle2():
    if btn.text() == 'Answer':
        check_answer()
        show_answer()
    elif btn.text() == 'Next question':
        if len(questions) > 0:
            next_question()
        else:
            label.setText('Your score: ' + str(correct_answer))
            options_box.hide()
            btn.hide()

def handle():
    global options, is_next_question
    if len(questions) > 0:
        check_answer()
        if is_next_question == False:
            show_answer()
            is_next_question = True
        else:
            next_question()
            is_next_question = False
    else:
        check_answer()

        if is_next_question == False:
            show_answer()
            is_next_question = True
        else:
            next_question()
            is_next_question = False

        label.setText('Your score: ' + str(correct_answer))
        options_box.hide()
        btn.hide()

app = QApplication([]) #keep track of widgets
window = QWidget() #create a window for adding widgets

icon = QIcon(r"C:\Users\Admin\Downloads\IMG_20200713_180852_4.jpg")
window.setWindowIcon(icon)

# #BACKGROUND
# background = QImage('2022七夕横en.jpg').scaled(QSize(500, 300))
# pallete = QPalette()
# pallete.setBrush(QPalette.window, QBrush(background))
# window.setPalette(pallete)

window.setWindowTitle('Memory Card')
window.setFixedSize(500, 300)

bg_img = QPixmap(r"C:\Users\Admin\Downloads\1670333849220.png") 
bg = QLabel()
bg.setPixmap(bg_img)
bg.setFixedSize(500, 300)

#H: horizontal      V: verticle

main_layout = QVBoxLayout()

main_layout.addWidget(bg)

current_question = randint(0, len(questions) - 1) # Random the first question

label = QLabel(questions[current_question][0], alignment=Qt.AlignCenter) # Set the first question
label.setStyleSheet('background-color: #458cba; color: #ffffff; border-bottom: 3px solid #BA7345; font-size: 18px; font-family: Courier')
# border-top/bottom/left/right
main_layout.addWidget(label)

# QUESTION SCREEN
options_box = QGroupBox('Answer options')
main_layout.addWidget(options_box)

co = QHBoxLayout()
rb = QRadioButton() 
co.addWidget(rb)
rb2 = QRadioButton()
co.addWidget(rb2)

co1 = QHBoxLayout()
rb3 = QRadioButton()
co1.addWidget(rb3)
rb4 = QRadioButton()
co1.addWidget(rb4)

options = [rb, rb2, rb3, rb4] # Store them in a list
shuffle(options) # Shuffle the position
options[0].setText(questions[current_question][1]) # Set the answers for the first question
options[1].setText(questions[current_question][2])
options[2].setText(questions[current_question][3])
options[3].setText(questions[current_question][4])
del questions[current_question] # Delete the already shown questions
# 3 questions: max_index = 2
# del 1 question: max_index = 1

options_box_layout = QVBoxLayout()
options_box_layout.addLayout(co)
options_box_layout.addLayout(co1)
options_box.setLayout(options_box_layout)

# RESULT SCREEN
correct_option = QLabel()
is_correct_label = QLabel()
co.addWidget(is_correct_label)
co1.addWidget(correct_option)
is_correct_label.hide()
correct_option.hide()
options_box.show()

btn = QPushButton('Answer')
btn.setStyleSheet('border-bottom: 3px solid #458cba; border-top: 3px solid #BA7345; border-left: 3px solid #458cba; border-right: 3px solid #458cba')
main_layout.addWidget(btn, alignment=Qt.AlignCenter)

# Handle click event
btn.clicked.connect(handle2)



window.setLayout(main_layout)
window.show()
app.exec_()


# Step 1: Choose answer
# Step 2: Show result
# Switching: hide buttons -> show result texts
# Step 3: Choose answer