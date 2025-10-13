workers = [
    {
        'name': 'Петро Петров',
        'age': 30,
        'job': 'Безробітний',
        'skills': ['Python', 'HTML CSS']
    },
    {
        'name': 'Ольга Ольгова',
        'age': 27,
        'job': 'Meta inc.',
        'skills': ['C', 'C++', 'C#', 'Assembler']
    },
    {
        'name': 'Денис Денисов',
        'age': 45,
        'job': 'Google inc.',
        'skills': ['Python', 'Django', 'Flask']
    }
]

for worker in workers:
    print(f"{worker['name']}, {worker['age']} років")
    print(f"  Місце роботи: {worker['job']}")
    print(f"  Навички:")
    for skill in worker["skills"]:
        print(f'     {skill}')
    print('-'* 30)

print('\n'.join(f'{index}. {worker['name']}, {worker['age']} років:\n\t-Місце роботи: {worker['job']}\n\t-Навички:\n{'\n'.join(f'\t\t-{skill}' for skill in worker['skills'])}' for index, worker in enumerate(workers, start=1)))
