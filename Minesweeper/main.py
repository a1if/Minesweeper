from tkinter import *
import settings
import utils
from cells import cell

root = Tk()
# Override the settings of the window
root.configure(bg="black")
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title("Minesweeper")
root.resizable(False, False)

top_frame = Frame(
    root,
    bg='Light Green',
    width=settings.WIDTH,
    height=utils.height_p(25)
)
top_frame.place(x=0, y=0)

game_title = Label(
    top_frame,
    bg = 'black',
    fg = 'white',
    text= 'Minesweeper',
    font=('Roman',30)
)
game_title.place(
    x = utils.width_p(25) , y =0
)

left_frame = Frame(
    root,
    bg='black',
    width=utils.width_p(25),
    height=utils.height_p(75)
)
left_frame.place(x=0, y=utils.height_p(25))

center_frame = Frame(
    root,
    bg= 'black',
    width=utils.width_p(75),
    height=utils.height_p(75)
)
center_frame.place(
    x=utils.width_p(25),
    y=utils.height_p(25),
)

for x in range(settings.grid_size):
    for  y in range(settings.grid_size):
        c = cell(x,y) 
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(column=x,row=y)

cell.create_cell_count_label(left_frame)
cell.cell_count_label_object.place(x=0,y=0)
cell.randomize_mines()


# Run the window

root.mainloop()