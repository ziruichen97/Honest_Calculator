def is_one_digit(v):
    return True if -10 < v < 10 and v.is_integer() else False


def check(v1, v2, v3):
    msg = ""
    msg += msgs[6] if is_one_digit(v1) and is_one_digit(v2) else ""
    msg += msgs[7] if (v1 == 1 or v2 == 1) and v3 == "*" else ""
    msg += msgs[8] if (v1 == 0 or v2 == 0) and (v3 in "+-*") else ""
    print((msgs[9] + msg) if msg != "" else msg)


# operation using dict,
# lambda: an anonymous function,
#         which means it is a function only with one expression so does not need a name.
#         It makes the code shorter and more readable
# input1, input2: function(input1, input2) -> the result will return automatically
operation = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y
}


def store_result(result):
    global memory
    while True:
        ans = input(msgs[4])
        if ans in 'yn':
            if ans == 'y':
                if is_one_digit(result) is True:
                    msg_index = 10
                    while msg_index <= 12:
                        ans = input(msgs[msg_index])
                        if ans in "yn":
                            if ans == 'y':
                                if msg_index == 12:
                                    memory = result
                                    break
                                msg_index += 1
                            else:
                                break
                else:
                    memory = result
            break
            # The while loops breaks when it receives "y" or "n",
            # thus writing only one break here instead multiple in the loop
            # optimizes the beauty and readability of the code.


def check_continuation():
    while True:
        ans = input(msgs[5])
        if ans in 'yn':
            if ans == 'y':
                return True
            else:
                return False


def calculation():
    global memory
    while True:
        x, oper, y = input(msgs[0]).split(" ")
        try:
            x = memory if x == "M" else float(x)
            y = memory if y == "M" else float(y)
        except ValueError:
            # - A ValueError occurs when a built-in operation or function receives
            #   an argument that has the right type but an inappropriate value
            #   This type of inaccuracy is most common in mathematical operations.
            #   For example: float("5.0") is ok but float("A") is not possible;
            #                In float("A") case:
            #                   The float function takes in a right type of argument,
            #                   which is string, but it cannot run because the value
            #                   of the string "A" is wrong.
            #                   "A" cannot be converted into float.
            # - A TypeError, is raised when an operation receives an incorrect or unsupported object type.
            #   For example: float(["5"]) returns TypeError, because float() function does not
            #   take in list type as an argument
            print(msgs[1])
            continue
        try:
            result = operation[oper](x, y)
            # operation = {
            #   "+": lambda x, y: x + y,
            #   "-": lambda x, y: x - y,
            #   "*": lambda x, y: x * y,
            #   "/": lambda x, y: x / y
            # }
            # operation here is a dictionary, it takes in the operand as the key,
            # then the lambda function inside requires two value x, y, so they were passed in with (x,y)
            # For example: operation["+"](5.0, 3.0)
            #              -> operation["+"] = lambda x, y: x + y
            #              -> we need to pass in two value x, y,
            #              -> the value is passed in with (x,y), which makes:
            #              ->  f(x,y):
            #              ->    return x + y
            # lambda is often used with python built-in function such as filter() and map()
            # For example:
            #   Code: (lambda used with filter())
            #       number = [1,2,3,5,4,6,8,9,11,12]
            #       multiples_of_4 = list(filter(lambda a: a % 4 == 0 ,number))
            #           # filter here is an iterator, so it requires list comprehension
            #           # in list function to generate a corresponding list
            #       print(multiples_of_4)
            #   Return:
            #       [4, 8, 12]
            #   Code: (lambda used with map())
            #       number = [5,10,15,20]
            #       new_number = list(map(lambda c: c/5 ,number))
            #           # same as filter, map here is also an iterator, so it requires list comprehension
            #           # in list function to generate a corresponding list
            #       print(new_number)
            #   Return:
            #       [1.0,2.0,3.0,4.0]
            # For more on lambda -> https://pythonguides.com/python-list-comprehension/
            # For more on filter -> https://docs.python.org/3.9/library/functions.html#filter
            # For more on map -> https://docs.python.org/3.9/library/functions.html#map
            # For more on iterator -> https://www.w3schools.com/python/python_iterators.asp
        except KeyError:
            # KeyError occurs when dictionary cannot find the value in keys
            print(msgs[2])
            continue
        except ZeroDivisionError:
            # ZeroDivisionError occurs when the division is zero
            print(msgs[3])
            continue
        check(x, y, oper)
        print(result)
        store_result(result)
        if check_continuation() is False:
            break


# calling main, good habit
if __name__ == "__main__":
    memory = 0
    # set all the messages as dict, so time complexity is O(1), for list time complexity will be O(n)
    msgs = {
        0: "Enter an equation",
        1: "Do you even know what numbers are? Stay focused!",
        2: "Yes ... an interesting math operation. You've slept through all classes, haven't you?",
        3: "Yeah... division by zero. Smart move...",
        4: "Do you want to store the result? (y / n):",
        5: "Do you want to continue calculations? (y / n):",
        6: " ... lazy",
        7: " ... very lazy",
        8: " ... very, very lazy",
        9: "You are",
        10: "Are you sure? It is only one digit! (y / n)",
        11: "Don't be silly! It's just one number! Add to the memory? (y / n)",
        12: "Last chance! Do you really want to embarrass yourself? (y / n)",
    }
    calculation()
