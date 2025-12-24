class Friend:
    def __init__(self, name: str, phone: str, name_day_day: int, name_day_month: int) -> None:
        self.name = name
        self.phone = phone
        self.name_day_day = name_day_day
        self.name_day_month = name_day_month

    def __str__(self) -> str:
        return f"{self.name}: {self.name_day_day}.{self.name_day_month}."
    

def print_friends(friends: list[Friend]) -> None:
    print("PRIATELIA:")
    print("\n".join(str(friend) for friend in friends))

def main() -> None:
    friends = []

    with open("Kamosi.txt", "r") as f:
        for line in f.readlines():
            values = line.split(";")
            numbers = values[1].split()

            friends.append(Friend(values[0], numbers[0], int(numbers[1]), int(numbers[2])))

    friends = sorted(friends, key=lambda p: (p.name_day_month, p.name_day_day))

    print_friends(friends)

    months = {key: 0 for key in range(1, 13)}
    
    for friend in friends:
        months[friend.name_day_month] += 1

    print()
    print("\t".join(str(key) for key in months.keys()))
    print("\t".join(str(count) for count in months.values()))

    month = int(input("\nzadajte mesiac, pre ktory chcete zistit, kto ma meniny: "))
    friends_to_show = [friend for friend in friends if friend.name_day_month == month]

    print(", ".join(str(friend) for friend in friends_to_show)) if len(friends_to_show) > 0 else print("v zadanom mesiaci nema meniny nikto")

    friend_given = input("\nzadajte meno priatela na vymazanie: ")

    for friend in friends:
        if friend.name == friend_given:
            print(f"priatel {friend_given} bol odstraneny\n")
            friends.remove(friend)
            break
    else:
        print(f"priatel {friend_given} nebol najdeny, a preto ani nebol odstraneny\n")

    print_friends(friends)

    phone = input("\nzadajte telefonne cislo na vyhladanie: ")

    for friend in friends:
        if friend.phone == phone:
            print(friend)
            break
    else:
        print("zadany priatel nebol najdeny")


if __name__ == "__main__":
    main()
