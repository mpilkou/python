from threading import Lock

def is_close(my_fun):
    def execute_fun(self, *args, **kwargs):
        if self.balanse == None:
            raise ValueError
        return my_fun(self, *args, **kwargs)
    return execute_fun

class BankAccount(object):
    def __init__(self):
        self._lock = Lock()

    @is_close
    def get_balance(self):
        if self.balanse == None:
            raise ValueError
        return self.balanse

    def open(self):
        self.balanse = 0

    @is_close
    def deposit(self, amount):
        with self._lock:
            if self.balanse == None or amount < 0:
                raise ValueError
            self.balanse += amount

    @is_close
    def withdraw(self, amount):
        with self._lock:
            if amount > self.balanse or self.balanse == None or amount < 0:
                raise ValueError
            else:
                self.balanse -= amount

    def close(self):
        self.balanse = None
