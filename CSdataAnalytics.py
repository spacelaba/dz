import json
import os.path


def stat_input(prompt):
    # Repeat until a number is writen
    while True:
        val = input(prompt)
        if val.isdigit():
            val = int(val)
            return val
        print("[Invalid input.]")


choice = ""
print("------CS Stats Reader------")
while choice != "0":
    print("\n1 - read stats\n2 - write stats\n0 - exit\n")
    choice = input("Your choice: ")

    if choice == "1":
        if not os.path.isfile("stats.json"):
            print("No stats have been written yet.")
        else:
            with open("stats.json", "r") as outfile:
                stats = json.load(outfile)
            print("Games played: " + str(stats["games"]))
            print("Kills performed: " + str(stats["kills"]))
            print("Deaths occured: " + str(stats["deaths"]))

    elif choice == "2":
        # No idea what stats are there in cs, who knows please add more if needed
        stats = {
            "games": stat_input("Input the amount of games played: "),
            "kills": stat_input("Input the amount of kills performed: "),
            "deaths": stat_input("Input the amount of deaths that occurred: "),
        }

        with open("stats.json", "w") as outfile:
            outfile.write(json.dumps(stats))

        print()

    elif choice != "0":
        print("[Invalid choice.]")

    print("\n---------------------------")
