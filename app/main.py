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
        i=0
        while i < len(file_contents):
            if(file_contents[i] == '\n'):
                line_number += 1

            elif (file_contents[i] == '('):
                print('LEFT_PAREN ( null')
            elif(file_contents[i] == ')'):
                print('RIGHT_PAREN ) null')
            elif(file_contents[i] == '{'):
                print('LEFT_BRACE { null')
            elif(file_contents[i] == '}'):
                print('RIGHT_BRACE } null')
            elif(file_contents[i] == ','):
                print('COMMA , null')
            elif(file_contents[i] == '.'):
                print('DOT . null')
            elif(file_contents[i] == '-'):
                print('MINUS - null')
            elif(file_contents[i] == '+'):
                print('PLUS + null')
            elif(file_contents[i] == ';'):
                print('SEMICOLON ; null')
            elif(file_contents[i] == '*'):
                print('STAR * null')
            elif(file_contents[i] =='='):
                if( i < len(file_contents)-1) and file_contents[i+1] == '=':
                    i+=1
                    print('EQUAL_EQUAL == null')

                else:
                    print('EQUAL = null')
            
            elif(file_contents[i] =='!'):
                if( i < len(file_contents)-1) and file_contents[i+1] == '=':
                    i+=1
                    print('BANG_EQUAL != null')
                    
                else:
                    print('BANG ! null')

            elif(file_contents[i] == '<'):
                if(i < len(file_contents)-1 and file_contents[i+1] == '='):
                    i+=1
                    print('LESS_EQUAL <= null')
                
                else:
                    print('LESS < null')

            elif(file_contents[i] == '>'):
                if(i < len(file_contents)-1 and file_contents[i+1] == '='):
                    i+=1
                    print('GREATER_EQUAL >= null')
                
                else:
                    print('GREATER > null')

            elif(file_contents[i] == '/'):
                if(i < len(file_contents)-1 and file_contents[i+1] == '/'):
                    i+=1
                    while(i < len(file_contents)-1 and file_contents[i] != '\n'):
                        i+=1
                    line_number += 1
                
                else:
                    print('SLASH / null')

            elif(file_contents[i] == ' ' or file_contents[i] == '\t'):
                #i+=0
                pass
                #continue

            elif(file_contents[i] == '"'):
                i+= 1
                string = ''
                terminateFlag = False
                #counter = 0
                while(i < len(file_contents)):

                    
                    if(file_contents[i] == '"'):
                        print(f'STRING "{string}" {string}')
                        terminateFlag = True
                        break

                    #if(i >= len(file_contents)):
                        

                    string += file_contents[i]
                    i+=1
                if(not terminateFlag):
                    error_flag = True
                    print(f'[line {line_number}] Error: Unterminated string.', file=sys.stderr)

            elif(file_contents[i].isnumeric() ):
                num = ''
                decimalValue = False
                decimalPlaces = 0

                while(i <= len(file_contents)-1 and (file_contents[i].isnumeric() or file_contents[i] == '.') ):
                    if(file_contents[i] =='.' and decimalValue):
                        i-=1
                        break
                    if(file_contents[i] =='.'):
                        decimalValue = True
                    
                    if(decimalValue):
                        decimalPlaces += 1

                    num += file_contents[i]
                    i+= 1
                '''
                if(not num[-1].isnumeric()):
                    num = num[:-1]
                    i-=2
                '''
                num = float(num)
                #print(num.is_integer)
                if(not decimalValue):
                    #num = num[:-1]
                    #i-=1
                    print(f'NUMBER {int(num)} {int(num)}.0')
                else:
                    print(f'NUMBER {num:.{decimalPlaces-1}f} {num}')
                i-=1

                
                

                

            
            else:
                error_flag = True
                print(f'[line {line_number}] Error: Unexpected character: {file_contents[i]}', file=sys.stderr)
            i+=1
                
        if(error_flag):
            print('EOF  null')
            sys.exit(65)
        
            

            
        print('EOF  null')
    else:
         print("EOF  null") # Placeholder, remove this line when implementing the scanner
         
    

if __name__ == "__main__":
    main()
