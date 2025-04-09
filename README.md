# InMemoryDB - Extra Credit Assignment

## How to Run

1. Make sure you have **Python 3** installed.
2. Clone this project repo.
3. Open your terminal or command prompt.
4. Navigate to the folder containing `inmemorydb.py`.
5. Run the code with:

```bash
python3 inmemorydb.py
```

No additional libraries or dependencies are required.

---

## Reflection and Suggestions

This assignment offers a hands-on introduction to transaction-based data storage systems. It effectively simulates key database features such as staging, committing, and rolling back changes. To make this an official future assignment, the instructions should clearly define expected error messages and whether `get()` should return staged values during a transaction. Including extra methods like `delete(key)` or nested transactions could enrich the challenge. For grading, an automated test suite could be provided to validate behavior under various transaction scenarios, ensuring both functional accuracy and robust logic. Additionally, requiring basic unit tests from students could reinforce good testing practices.
