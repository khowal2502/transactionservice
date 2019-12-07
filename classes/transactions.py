from utils.DBConnection import DBConnection


class Transaction:

    transaction_id = None
    amount = None
    txn_type = None
    parent_id = None
    connection = None
    db = None

    def __init__(self, transaction_id=None, amount=None, type=None, parent_id=None):
        self.transaction_id = transaction_id
        self.amount = amount
        self.txn_type = type
        self.parent_id = parent_id

        dbconn = DBConnection()
        self.db, self.connection = dbconn.create_connection()

    def insert_txn(self):
        query = "INSERT INTO transactions (id, amount, type, parent_id) VALUES " \
                "(%s, %s, %s, %s)"
        val = (self.transaction_id, self.amount, self.txn_type, self.parent_id)
        self.connection.execute(query, val)
        self.db.commit()

        return self.connection.rowcount

    def fetch_txn(self, txn_id):
        query = "SELECT * FROM transactions WHERE id = %s"
        vals = (txn_id,)

        self.connection.execute(query, vals)
        res = self.connection.fetchone()

        self.transaction_id = res[0]
        self.amount = res[1]
        self.txn_type = res[2]
        self.parent_id = res[3]

    def fetch_ids_by_type(self, type):
        query = "SELECT * FROM transactions WHERE type = %s"
        vals = (type,)

        self.connection.execute(query, vals)
        resp = self.connection.fetchall()

        ids = []
        for txn in resp:
            ids.append(txn[0])

        return ids

