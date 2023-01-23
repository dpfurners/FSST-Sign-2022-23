# Manager Project
# Primfaktorzerlegung
# Dominik -> Manager
# Daniel -> Programmer

try:
    print("A small Program to divide a number into its Primefactors.\n")
    while True:
        factors = []
        valid_num = None
        updated_num = None
        if valid_num is None:
            try:
                valid_num = int(input("Please insert a number: "))
            except ValueError:
                print(f"Please insert a valid number ({valid_num} is not valid)")
                valid_num = None
                continue
        updated_num = valid_num
        """"""
        current_factor = 2
        while True:
            while (int(updated_num) % current_factor) == 0:
                factors.append(current_factor)
                updated_num /= current_factor
            else:
                if int(updated_num) == 1:
                    break
                current_factor += 1
                continue
        print(f"The primefactors of {valid_num} = {' * '.join(map(str, factors))}")
except KeyboardInterrupt:
    print("Bye!")
