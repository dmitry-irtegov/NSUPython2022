import copy


class Table():
    """Implementation of the Table class, which stores data as a two-dimensional
table with rows and columns.

    Attributes
    ----------
    rows : array, optional
        Array that has information about rows of the Table.

    Methods
    -------
    tail(n):
        Returns n last rows of the Table.
    head(n):
        Returns n first rows of the Table.
    get_rows(rows_indexes):
        A method that uses a list of indexes to create a new Table containing only
        these rows.
    get_columns(columns_indexes):
        A method that uses a list of indexes to create a new Table containing only
        these columns.
    add_row(row):
        A method that adds new row to the Table.
    insert(row, column, val):
        A method that inserts value in a specific cell.
    merge_by_rows(self, table):
        Merges Tables by rows.
    merge_by_columns(self, table):
        Merges Tables by columns.
        """

    def __init__(self, rows=[]):
        """
        Constructs all the necessary attributes for the Table object.

        Parameters
        ----------
            rows: array, optional
                Array that has information about rows of the Table.

        """
        self.__table = []
        self.__rows_num = len(rows)
        if len(rows) > 0:
            self.__columns_num = max(len(row) for row in rows)
        else:
            self.__columns_num = 0
        for row in rows:
            self.add_row(row)

    def __str__(self):
        """
        Converts the Table object to a string type.

        Parameters
        ----------
        """
        result = ""
        for row in self.__table:
            for elem in row:
                result += ' '.join([str(elem)])
            result += '\n'
        return result

    def tail(self, n):
        """
        Returns last n rows of the Table.

        Parameters
        ----------
            n: int
                Number of rows.

        Returns
        -------
            tail : Table
                New Table that contains last n rows of the original Table.

        Raises
        ------
        ValueError
            Because you passed argument greater than the number of the rows
            in the original Table.
        """
        if len(self.__table) < n:
            raise ValueError()
        tail = Table(copy.deepcopy(self.__table[-n:]))
        return tail

    def head(self, n):
        """
        Returns first n rows of the Table.

        Parameters
        ----------
            n: int
                Number of rows.

        Returns
        -------
            head : Table
                New Table that contains first n rows of the original Table.

        Raises
        ------
        ValueError
            Because you passed argument greater than the number of the rows
            in the original Table.
        """
        if len(self.__table) < n:
            raise ValueError()
        head = Table(copy.deepcopy(self.__table[:n]))
        return head

    def get_row(self, n):
        """
        Returns nth row of the Table.

        Parameters
        ----------
            n: int
                Number of row you want to get.

        Returns
        -------
            row : array
                Array that contains values of the nth row of the Table.
        """
        row = self.__table[n]
        return row

    def get_rows(self, rows_indexes):
        """
        Returns the rows of the Table whose indexes are defined in the
        passed parameter.

        Parameters
        ----------
            rows_indexes: array of int
                Array that contains indexes of the rows we want to get.

        Returns
        -------
            rows : Table
                New Table that contains rows with required indexes.
        """
        rows = Table()
        for i in rows_indexes:
            rows.add_row(self.__table[i])

        return rows

    def get_columns(self, columns_indexes):
        """
        Returns the columns of the Table whose indexes are defined in the
        passed parameter.

        Parameters
        ----------
            columns_indexes: array of int
                Array that contains indexes of the rows we want to get.

        Returns
        -------
            columns : Table
                New Table that contains columns with required indexes.
        """
        new_rows = []
        for row in copy.deepcopy(self.__table):
            new_row = []
            for i in columns_indexes:
                new_row.append(row[i])
            new_rows.append(new_row)

        columns = Table(new_rows)
        return columns

    def add_row(self, row):
        """
        Method that adds new row to the Table.

        Parameters
        ----------
            row: array
                Array of values that we want to add to the Table.

        Returns
        -------
        """
        if len(row) < self.__columns_num:
            row += [0] * (self.__columns_num - len(row))

        elif len(row) > self.__columns_num:
            for row_in in self.__table:
                row_in += [0] * (len(row) - self.__columns_num)
            self.__columns_num = len(row)

        self.__table.append(row)

    def insert(self, row, column, val):
        """
        Method that inserts new value to the defined place in the Table.

        Parameters
        ----------
            row: int
                Number of the row in the Table where we want to add value.
            column: int
                Number of the column in the Table where we want to add value.
            val:
                Value that we want to insert in the Table.

        Returns
        -------
        """
        self.__table[row][column] = val

    def merge_by_rows(self, table):
        """
        Method that merges table (parameter) to the original Table by rows.
        The table passed through the parameter is added to the end of the
        original Table.

        Parameters
        ----------
            table: Table
                Table that we want to merge with the original Table.

        Returns
        -------
            merged_table: Table
                Resulting Table is a join of two tables.
        """
        merged_table = Table(copy.deepcopy(self.__table) + copy.deepcopy(table.__table))
        return merged_table

    def merge_by_columns(self, table):
        """
        Method that merges table (parameter) to the original Table by
        columns. The table passed as a parameter is assigned to the right
        of the original Table.

        Parameters
        ----------
            table: Table
                Table that we want to merge with the original Table.

        Returns
        -------
            merged_table: Table
                Resulting Table is a join of two tables.
        """
        original_table = copy.deepcopy(self.__table)
        second_table = copy.deepcopy(table.__table)
        while len(second_table) > len(original_table):
            original_table.append([0] * self.__columns_num)
        for i in range(len(second_table)):
            original_table[i] += second_table[i]

        merged_table = Table(original_table)
        return merged_table