This program was created by Kim jeongho using python3.
[output test result]

---

\***\*\*\*\*\*\*\***\*\*\***\*\*\*\*\*\*\*** RUNNING BANKING SYSTEM 3.0 \***\*\*\*\*\*\*\***\*\*\***\*\*\*\*\*\*\***

---

---

MAIN MENU
1.create account  
2.depositn
3.withdraw
4.list print
0.exit
please select menu >> 1

---

main menu > create account

- Account is 8 letters. higher than 10000001
- Name is minimum 2 letters, maximum 5 letters.
- Start deposit is higher than 1,000, less than 10,000,000
- Interest rate is higher than 0.0, less than 20.0 without "%" signal
- Credit rating has to select one of "A", "B", "C"

---

main menu > create account > account type
1.normal account
2.credit account
please select menu [x:main menu] >> 1

---

[create normal account]
account number(8 numbers) [x:main menu] >> 1000006
Err - wrong input

---

[create normal account]
account number(8 numbers) [x:main menu] >> 10000006
name [x:main menu b:previous step] >> x

---

MAIN MENU
1.create account
2.depositn
3.withdraw
4.list print
0.exit
please select menu >> 1

---

main menu > create account

- Account is 8 letters. higher than 10000001
- Name is minimum 2 letters, maximum 5 letters.
- Start deposit is higher than 1,000, less than 10,000,000
- Interest rate is higher than 0.0, less than 20.0 without "%" signal
- Credit grade has to select one of "A", "B", "C"

---

main menu > create account > account type
1.normal account
2.credit account
please select menu [x:main menu] >> 2

---

[create credit account]
account number(8 numbers) [x:main menu] >> 10000001
Err - already exist same account number

---

[create credit account]
account number(8 numbers) [x:main menu] >> 10000006
name [x:main menu b:previous step] >> Kim Jeongho
Err - wrong input
name [x:main menu b:previous step] >> KIM JH
Err - wrong input
name [x:main menu b:previous step] >> KIMJH
start deposit money [x:main menu b:previous step] >> 50000000
Err - wrong input
start deposit money [x:main menu b:previous step] >> 5000000
interest rate [x:main menu b:previous step] >> aws
Err - wrong input
interest rate [x:main menu b:previous step] >> 20
credit grade(A, B, C) [x:main menu b:previous step] >> 20
Err - wrong input
credit grade(A, B, C) [x:main menu b:previous step] >> 5
Err - wrong input
credit grade(A, B, C) [x:main menu b:previous step] >> A

---

[input information]
Account Name Current Money Grade Rate Original Money Rate Money
2030-10000006 KIMJH 5,000,000 A 20.0 0 0
KIMJH Do you want to save this? [y:save x:main menu b:previous step] >> y
Msg - Completed to save

---

MAIN MENU
1.create account
2.depositn
3.withdraw
4.list print
0.exit
please select menu >> 2

---

main menu > remittance

- A remittance money is higher than 1,000, less than 99,999,999
  deposit account number [x:main menu] >> 10000006
  Err - wrong input
  deposit account number [x:main menu] >> 2020-10000006
  Err - there is no account number.
  deposit account number [x:main menu] >> x

---

MAIN MENU
1.create account
2.depositn
3.withdraw
4.list print
0.exit
please select menu >> 4

---

[whole information]
Account Name Current Money Grade Rate Original Money Rate Money
2030-10000001 KIMJH 7,440,000 A 20.0 0 0
2030-10000002 POPO 2,000,000 B 15.0 0 0
2030-10000003 CSM 4,250,000 B 2.5 0 0
2020-10000004 TEST 100,000 - 2.5 0 0
2020-10000001 TEST 100,000 - 2.0 0 0
2020-10000005 AKA 2,000,000 - 20.0 0 0
2030-10000006 KIMJH 5,000,000 A 20.0 0 0

---

MAIN MENU
1.create account
2.depositn
3.withdraw
4.list print
0.exit
please select menu >> 2

---

main menu > remittance

- A remittance money is higher than 1,000, less than 99,999,999
  deposit account number [x:main menu] >> 2030-10000001
  withdraw account number [x:main menu b:previous step] >> 203010000002
  Err - wrong input
  withdraw account number [x:main menu b:previous step] >> 2030-10000003
  remittance how much [x:main menu b:previous step] >> 50
  Err - wrong input
  remittance how much [x:main menu b:previous step] >> 100000

---

[input information]
Account Name Money
Send Account 2030-10000003 CSM - 100,000
Get Account 2030-10000001 KIMJH + 100,000
Do you want to remit? [y:yes x:main menu b:previous step] >> y
Msg - 100,000 completed to remit.
Account Name Money
Send Account 2030-10000003 CSM 4,150,000
Get Account 2030-10000001 KIMJH 7,540,000

---

## deposit account number [x:main menu] >> x

MAIN MENU
1.create account
2.depositn
3.withdraw
4.list print
0.exit
please select menu >> 3

---

main menu > withdraw

- The withdraw is higher than 10,000
  withdraw account number [x:main menu] >> 2030-10000001
  withdraw money [x:main menu b:previous step] >> 20
  Err - wrong input
  withdraw money [x:main menu b:previous step] >> 40000

---

[withdraw 정보]
Account Name Withdraw Money
2030-10000001 KIMJH 40,000
do you want to withdraw? [y:yes x:main menu b:previous step] >> y
Msg - 40,000 completed to withdraw.
Account Name Money
Account 2030-10000001 KIMJH 7,500,000

---

## withdraw account number [x:main menu] >> x

MAIN MENU
1.create account
2.depositn
3.withdraw
4.list print
0.exit
please select menu >> 0
Thank you~!
