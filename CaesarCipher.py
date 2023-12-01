choose = input(f"You chose encode or decode: ").lower()
if choose == "encode":
    password = ""
    encrypt_code = input("Type your message: ").lower()
    shift_number = int(input("Type your shift number: "))
    for i in encrypt_code:
        password = password + chr(ord(i)+shift_number)
    print(f"Your password is {password}")
elif choose == "decode":
    message = ""
    solve_code = (input("Type your password: "))
    shift_number = int(input("Type your shift number: "))
    for i in solve_code:
        message = message + chr((ord(i)-shift_number))
    print(f"Your massage is {message}")