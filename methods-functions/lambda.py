full_name = lambda first_name, last_name: f'{first_name} {last_name}'

def greeting(name):
    print(f"Hi, {name}")

greeting(full_name('Brian', 'Kozub'))