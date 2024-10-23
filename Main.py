import customtkinter as ctk

class Calculator:
    def __init__(self):
        self.__root = ctk.CTk()
        self.Main_Window()
        self.__root.mainloop()
    
    def Main_Window(self):
        self.__root.geometry('600x600')
        self.__root.title('Calculator')
        self.__contents()
    
    def __get_root(self):
        return self.__root
    def __contents(self):
        self.__main_frame = ctk.CTkFrame(self.__get_root(), width=600, height=600, corner_radius= 0).place(relx = 0.5, rely =0.5, anchor='center')
        self.__entry_widget()
        self.__set_button_frame()
        self.__set_switch_frame()

    def __get_main_frame(self):
        return self.__main_frame
    
    def __var(self):
        self.__entry_var = ctk.StringVar()
        return self.__entry_var

    def __entry_widget(self):
        self.__entry = ctk.CTkEntry(self.__get_main_frame(), width= 500, height= 100,font= ('Poppins', 30), corner_radius= 0, textvariable= self.__var(), justify = 'right')
        self.__entry.configure(state='readonly')
        self.__entry.place(relx = 0.5, rely= 0.05, anchor='n')

    def __set_button_frame(self):
        self.__button_frames = ctk.CTkFrame(self.__get_main_frame(), width= 550, height= 300,corner_radius= 0)
        self.__button_frames.place(relx =0.5, rely =0.7, anchor = 'center')
        self.__set_buttons()
        self.__button_frames.grid_propagate(False)
        for i in range(4):
            self.__button_frames.grid_rowconfigure(i, weight=1)
        for j in range(4):
            self.__button_frames.grid_columnconfigure(j, weight=1)
        
        

    def __get_button_frame(self):
        return self.__button_frames
    
    def __set_buttons(self):
        self.__button1 = ctk.CTkButton(self.__get_button_frame(), text= 'C', corner_radius= 0, font= ('Poppins', 20), command= lambda: self.__update_entry('clear', 'sub'))
        self.__button1.grid(row=4, column=0, sticky= 'nsew')
        self.__button2 = ctk.CTkButton(self.__get_button_frame(), text= 'AC', corner_radius= 0, font= ('Poppins', 20), command= lambda: self.__update_entry('Allclear', 'sub'))
        self.__button2.grid(row=4, column=1, sticky= 'nsew')
        self.__button3 = ctk.CTkButton(self.__get_button_frame(), text= '7', corner_radius= 0, font= ('Poppins', 20), command= lambda: self.__update_entry('7', 'inputs'))
        self.__button3.grid(row=0, column=0, sticky= 'nsew')
        self.__button4 = ctk.CTkButton(self.__get_button_frame(), text= '8', corner_radius= 0, font= ('Poppins', 20), command= lambda: self.__update_entry('8', 'inputs'))
        self.__button4.grid(row=0, column=1, sticky= 'nsew')
        self.__button5 = ctk.CTkButton(self.__get_button_frame(), text= '9', corner_radius= 0, font= ('Poppins', 20), command= lambda: self.__update_entry('9', 'inputs'))
        self.__button5.grid(row=0, column=2, sticky= 'nsew')
        self.__button6 = ctk.CTkButton(self.__get_button_frame(), text= '+', corner_radius= 0, font= ('Poppins', 20), command= lambda: self.__update_entry('+', 'operation'))
        self.__button6.grid(row=0, column=3, sticky= 'nsew')
        self.__button7 = ctk.CTkButton(self.__get_button_frame(), text= '4', corner_radius= 0, font= ('Poppins', 20), command= lambda: self.__update_entry('4', 'inputs'))
        self.__button7.grid(row=1, column=0, sticky= 'nsew')
        self.__button8 = ctk.CTkButton(self.__get_button_frame(), text= '5', corner_radius= 0, font= ('Poppins', 20), command= lambda: self.__update_entry('5', 'inputs'))
        self.__button8.grid(row=1, column=1, sticky= 'nsew')
        self.__button9 = ctk.CTkButton(self.__get_button_frame(), text= '6', corner_radius= 0, font= ('Poppins', 20), command= lambda: self.__update_entry('6', 'inputs'))
        self.__button9.grid(row=1, column=2, sticky= 'nsew')
        self.__button10 = ctk.CTkButton(self.__get_button_frame(), text= '-', corner_radius= 0, font= ('Poppins', 20), command= lambda: self.__update_entry('-', 'operation'))
        self.__button10.grid(row=1, column=3, sticky= 'nsew')
        self.__button11 = ctk.CTkButton(self.__get_button_frame(), text= '1', corner_radius= 0, font= ('Poppins', 20), command= lambda: self.__update_entry('1', 'inputs'))
        self.__button11.grid(row=2, column=0, sticky= 'nsew')
        self.__button12 = ctk.CTkButton(self.__get_button_frame(), text= '2', corner_radius= 0, font= ('Poppins', 20), command= lambda: self.__update_entry('2', 'inputs'))
        self.__button12.grid(row=2, column=1, sticky= 'nsew')
        self.__button13 = ctk.CTkButton(self.__get_button_frame(), text= '3', corner_radius= 0, font= ('Poppins', 20), command= lambda: self.__update_entry('3', 'inputs'))
        self.__button13.grid(row=2, column=2, sticky= 'nsew')
        self.__button14 = ctk.CTkButton(self.__get_button_frame(), text= '*', corner_radius= 0, font= ('Poppins', 20), command= lambda: self.__update_entry('*', 'operation'))
        self.__button14.grid(row=2, column=3, sticky= 'nsew')
        self.__button15 = ctk.CTkButton(self.__get_button_frame(), text= '.', corner_radius= 0, font= ('Poppins', 20), command= lambda: self.__update_entry('.', 'inputs'))
        self.__button15.grid(row=3, column=0, sticky= 'nsew')
        self.__button16 = ctk.CTkButton(self.__get_button_frame(), text= '0', corner_radius= 0, font= ('Poppins', 20), command= lambda: self.__update_entry('0', 'inputs'))
        self.__button16.grid(row=3, column=1, sticky= 'nsew')
        self.__button17 = ctk.CTkButton(self.__get_button_frame(), text= '+/-', corner_radius= 0, font= ('Poppins', 20), command= lambda: self.__update_entry('', '+/-'))
        self.__button17.grid(row=3, column=2, sticky= 'nsew')
        self.__button18 = ctk.CTkButton(self.__get_button_frame(), text= '/', corner_radius= 0, font= ('Poppins', 20), command= lambda: self.__update_entry('/', 'operation'))
        self.__button18.grid(row=3, column=3, sticky= 'nsew')
        self.__button19 = ctk.CTkButton(self.__get_button_frame(), text= '=', corner_radius= 0, font= ('Poppins', 40), command= lambda: self.__equal_method())
        self.__button19.grid(row=4, column=2, columnspan= 4, sticky= 'nsew')
        self.buttonArray = [self.__button1,self.__button2,self.__button3,self.__button4,self.__button5,self.__button6,
        self.__button7,self.__button8,self.__button9,self.__button10,self.__button11,self.__button12,self.__button13,
        self.__button14,self.__button15,self.__button16,self.__button17,self.__button18,self.__button19,]
    def __update_entry(self, obj, func):
        match func:
            case 'inputs':
                self.__entry.configure(state='normal')
                self.__current_val = self.__entry_var.get()
                if '.' in self.__current_val:
                   if obj != '.':
                    self.__current_val += obj
                    self.__entry_var.set(self.__current_val)
                    self.__entry.configure(state='readonly')
                elif '.' not in self.__current_val:
                    self.__current_val += obj
                    self.__entry_var.set(self.__current_val)
                    self.__entry.configure(state='readonly')
            case 'operation':
                if obj == '+':
                    self.__entry.configure(state ='normal')
                    self.__num1 = self.__entry_var.get()
                    self.__entry_var.set('')
                    self.__operator = '+'
                    self.__entry.configure(state='readonly')
                elif obj == '-':
                    self.__entry.configure(state ='normal')
                    self.__num1 = self.__entry_var.get()
                    self.__entry_var.set('')
                    self.__operator = '-'
                    self.__entry.configure(state='readonly')
                elif obj == '/':
                    self.__entry.configure(state ='normal')
                    self.__num1 = self.__entry_var.get()
                    self.__entry_var.set('')
                    self.__operator = '/'
                    self.__entry.configure(state='readonly')
                elif obj == '*':
                    self.__entry.configure(state ='normal')
                    self.__num1 = self.__entry_var.get()
                    self.__entry_var.set('')
                    self.__operator = '*'
                    self.__entry.configure(state='readonly')
            case '+/-':
                    self.__entry.configure(state ='normal')
                    self.__integerVal= self.__entry_var.get()
                    if self.__integerVal[0] != '-':
                        self.__integerVal = '-' + self.__integerVal
                    elif self.__integerVal[0] == '-':
                        self.__integerVal = self.__integerVal[1:]
                    self.__entry_var.set(self.__integerVal)
                    self.__entry.configure(state='readonly')
            case 'sub':
                if obj == 'clear':
                    self.__entry.configure(state ='normal')
                    self.__storage = self.__entry_var.get()
                    self.__new_value = ''
                    for value in range(len(self.__storage)-1):
                        self.__new_value +=self.__storage[value]
                    self.__entry_var.set(f'{self.__new_value}')
                    self.__entry.configure(state='readonly')
                elif obj == 'Allclear':
                    self.__entry.configure(state ='normal')
                    self.__entry_var.set('')
                    self.__entry.configure(state='readonly')
    
    def __get_operator(self):
        return self.__operator
    
    def __get_num1(self):
        return float(self.__num1)

    def __equal_method(self):
        self.__entry.configure(state ='normal')
        self.__num2 = self.__entry_var.get()
        match self.__get_operator():
            case '+':
                self.__equal = self.__get_num1() + float(self.__num2)
            case '-':
                self.__equal = self.__get_num1() - float(self.__num2)
            case '/':
                self.__equal = self.__get_num1() / float(self.__num2)
            case '*':
                self.__equal = self.__get_num1() * float(self.__num2)
        self.__entry_var.set(f'{self.__equal:.2f}')
        self.__entry.configure(state = 'readonly')

    def __set_switch_frame(self):
        self.__switch_frame = ctk.CTkFrame(self.__get_main_frame(), width= 200, height= 50, corner_radius= 0)
        self.__switch_frame.place(relx = 0.78, rely= 0.4, anchor= 'center')
        self.__on_off_method()

    def __on_off_method(self):
        self.var = ctk.StringVar(value='off')
        self.__on = ctk.CTkRadioButton(self.__switch_frame, text= 'On',width=200, height=10, fg_color= 'black', command=lambda: self.on_off('on'), variable= self.var, value= 'on')
        self.__on.place(relx = 0.5, rely = 0.25, anchor = 'center')

        self.__off = ctk.CTkRadioButton(self.__switch_frame, text= 'Off', width=200, height=10, fg_color= 'black', command = lambda: self.on_off('off'), variable= self.var, value= 'off')
        self.__off.place(relx = 0.5, rely = 0.75, anchor = 'center')
        self.on_off(self.var.get())
    
    def on_off(self, ID):
        match ID:
            case 'on':
                for btn in range(len(self.buttonArray)):
                    self.buttonArray[btn].configure(state=ctk.NORMAL)
            case 'off':
                for btn in range(len(self.buttonArray)):
                    self.buttonArray[btn].configure(state=ctk.DISABLED)
run = Calculator()