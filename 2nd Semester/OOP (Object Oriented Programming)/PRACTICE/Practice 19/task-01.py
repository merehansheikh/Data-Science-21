class Atm:
    pass
class BankAccount:
    def __init__(self) -> None:
        self.type = self.type_of_account()
    def type_of_account(self):
        x = input('Enter 1 for \"Current Account\" and 2 for \"Saving Account\"')
        return x
class AtmCard:
    def __init__(self, card_num, issue_date, exp_date, CCV):
        self.card_num = card_num
        self.issue_date = issue_date
        self.exp_date = exp_date
        self.ccv = CCV

class Customer:
    def __init__(self, name, card, acc):
        self.name = name
        self.cust = card
        self.acc = acc
def main():
    cust = Customer(input('Name:'), AtmCard(int(input('card_num')), int(input('issue_date')), int(input('exp_date')), int(input('CCV'))))

main()