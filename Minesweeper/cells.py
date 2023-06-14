from tkinter import Button , Label
import random
import settings
import ctypes
import sys
class cell:
    all = []
    cell_count = settings.cell_count
    cell_count_label_object = None
    def __init__(self ,x,y, is_mine = False):
        self.is_mine = is_mine
        self.is_opened = False
        self.is_mine_candidate = False
        self.cell_btn_object = None
        self.x = x
        self.y = y 

        cell.all.append(self)

    def create_btn_object(self,location):
        btn = Button(location , 
                      width=5,
                      height = 2,
                      #text = f'{self.x},{self.y}'
                      )

        btn.bind('<Button-1>', self.left_click_button)
        btn.bind('<Button-3>', self.right_click_button)
        self.cell_btn_object = btn


    @staticmethod
    def create_cell_count_label(location):
        lbl = Label(
            location,
            bg = 'black',
            fg = 'white', 
            text=f'Cells left: {cell.cell_count}',
            #width= 5, height= 2
            font=("ROMAN",15)
        )
        cell.cell_count_label_object = lbl


    def left_click_button(self,event):
        if self.is_mine:
            self.show_mine()
        else:
            if self.surrounded_cells_mines_length == 0:
                for cell_obj in self.surrounded_cells:
                    cell_obj.show_cell()
            self.show_cell()
            if cell.cell_count == settings.mines_count:
                 ctypes.windll.user32.MessageBoxW(
            0,"আপনি জিতে 10 গেছেন  কোটি টাকা 🐸",'খেলা লাগবো না আর',0
            )
        self.cell_btn_object.unbind('<Button-1>')
        self.cell_btn_object.unbind('<Button-3>')

    def get_cell_by_axis(self,x,y):
        for Cell in cell.all:
            if Cell.x == x and  Cell.y == y:
                return Cell
 
    @property
    def surrounded_cells(self):
        cells = [
            self.get_cell_by_axis(self.x -1 , self.y - 1 ),
            self.get_cell_by_axis(self.x -1 , self.y  ),
            self.get_cell_by_axis(self.x -1 , self.y + 1),
            self.get_cell_by_axis(self.x , self.y - 1 ),
            self.get_cell_by_axis(self.x +1 , self.y - 1 ),
            self.get_cell_by_axis(self.x + 1 , self.y ),
            self.get_cell_by_axis(self.x + 1 , self.y + 1 ),
            self.get_cell_by_axis(self.x  , self.y + 1 )
        ]
        cells = [cell for cell in cells if cell is not None]
        return cells
 
    @property
    def surrounded_cells_mines_length(self):
        counter = 0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                counter += 1

        return counter

    def show_cell(self):
        if not self.is_opened:
             cell.cell_count -= 1
             self.cell_btn_object.configure(text=self.surrounded_cells_mines_length)
            # print(self.get_cell_by_axis(0,0))
             if cell.cell_count_label_object:
                cell.cell_count_label_object.configure(
                text=f'Cells left: {cell.cell_count}'
            )
             self.cell_btn_object.configure(
                bg= 'SystemButtonFace'
            )
        self.is_opened = True

    def show_mine(self):
        self.cell_btn_object.configure(bg='red')
        ctypes.windll.user32.MessageBoxW(
            0,"বাল খেলসো,মারা খাও এহন😒",'খেলা লাগবো না আর',0
            )
        sys.exit()
        

    def right_click_button(self,event):
        if not self.is_mine_candidate:
          self.cell_btn_object.configure(
            bg = 'Green'
          )
          self.is_mine_candidate = True
        else:
            self.cell_btn_object.configure(
                bg = 'SystemButtonFace'
            )
            self.is_mine_candidate = False


    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(cell.all, 
                                settings.mines_count )

        for picked_cell in picked_cells:
            picked_cell.is_mine = True
        
    def __repr__(self):
        return f"Cell({self.x},{self.y})"