# PyQt5: To create application on computer

from PyQt5.QtWidgets import *
from random import randint, shuffle

app = QApplication([]) # Keep track of your widgets
window = QWidget() # Create a window to keep your widgets

# QHBoxLayout, QVBoxLayout
# H: horizontal, V: vertical
main_layout = QVBoxLayout()

questions = [
    ['Question1', 'Correct', 'Wrong1', 'Wrong2', 'Wrong3'],
    ['Question2', 'Correct', 'Wrong1', 'Wrong2', 'Wrong3'],
    ['Question3', 'Correct', 'Wrong1', 'Wrong2', 'Wrong3'],
    ['Question4', 'Correct', 'Wrong1', 'Wrong2', 'Wrong3']
]

# Hello World -> my_string[0] == 'H'
# list -> questions[0] :  ['Question1', 'Correct', 'Wrong1', 'Wrong2', 'Wrong3']
# questions[0][0]: 'Question1'

quest_num = randint(0, len(questions) - 1)
score = 0
num_of_questions = len(questions)

# processing memory
# physical memory

def final_result():
    button_choices[0].hide()
    button_choices[1].hide()
    button_choices[2].hide()
    button_choices[3].hide()
    question.setText('Your score: ' + str(score) + '/' + str(num_of_questions))
    next_btn.hide()

def next_question(): # change the question
    global quest_num
    global score

    if button_choices[0].isChecked():
        score += 1
        box = QDialog()
        box.setFixedSize(200, 100)
        box.setWindowTitle('Result')
        label =  QLabel('Correct', box)
        box.exec()
    else:
        box = QDialog()
        box.setFixedSize(200, 100)
        box.setWindowTitle('Result')
        label1 =  QLabel('Incorrect!', box)
        label2 =  QLabel('The correct answer is ' + questions[quest_num][1], box)
        label2.move(0, 50) # Move label2 to position (0, 50)
        box.exec()
    
    del questions[quest_num] # Remove the question that was just asked
    if questions: # If there are still questions left
        button_choices[0].setAutoExclusive(False)
        button_choices[1].setAutoExclusive(False)
        button_choices[2].setAutoExclusive(False)
        button_choices[3].setAutoExclusive(False)

        button_choices[0].setChecked(False)
        button_choices[1].setChecked(False)
        button_choices[2].setChecked(False)
        button_choices[3].setChecked(False)

        quest_num = randint(0, len(questions) - 1)
        shuffle(button_choices)
        question.setText(questions[quest_num][0])
        button_choices[0].setText(questions[quest_num][1])
        button_choices[1].setText(questions[quest_num][2])
        button_choices[2].setText(questions[quest_num][3])
        button_choices[3].setText(questions[quest_num][4])

    else:
        final_result()

question = QLabel(questions[0][0])
main_layout.addWidget(question)

# QVBoxLayout
row1 = QHBoxLayout()
row2 = QHBoxLayout()

button5 = QRadioButton() # memory address of button5
button6 = QRadioButton()
button7 = QRadioButton()
button8 = QRadioButton()

row1.addWidget(button5) # add the address of button5 to row1
row1.addWidget(button6)
row2.addWidget(button7)
row2.addWidget(button8)

button_choices = [button5, button6, button7, button8]
shuffle(button_choices) # Randomize the order of the buttons
button_choices[0].setText(questions[quest_num][1])
button_choices[1].setText(questions[quest_num][2])
button_choices[2].setText(questions[quest_num][3])
button_choices[3].setText(questions[quest_num][4])


main_layout.addLayout(row1)
main_layout.addLayout(row2)

next_btn = QPushButton('Next question')
main_layout.addWidget(next_btn)

next_btn.clicked.connect(next_question)

window.setLayout(main_layout) # Create a canvas for window

window.show()
app.exec_()

# Window setup
# 1. Set the window title
# 2. Set the window size
# 3. Set the window position
# 4. Set the window icon
# 5. Set the window background color
# 6. Set the window border color
# 7. Set the window border style
# 8. Set the window border width

# Decoration
# 1. border-top/bottom/left/right
# 2. border-radius
# 3. border-color
# 4. border-image
# 5. border-style
# 6. border-width
# 7. border
# 8. background-color
# 9. color
# 10. font-size
# 11. font-family
# 12. font-weight
# 13. font-style
# 14. font-variant
# 15. font
# 16. text-align
# 17. text-decoration
# 18. text-transform
# 19. text-indent
# 20. text-shadow
# 21. text-overflow
# 22. text-underline-position
# 23. text-emphasis
# 24. text-justify
# 25. text-orientation
# 26. text-overflow
# 27. text-rendering
# 28. text-underline-position
