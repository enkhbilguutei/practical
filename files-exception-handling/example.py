def main(): 
    try: 
        number1, number2 = eval (
            input("Enter two number, separeted by a comma:"))
        result = number1 / number2 
        print("Result is", result)
    except ZeroDivisionError:
        print("Division by zero")
    except SyntaxError:
        print("A omma may be missing in the input")
    except:
        print("Something wrong in the input")
    else:
        print("No exceptions")
    finally:
        print("The finally clause is executed")
main()       