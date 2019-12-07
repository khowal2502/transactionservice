from classes.transactions import Transaction


class TransactionService:

    def valid_request(self, txn_id, json):
        if txn_id is None:
            return False

        if "amount" in json:
            if "type" in json:
                return True

        return False

    def get_txn(self, txn_id):
        txn = Transaction()
        txn.fetch_txn(txn_id)

        return txn

    def insert_txn(self, txn_id, json):
        parent_id = None
        if 'parent_id' in json:
            parent_id = json["parent_id"]

        txn = Transaction(int(txn_id), json["amount"], json["type"], parent_id)

        return txn.insert_txn()


    def get_txn_sum(self, txn_id):
        txn = self.get_txn(txn_id)

        sum = txn.amount
        while txn.parent_id is not None:
            txn = self.get_txn(txn.parent_id)
            sum += txn.amount

        return sum

    def get_txn_ids_by_type(self, type):
        txn = Transaction()
        ids = txn.fetch_ids_by_type(type)

        return ids


