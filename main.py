# Program make a simple calculator
import simpCal
import logging

def askToquit(): #종료 함수
    while True:
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation.lower() == "no":
            next_calculation = input("Are you sure? (yes/no): ")
            if next_calculation.lower() == "yes":
                break

            elif next_calculation.lower() == "no":
                return 1

            elif next_calculation.lower() != "no":
                print(next_calculation + " ?")

        elif next_calculation.lower() == "yes":
            return 1

        elif next_calculation.lower() != "yes":
            print(next_calculation + " ?")
    return 0
#기록 형식
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#로그 파일 사용 설정
logger1 = logging.getLogger("Record_Calc")
logger1.setLevel(logging.DEBUG)

fileHandler1 = logging.FileHandler(filename = '../Users/사용자/Documents/GitHub/Midproject_simpleCalc/calcRec.log', mode = "a")
fileHandler1.setFormatter(formatter)
logger1.addHandler(fileHandler1)

logger2 = logging.getLogger("Record_Error")
logger2.setLevel(logging.DEBUG)

fileHandler2 = logging.FileHandler(filename = '../Users/사용자/Documents/GitHub/Midproject_simpleCalc/wrongRec.log', mode = "a")
fileHandler2.setFormatter(formatter)
logger2.addHandler(fileHandler2)

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide") 

while True:
    choice = input("Enter choice(1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", simpCal.add(num1, num2))
            str = num1, "+", num2, "=", simpCal.add(num1, num2)
            logger1.debug(str)

        elif choice == '2':
            print(num1, "-", num2, "=", simpCal.subtract(num1, num2))
            str = num1, "-", num2, "=", simpCal.subtract(num1, num2)
            logger1.debug(str)

        elif choice == '3':
            print(num1, "*", num2, "=", simpCal.multiply(num1, num2))
            str = num1, "*", num2, "=", simpCal.multiply(num1, num2)
            logger1.debug(str)

        elif choice == '4':
            while True:
                if num2 != 0:
                    break
                print("This is Divide by zero error")
                num2 = float(input("Enter second number: "))
                logger2.error('Divide by zero error')
                
            print(num1, "/", num2, "=", simpCal.divide(num1, num2))
            str = num1, "/", num2, "=", simpCal.divide(num1, num2)
            logger1.debug(str)

        if(askToquit() == 0):
            break

    else:
        print("Invalid Input") 
        logger2.error('Invalid Input')
