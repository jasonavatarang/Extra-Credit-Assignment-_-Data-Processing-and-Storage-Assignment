# inmemorydb.py

class InMemoryDB:
    def __init__(self):
        self.store = {}             # Committed values
        self.transaction = None     # Temporary staged values during a transaction

    def begin_transaction(self):
        if self.transaction is not None:
            print("Error: Transaction already in progress.")
            return
        self.transaction = {}
        print("Transaction started.")

    def put(self, key, value):
        if self.transaction is None:
            print("Error: No active transaction. Use begin_transaction().")
            return
        self.transaction[key] = value
        print(f"Staged: {key} = {value}")

    def get(self, key):
        if self.transaction is not None and key in self.transaction:
            return self.transaction[key]
        return self.store.get(key, None)

    def commit(self):
        if self.transaction is None:
            print("Error: No active transaction to commit.")
            return
        self.store.update(self.transaction)
        self.transaction = None
        print("Transaction committed.")

    def rollback(self):
        if self.transaction is None:
            print("Error: No active transaction to rollback.")
            return
        self.transaction = None
        print("Transaction rolled back.")


# Sample usage for testing
if __name__ == "__main__":
    db = InMemoryDB()
    print("Initial get(A):", db.get("A"))
    db.put("A", 5)                  # Should error
    db.begin_transaction()
    db.put("A", 10)
    print("During transaction get(A):", db.get("A"))
    db.rollback()
    print("After rollback get(A):", db.get("A"))
    db.begin_transaction()
    db.put("A", 20)
    db.commit()
    print("After commit get(A):", db.get("A"))
