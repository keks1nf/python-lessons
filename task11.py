def main():
    with open("files\\input.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()

    good_students = []

    for line in lines:
        parts = line.split()
        surname = parts[0]
        grades = list(map(int, parts[2:]))
        average = sum(grades) / len(grades)

        if average > 6:
            good_students.append(surname)

    with open("files\\output.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(good_students))


if __name__ == "__main__":
    main()


