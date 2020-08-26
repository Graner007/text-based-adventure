import sys
from sty import fg, rs

def invalid_text(ask):
    if ask != 'quit':
        print(fg(255,10,10)+'Invalid choice, you lost!'+fg.rs)

def main():
    ask = input(fg(255,255,10)+'Would you like to play with me? '+fg.rs).lower().strip()
    if ask == 'quit':
        print("Good-bye!")
        sys.exit()
    if ask == "yes":
        print(fg(255,255,10)+'\nAll right, then...'+fg.rs)
        ask = input(fg(255,255,10)+'You reach a crossroads, would you like to go left or right? '+fg.rs).lower().strip()
        if ask == "left":
            ask = input(fg(255,255,10)+'\nYou encounter a monster, wuold you like to run or attack? '+fg.rs)
            if ask == "attack":
                print(fg(255,10,10)+'That was not the greatest idea, you lost!'+fg.rs)
            elif ask == "run":
                print(fg(255,255,10)+'\nGood choice, you made it away safely'+fg.rs)
                ask = input(fg(255,255,10)+'You see a car and a plane, which would you like to take? '+fg.rs)
                if ask == "plane": 
                    print(fg(255,10,10)+'You do not know how to fly, you lost!'+fg.rs)
                elif ask == 'car':
                    print(fg(10,255,10)+'You won!'+fg.rs)
                else:
                    invalid_text(ask)
            else:
                invalid_text(ask)
        elif ask == "right":
            print(fg(255,10,10)+'You got a knife into your back, you lost!'+fg.rs)
        else:
            invalid_text(ask)
    elif ask == "no":
        print(fg(255,10,10)+"That's to bad!"+fg.rs)
    else:
        invalid_text(ask)

if __name__ == '__main__':
    print(fg(255,127,80)+"Hello my friend, welcome to the Text Based Adventure game!\n"+fg.rs)
    main()