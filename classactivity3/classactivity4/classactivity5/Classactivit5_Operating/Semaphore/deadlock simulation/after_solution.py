import threading
import time

print_lock = threading.Lock()  # lock for printing

# Shared Resource Class
class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.lock = threading.Semaphore(1)


account1 = Account("Account1", 1000)
account2 = Account("Account2", 1000)


def safe_print(msg):
    with print_lock:
        print(msg, flush=True)


# Deadlock-free transfer function
def transfer(from_account, to_account, amount):
    # Enforce ordering by account name
    first, second = (from_account, to_account) if from_account.name < to_account.name else (to_account, from_account)

    safe_print(f"{threading.current_thread().name} locking {first.name}")
    first.lock.acquire()

    time.sleep(1)  # simulate delay

    safe_print(f"{threading.current_thread().name} locking {second.name}")
    second.lock.acquire()

    # -------- Critical Section --------
    safe_print(f"{threading.current_thread().name} transferring {amount} from {from_account.name} to {to_account.name}")
    from_account.balance -= amount
    to_account.balance += amount
    # ---------------------------------

    second.lock.release()
    first.lock.release()


# Create two threads
t1 = threading.Thread(target=transfer, name="Thread-1", args=(account1, account2, 100))
t2 = threading.Thread(target=transfer, name="Thread-2", args=(account2, account1, 200))

t1.start()
t2.start()

t1.join()
t2.join()

safe_print(f"Final balance: {account1.name}={account1.balance}, {account2.name}={account2.balance}")
