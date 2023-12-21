import random
import tkinter as tk
from tkinter import messagebox

MIN_ROW_COUNT, MAX_ROW_COUNT = 5, 30
MIN_COLUMN_COUNT, MAX_COLUMN_COUNT = 5, 30
MIN_MINE_COUNT, MAX_MINE_COUNT = 1, 800


class MinesweeperCell:
    def __init__(self, row, column):
        self.row, self.column = row, column
        self.state, self.mined, self.counter = 'closed', False, 0

    MARK_SEQUENCE = ['closed', 'flagged', 'questioned']

    def next_mark(self):
        self.state = self.MARK_SEQUENCE[(self.MARK_SEQUENCE.index(self.state) + 1) % len(self.MARK_SEQUENCE)]

    def open(self):
        if self.state != 'flagged':
            self.state = 'opened'


class MinesweeperModel:
    def __init__(self):
        self.start_game()

    def get_row_count(self):
        return self.row_count

    def get_column_count(self):
        return self.column_count

    def get_mine_count(self):
        return self.mine_count

    def start_game(self, row_count=15, column_count=15, mine_count=15):
        self.row_count = max(min(row_count, MAX_ROW_COUNT), MIN_ROW_COUNT)
        self.column_count = max(min(column_count, MAX_COLUMN_COUNT), MIN_COLUMN_COUNT)
        self.mine_count = max(min(mine_count, MAX_MINE_COUNT), MIN_MINE_COUNT)
        self.first_step, self.game_over = True, False
        self.cells_table = [[MinesweeperCell(row, column) for column in range(self.column_count)] for row in
                            range(self.row_count)]

    def get_cell(self, row, column):
        return self.cells_table[row][column] if 0 <= row < self.row_count and 0 <= column < self.column_count else None

    def is_win(self):
        return all(cell.mined or cell.state == 'opened' for row in self.cells_table for cell in row)

    def is_game_over(self):
        return self.game_over

    def open_cell(self, row, column):
        cell = self.get_cell(row, column)
        if not cell:
            return

        cell.open()

        if cell.mined:
            self.game_over = True
            return

        if self.first_step:
            self.first_step = False
            self.generate_mines()

        cell.counter = self.count_mines_around_cell(row, column)
        if cell.counter == 0:
            neighbours = self.get_cell_neighbours(row, column)
            for n in neighbours:
                if n.state == 'closed':
                    self.open_cell(n.row, n.column)

    def next_cell_mark(self, row, column):
        cell = self.get_cell(row, column)
        if cell:
            cell.next_mark()

    def generate_mines(self):
        for _ in range(self.mine_count):
            while True:
                row, column = random.randint(0, self.row_count - 1), random.randint(0, self.column_count - 1)
                cell = self.get_cell(row, column)
                if not cell.state == 'opened' and not cell.mined:
                    cell.mined = True
                    break

    def count_mines_around_cell(self, row, column):
        neighbours = self.get_cell_neighbours(row, column)
        return sum(1 for n in neighbours if n.mined)

    def get_cell_neighbours(self, row, column):
        neighbours = [self.get_cell(r, column - 1) for r in range(row - 1, row + 2)]
        neighbours += [self.get_cell(r, column) for r in range(row - 1, row + 2) if r != row]
        neighbours += [self.get_cell(r, column + 1) for r in range(row - 1, row + 2)]
        return filter(None, neighbours)


class MinesweeperView(tk.Frame):
    def __init__(self, model, controller, parent=None):
        super().__init__(parent)
        self.model, self.controller = model, controller
        self.controller.set_view(self)

        self.row_count_var = tk.IntVar(value=self.model.get_row_count())
        self.column_count_var = tk.IntVar(value=self.model.get_column_count())
        self.mine_count_var = tk.IntVar(value=self.model.get_mine_count())
        self.board = None
        self.create_board()

        panel = tk.Frame(self)
        panel.pack(side=tk.BOTTOM, fill=tk.X)

        tk.Button(panel, text='Новая игра', command=self.controller.start_new_game).pack(side=tk.RIGHT)
        for label, var in [('Количество мин: ', self.mine_count_var),
                           ('Размер поля: ', self.row_count_var),
                           ('x', self.column_count_var)]:
            self.create_spinbox(panel, label, var)

    def create_spinbox(self, parent, label, var):
        tk.Label(parent, text=label).pack(side=tk.RIGHT)
        spinbox = tk.Spinbox(parent, from_=MIN_MINE_COUNT, to=MAX_MINE_COUNT, textvariable=var, width=5)
        spinbox.pack(side=tk.RIGHT)

    def sync_with_model(self):
        for row in range(self.model.get_row_count()):
            for column in range(self.model.get_column_count()):
                cell = self.model.get_cell(row, column)
                if cell:
                    btn = self.buttons_table[row][column]

                    if self.model.is_game_over() and cell.mined:
                        btn.config(bg='black', text='')

                    if cell.state == 'closed':
                        btn.config(text='')
                    elif cell.state == 'opened':
                        btn.config(relief=tk.SUNKEN, text='')
                        if cell.counter > 0:
                            btn.config(text=cell.counter)
                        elif cell.mined:
                            btn.config(bg='red')
                    elif cell.state == 'flagged':
                        btn.config(text='P')
                    elif cell.state == 'questioned':
                        btn.config(text='?')

    def block_cell(self, row, column, block=True):
        btn = self.buttons_table[row][column]
        if btn:
            btn.bind('<Button-1>', 'break') if block else btn.unbind('<Button-1>')

    def get_game_settings(self):
        return self.row_count_var.get(), self.column_count_var.get(), self.mine_count_var.get()

    def update_model_settings(self):
        row_count = self.row_count_var.get()
        column_count = self.column_count_var.get()
        mine_count = self.mine_count_var.get()

        self.model.start_game(row_count, column_count, mine_count)

        self.row_count_var.set(row_count)
        self.column_count_var.set(column_count)
        self.mine_count_var.set(mine_count)

        self.create_board()

    def create_board(self):
        try:
            self.board.pack_forget()
            self.board.destroy()
            for var_name in ['row_count_var', 'column_count_var', 'mine_count_var']:
                setattr(self, var_name, tk.IntVar(value=getattr(self.model, var_name)._get()))
        except:
            pass

        self.board = tk.Frame(self)
        self.board.pack()
        self.buttons_table = []
        for row in range(self.model.get_row_count()):
            line = tk.Frame(self.board)
            line.pack(side=tk.TOP)
            buttons_row = []
            for column in range(self.model.get_column_count()):
                btn = tk.Button(
                    line,
                    width=2,
                    height=1,
                    command=lambda r=row, c=column: self.controller.on_left_click(r, c),
                    padx=0,
                    pady=0
                )
                btn.pack(side=tk.LEFT)
                btn.bind('<Button-3>', lambda e, r=row, c=column: self.controller.on_right_click(r, c))
                buttons_row.append(btn)

            self.buttons_table.append(buttons_row)

    def show_game_over_message(self):
        messagebox.showinfo('Игра окончена!', 'Вы проиграли!')
        self.controller.start_new_game()

    def show_win_message(self):
        messagebox.showinfo('Поздравляем!', 'Вы выиграли!')
        self.controller.start_new_game()


class MinesweeperController:
    def __init__(self, model):
        self.model = model

    def set_view(self, view):
        self.view = view

    def start_new_game(self):
        self.view.update_model_settings()
        self.view.create_board()

    def on_left_click(self, row, column):
        self.model.open_cell(row, column)
        self.view.sync_with_model()
        if self.model.is_win():
            self.view.show_win_message()
        elif self.model.is_game_over():
            self.view.show_game_over_message()

    def on_right_click(self, row, column):
        self.model.next_cell_mark(row, column)
        self.view.block_cell(row, column, self.model.get_cell(row, column).state == 'flagged')
        self.view.sync_with_model()


model = MinesweeperModel()
controller = MinesweeperController(model)
view = MinesweeperView(model, controller)
view.pack()
view.mainloop()
