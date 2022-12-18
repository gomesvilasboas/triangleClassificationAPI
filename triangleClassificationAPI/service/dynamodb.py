import boto3
from flask import abort


class DynamoDB:
    def __init__(self, table_name):
        self._client = boto3.client('dynamodb')
        self._table = table_name

    @property
    def client(self):
        return self._client

    @property
    def table_name(self):
        return self._table

    def scan_table(self):
        try:
            paginator = self.client.get_paginator("scan")
            for page in paginator.paginate(TableName=self.table_name):
                yield from page["Items"]
        except Exception as ex:
            abort(500, 'Pagination goes wrong. ' + str(ex))

    def get_register_paginated(self, page):
        data = list()
        try:
            for item in self.scan_table():
                data.append(item)
            return {"data", data}
        except Exception as ex:
            abort(500, 'Cannot get items from database. ' + str(ex))

    def save_item(self, item):
        try:
            self.table.put_item(TableName=self.table_name, item)
        except Exception as ex:
            abort(500, 'Cannot save item into database')