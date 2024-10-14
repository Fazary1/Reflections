rooms = {
    "front lawn": {
        "description": "You are standing at the front door of a large mansion with a pizza-box in your hand. You're supposed to be delivering the food to this house, so maybe you could try ringing the doorbell.",
        "north": "living room",
        "objects": [],
        "hidden_objects": []
    },
    "living room": {
        "entrance": "",
        "description": "You are in a grand living room with marble floors. A chandelier hangs from the ceiling, and a man is sitting in a pool of his blood on the couch. The dining room is to the north. To the west, a door is slightly ajar, revealing a luxurious bathroom behind it. There is another door to the east. The tv is on.",
        "north": "dining room",
        "east": "elevator",
        "west": "bathroom",
        "objects": ["pizza-box"],
        "hidden_objects": []
    },
    "kitchen": {
        "entrance": "You step into the kitchen, elegant but simple. On the countertop are a knife and various utensils, and the smell of baked bread fills the air.",
        "description": "You are in an elegant but simple kitchen. On the countertop are a knife and various utensils. The smell of baked bread fills the air.",
        "west": "dining room",
        "objects": [],
        "hidden_objects": ["knife"]
    },
    "dining room": {
        "entrance": "You walk into an elegant dining room, dominated by a large table in its center. The walls are adorned with beautiful paintings. There is a passage leading east.",
        "description": "You are in an elegant dining room with a large table in its center. The walls are covered with beautiful paintings. There is a passage leading east.",
        "east": "kitchen",
        "south": "living room",
        "objects": [],
        "hidden_objects": []
    },
    "bathroom": {
        "entrance": "You step into a luxurious bathroom, complete with a spacious shower and a gold-plated sink. In the corner to the west, there is a small panel that seems different from the rest.",
        "description": "You are in a luxurious bathroom with a spacious shower and a gold-plated sink. In the corner to the west is a small panel that seems different from the rest.",
        "east": "living room",
        "objects": [],
        "hidden_objects": []
    },
    "elevator": {
        "entrance": "You enter a modern and well-lit elevator. The walls are so polished that you can see your reflection staring back at you. There are three buttons: g, 1, and 2.",
        "description": "You are in a modern and well-lit elevator. The walls are so well polished that you can see your reflection staring back at you. There are three buttons: g, 1, and 2.",
        "objects": [],
        "hidden_objects": []
    },
    "hallway": {
        "entrance": "You enter a dimly-lit hallway that stretches to the north and to the south. Doors lead to other rooms at either end. The elevator is to the east.",
        "description": "You are in a dimly-lit hallway that extends north and south. There are doors leading to other rooms at either end. The elevator is to the east.",
        "east": "elevator",
        "south": "large bedroom",
        "north": "small bedroom",
        "objects": [],
        "hidden_objects": []
    },
    "large bedroom": {
        "entrance": "You open the door and enter a spacious bedroom with a large bed draped in velvet covers. The air feels heavy, and shadows seem to linger longer than they should. There's a door to the south.",
        "description": "You are in a spacious bedroom with a large bed draped in velvet covers. The air feels heavy, and shadows seem to linger longer than they should. There's a door to the south.",
        "north": "hallway",
        "south": "attic",
        "objects": [],
        "hidden_objects": []
    },
    "small bedroom": {
        "entrance": "You open the door and step into a cozy small bedroom. A single bed is pushed against the far wall next to a small nightstand with a single drawer. The room is modestly furnished, but the silence in here is thick, as if the room is holding its breath.",
        "description": "You are in a small bedroom. The room is cozy, with a single bed pushed against the far wall next to a small nightstand with a single drawer. The room is modestly furnished, but the silence in here is thick, as if the room is holding its breath.",
        "south": "hallway",
        "objects": [],
        "hidden_objects": ["flashlight", "notebook"]
    },
    "attic": {
        "entrance": "You open the door and turn on the flashlight with a click. You climb into the attic, dark and filled with old, dust-covered furniture. In the corner, a small cupboard beckons. Above it, a mirror reflects the room with strange, distorted angles. There is something unsettling about the atmosphere.",
        "description": "You are in a dark attic. The only light is coming from your little flashlight. Old, dust-covered furniture is scattered around the room. A small cupboard stands in the corner, and above it, a mirror reflects the room in strange, distorted angles. There’s something unsettling about it, as if it knows more than it lets on.",
        "north": "large bedroom",
        "objects": [],
        "hidden_objects": ["key"]
    },
    "office": {
        "entrance": "A sudden blast of cool air washes over you, and you find yourself in a large office. Through the closed windows, you can see the city stretching out beneath you, filled with bright lights that seem to mirror the stars in the night sky. It's peaceful up here. A computer sits on a desk in front of you, and the elevator is to the east.",
        "description": "You are in a large office on the top floor. You can see the city stretching out beneath you, filled with bright lights that seem to mirror the stars in the night sky. A computer sits on a desk in front of you, and the elevator is to the east.",
        "east": "elevator",
        "objects": [],
        "hidden_objects": []
    }
}


end = False


import requests
import json

def talk():
    url = 'https://pretty-schools-check.loca.lt/webhooks/rest/webhook'

    while True:
        user_message = input("\nYou: ")
        if user_message.strip().lower() == "exit":
            look()
            return
        payload = {
            "sender": {"id": "user"},  # Use a dictionary for sender
            "message": user_message
            }
        try:
            # Send the request to the Rasa server
            response = requests.post(url, headers={"Content-Type": "application/json"}, data=json.dumps(payload))

            # Check for a successful response
            if response.status_code == 200:
                response_data = response.json()

                # Print the response from the AI
                for msg in response_data:
                    print(f"\nReflection: {msg['text']}")
            else:
                print(f"\nYour reflection remains silent...\n")

        except requests.exceptions.RequestException as e:
            print(f"\nYour reflection remains silent...\n")


def dead_ending():
    print("\nYou drop everything and crawl through the tunnel. It's over. You're safe.")
    print("\nThat man was a criminal. The worst kind, ruining people's lives and breaking families apart. It had to be done...")

    while True:
        command = input("\nKeep moving 'forward'\n\n").strip().lower()
        if command == "forward":
            print("\nHe was a criminal, and now he paid the price. You made your choice. But what about his daughter...")

            while True:
                command2 = input("\nKeep moving 'forward'\n\n").strip().lower()
                if command2 == "forward":
                    print("\nYou can see light coming from the other end. You're almost there.")
                    print("\nYou made the right choice, right? Or was it wrong? It doesn't matter now, does it? You made your choice, and you're gonna have to live with it. It's done.")

                    while True:
                        command3 = input("\nWhatever happens now, you just need to keep moving 'FORWARD'\n\n").strip().lower()
                        if command3 == "forward":
                            print("\n'THE END'\n")
                            global end
                            end = True
                            return

def alive_ending():
    print("\nYou drop everything and crawl through the tunnel. It's over. You're safe.")
    print("\nThat man was a criminal. The worst kind, ruining people's lives and breaking families apart. and now he's getting away with it...")

    while True:
        command = input("\nKeep moving 'forward'\n\n").strip().lower()
        if command == "forward":
            print("\nYou made your choice. He was a criminal. He hurt countless people, and he'll hurt countless more. And you let him.")

            while True:
                command2 = input("\nKeep moving 'forward'\n\n").strip().lower()
                if command2 == "forward":
                    print("\nYou can see light coming from the other end. You're almost there.")
                    print("\nIt wasn't up to you to stop him. You made the right choice, right? Or was it wrong? It doesn't matter now, does it? You made your choice, and you're gonna have to live with it. It's done.")

                    while True:
                        command3 = input("\nWhatever happens now, you just need to keep moving 'FORWARD'\n\n").strip().lower()
                        if command3 == "forward":
                            print("\n'THE END'\n")
                            global end
                            end = True
                            return




inventory = []

undiscovered = list(rooms.keys())

def first_time():
    if location == "elevator":
        elev()
    elif location == "bathroom" and "elevator" in undiscovered and "attic" in undiscovered:
        bath()
    elif location == "attic":
        att()


def help():
    print("\n" + "Command list:")
    print("- 'look'")
    print("- 'north', 'south', 'east', 'west'")
    print("- 'examine...'")
    print("- 'inventory'")
    print("- 'take...'")
    print("- 'drop...'")
    print("- 'quit'" + "\n")


def look():
    if location == "attic" and "flashlight" not in inventory:
        print("\nIt's too dark to see anything.\n")
    else:
        print("\n" + rooms[location]["description"] + "\n")
        if rooms[location]["objects"]:
            print("You see: " + ", ".join(rooms[location]["objects"]) + "\n")

def move(direction):
    global location
    if direction in rooms[location]:
        location = rooms[location][direction]
        if location == "attic" and "flashlight" not in inventory:
            print("\nAs you open the door, you are faced with nothing but darkness. You can hardly make out your own hands. Surely there's some way to get some light in here...\n")
        elif location in undiscovered:
            print("\n" + rooms[location]["entrance"] + "\n")
            first_time()
            undiscovered.remove(location)
        else:
            print("\n" + rooms[location]["description"] + "\n")
            if rooms[location]["objects"]:
                print("You see: " + ", ".join(rooms[location]["objects"]) + "\n")
    else:
        print("\n" + "You can't go that way." + "\n")


def pickup(object):
    if object in rooms[location]["hidden_objects"] or object in rooms[location]["objects"]:
        if object in rooms[location]["hidden_objects"]:
            rooms[location]["hidden_objects"].remove(object)
        if object in rooms[location]["objects"]:
            rooms[location]["objects"].remove(object)
        inventory.append(object)
        print("\nYou take the " + object + ".\n")
    else:
        print("\nThere's nothing like that here.\n")

def drop(object):
    if object in inventory:
        inventory.remove(object)
        rooms[location]["objects"].append(object)
        print("\nYou drop the " + object + ".\n")
    else:
        print("\nYou don't have that.\n")





def main_menu():
    print("\n __________________________________")
    print("| Thursday, August 15, 2024        |")
    print("| 11:15PM 🕚 ⏾                     |")
    print("|                                  |")
    print("|                                  |")
    print("|      📄         📁         📁    |")
    print("|     sec       work       img     |")
    print("|                                  |")
    print("|                       logout ->  |")
    print(" __________________________________")
    print(r"    _____//            \\_____      "+"\n")

def security_menu():
    print("\n __________________________________")
    print("| Thursday, August 15, 2024        |")
    print("| 11:15PM 🕚 ⏾                     |")
    print("|                         back ->  |")
    print("| > Security                       |")
    print("|     Personal ID: DV-04729X.      |")
    print("|     Bank account: 187-402-5943   |")
    print("|     Emergency escape code: 9417  |")
    print("|                                  |")
    print(" __________________________________")
    print(r"    _____//            \\_____      "+"\n")

def work_menu():
    print("\n __________________________________")
    print("| Thursday, August 15, 2024        |")
    print("| 11:15PM 🕚 ⏾                     |")
    print("|                         back ->  |")
    print("|                                  |")
    print("|      📄         📄         📄    |")
    print("|  contacts   shipments   payments |")
    print("|                                  |")
    print("|                                  |")
    print(" __________________________________")
    print(r"    _____//            \\_____      "+"\n")

def img_menu():
    print("\n __________________________________")
    print("| Thursday, August 15, 2024        |")
    print("| 11:15PM 🕚 ⏾                     |")
    print("|                         back ->  |")
    print("|                                  |")
    print("|  > All images have been removed_ |")
    print("|                                  |")
    print("|                                  |")
    print("|                                  |")
    print(" __________________________________")
    print(r"    _____//            \\_____      "+"\n")

def contacts_page():
    print("\n- F. Marconi (warehouse)")
    print("- K. Williams (logistics)")
    print("- Z. Ivanov (security)")
    print("\n<- back\n")

def shipments_page():
    print("\nDate         | Location   | Quantity")
    print("--------------------------------  ")
    print("Aug 10, 2024 | Port C     | 45 ")
    print("Aug 15, 2024 | Terminal 5 | 30")
    print("\n<- back\n")

def payments_page():
    print("\n- $120,000 to D.A. offshore (confirmed)")
    print("- $85,000 to F.M. transport (pending)")
    print("\n<- back\n")

def main_process():
    while True:
        command = input().strip().lower()
        if command == "sec":
            security_menu()
            secimg_process()
        elif command == "work":
            work_menu()
            work_process()
        elif command == "img":
            img_menu()
            secimg_process()
        elif command in ["logout", "log out", "log off"]:
            print("\nLOGGED OUT\n")
            look()
            break
        else:
            print("\nInvalid Command\n")

def secimg_process():
    while True:
        command = input().strip().lower()
        if command == "back":
            main_menu()
            break
        else:
            print("\nInvalid Command\n")

def work_process():
    while True:
        command = input().strip().lower()
        if command == "contacts":
            contacts_page()
            work2process()
        elif command == "shipments":
            shipments_page()
            work2process()
        elif command == "payments":
            payments_page()
            work2process()
        elif command == "back":
            main_menu()
            break
        else:
            print("\nInvalid Command\n")

def work2process():
    while True:
        command = input().strip().lower()
        if command == "back":
            work_menu()
            break
        else:
            print("\nInvalid Command\n")

def computerize():
    while True:
        print("\nENTER PASSWORD:")
        ask = input().strip()
        if ask == "LS09601":
            print("\nWelcome, DEREK VANE\n")
            main_menu()
            main_process()
            break
        else:
            print("\nWRONG PASSWORD\n")
            look()
            break


life = True


panel = False



def examination(object):
    if object == "panel" and location == "bathroom":
        print("\n" + "You notice a small keyhole on the strange panel.\n")
        if "key" in inventory:
            print("You quickly take out the key from the attic and insert it. the panel clicks open, and you find a small steel gate, but it won't budge. There is a keypad on the gate.\n")
            global panel
            panel = True
    elif object == "tv" and location == "living room":
        print("\n" + "News headlines can be seen at the bottom of the tv screen:")
        print("'Breaking: New Allegations Surface Against the CEO of Starlight Holdings — Suspected Links to Organized Crime and Human Trafficking. CEO Vane Firmly Denies All Claims.'")
        print("\nIt's a cruel world we live in...\n")
    elif object == "drawer" and location == "small bedroom":
        print("\nYou open the drawer. You find: " + ", ".join(rooms["small bedroom"]["hidden_objects"]) + "\n")
    elif object == "notebook" and ("notebook" in inventory or "notebook" in rooms[location]["objects"] or "notebook" in rooms[location]["hidden_objects"]):
        print("\nIt's a bright red notebook with a name imprinted on its cover: Sarah Vane. That name sounds familiar. You open the notebook...\n")
        print("-----------------------------------------------")
        print("August 14, 2024                                |")
        print("                                               |")
        print("It's really late. I have school tomorrow, but  |")
        print("I'm having trouble sleeping. We were being     |")
        print("followed by a lot of people with cameras today,|")
        print("and someone started yelling really bad words at|")
        print("my dad. Dad said everything will be ok, but I'm|")
        print("scared.                                        |")
        print("I went into his office on the top floor today. |")
        print("There were strange strange files with a lot of |")
        print("names and numbers I didn't understand, but dad |")
        print("caught me and got really upset. He yelled at me|")
        print("and told me to never go there again. I've never|")
        print("seen him get this angry before.                |")
        print("I'm going to sleep over at Grandma's tomorrow, |")
        print("and she said we're gonna bake cookies together.|")
        print("I'm excited. Maybe everything really will be   |")
        print("ok after all.                                  |")
        print("-----------------------------------------------\n")
    elif object == "cupboard" and location == "attic":
        if "flashlight" in inventory:
            print("\nCash. Lots of it, brand new thousand dollar bills.\n")
            if "key" in rooms["attic"]["hidden_objects"]:
                print("On top of the pile is a glistening key.\n")
        else:
            print("\nIt's too dark to see anything.\n")
    elif object == "pizza-box" and ("pizza-box" in inventory or "pizza-box" in rooms[location]["objects"] or "pizza-box" in rooms[location]["hidden_objects"]):
        print(" _______________________")
        print("|                       |")
        print("|  ERNESTO'S PIZZERIA,  |")
        print("|       Since 1995      |")
        print("| <%)               (%> |")
        print("|     for delivery,     |")
        print("|         call:         |")
        print("|                       |")
        print("|      # 1096057 #      |")
        print(" _______________________")
        print("\nYou open the pizza box. It's... empty?\n")
    elif object == "computer" and location == "office":
        computerize()
    elif object == "keypad" and location == "bathroom" and panel == True:
        number = input("\nENTER CODE: ").strip().lower()
        if number == "9417":
            print("\nThe steel gate swiftly opens.")
            if life == True:
                print("\nA familiar voice voice calls out to you from the bathroom mirror.")
                print("\n'Wait! Are you just going to leave? Without making things right? You know what you have to do...'")
                while True:
                    answer = input("\nLeave?\n\n-> yes\n-> no\n\n").strip().lower()
                    if answer == "yes":
                        alive_ending()
                    elif answer == "no":
                        look()
                        break
            else:
                while True:
                    answer = input("\nLeave?\n\n->yes\n->no\n").strip().lower()
                    if answer == "yes":
                        dead_ending()
                        break
                    elif answer == "no":
                        look()
                        break
        else:
            print("INCORRECT CODE")
            look()
    else:
        print("\nNothing to examine.\n")


def elev():
    print("\nOnce more, your reflection's expression changes abruptly.\n\n'Look at you, running around like a maniac.'\n")
def bath():
    print("As you look around the bathroom, you notice your reflection looking back at you in the mirror. For a split second, your expression in the mirror changes, and you find your reflection staring at you with disgust.\n")
def att():
    print("\nA loud voice comes from the mirror:\n")
    print("Reflection: Damn it. It was all going well, but you just had to take over. You couldn't mind your own business and leave the pizza on the doorstep? Now we're trapped in here, and the cops are coming...\n")
    print("- Type 'talk' near any reflective surface to interact and 'exit' to leave -\n")

def motion(to):
    global location
    location = (to)
    print("\n" + "The elevator doors open.")
    if location in undiscovered:
        print("\n" + rooms[location]["entrance"] + "\n")
        first_time()
        undiscovered.remove(location)
    else:
        print("\n" + rooms[location]["description"] + "\n")
        if rooms[location]["objects"]:
            print("You see: " + ", ".join(rooms[location]["objects"]) + "\n")


location = "front lawn"



look()

def game():
    while True:
        if end == True:
            return
        command = input().strip().lower()
        if command == "press g" and location == "elevator":
            motion("living room")
        elif command == "press 1" and location == "elevator":
            motion("hallway")
        elif command == "press 2" and location == "elevator":
            motion ("office")
        elif command == "look":
            look()
        elif command == "help":
            help()
        elif command in ["north", "south", "east", "west"]:
            move(command)

        elif command.split()[0] == "examine":
            examination(command.split()[1])

        elif command.split()[0] == "open":
            open(command.split()[1])

        elif command.split()[0] in ["take", "pickup"]:
            pickup(command.split()[1])

        elif command.split()[0] == "drop":
            drop(command.split()[1])

        elif command == "inventory":
            print(", ".join(inventory) + "\n")


        elif command == "talk" and location in ["bathroom", "elevator", "attic"]:
            if __name__ == "__main__":
                talk()


        elif command in ["stab", "stab him", "stab the man", "kill", "kill him", "kill the man", "end him", "finish him", "take his life"] and location == "living room":
            if "knife" in inventory:
                print("\nYou take out your knife.\n")
                print("In one swift motion, you take his life.\n")
                print("He's dead.\n")
                global life
                life = False
            else:
                print("\nYou don't have a weapon...\n")

        elif command == "quit":
            print("\n" + "Thanks for playing" + "\n")
            break
        else:
            print("\n" + "You don't understand that command" + "\n")


def start():
    class BreakAllLoops(Exception):
        pass

    try:
        while True:
            command = input().strip().lower()
            if command in ["ring doorbell", "ring the doorbell", "ring"]:
                print("\n" + "You ring the doorbell and wait for a few seconds, but no one comes to the door. Strange." + "\n" + "\n" + "As you examine the door in front of you, you notice that it is unlocked. Maybe you should enter and leave the food inside." + "\n" + "\n" + "Type 'north', 'south', 'east', and 'west' to move in the corresponding direction." + "\n")
                while True:
                    command2 = input().strip().lower()
                    if command2 == "north":
                        move("north")
                        print("As you enter the mansion, you immediately drop the food in shock as your eyes fall on a horrific sight. On the couch is a man lying in a pool of blood. He's not moving." + "\n" + "\n" + "As you move closer to inspect the body, you notice that the man is alive, just unconscious. He has what appears to be a stab wound on his neck, and he's bleeding heavily. Quick, cover the wound to stop the bleeding." + "\n")
                        while True:
                            command3 = input().strip().lower()
                            if command3 in ["cover wound", "cover the wound", "save him", "stop bleeding", "stop the bleeding", "save the man"]:
                                print("\n" + "You skillfully cover the wound and the bleeding stops. That's a job too well done for someone who works as a delivery guy, but whatever. Now's not the time to be thinking about stuff like that. You quickly call 911. They're on their way. You should probably wait outside. " + "\n")
                                while True:
                                    command4 = input().strip().lower()
                                    if command4 in ["south", "outside", "back", "go back", "get out"]:
                                        print("\n" + "You begin to head towards the exit, but the sudden sound of multiple alarms catches you off guard. In the blink of an eye, steel bars descend on all doors and windows. The mansion's security system has been triggered." + "\n" + "\n" + "You're trapped" + "\n" + "\n" + "There doesn't seem to be a way out, but the cops are already on the way. In the meantime, it wouldn't hurt to explore the house a little." + "\n" + "\n" + "Type 'help' at any time for a list of commands." + "\n")
                                        game()
                                        raise BreakAllLoops
                                    else:
                                        print("\n" + "You can't do that. Just get out for now." + "\n")
                            else:
                                print("\n" + "You can't do that. Maybe you should focus on stopping the bleeding." + "\n")
                    else:
                        print("\n" + "You can't do that" + "\n")
            else:
                print("\n" + "You can't do that." + "\n")
    except BreakAllLoops:
        pass

start()
