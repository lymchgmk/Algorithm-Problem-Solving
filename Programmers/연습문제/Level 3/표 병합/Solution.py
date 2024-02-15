class Cell:
    EMPTY = "EMPTY"

    def __init__(self, r, c, value=None):
        self.coordinate = (r, c)
        self.value = value
        self.parent = self
        self.children = []

    def get_value(self):
        return self.value if self.value else Cell.EMPTY


class Table:
    MAX_SIZE = 50
    UPDATE, MERGE, UNMERGE, PRINT = "UPDATE", "MERGE", "UNMERGE", "PRINT"
    FLAG_UPDATE1, FLAG_UPDATE2 = 3, 2
    print_result = []

    def __init__(self, size=MAX_SIZE):
        self.cells = {(r, c): Cell(r, c) for r in range(1, size + 1) for c in range(1, size + 1)}

    def _get(self, r, c):
        return self.cells[(r, c)]

    def _find(self, r, c):
        if self._get(r, c) != self._get(r, c).parent:
            pr, pc = self._get(r, c).parent.coordinate
            return self._find(pr, pc)

        return self._get(r, c)

    def _union(self, r1, c1, r2, c2):
        cell1, cell2 = self._find(r1, c1), self._find(r2, c2)
        cell2.parent = cell1
        for child_cell in cell2.children:
            child_cell.parent = child_cell
            _r, _c = child_cell.coordinate
            self._union(r1, c1, _r, _c)
        cell2.children = []
        cell1.children.append(cell2)

    def update1(self, r, c, value):
        r, c = int(r), int(c)
        self._find(r, c).value = value

    def update2(self, value1, value2):
        for r, c in self.cells.keys():
            if self._find(r, c).value == value1:
                self.update1(r, c, value2)

    def merge(self, r1, c1, r2, c2):
        r1, c1, r2, c2 = int(r1), int(c1), int(r2), int(c2)
        parent_cell1, parent_cell2 = self._find(r1, c1), self._find(r2, c2)
        pr1, pc1 = parent_cell1.coordinate
        pr2, pc2 = parent_cell2.coordinate

        if pr1 == pr2 and pc1 == pc2:
            return

        if parent_cell1.value:
            self._union(pr1, pc1, pr2, pc2)
        else:
            self._union(pr2, pc2, pr1, pc1)

    def unmerge(self, r, c):
        r, c = int(r), int(c)
        root_cell = self._find(r, c)
        _cached_value = root_cell.value
        root_cell.value = None
        for child_cell in root_cell.children:
            child_cell.parent = child_cell
            child_cell.value = None
        root_cell.children = []
        self._find(r, c).value = _cached_value

    def print(self, r, c):
        r, c = int(r), int(c)
        cell = self._find(r, c)
        Table.print_result.append(cell.get_value())


def solution(commands):
    table = Table()
    for command in commands:
        query_command, *query_items = command.split()
        if query_command == Table.UPDATE:
            if len(query_items) == Table.FLAG_UPDATE1:
                r, c, value = query_items
                table.update1(r, c, value)
            elif len(query_items) == Table.FLAG_UPDATE2:
                value1, value2 = query_items
                table.update2(value1, value2)
        elif query_command == Table.MERGE:
            r1, c1, r2, c2 = query_items
            table.merge(r1, c1, r2, c2)
        elif query_command == Table.UNMERGE:
            r, c = query_items
            table.unmerge(r, c)
        elif query_command == Table.PRINT:
            r, c = query_items
            table.print(r, c)

    return table.print_result


if __name__ == "__main__":
    # commands = ["UPDATE 1 1 a", "UPDATE 1 2 b", "UPDATE 2 1 c", "UPDATE 2 2 d", "MERGE 1 1 1 2", "MERGE 2 2 2 1", "MERGE 2 1 1 1", "PRINT 1 1", "UNMERGE 2 2", "PRINT 1 1"]
    commands = ["UPDATE 1 1 A", "UPDATE 2 2 B", "UPDATE 3 3 C", "UPDATE 4 4 D", "MERGE 1 1 2 2", "MERGE 3 3 4 4", "MERGE 1 1 4 4", "UNMERGE 3 3", "PRINT 1 1", "PRINT 2 2", "PRINT 3 3", "PRINT 4 4"]
    # commands = ["UPDATE 1 1 menu", "MERGE 1 1 1 2", "MERGE 1 1 1 3", "MERGE 1 1 1 4", "MERGE 1 2 1 3", "UPDATE 1 1 hansik", "PRINT 1 1", "PRINT 1 2", "PRINT 1 3", "PRINT 1 4"]
    result = ["d", "EMPTY"]
    print(solution(commands))
