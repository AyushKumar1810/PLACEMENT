# A transaction is possibly invalid if:

# the amount exceeds $1000, or;
# if it occurs within (and including) 60 minutes of another transaction with the same name in a different city.
# You are given an array of strings transaction where transactions[i] consists of comma-separated values representing the name, time (in minutes), amount, and city of the transaction.

# Return a list of transactions that are possibly invalid. You may return the answer in any order.

# Example 1:

# Input: transactions = ["alice,20,800,mtv","alice,50,100,beijing"]
# Output: ["alice,20,800,mtv","alice,50,100,beijing"]
# Explanation: The first transaction is invalid because the second transaction occurs within a difference of 60 minutes, have the same name and is in a different city. Similarly the second one is invalid too.
# Example 2:

# Input: transactions = ["alice,20,800,mtv","alice,50,1200,mtv"]
# Output: ["alice,50,1200,mtv"]
# Example 3:

# Input: transactions = ["alice,20,800,mtv","bob,50,1200,mtv"]
# Output: ["bob,50,1200,mtv"]

def invalidTransactions(transactions):
    transaction_map = {}
    invalid_transactions = []

    for transaction in transactions:
        name, time, amount, city = transaction.split(',')
        time = int(time)
        amount = int(amount)

        if amount > 1000:
            invalid_transactions.append(transaction)

        if name not in transaction_map:
            transaction_map[name] = [(time, city)]
        else:
            for prev_time, prev_city in transaction_map[name]:
                if prev_city != city and abs(prev_time - time) <= 60:
                    invalid_transactions.append(transaction)
                    invalid_transactions.append(f"{name},{prev_time},{amount},{prev_city}")
                    break
            transaction_map[name].append((time, city))

    return invalid_transactions

# Example usage:
transactions1 = ["alice,20,800,mtv","alice,50,100,beijing"]
print(invalidTransactions(transactions1))  # Output: ["alice,20,800,mtv","alice,50,100,beijing"]

transactions2 = ["alice,20,800,mtv","alice,50,1200,mtv"]
print(invalidTransactions(transactions2))  # Output: ["alice,50,1200,mtv"]

transactions3 = ["alice,20,800,mtv","bob,50,1200,mtv"]
print(invalidTransactions(transactions3))  # Output: ["bob,50,1200,mtv"]
