def main() -> None:
    with open("4-Ziaci.txt", "r") as f:
        rows = f.readlines()
        girl_count = int(rows[1])
        girls = []
        boys = []

        for i, row in enumerate(rows[2:]):
            if i < girl_count:
                girls.append(int(row.strip()))
            else:
                boys.append(int(row.strip()))

    girls = sorted(girls, reverse=True)
    boys = sorted(boys, reverse=True)
    avg_girls = round(sum(girls) / len(girls))
    avg_boys = round(sum(boys) / len(boys))
    avg_all = round((sum(girls) + sum(boys)) / (len(girls) + len(boys)))
    averages = [avg_girls, avg_boys, avg_all]

    with open("4-Ziaci.txt", "a") as f:
        f.write("\n".join(str(_) for _ in averages))
    
    print(f"priemerna vyska dievcat: {avg_girls}")
    print(f"priemerna vyska chlapcov: {avg_boys}")
    print(f"priemerna vyska triedy: {avg_all}")
    print(f"traja najvyssi chlapci: {", ".join(str(_) for _ in boys[0:3])}")
    print(f"tri najvyssie dievcata: {", ".join(str(_) for _ in girls[0:3])}")


if __name__ == "__main__":
    main()
