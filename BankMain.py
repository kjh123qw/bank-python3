# -*- coding:utf-8 -*-
'''
Created on 2020. 1. 31.

@author: kosmo-18
'''

import pickle

customerList = {}


def main():
    """main method"""
    loadInfo()
    while 1:
        print("-" * 80)
        print("MAIN MENU")
        print("{:12}\n{:12}\n{:12}\n{:12}\n{:12}".format("1.create account",
                                                         "2.depositn", "3.withdraw", "4.list print", "0.exit"))
        print("please select menu >> ", end="")
        inp = input()
        if(valInput(inp, int, 4)):
            if(inp.__eq__("1")):
                createAcc()
            elif(inp.__eq__("2")):
                deposit()
            elif(inp.__eq__("3")):
                withdraw()
            elif(inp.__eq__("4")):
                printInfo()
            elif(inp.__eq__("0")):
                print("Thank you~!")
                break
        else:
            print("wrong input")


def createAcc():
    """create account method"""
    global customerList
    step = 0
    account = ""
    name = ""
    curMoney = 0
    grade = ""
    rate = 0.0
    orgMoney = 0
    ratMoney = 0
    accType = ""
    print("-" * 80)
    print("main menu > create account")
    print(" * Account is 8 letters. higher than 10000001")
    print(" * Name is minimum 2 letters, maximum 5 letters.")
    print(" * Start deposit is higher than 1,000, less than 10,000,000")
    print(" * Interest rate is higher than 0.0, less than 20.0 without \"%\" signal")
    print(" * Credit rating has to select one of \"A\", \"B\", \"C\"")
    while 1:
        if(step == 0):
            print("-" * 80)
            print("main menu > create account > account type")
            print("{:12}\n{:12}".format("1.normal account", "2.credit account"))
            print("please select menu [x:main menu] >> ", end="")
            inp = input()
            if(inp.__eq__("x")):
                break
            elif(valInput(inp, int, 2, 1)):
                if(inp.__eq__("1")):
                    accType = "Common"
                elif(inp.__eq__("2")):
                    accType = "Credit"
                step = 1
            else:
                print("  Err - wrong input")
        elif(step == 1):
            print("-" * 80)
            if(accType.__eq__("Common")):
                print("[create normal account]")
            else:
                print("[create credit account]")
            print("account number(8 numbers) [x:main menu] >> ", end="")
            inp = input()
            if(inp.__eq__("x")):
                break
            elif(inp.__eq__("b")):
                step = 0
            else:
                if(valInput(inp, int, 99999999, 10000001)):
                    if(accType.__eq__("Common")):
                        account = "2020-" + inp
                    else:
                        account = "2030-" + inp
                    if(len(customerList) == 0 or not account in customerList.keys()):
                        step = 2
                    else:
                        print("  Err - already exist same account number")
                else:
                    print("  Err - wrong input")
        elif(step == 2):
            print("name [x:main menu b:previous step] >> ", end="")
            inp = input()
            if(inp.__eq__("x")):
                break
            elif(inp.__eq__("b")):
                step = 1
            else:
                if(valInput(inp, str, 5, 1)):
                    name = inp
                    step = 3
                else:
                    print("  Err - wrong input")
        elif(step == 3):
            print(
                "start deposit money [x:main menu b:previous step] >> ", end="")
            inp = input()
            if(inp.__eq__("x")):
                break
            elif(inp.__eq__("b")):
                step = 2
            else:
                if(valInput(inp, int, 10000000, 1000)):
                    curMoney = int(inp)
                    step = 4
                else:
                    print("  Err - wrong input")
        elif(step == 4):
            print("interest rate [x:main menu b:previous step] >> ", end="")
            inp = input()
            if(inp.__eq__("x")):
                break
            elif(inp.__eq__("b")):
                step = 3
            else:
                if(valInput(inp, float, 20.0, 0.0)):
                    rate = float(inp)
                    if(accType.__eq__("Common")):
                        grade = "-"
                        step = 6
                    else:
                        step = 5
                else:
                    print("  Err - wrong input")
        elif(step == 5):
            print("credit rate [x:main menu b:previous step] >> ", end="")
            inp = input()
            if(inp.__eq__("x")):
                break
            elif(inp.__eq__("b")):
                step = 4
            else:
                if(inp.__eq__("A") or inp.__eq__("B") or inp.__eq__("C")):
                    grade = inp
                    step = 6
                else:
                    print("  Err - wrong input")
        elif(step == 6):
            print("-" * 80)
            print("[input information]")
            print("{:^14} {:^7} {:^14} {:^7} {:^5} {:^14} {:^14}".format(
                "Account", "Name", "Current Money", "Grade", "Rate", "Original Money", "Rate Money"))
            print("{:14} {:^7} {:14,d} {:^7} {:5.1f} {:14,d} {:14,d}".format(
                account, name, curMoney, grade, rate, orgMoney, ratMoney))
            print("{:7} Do you want to save this? [y:save x:main menu b:previous step] >> ".format(
                name), end="")
            inp = input()
            if(inp.__eq__("x")):
                break
            elif(inp.__eq__("b")):
                step = 5
            elif(inp.__eq__("y")):
                step = 7
            else:
                print("  Err - wrong input")
        elif(step == 7):
            print("  Msg - Completed to save")
            cst = Customer(account, name, curMoney, grade,
                           rate, orgMoney, ratMoney)
            customerList[account] = cst
            saveInfo()
            break


def deposit():
    """deposit method"""
    global customerList
    step = 0
    sendAccount = ""
    getAccount = ""
    sendingMoney = 0
    print("-" * 80)
    print("main menu > remittance")
    print(" * A remittance money is higher than 1,000, less than 99,999,999")
    while 1:
        if(step == 0):
            print("deposit accountnumber [x:main menu] >> ", end="")
            inp = input()
            if(inp.__eq__("x")):
                break
            else:
                if(valInput(inp, str, 13, 12)):
                    if(inp in customerList.keys()):
                        getAccount = inp
                        step = 1
                    else:
                        print("  Err - there is no account number.")
                else:
                    print("  Err - wrong input")
        elif(step == 1):
            print(
                "withdraw account number [x:main menu b:previous step] >> ", end="")
            inp = input()
            if(inp.__eq__("x")):
                break
            elif(inp.__eq__("b")):
                step = 0
            else:
                if(valInput(inp, str, 13, 12)):
                    if(inp in customerList.keys()):
                        if(not getAccount.__eq__(inp)):
                            sendAccount = inp
                            step = 2
                        else:
                            print("  Err - it same the deposit account number.")
                    else:
                        print("  Err - there is no account number.")
                else:
                    print("  Err - wrong input")
        elif(step == 2):
            print(
                "remittance how much [x:main menu b:previous step] >> ", end="")
            inp = input()
            if(inp.__eq__("x")):
                break
            elif(inp.__eq__("b")):
                step = 1
            else:
                if(valInput(inp, int, 99999999, 1000)):
                    if(customerList[sendAccount].curMoney >= 1000):
                        if(valInput(inp, int, customerList[sendAccount].curMoney, 1000)):
                            sendingMoney = int(inp)
                            step = 3
                        else:
                            print(
                                "  Err - not enough. you can withdraw {:,d}.".format(customerList[sendAccount].curMoney))
                    else:
                        print("  Err - there is less than 1,000 in the account.")
                else:
                    print("  Err - wrong input")
        elif(step == 3):
            print("-" * 80)
            print("[input information]")
            print("{:^14} {:^14} {:^10} {:^14}".format(
                "", "Account", "Name", "Money"))
            print("{:14} {:14} {:10} -{:13,d}".format("Send Account",
                                                      sendAccount, customerList[sendAccount].name, sendingMoney))
            print("{:14} {:14} {:10} +{:13,d}".format("Get Account",
                                                      getAccount, customerList[getAccount].name, sendingMoney))
            print(
                "Do you want to remit? [y:yes x:main menu b:previous step] >> ", end="")
            inp = input()
            if(inp.__eq__("x")):
                break
            elif(inp.__eq__("b")):
                step = 2
            elif(inp.__eq__("y")):
                step = 4
            else:
                print("  Err - wrong input")
        elif(step == 4):
            customerList[sendAccount].curMoney -= sendingMoney
            customerList[getAccount].curMoney += sendingMoney
            print("  Msg - {:,d} completed to remit.".format(sendingMoney))
            print("{:^14} {:^14} {:^10} {:^14}".format(
                "", "Account", "Name", "Money"))
            print("{:14} {:14} {:10} {:14,d}".format("Send Account", sendAccount,
                                                     customerList[sendAccount].name, customerList[sendAccount].curMoney))
            print("{:14} {:14} {:10} {:14,d}".format("Get Account", getAccount,
                                                     customerList[getAccount].name, customerList[getAccount].curMoney))
            step = 0
            saveInfo()
            print("-" * 80)


def withdraw():
    """withdraw method"""
    global customerList
    step = 0
    trgAccount = ""
    wdrMoney = 0
    print("-" * 80)
    print("main menu > withdraw")
    print(" * The withdraw is higher than 10,000")
    while 1:
        if(step == 0):
            print("withdraw account number [x:main menu] >> ", end="")
            inp = input()
            if(inp.__eq__("x")):
                break
            else:
                if(valInput(inp, str, 13, 12)):
                    if(inp in customerList.keys()):
                        trgAccount = inp
                        step = 1
                    else:
                        print("  Err - there is no account number.")
                else:
                    print("  Err - wrong input")
        elif(step == 1):
            print("withdraw money [x:main menu b:previous step] >> ", end="")
            inp = input()
            if(inp.__eq__("x")):
                break
            elif(inp.__eq__("b")):
                step = 1
            else:
                if(valInput(inp, int, 99999999, 10000)):
                    if(customerList[trgAccount].curMoney >= 10000):
                        if(valInput(inp, int, customerList[trgAccount].curMoney, 10000)):
                            wdrMoney = int(inp)
                            step = 2
                        else:
                            print(
                                "  Err - not enough. you can withdraw {:,d}.".format(customerList[trgAccount].curMoney))
                    else:
                        print("  Err - there is less than 1,000 in the account.")
                else:
                    print("  Err - wrong input")
        elif(step == 2):
            print("-" * 80)
            print("[withdraw 정보]")
            print("{:^14} {:^7} {:^14}".format(
                "Account", "Name", "Withdraw Money"))
            print("{:14} {:7} {:14,d}".format(trgAccount,
                                              customerList[trgAccount].name, wdrMoney))
            print(
                "do you want to withdraw? [y:yes x:main menu b:previous step] >> ", end="")
            inp = input()
            if(inp.__eq__("x")):
                break
            elif(inp.__eq__("b")):
                step = 1
            elif(inp.__eq__("y")):
                step = 3
            else:
                print("  Err - wrong input")
        elif(step == 3):
            customerList[trgAccount].curMoney -= wdrMoney
            print("  Msg - {:,d} completed to withdraw.".format(wdrMoney))
            print("{:^14} {:^14} {:^7} {:^14}".format(
                "", "Account", "Name", "Money"))
            print("{:14} {:14} {:7} {:14,d}".format("Account", trgAccount,
                                                    customerList[trgAccount].name, customerList[trgAccount].curMoney))
            step = 0
            saveInfo()
            print("-" * 80)


def printInfo():
    if(len(customerList) == 0):
        print("there is no information.")
    else:
        print("-" * 80)
        print("[whole information]")
        print("{:^14} {:^7} {:^14} {:^7} {:^5} {:^14} {:^14}".format(
            "Account", "Name", "Current Money", "Grade", "Rate", "Original Money", "Rate Money"))
        for account in customerList:
            print(customerList[account])


def saveInfo():
    """save method"""
    global customerList
    saveDict = {}

    if(len(customerList) == 0):
        print("there is no save information.")
    else:
        for account in customerList:
            saveDict[account] = customerList[account].returnInfo()
        f = open('dbBank.txt', 'wb')
        pickle.dump(saveDict, f)
        f.close()


def loadInfo():
    """load method"""
    global customerList
    try:
        f = open('dbBank.txt', 'rb')
        loadData = pickle.load(f)
        for account in loadData:
            customerList[account] = Customer(loadData[account][0], loadData[account][1], loadData[account]
                                             [2], loadData[account][3], loadData[account][4], loadData[account][5], loadData[account][6])
    except:
        pass


def valInput(inp, ty, limit, less=0):
    """input value check method
    inp: the input value / ty: check type / [ty(int)]limit: limit by the number / [ty(str)]limit: limit by the letter"""
    retVal = False
    if(ty == int):
        try:
            inpNum = int(inp)
            if(less <= inpNum and inpNum <= limit):
                retVal = True
        except:
            pass
    elif(ty == float):
        try:
            inpNum = float(inp)
            if(less <= inpNum and inpNum <= limit):
                retVal = True
        except:
            pass
    elif(ty == str):
        if(less < len(inp) and len(inp) <= limit):
            retVal = True
    return retVal


class Customer:
    def __init__(self, account, name, curMoney, grade, rate, orgMoney, ratMoney):
        self.account = account
        self.name = name
        self.curMoney = int(curMoney)
        self.grade = grade
        self.rate = float(rate)
        self.orgMoney = int(orgMoney)
        self.ratMoney = int(ratMoney)

    def __str__(self):
        return "{:14} {:^7} {:14,d} {:^7} {:5.1f} {:14,d} {:14,d}".format(self.account, self.name, self.curMoney, self.grade, self.rate, self.orgMoney, self.ratMoney)

    def returnInfo(self):
        return self.account, self.name, self.curMoney, self.grade, self.rate, self.orgMoney, self.ratMoney


main()
