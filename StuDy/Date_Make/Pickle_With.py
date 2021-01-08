import pickle

with open("donggo.pickle", "rb") as profile:
    print(pickle.load(profile))

