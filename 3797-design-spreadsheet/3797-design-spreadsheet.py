class Spreadsheet:
    def __init__(self, rows: int):
        """
        Inicjalizacja arkusza o 26 kolumnach (A–Z) i podanej liczbie wierszy.
        Wszystkie komórki początkowo mają wartość 0.
        """
        self.rows = rows
        # 26 kolumn, indeksy 0..25 odpowiadają A..Z
        self.grid = [[0] * 26 for _ in range(rows)]

    def _parse_cell(self, cell: str):
        """
        Zamienia nazwę komórki np. 'B10' na indeksy (row_idx, col_idx) zero-indexed.
        """
        col = ord(cell[0]) - ord('A')
        row = int(cell[1:]) - 1   # bo w danych jest 1-indeksowane
        return row, col

    def setCell(self, cell: str, value: int) -> None:
        """
        Ustawia wartość podanej komórki.
        """
        r, c = self._parse_cell(cell)
        self.grid[r][c] = value

    def resetCell(self, cell: str) -> None:
        """
        Resetuje wartość podanej komórki do 0.
        """
        r, c = self._parse_cell(cell)
        self.grid[r][c] = 0

    def _value_of_token(self, token: str) -> int:
        """
        Zwraca wartość pojedynczego składnika formuły:
        – jeśli to liczba, konwertuje na int
        – jeśli to referencja do komórki, zwraca wartość komórki (domyślnie 0 jeśli nie ustawiono)
        """
        if token[0].isalpha():
            r, c = self._parse_cell(token)
            # Jeśli wiersz poza zakresem – przyjmujemy 0
            if 0 <= r < self.rows:
                return self.grid[r][c]
            return 0
        else:
            return int(token)

    def getValue(self, formula: str) -> int:
        """
        Oblicza wartość formuły w postaci "=X+Y"
        gdzie X i Y są albo liczbami, albo referencjami do komórek.
        """
        # usuwamy znak '=' z przodu
        if formula.startswith('='):
            formula = formula[1:]
        # rozdzielamy na składniki po '+'
        tokens = formula.split('+')
        return sum(self._value_of_token(tok) for tok in tokens)
