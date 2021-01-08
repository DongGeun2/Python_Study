# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요")


# with open("donggo.txt", "r") as study_file:
#     print(study_file.read())


with open("score.txt", "r") as f:
    score = []
    for line in f:
        score.append(int(line))
    print(score)

print("Avreage : {:6.3}".format(sum(score)/len(score)))


with open("text.txt", "w") as f:
    f.write("niceman!\n")

with open("text.txt", "a") as f:
    f.write("goodman!\n")

from random import randint

with open("text2.txt", "w") as f:
    for cnt in range(6):
        f.write(str(randint(1, 50)))
        f.write("\n")




with open("text3.txt", "w") as f:
    list = ["kim\n", "park\n", "cho\n"]
    f.writelines(list)
    


