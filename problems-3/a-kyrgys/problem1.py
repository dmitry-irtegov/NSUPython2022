import copy


class Table:

    def __init__(self, rows=[]):
        self.__table = []
        self.__rows_num = len(rows)
        if len(rows) > 0:
            self.__columns_num = max(len(row) for row in rows)
        else:
            self.__columns_num = 0
        for row in rows:
            self.add_row(row)

    def __str__(self):
        result = ""
        for row in self.__table:
            result += ' '.join([str(elem) for elem in row]) + '\n'
        return result

    def tail(self, n):
        if len(self.__table) < n:
            raise ValueError("Number of rows is less than the input parameter.")
        tail = Table(copy.deepcopy(self.__table[-n:]))
        return tail

    def head(self, n):
        if len(self.__table) < n:
            raise ValueError("Number of rows is less than the input parameter.")
        head = Table(copy.deepcopy(self.__table[:n]))
        return head

    def get_row(self, n):
        row = self.__table[n]
        return row

    def get_rows(self, rows_indexes):
        rows = Table()
        for i in rows_indexes:
            rows.add_row(self.__table[i])

        return rows

    def get_columns(self, columns_indexes):
        new_rows = []
        for row in copy.deepcopy(self.__table):
            new_row = []
            for i in columns_indexes:
                new_row.append(row[i])
            new_rows.append(new_row)

        columns = Table(new_rows)
        return columns

    def add_row(self, row):
        if len(row) < self.__columns_num:
            row += [0] * (self.__columns_num - len(row))

        elif len(row) > self.__columns_num:
            for row_in in self.__table:
                row_in += [0] * (len(row) - self.__columns_num)
            self.__columns_num = len(row)

        self.__table.append(row)

    def insert(self, row, column, val):
        self.__table[row][column] = val

    def merge_by_rows(self, table):
        merged_table = Table(copy.deepcopy(self.__table) + copy.deepcopy(table.__table))
        return merged_table

    def merge_by_columns(self, table):
        original_table = copy.deepcopy(self.__table)
        second_table = copy.deepcopy(table.__table)
        while len(second_table) > len(original_table):
            original_table.append([0] * self.__columns_num)
        for i in range(len(second_table)):
            original_table[i] += second_table[i]

        merged_table = Table(original_table)
        return merged_table


