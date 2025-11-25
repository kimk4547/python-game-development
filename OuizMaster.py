import pgzrun
import random
title = "Quiz Master"
WIDTH=900
HEIGHT=700
#LAYOUT
marquee_box = Rect((0,0),(WIDTH,HEIGHT))
question_box = Rect((200,100),(600,120))
answer_boxes = [
    Rect((50,220),(380,100)),
    Rect((470,220),(380,100)),
    Rect((50,350),(380,100)),
    Rect((470,350),(380,100)),
]
timer_box = Rect((720,460),(150,80))
skip_box = Rect ((50,460),(150,80))

#Game variables
questions = []
current_question = []
question_index = 0
score = 0
time_left = 15
game_over_flag = False


#Marquee settings
marquee_text = "Welcome to QuizMaster!"
marquee_x = WIDTH

#Load questions from file
def load_questions(filename = "questions.txt"):
    global questions
    with open(filename, "r", encoding= "utf") as f:
        for line in f:
            parts = line. strip().split(",")
            print("Debug", parts)
            if len(parts) ==6:
                questions.append(parts)
    random.shuffle(questions)
    print("Total questions loaded", len(questions))
#next question function
def next_question():
    global current_question, question_index, time_left, game_over_flag

    if question_index < len(questions):
        current_question = questions[question_index]
        question_index +=1
        time_left = 15
    else:
        game_over_flag = True
# draw screen

def draw():
    screen.clear()
    screen.fill("black")
    #marquee
    screen.draw.filled_rect(marquee_box, "darkblue")
    screen.draw.text(marquee_text, (marquee_x, 15), color = "white", fontsize = 30)

    if game_over_flag:
        msg = f"Game Over /n Your Score: {score}/{len(questions)}"
        screen.draw.textbox(msg, Rect((150, 200),(600, 250)), color = "white")
        return
#question box
    screen.draw.filled_rect(question_box, "navy")
    screen.draw.textbox(current_question[0], question_box, color = "white") 

#timer box
    screen.draw.filled_rect(timer_box, "purple")
    screen.draw.textbox(str(time_left), timer_box, color = "white") 

# skip button
    screen.draw.filled_rect(skip_box, "purple")
    screen.draw.textbox("Skip", skip_box, color = "white") 

#answer boxes
    for i, box in enumerate(answer_boxes):
        screen.draw.filled_rect(box, "darkorange")
        screen.draw.textbox(current_question[ i + 1 ], box, color = "black")


# handle marquee movment


def update():
    global marquee_x
    marquee_x -= 2
    if marquee_x + 600 < 0:
        marquee_x = WIDTH
#countdown timer
def update_timer():
    global time_left, game_over_flag
    if not game_over_flag:
        if time_left > 0:
            time_left -= 1
    else:
        next_question() 
#mouse click handler
def on_mouse_down(pos):
    global score

    if game_over_flag:
        return
    for i ,box in enumerate(answer_boxes):
        if box.collidepoint(pos):
            if int(current_question[5]) == i +1:
                score +=1
        next_question()
        return
#skip button
    if skip_box.collidepoint(pos):
        next_question()


#start the game
load_questions()
next_question()
clock.schedule_interval(update_timer,1)

pgzrun.go()

         
        
