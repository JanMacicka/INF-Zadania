class Reaction:
    def __init__(self, hour: int, minute: int, positive: bool) -> None:
        self.hour = hour
        self.minute = minute
        self.positive = positive

reactions = []
hours = {}
days = []

with open("Spokojnost.txt", "r", encoding="utf-8") as f:
    for line in f.readlines():
        values = line.split()
        time = values[0].split(":")
        hour = int(time[0])
        minute = int(time[1])
        positive = values[1] == "áno"

        reactions.append(Reaction(hour, minute, positive))

print(f"pocet vsetkych vyjadreni: {len(reactions)}\n")

for i, reaction in enumerate(reactions):
    if reaction.hour in hours.keys():
        hours[reaction.hour] += 1
    else:
        hours[reaction.hour] = 1

    if i > 0:
        if reactions[i].hour < reactions[i - 1].hour or (reactions[i].hour == reactions[i - 1].hour) and (reactions[i].minute < reactions[i - 1].minute):
            days.append(1)
        else:
            days[-1] += 1
    else:
        days.append(1)


for hour in sorted(hours):
    print(f"{hour}. hodina: {hours[hour]}")

print(f"\npocet dni: {len(days)}\n")

for i, day in enumerate(days):
    print(f"{i + 1}. den: {day} reakcii")