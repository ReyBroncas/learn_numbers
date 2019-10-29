import copy
import random

def sequence_cut(input_list, difficulty):

    for each in copy.copy(input_list):
        if each < difficulty[0]:
            input_list.remove(each)
        if each > difficulty[-1]:
            input_list.remove(each)
    return input_list

def lucky_numbers(difficulty):

    raw = []
    lucky_raw = []
    def eliminator(raw,step):
        i = 0
        output_list = []
        while i < len(raw):
            if ((i+1) % (step) != 0):
                output_list.append(raw[i])
            i += 1
        return output_list
    for each in range(1,difficulty[-1],2):
        raw.append(each)
    f = 1
    while 1:
        raw = eliminator(raw,raw[f])
        if raw == eliminator(raw,raw[f]):
            break
        f += 1
    raw = sequence_cut(raw,difficulty)
    return [raw[random.randrange(len(raw))],raw]

def prime_numbers(difficulty):
    figures = []
    for i in range(difficulty[1] + 1):
        figures.append(i)

    prime_numbers = []
    for number in range(len(figures)):
        if (number == 1) or (number == 2):
            prime_numbers.append(number)
        else:
            count = 2
            while count <= number:
                if count == number:
                    prime_numbers.append(number)
                    break
                if number % count == 0:
                    break
                else:
                    count += 1
                    continue
    prime_numbers = sequence_cut(prime_numbers,difficulty)
    return [prime_numbers[random.randrange(len(prime_numbers))],prime_numbers]

def ulam_numbers(difficulty):
    arr = [1,2]
    arr2 = set()
    arr2.add(1)
    arr2.add(2)
    for i in range(3, difficulty[-1]):
        if len(arr) == difficulty[-1]:
            break
        count = 0
        for j in range(0, len(arr)):
            if (i - arr[j]) in arr2 and arr[j] != (i - arr[j]):
                count += 1
            if count > 2:
                break
        if count == 2:
            arr.append(i)
            arr2.add(i)
    arr = sequence_cut(arr,difficulty)
    return [arr[random.randrange(len(arr))],arr]

def input_validator(x):
    try:
        x = int(x)
        if x>0:
            return True
        else:
            print("The number can't be negative")
            return False
    except:
        print("Please enter digits, not symbols")
        return False

def choose_difficulty():
    print("Choose difficulty from 1 to 3 [1 -> EASY ; 2 -> NORMAL ; 3 -> HARD]")           #    <-  Ілюстрації до складності на весь екран
    game_difficulty = input()
    if input_validator(game_difficulty)==True:
        game_difficulty = int(game_difficulty)
        if (game_difficulty>=1) and (game_difficulty<=3):
            return game_difficulty
    else:
        return 1

def randomize_number_output(num1,num2,num3):
    number_list = [(num1,1),(num2,2),(num3,3)]
    return number_list[random.randint(0,len(number_list)-1)]
