import sys
import os
import time
def draw(status_line,global_line,base_line):
    os.system('clear')
    score = 123
    #printing status_line
    for each in status_line:
        print('\033[1;31;40m {}'.format(each))
    #printing ----- line
    print('\033[1;37;40m-'*len(global_line[1]))
    #printing global_line
    for each in global_line:
        print(each)
    for each in base_line:
        print(each)

def qustion_area_maker(question_text):
    output_list = []
    i = 0
    while i < 5:
        output_list.append('|\033[33m '+ question_text[i] + ' '*(58-len(question_text[i])-1) + '\033[1;37;40m|')
        i += 1
    output_list.insert(0,'+'+'-'*58+'+')
    output_list.append('+'+'-'*58+'+')
    return output_list
def animation_draw(anim_lines,status_line,base_line):
    x = 0
    while x < 10:
        draw(status_line,anim_lines[x],base_line)
        time.sleep(0.05)
        x += 1
def draw_proccessing(text_area,user,man,heart,user_live,man_live,score,numbers,animation=False):
    global_line = []
    if not animation:
        status_line = []
        score = 'Score: ' + str(score)
        #add hearts of user
        heart_u = heart[0]*user_live+heart[1]*user_live
        heart_u = denester(heart_u,2,len(heart[0])*user_live)
        #add hearts of man
        heart_m = heart[0]*man_live+heart[1]*man_live
        heart_m = denester(heart_m,2,len(heart[0])*man_live)
        # by default line lenght = 93
        space1 = ' '*((93//2)-len(heart_u[0])-len(score))
        space2 = ' '*((93//2)-len(heart_m[0])-len(score))
        #making status_line
        status_line.extend(''.join(heart_u[0]+space1+score+space2+heart_m[0]+'H'))
        status_line.extend(''.join(' '+heart_u[1]+space1+' '*len(score)+space2+' '+heart_m[1]+'H'))
        status_line = denester(status_line,2,len(status_line)/2)

        base_line = []
        bullet_lines = []
        x = 0
        for each in numbers:
            bullet = []
            bullet.append('\033[31m|'+' '*((18//2)-len(str(each)))+str(each)+' '*((18//2)-len(str(each)))+'| \\')
            bullet.insert(0,'\033[31m '+'_'*((18//2)-len(str(each)))+'_'*len(str(each))+'_'*((18//2)-len(str(each)))+'_  ')
            bullet.append('\033[31m|'+'_'*((18//2)-len(str(each)))+'_'*len(str(each))+'_'*((18//2)-len(str(each)))+'|_/')
            bullet_lines.append(bullet)
        while x <3 :
            base_line.append(''.join(bullet_lines[0][x]+' '*8+bullet_lines[1][x]+' '*8+bullet_lines[2][x]))
            x += 1



    #making global_line
    for line in range(16):
        if line < 9:
            global_line.extend(''.join(user[line]+man[line]+'H'))

        else:

            global_line.extend(''.join(text_area[line-9]+man[line]+'H'))
    global_line = denester(global_line,16,len(global_line)/16)

    if animation:
        return global_line
    else:
        return status_line,global_line,base_line

def denester(asciistr,height,width):
    '''
    (string,int) -> list
    function slices an ascii docstring image into string lines
    >>> denester([--+--X\n--+--X],2)
    [['-', '-', '+', '-', '-'], ['-', '-', '+', '-', '-']]
    '''
    output_list = []
    asciistr = list(asciistr)
    i = 1
    ch = 0

    while i <= height:
        line = []
        while ch < width:
            if (asciistr[ch] == 'H'):
                break
            if (asciistr[ch] == '\\'):
                pass # a bug here with slash
            if (asciistr[ch] != '\n'):
                line.append(asciistr[ch])
            ch += 1

        ch += 1
        i += 1
        width *=2
        output_list.append(''.join(line))
    return output_list
