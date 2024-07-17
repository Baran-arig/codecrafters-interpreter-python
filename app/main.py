import sys


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!", file=sys.stderr)

    if len(sys.argv) < 3:
        print("Usage: ./your_program.sh tokenize <filename>", file=sys.stderr)
        exit(1)

    command = sys.argv[1]
    filename = sys.argv[2]

    if command != "tokenize":
        print(f"Unknown command: {command}", file=sys.stderr)
        exit(1)

    with open(filename) as file:
        file_contents = file.read()

    # Uncomment this block to pass the first stage
    if file_contents:
         #raise NotImplementedError("Scanner not implemented")
        line_number = 1
        error_flag = False
        for char in file_contents:
            if(char == '/n'):
                line_number += 1

            if (char == '('):
                print('LEFT_PAREN ( null')
            elif(char == ')'):
                print('RIGHT_PAREN ) null')
            elif(char == '{'):
                print('LEFT_BRACE { null')
            elif(char == '}'):
                print('RIGHT_BRACE } null')
            elif(char == ','):
                print('COMMA , null')
            elif(char == '.'):
                print('DOT . null')
            elif(char == '-'):
                print('MINUS - null')
            elif(char == '+'):
                print('PLUS + null')
            elif(char == ';'):
                print('SEMICOLON ; null')
            elif(char == '*'):
                print('STAR * null')
            else:
                error_flag = True
                print(f'[line {line_number}] Error: Unexpected character: {char}', file=sys.stderr)
                
        if(error_flag == True):
            print('EOF  null')
            sys.exit(65)

            
        print('EOF  null')
    else:
         print("EOF  null") # Placeholder, remove this line when implementing the scanner
         
    

if __name__ == "__main__":
    main()
