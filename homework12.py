# ###
# def main():
#     with open("files\\input.txt", "r", encoding="utf-8") as f:
#         lines = f.readlines()
#
#     good_students = []
#
#     for line in lines:
#         parts = line.split()
#         surname = parts[0]
#         grades = list(map(int, parts[2:]))
#         average = sum(grades) / len(grades)
#
#         if average > 6:
#             good_students.append(surname)
#
#     with open("files\\output.txt", "w", encoding="utf-8") as f:
#         f.write("\n".join(good_students))
#
#
# if __name__ == "__main__":
#     main()
#


#1
# def merge_files(output_filename: str, *input_filenames: str):
#     with open(output_filename, 'w', encoding='utf-8') as outfile:
#         for fname in input_filenames:
#             try:
#                 with open(fname, 'r', encoding='utf-8') as infile:
#                     outfile.write(infile.read())
#                     outfile.write("\n")
#             except FileNotFoundError:
#                 print(f"Помилка: файл '{fname}' не знайдено.")
#             except Exception as e:
#                 print(f"Помилка при читанні файлу '{fname}': {e}")
#     print(f"Вміст файлів об’єднано у '{output_filename}'.")
#
#
# merge_files("files\\merged.txt", "files\\file1.txt", "files\\file2.txt", "files\\file3.txt")

#2
# def show_list_elements():
#     try:
#         user_input = input("Введіть елементи списку через кому: ")
#         items = [item.strip() for item in user_input.split(',')]
#
#         print("\nСписок з індексами:")
#         for i in range(len(items)):
#             print(f"Індекс {i}: {items[i]}")
#
#     except IndexError:
#         print("Помилка:  індексу не існує у списку.")
#     except ValueError:
#         print("Помилка: потрібно вводити числа для індексу.")
#
# show_list_elements()

#3
# def read_file(filename):
#     try:
#         with open(filename, "r", encoding="utf-8") as file:
#             content = file.read()
#             print("Вміст файлу:\n")
#             print(content)
#     except FileNotFoundError:
#         print(f"Помилка: файл '{filename}' не знайдено.")
#
# filename = input("Введіть назву файлу для відкриття: ")
# read_file(filename)
#4
def olympiad_results(input_file, output_file):
    winners = {9: 0, 10: 0, 11: 0}

    try:
        with open(input_file, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split()
                if len(parts) < 3:
                    continue

                grade = int(parts[-2])
                score = int(parts[-1])


                if score > winners[grade]:
                    winners[grade] = score


        with open(output_file, "w", encoding="utf-8") as f_out:
            f_out.write(f"{winners[9]} {winners[10]} {winners[11]}")

        print("Результати записано у файл", output_file)

    except FileNotFoundError:
        print(f"Помилка: файл '{input_file}' не знайдено.")


olympiad_results("files\\input.txt", "files\\output1.txt")
