def read_file(filename):
    with open("project5/intro.txt", "r") as file:
        intro = file.read()
        print(intro)
    with open("project5/instruction.txt", "r") as file:
        instruction = file.read()
        print(instruction)
    with open("project5/mission0.txt", "r") as file:
        mission0 = file.read()
    with open("project5/mission1.txt", "r") as file:
        mission1 = file.read()
    with open("project5/mission2.txt", "r") as file:
        mission2 = file.read()
    with open("project5/mission3.txt", "r") as file:
        mission3 = file.read()
    with open("project5/mission4.txt", "r") as file:
        mission4 = file.read()
    with open("project5/mission5.txt", "r") as file:
        mission5 = file.read()
    with open("project5/score.txt", "r") as file:
        saved_score = file.read()