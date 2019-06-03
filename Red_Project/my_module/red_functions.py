import time

answer_A=['a','A']
answer_B=['b','B']
answer_C=['c','C']
red_name=['Red','red','RED']
error='\nPlease follow the answer format'
energy=0
has_doorknob=False


def start():
    print("\nYou're playing little red riding hood! You're delivering cookies to your grandma's house.")
    print("But on your way you got lost. You...")
    time.sleep(1)
    print("  \nA. Stop and rest  \nB. Keep walking")
    answer=input(">")
    if answer in answer_A:
        stop_and_rest()
    elif answer in answer_B:
        witch_house()
    else:
        print(error)
        start()

def stop_and_rest():
    global energy
    print("\nYou decided to rest. Do you want to...")
    time.sleep(1)
    print("  \nA. Eat the cookies  \nB. Take a nap  \nC. Just sit")
    answer=input(">")
    if answer in answer_A:
        print("\nYou ate all the cookies except for one and gained some energy.")
        energy=energy+20
        witch_house()
    elif answer in answer_B:
        print("\nYou took a nap. But you let your guard down in the woods and got eaten by wolves. \nYou're dead")
    elif answer in answer_C:
        print("\nYou just sit there.")
        energy+=10
        witch_house()
    else:
        print(error)
        time.sleep(1)
        stop_and_rest()

def witch_house():
    time.sleep(1)
    global has_doorknob
    print("\nYou got up and kept walking. You pass by a house covered in candy."
          "It's a very memorable landmark, and you remember your way to grandma's house."
          "Do you...")
    time.sleep(1)
    print(" \nA. Go inside the house  \nB. Resist the candy and keep walking  \nC. Take a piece of candy from her house")
    answer=input(">")
    time.sleep(1)
    if answer in answer_A:
        go_inside()
    elif answer in answer_B:
        print("\nYou keep walking.")
        to_grandmas()
    elif answer in answer_C:
        print("\nYou steal the doorknob, which is made out of chocolate, and hope that the house owner doesn't notice."
             "You keep walking to grandma's house.")
        has_doorknob=True
        to_grandmas()
    else:
        print(error)
        time.sleep(1)
        witch_house()

def go_inside():
    time.sleep(1)
    global energy
    print("\nYou go inside the house. The witch from Hanzel and Gretel welcomes you. "
         "Without wasting any time, she tries to drag you into the oven.")
    time.sleep(1)
    if energy==20:
        print("\nYou fight the witch and escape from her. You run to grandma's house.")
        energy=energy/2
        to_grandmas()
    elif energy<20:
        print("\nYou try to fight the witch but fail and you die.")

def to_grandmas():
    time.sleep(1)
    global energy
    global has_doorknob
    print("\nYou arrive at grandma's house. There's a wolf there trying really hard to pretend to be your grandma. "
         "Do you...")
    time.sleep(1)
    print("  \nA. Give the wolf a cookie.  \nB. Attack the wolf  \nC. Run away")
    answer=input(">")
    if answer in answer_A:
        print("\nYou give the wolf a cookie. The wolf says, 'Ha you fell for my trap. I'm gonna eat you now.'")
        time.sleep(1)
        if has_doorknob==True:
            print("\nBefore the wolf eats you, the witch from the candy house breaks down the door and kills the wolf. "
                 "You give her back the doorknob, but the witch is still mad. She eats you. You died.")
        else:
            print("\nThe wolf eats you. You died.")
    elif answer in answer_B:
        time.sleep(1)
        if energy>=10:
            print("\nYou don't want to touch the wolf with your bare hands, so you kick the wolf. "
                 "It sends the wolf flying out of the bed and out the window conveniently located beside the bed. "
                 "In addition, it knocks down the witch from the candy house who was waiting for you outside.")
            time.sleep(1)
            print("\n\nYou win!")
        elif energy<10:
            print("\nYou're weak and you're fighting a wolf. It's hopeless.")
            time.sleep(1)
            if has_doorknob==True:
                print("\nYou decide to throw the chocolate doorknob at the wolf. The doorknob knocks it out, "
                     "bounces off the wolf, out the window, and knocks out the witch from the candy house "
                      "waiting for you outside.")
                time.sleep(1)
                print("\n\nYou win!")
            else:
                print("The wolf eats you. You died.")
    elif answer in answer_C:
        time.sleep(1)
        if energy<=10:
            print("\nYou run from the wolf's scary claws.")
            time.sleep(1)
            if has_doorknob==True:
                print("\nBut the witch from the candy house was waiting outside for you."
                "She punishes you for taking her doorknob by eating you. You died.")
            else:
                print("\nYou successfully ran away from the wolf.")
                time.sleep(1)
                print("\n\nYou win!")
        elif energy<10:
            print("\nYou try to run but you're tired from walking in the woods. You died.")
    else:
        print(error)
        to_grandmas()
