import customtkinter as ctk
class Main:
    def __init__(self):
        self.__root = ctk.CTk()
        self.Main_window()
        
    def Main_window(self):
        self.__root.title('Calculator')
        self.__root.after(100, lambda: self.__get_fullscreen())
        self.__body()
        self.__root.mainloop()

    def __get_main_width_height(self, percentage, dimension):
        if dimension == 'width':
            return int(self.__root.winfo_screenwidth() * percentage)
        elif dimension == 'height':
            return int(self.__root.winfo_screenheight() * percentage)
        else:
            pass

    def __get_output_frame(self, percentage, dimension):
        if dimension == 'width':
            return self.__get_main_width_height(percentage, dimension)
        elif dimension == 'height':
            return self.__get_main_width_height(percentage, dimension)
        else:
            pass
    
    def __get_fullscreen(self):
        return self.__root.state('zoomed')

    def __get_root(self):
        return self.__root
    
    def __body(self):
        self.__output_frame = ctk.CTkFrame(self.__get_root(), 
                                           width=self.__get_output_frame(0.9, 'width'), 
                                           height= self.__get_output_frame(0.1, 'height'),
                                           fg_color= 'black')
        self.__output_frame.place(relx = 0.5, rely = 0.03, anchor='n')
        self.__button_inputs_frame = ctk.CTkFrame(self.__get_root(),
                                           width= self.__get_output_frame(0.5, 'width'),
                                           height= self.__get_output_frame(0.6, 'height'),
                                           fg_color= 'pink')
        self.__button_inputs_frame.place(relx = 0.3, rely = 0.2, anchor='n')
        self.__operation_inputs_frame = ctk.CTkFrame(self.__get_root(),
                                           width= self.__get_output_frame(0.3, 'width'),
                                           height= self.__get_output_frame(0.3, 'height'),
                                           fg_color= 'green')
        self.__operation_inputs_frame.place(relx = 0.75, rely = 0.4, anchor = 'n')
        self.__switch_on_off_frame = ctk.CTkFrame(self.__get_root(),
                                           width= self.__get_output_frame(0.3, 'width'),
                                           height= self.__get_output_frame(0.1, 'height'),
                                           fg_color= 'yellow')
        self.__switch_on_off_frame.place(relx = 0.75, rely = 0.2, anchor = 'n')
        self.__equal_button_frame = ctk.CTkFrame(self.__get_root(),
                                           width= self.__get_output_frame(0.3, 'width'),
                                           height= self.__get_output_frame(0.1, 'height'),
                                           fg_color= 'red')
        self.__equal_button_frame.place(relx= 0.75, rely = 0.74, anchor = 'n')
        self.__number_buttons()

    def __get_frames(self, frame):
        match frame:
            case 'output':
                return self.__output_frame
            case 'numbuts':
                return self.__button_inputs_frame
            case 'switch':
                return self.__switch_on_off_frame
            case 'equal':
                return self.__equal_button_frame
            
    def __number_buttons(self):
        ctk.CTkButton(self.__get_frames('numbuts'), text= '0',).grid(row=3, column='2', sticky = 'ew')
        ctk.CTkButton(self.__get_frames('numbuts'), text= '1').grid(row=2, column='1', sticky = 'ew')
        ctk.CTkButton(self.__get_frames('numbuts'), text= '2').grid(row=2, column='2', sticky = 'ew')
        ctk.CTkButton(self.__get_frames('numbuts'), text= '3').grid(row=2, column='3', sticky = 'ew')
        ctk.CTkButton(self.__get_frames('numbuts'), text= '4').grid(row=1, column='1', sticky = 'ew')
        ctk.CTkButton(self.__get_frames('numbuts'), text= '5').grid(row=1, column='2', sticky = 'ew')
        ctk.CTkButton(self.__get_frames('numbuts'), text= '6').grid(row=1, column='3', sticky = 'ew')
        ctk.CTkButton(self.__get_frames('numbuts'), text= '7').grid(row=0, column='1', sticky = 'ew')
        ctk.CTkButton(self.__get_frames('numbuts'), text= '8').grid(row=0, column='2', sticky = 'ew')
        ctk.CTkButton(self.__get_frames('numbuts'), text= '9').grid(row=0, column='3', sticky = 'ew')
run = Main()    