def greeter(first_name, last_name=''):
    if last_name == '':
        print(f"Hello, {first_name}.")
    else:
        print(f"Hello {first_name} {last_name}!")

first_name = input("Type first name ")
last_name = input("Type last name (Press Enter to skip) ")

greeter(first_name, last_name)