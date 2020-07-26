from datetime import datetime


class BankAccount(object):

    def __init__(self, username, card_no, balance):
        self.username = username
        self.card_no = card_no
        self.balance = balance
        self.history_lst = []

    def deposit(self, amount):
        if not self.is_amount_legitimate(amount):
            print('金额不合法')
            return
        self.balance += amount
        log = '{operate_time}{username}存入{amount}元'.format(
            operate_time=self._get_current_time(),
            username=self.username,
            amount=amount)
        self.history_lst.append(log)

    def withdrawal(self, amount):

        if not self.is_amount_legitimate(amount):
            print('金额不合法')
            return
        self.balance -= amount
        log = '{operate_time}{username}取出{amount}元'.format(
            operate_time=self._get_current_time(),
            username=self.username,
            amount=amount)
        self.history_lst.append(log)

    def transfer(self, another, amount):

        self.balance -= amount
        log = '{operate_time}{username}向{another_username}转账{amount}元'.format(
            operate_time=self._get_current_time(),
            username=self.username,
            another_username=another.username,
            amount=amount)
        self.history_lst.append(log)

    def accept_transfer(self, another, amount):

        self.balance += amount
        log = '{operate_time}{username}收到{another_username}转来{amount}元'.format(
            operate_time=self._get_current_time(),
            username=self.username,
            another_username=another.username,
            amount=amount)
        self.history_lst.append(log)

    def history(self):

        for log in self.history_lst:
            print(log)

    @classmethod
    def is_amount_legitimate(cls, amount):

        if not isinstance(amount, (float, int)):
            return False

        if amount <= 0:
            return False

        return True

    @classmethod
    def _get_current_time(cls):
        now = datetime.now()
        current_time = now.strftime('%Y-%m-%d %H:%M:%S')
        return current_time


if __name__ == '__main__':
    account_1 = BankAccount('小明', '248252543', 4932.13)
    account_2 = BankAccount('小红', '429845363', 3211.9)
    account_1.deposit(400)
    account_1.withdrawal(300)
    account_1.transfer(account_2, 1024)
    account_1.history()
    account_2.history()
