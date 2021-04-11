
"""
Program Sieve

Main class for application
Author: Jörg Sahlmann

"""

import tkinter as tk
from tkinter import *
from functools import partial
from module_db import search_file, insert_db, update_db, search_files_db

def buttonCloseClick(vn):
    print(vn)
    print("Close")
    sys.exit()


def buttonChooseClick():
    print("Choose")


def buttonSaveClick(vn, mfp, ins_update):
    c1 = 0 
    c2 = vn[0].get() + vn[1].get() + vn[2].get() + vn[3].get() + vn[4].get() + vn[5].get() + vn[6].get() + vn[7].get() + vn[8].get() + vn[9].get() + vn[10].get() + vn[11].get()
    c3 = vn[12].get() + vn[13].get() + vn[14].get() + vn[15].get() + vn[16].get() + vn[17].get() + vn[18].get() + vn[19].get() + vn[20].get() + vn[21].get() + vn[22].get() + vn[23].get() 
    c4 = vn[24].get() + vn[25].get() + vn[26].get() + vn[27].get() + vn[28].get() + vn[29].get() + vn[30].get() + vn[31].get() + vn[32].get() + vn[33].get() + vn[34].get() + vn[35].get() 
    c5 = vn[36].get() + vn[37].get() + vn[38].get() + vn[39].get() + vn[40].get() + vn[41].get() + vn[42].get() + vn[43].get() + vn[44].get() + vn[45].get() + vn[46].get() + vn[47].get() 
    c6 = vn[48].get() + vn[49].get() + vn[50].get() + vn[51].get() + vn[52].get() + vn[53].get() + vn[54].get() + vn[55].get() + vn[56].get() + vn[57].get() + vn[58].get() + vn[59].get() 
    c7 = vn[60].get() + vn[61].get() + vn[62].get() + vn[63].get() + vn[64].get() + vn[65].get() + vn[66].get() + vn[67].get() + vn[68].get() + vn[69].get() + vn[70].get() + vn[71].get()  
    c8 = vn[72].get() + vn[73].get() + vn[74].get() + vn[75].get() + vn[76].get() + vn[77].get() + vn[78].get() + vn[79].get() + vn[80].get() + vn[81].get() + vn[82].get() + vn[83].get() + vn[84].get() + vn[85].get()
    c9 = vn[86].get() + vn[87].get() + vn[88].get() + vn[89].get() + vn[90].get() + vn[91].get() + vn[92].get() + vn[93].get() + vn[94].get() + vn[95].get() + vn[96].get() + vn[97].get() + vn[98].get() + vn[99].get()
    c10 = vn[100].get() + vn[101].get() + vn[102].get() + vn[103].get() + vn[104].get() + vn[105].get() + vn[106].get() + vn[107].get() + vn[108].get() + vn[109].get() + vn[110].get() + vn[111].get() + vn[112].get() + vn[113].get()
    c11 = vn[114].get() + vn[115].get() + vn[116].get() + vn[117].get() + vn[118].get() + vn[119].get() + vn[120].get() + vn[121].get() + vn[122].get() + vn[123].get() + vn[124].get() + vn[125].get() + vn[126].get() + vn[127].get()
    c12 = vn[128].get() + vn[129].get() + vn[130].get() + vn[131].get() + vn[132].get() + vn[133].get() + vn[134].get() + vn[135].get() + vn[136].get() + vn[137].get() + vn[138].get() + vn[139].get() + vn[140].get() + vn[141].get()
    c13 = 0 
    c14 = 0 
    c15 = 0 
    c16 = 0 
    c17 = 0 
    c18 = 0 
    c19 = 0 
    c20 = 0
    if ins_update == -1:
        insert_db(r"E:\\ablage\\ksfe_2021\\prgsieve\\sieve.db", mfp, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19, c20)
    elif ins_update == 1:
        update_db(r"E:\\ablage\\ksfe_2021\\prgsieve\\sieve.db", mfp, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19, c20)
    else:
        print("Nothing to do for database.")
    print("Save")


def buttonSearchClick(vn):
    c1 = 0 
    c2 = vn[0].get() + vn[1].get() + vn[2].get() + vn[3].get() + vn[4].get() + vn[5].get() + vn[6].get() + vn[7].get() + vn[8].get() + vn[9].get() + vn[10].get() + vn[11].get()
    c3 = vn[12].get() + vn[13].get() + vn[14].get() + vn[15].get() + vn[16].get() + vn[17].get() + vn[18].get() + vn[19].get() + vn[20].get() + vn[21].get() + vn[22].get() + vn[23].get() 
    c4 = vn[24].get() + vn[25].get() + vn[26].get() + vn[27].get() + vn[28].get() + vn[29].get() + vn[30].get() + vn[31].get() + vn[32].get() + vn[33].get() + vn[34].get() + vn[35].get() 
    c5 = vn[36].get() + vn[37].get() + vn[38].get() + vn[39].get() + vn[40].get() + vn[41].get() + vn[42].get() + vn[43].get() + vn[44].get() + vn[45].get() + vn[46].get() + vn[47].get() 
    c6 = vn[48].get() + vn[49].get() + vn[50].get() + vn[51].get() + vn[52].get() + vn[53].get() + vn[54].get() + vn[55].get() + vn[56].get() + vn[57].get() + vn[58].get() + vn[59].get() 
    c7 = vn[60].get() + vn[61].get() + vn[62].get() + vn[63].get() + vn[64].get() + vn[65].get() + vn[66].get() + vn[67].get() + vn[68].get() + vn[69].get() + vn[70].get() + vn[71].get()  
    c8 = vn[72].get() + vn[73].get() + vn[74].get() + vn[75].get() + vn[76].get() + vn[77].get() + vn[78].get() + vn[79].get() + vn[80].get() + vn[81].get() + vn[82].get() + vn[83].get() + vn[84].get() + vn[85].get()
    c9 = vn[86].get() + vn[87].get() + vn[88].get() + vn[89].get() + vn[90].get() + vn[91].get() + vn[92].get() + vn[93].get() + vn[94].get() + vn[95].get() + vn[96].get() + vn[97].get() + vn[98].get() + vn[99].get()
    c10 = vn[100].get() + vn[101].get() + vn[102].get() + vn[103].get() + vn[104].get() + vn[105].get() + vn[106].get() + vn[107].get() + vn[108].get() + vn[109].get() + vn[110].get() + vn[111].get() + vn[112].get() + vn[113].get()
    c11 = vn[114].get() + vn[115].get() + vn[116].get() + vn[117].get() + vn[118].get() + vn[119].get() + vn[120].get() + vn[121].get() + vn[122].get() + vn[123].get() + vn[124].get() + vn[125].get() + vn[126].get() + vn[127].get()
    c12 = vn[128].get() + vn[129].get() + vn[130].get() + vn[131].get() + vn[132].get() + vn[133].get() + vn[134].get() + vn[135].get() + vn[136].get() + vn[137].get() + vn[138].get() + vn[139].get() + vn[140].get() + vn[141].get()
    c13 = 0 
    c14 = 0 
    c15 = 0 
    c16 = 0 
    c17 = 0 
    c18 = 0 
    c19 = 0 
    c20 = 0
    search_files_db(r"E:\\ablage\\ksfe_2021\\prgsieve\\sieve.db", c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19, c20)
    print("Search")


class PrgSieve(Frame):

    def __init__(self, mfp):
        super().__init__()
        self.vars = []
        self.initUI(mfp)
    
    def initUI(self, myfilepath):

        self.master.title("Program Sieve")

        fl = search_file(r"E:\\ablage\\ksfe_2021\\prgsieve\\sieve.db", myfilepath)

        # =============================================================================================================
        # Label File
        labelFile = Label(self, text = 'File')
        labelFile.grid(row = 0, column = 0, padx = '5', pady = '5', sticky = 'ew')
        # Entry for path and filename
        entryFileText = StringVar()
        entryFile = Entry(self, bg = 'white', width = '8', textvariable = entryFileText)
        entryFile.grid(row = 0, column = 1, columnspan = 10, padx = '5', pady = '5', sticky = 'ew')
        entryFileText.set(myfilepath)

        # =============================================================================================================
        # Label R2 = Language 
        label_R2C0 = Label(self, bg = '#80CCFF', text = 'Language')
        label_R2C0.grid(row = 2, column = 0, padx = '5', pady = '5', sticky = 'ew')
        # Checkbutton R2C1 = SAS
        value_R2C1 = IntVar()
        cb_R2C1 = Checkbutton(self, anchor='w', text='SAS', offvalue = 0, onvalue = 1, variable = value_R2C1)
        cb_R2C1.grid(row = 2, column = 1, sticky=W+E)
        if fl[1] & 1:
            cb_R2C1.select()
        self.vars.append(value_R2C1) # 0
        # Checkbutton R2C2 = R
        value_R2C2 = IntVar()
        cb_R2C2 = Checkbutton(self, anchor='w', text='R', offvalue = 0, onvalue = 2, variable = value_R2C2)
        cb_R2C2.grid(row = 2, column = 2, sticky=W+E)
        if fl[1] & 2:
            cb_R2C2.select()
        self.vars.append(value_R2C2) # 1
        # Checkbutton R2C3 = Python
        value_R2C3 = IntVar()
        cb_R2C3 = Checkbutton(self, anchor='w', text='Python', offvalue = 0, onvalue = 4, variable = value_R2C3)
        cb_R2C3.grid(row = 2, column = 3, sticky=W+E)
        if fl[1] & 4:
            cb_R2C3.select()
        self.vars.append(value_R2C3) # 2
        # Checkbutton R2C4 = SQL
        value_R2C4 = IntVar()
        cb_R2C4 = Checkbutton(self, anchor='w', text='SQL', offvalue = 0, onvalue = 8, variable = value_R2C4)
        cb_R2C4.grid(row = 2, column = 4, sticky=W+E)
        if fl[1] & 8:
            cb_R2C4.select()
        self.vars.append(value_R2C4) # 3
        # Checkbutton R2C5 = Julia
        value_R2C5 = IntVar()
        cb_R2C5 = Checkbutton(self, anchor='w', text='Julia', offvalue = 0, onvalue = 16, variable = value_R2C5)
        cb_R2C5.grid(row = 2, column = 5, sticky=W+E)
        if fl[1] & 16:
            cb_R2C5.select()
        self.vars.append(value_R2C5) # 4
        # Checkbutton R2C6 = Matlab
        value_R2C6 = IntVar()
        cb_R2C6 = Checkbutton(self, anchor='w', text='Matlab', offvalue = 0, onvalue = 32, variable = value_R2C6)
        cb_R2C6.grid(row = 2, column = 6, sticky=W+E)
        if fl[1] & 32:
            cb_R2C6.select()
        self.vars.append(value_R2C6) # 5
        # Checkbutton R2C7 = Octave
        value_R2C7 = IntVar()
        cb_R2C7 = Checkbutton(self, anchor='w', text='Octave', offvalue = 0, onvalue = 64, variable = value_R2C7)
        cb_R2C7.grid(row = 2, column = 7, sticky=W+E)
        if fl[1] & 64:
            cb_R2C7.select()
        self.vars.append(value_R2C7) # 6
        # Checkbutton R2C8 = Language 8
        value_R2C8 = IntVar()
        cb_R2C8 = Checkbutton(self, anchor='w', text='Language 8', offvalue = 0, onvalue = 128, variable = value_R2C8)
        cb_R2C8.grid(row = 2, column = 8, sticky=W+E)
        if fl[1] & 128:
            cb_R2C8.select()
        self.vars.append(value_R2C8) # 7
        # Checkbutton R2C9 = Language 9
        value_R2C9 = IntVar()
        cb_R2C9 = Checkbutton(self, anchor='w', text='Language 9', offvalue = 0, onvalue = 256, variable = value_R2C9)
        cb_R2C9.grid(row = 2, column = 9, sticky=W+E)
        if fl[1] & 256:
            cb_R2C9.select()
        self.vars.append(value_R2C9) # 8
        # Checkbutton R2C10 = Language 10
        value_R2C10 = IntVar()
        cb_R2C10 = Checkbutton(self, anchor='w', text='Language 10', offvalue = 0, onvalue = 512, variable = value_R2C10)
        cb_R2C10.grid(row = 2, column = 10, sticky=W+E)
        if fl[1] & 512:
            cb_R2C10.select()
        self.vars.append(value_R2C10) # 9
        # Checkbutton R2C11 = Language 11
        value_R2C11 = IntVar()
        cb_R2C11 = Checkbutton(self, anchor='w', text='Language 11', offvalue = 0, onvalue = 1024, variable = value_R2C11)
        cb_R2C11.grid(row = 2, column = 11, sticky=W+E)
        if fl[1] & 1024:
            cb_R2C11.select()
        self.vars.append(value_R2C11) # 10
        # Checkbutton R2C12 = Language 12
        value_R2C12 = IntVar()
        cb_R2C12 = Checkbutton(self, anchor='w', text='Language 12', offvalue = 0, onvalue = 2048, variable = value_R2C12)
        cb_R2C12.grid(row = 2, column = 12, sticky=W+E)
        if fl[1] & 2048:
            cb_R2C12.select()
        self.vars.append(value_R2C12) # 11

        # =============================================================================================================
        # Label R3 = SDTM 1
        label_R3C0 = Label(self, bg = '#80CCFF', text = 'SDTM')
        label_R3C0.grid(row = 3, column = 0, padx = '5', pady = '5', sticky = 'ew')
        # Checkbutton R3C1 = SDTM_CO
        value_R3C1 = IntVar()
        cb_R3C1 = Checkbutton(self, anchor='w', text='CO', offvalue = 0, onvalue = 1, variable = value_R3C1)
        cb_R3C1.grid(row = 3, column = 1, sticky=W+E)
        if fl[2] & 1:
            cb_R3C1.select()
        self.vars.append(value_R3C1) # 12
        # Checkbutton R3C2 = SDTM_DM
        value_R3C2 = IntVar()
        cb_R3C2 = Checkbutton(self, anchor='w', text='DM', offvalue = 0, onvalue = 2, variable = value_R3C2)
        cb_R3C2.grid(row = 3, column = 2, sticky=W+E)
        if fl[2] & 2:
            cb_R3C2.select()
        self.vars.append(value_R3C2) # 13
        # Checkbutton R3C3 = SDTM_SE
        value_R3C3 = IntVar()
        cb_R3C3 = Checkbutton(self, anchor='w', text='SE', offvalue = 0, onvalue = 4, variable = value_R3C3)
        cb_R3C3.grid(row = 3, column = 3, sticky=W+E)
        if fl[2] & 4:
            cb_R3C3.select()
        self.vars.append(value_R3C3) # 14
        # Checkbutton R3C4 = SDTM_SV
        value_R3C4 = IntVar()
        cb_R3C4 = Checkbutton(self, anchor='w', text='SV', offvalue = 0, onvalue = 8, variable = value_R3C4)
        cb_R3C4.grid(row = 3, column = 4, sticky=W+E)
        if fl[2] & 8:
            cb_R3C4.select()
        self.vars.append(value_R3C4) # 15
        # Checkbutton R3C5 = SDTM_CM
        value_R3C5 = IntVar()
        cb_R3C5 = Checkbutton(self, anchor='w', text='CM', offvalue = 0, onvalue = 16, variable = value_R3C5)
        cb_R3C5.grid(row = 3, column = 5, sticky=W+E)
        if fl[2] & 16:
            cb_R3C5.select()
        self.vars.append(value_R3C5) # 16
        # Checkbutton R3C6 = SDTM_EC
        value_R3C6 = IntVar()
        cb_R3C6 = Checkbutton(self, anchor='w', text='EC', offvalue = 0, onvalue = 32, variable = value_R3C6)
        cb_R3C6.grid(row = 3, column = 6, sticky=W+E)
        if fl[2] & 32:
            cb_R3C6.select()
        self.vars.append(value_R3C6) # 17
        # Checkbutton R3C7 = SDTM_EX
        value_R3C7 = IntVar()
        cb_R3C7 = Checkbutton(self, anchor='w', text='EX', offvalue = 0, onvalue = 64, variable = value_R3C7)
        cb_R3C7.grid(row = 3, column = 7, sticky=W+E)
        if fl[2] & 64:
            cb_R3C7.select()
        self.vars.append(value_R3C7) # 18
        # Checkbutton R3C8 = SDTM_SU
        value_R3C8 = IntVar()
        cb_R3C8 = Checkbutton(self, anchor='w', text='SU', offvalue = 0, onvalue = 128, variable = value_R3C8)
        cb_R3C8.grid(row = 3, column = 8, sticky=W+E)
        if fl[2] & 128:
            cb_R3C8.select()
        self.vars.append(value_R3C8) # 19
        # Checkbutton R3C9 = SDTM_PR
        value_R3C9 = IntVar()
        cb_R3C9 = Checkbutton(self, anchor='w', text='PR', offvalue = 0, onvalue = 256, variable = value_R3C9)
        cb_R3C9.grid(row = 3, column = 9, sticky=W+E)
        if fl[2] & 256:
            cb_R3C9.select()
        self.vars.append(value_R3C9) # 20
        # Checkbutton R3C10 = SDTM_AE
        value_R3C10 = IntVar()
        cb_R3C10 = Checkbutton(self, anchor='w', text='AE', offvalue = 0, onvalue = 512, variable = value_R3C10)
        cb_R3C10.grid(row = 3, column = 10, sticky=W+E)
        if fl[2] & 512:
            cb_R3C10.select()
        self.vars.append(value_R3C10) # 21
        # Checkbutton R3C11 = SDTM_CE
        value_R3C11 = IntVar()
        cb_R3C11 = Checkbutton(self, anchor='w', text='CE', offvalue = 0, onvalue = 1024, variable = value_R3C11)
        cb_R3C11.grid(row = 3, column = 11, sticky=W+E)
        if fl[2] & 1024:
            cb_R3C11.select()
        self.vars.append(value_R3C11) # 22
        # Checkbutton R3C12 = SDTM_R3C12
        value_R3C12 = IntVar()
        cb_R3C12 = Checkbutton(self, anchor='w', text='DS', offvalue = 0, onvalue = 2048, variable = value_R3C12)
        cb_R3C12.grid(row = 3, column = 12, sticky=W+E)
        if fl[2] & 2048:
            cb_R3C12.select()
        self.vars.append(value_R3C12) # 23

        # =============================================================================================================
        # Label R4 = SDTM 2
        #label_R4C0 = Label(self, bg = '#80CCFF', text = 'SDTM 2')
        #label_R4C0.grid(row = 4, column = 0, padx = '5', pady = '5', sticky = 'ew')
        # Checkbutton R4C1 = SDTM_DV
        value_R4C1 = IntVar()
        cb_R4C1 = Checkbutton(self, anchor='w', text='DV', offvalue = 0, onvalue = 1, variable = value_R4C1)
        cb_R4C1.grid(row = 4, column = 1, sticky=W+E)
        if fl[3] & 1:
            cb_R4C1.select()
        self.vars.append(value_R4C1) # 24
        # Checkbutton R4C2 = SDTM_MH
        value_R4C2 = IntVar()
        cb_R4C2 = Checkbutton(self, anchor='w', text='MH', offvalue = 0, onvalue = 2, variable = value_R4C2)
        cb_R4C2.grid(row = 4, column = 2, sticky=W+E)
        if fl[3] & 2:
            cb_R4C2.select()
        self.vars.append(value_R4C2) # 25
        # Checkbutton R4C3 = SDTM_HO
        value_R4C3 = IntVar()
        cb_R4C3 = Checkbutton(self, anchor='w', text='HO', offvalue = 0, onvalue = 4, variable = value_R4C3)
        cb_R4C3.grid(row = 4, column = 3, sticky=W+E)
        if fl[3] & 4:
            cb_R4C3.select()
        self.vars.append(value_R4C3) # 26
        # Checkbutton R4C4 = SDTM_DA
        value_R4C4 = IntVar()
        cb_R4C4 = Checkbutton(self, anchor='w', text='DA', offvalue = 0, onvalue = 8, variable = value_R4C4)
        cb_R4C4.grid(row = 4, column = 4, sticky=W+E)
        if fl[3] & 8:
            cb_R4C4.select()
        self.vars.append(value_R4C4) # 27
        # Checkbutton R4C5 = SDTM_DD
        value_R4C5 = IntVar()
        cb_R4C5 = Checkbutton(self, anchor='w', text='DD', offvalue = 0, onvalue = 16, variable = value_R4C5)
        cb_R4C5.grid(row = 4, column = 5, sticky=W+E)
        if fl[3] & 16:
            cb_R4C5.select()
        self.vars.append(value_R4C5) # 28
        # Checkbutton R4C6 = SDTM_EG
        value_R4C6 = IntVar()
        cb_R4C6 = Checkbutton(self, anchor='w', text='EG', offvalue = 0, onvalue = 32, variable = value_R4C6)
        cb_R4C6.grid(row = 4, column = 6, sticky=W+E)
        if fl[3] & 32:
            cb_R4C6.select()
        self.vars.append(value_R4C6) # 29
        # Checkbutton R4C7 = SDTM_IE
        value_R4C7 = IntVar()
        cb_R4C7 = Checkbutton(self, anchor='w', text='IE', offvalue = 0, onvalue = 64, variable = value_R4C7)
        cb_R4C7.grid(row = 4, column = 7, sticky=W+E)
        if fl[3] & 64:
            cb_R4C7.select()
        self.vars.append(value_R4C7) # 30
        # Checkbutton R4C8 = SDTM_IS
        value_R4C8 = IntVar()
        cb_R4C8 = Checkbutton(self, anchor='w', text='IS', offvalue = 0, onvalue = 128, variable = value_R4C8)
        cb_R4C8.grid(row = 4, column = 8, sticky=W+E)
        if fl[3] & 128:
            cb_R4C8.select()
        self.vars.append(value_R4C8) # 31
        # Checkbutton R4C9 = SDTM_LB
        value_R4C9 = IntVar()
        cb_R4C9 = Checkbutton(self, anchor='w', text='LB', offvalue = 0, onvalue = 256, variable = value_R4C9)
        cb_R4C9.grid(row = 4, column = 9, sticky=W+E)
        if fl[3] & 256:
            cb_R4C9.select()
        self.vars.append(value_R4C9) # 32
        # Checkbutton R4C10 = SDTM_MB
        value_R4C10 = IntVar()
        cb_R4C10 = Checkbutton(self, anchor='w', text='MB', offvalue = 0, onvalue = 512, variable = value_R4C10)
        cb_R4C10.grid(row = 4, column = 10, sticky=W+E)
        if fl[3] & 512:
            cb_R4C10.select()
        self.vars.append(value_R4C10) # 33
        # Checkbutton R4C11 = SDTM_MI
        value_R4C11 = IntVar()
        cb_R4C11 = Checkbutton(self, anchor='w', text='MI', offvalue = 0, onvalue = 1024, variable = value_R4C11)
        cb_R4C11.grid(row = 4, column = 11, sticky=W+E)
        if fl[3] & 1024:
            cb_R4C11.select()
        self.vars.append(value_R4C11) # 34
        # Checkbutton R4C12 = SDTM_MO
        value_R4C12 = IntVar()
        cb_R4C12 = Checkbutton(self, anchor='w', text='MO', offvalue = 0, onvalue = 2048, variable = value_R4C12)
        cb_R4C12.grid(row = 4, column = 12, sticky=W+E)
        if fl[3] & 2048:
            cb_R4C12.select()
        self.vars.append(value_R4C12) # 35

        # =============================================================================================================
        # Label R5 = SDTM 3
        #label_R5C0 = Label(self, bg = '#80CCFF', text = 'SDTM 3')
        #label_R5C0.grid(row = 5, column = 0, padx = '5', pady = '5', sticky = 'ew')
        # Checkbutton R5C1 = SDTM_MS
        value_R5C1 = IntVar()
        cb_R5C1 = Checkbutton(self, anchor='w', text='MS', offvalue = 0, onvalue = 1, variable = value_R5C1)
        cb_R5C1.grid(row = 5, column = 1, sticky=W+E)
        if fl[4] & 1:
            cb_R5C1.select()
        self.vars.append(value_R5C1) # 36
        # Checkbutton R5C2 = SDTM_PC
        value_R5C2 = IntVar()
        cb_R5C2 = Checkbutton(self, anchor='w', text='PC', offvalue = 0, onvalue = 2, variable = value_R5C2)
        cb_R5C2.grid(row = 5, column = 2, sticky=W+E)
        if fl[4] & 2:
            cb_R5C2.select()
        self.vars.append(value_R5C2) # 37
        # Checkbutton R5C3 = SDTM_PP
        value_R5C3 = IntVar()
        cb_R5C3 = Checkbutton(self, anchor='w', text='PP', offvalue = 0, onvalue = 4, variable = value_R5C3)
        cb_R5C3.grid(row = 5, column = 3, sticky=W+E)
        if fl[4] & 4:
            cb_R5C3.select()
        self.vars.append(value_R5C3) # 38
        # Checkbutton R5C4 = SDTM_PE
        value_R5C4 = IntVar()
        cb_R5C4 = Checkbutton(self, anchor='w', text='PE', offvalue = 0, onvalue = 8, variable = value_R5C4)
        cb_R5C4.grid(row = 5, column = 4, sticky=W+E)
        if fl[4] & 8:
            cb_R5C4.select()
        self.vars.append(value_R5C4) # 39
        # Checkbutton R5C5 = SDTM_QS
        value_R5C5 = IntVar()
        cb_R5C5 = Checkbutton(self, anchor='w', text='QS', offvalue = 0, onvalue = 16, variable = value_R5C5)
        cb_R5C5.grid(row = 5, column = 5, sticky=W+E)
        if fl[4] & 16:
            cb_R5C5.select()
        self.vars.append(value_R5C5) # 40
        # Checkbutton R5C6 = SDTM_RP
        value_R5C6 = IntVar()
        cb_R5C6 = Checkbutton(self, anchor='w', text='RP', offvalue = 0, onvalue = 32, variable = value_R5C6)
        cb_R5C6.grid(row = 5, column = 6, sticky=W+E)
        if fl[4] & 32:
            cb_R5C6.select()
        self.vars.append(value_R5C6) # 41
        # Checkbutton R5C7 = SDTM_RS
        value_R5C7 = IntVar()
        cb_R5C7 = Checkbutton(self, anchor='w', text='RS', offvalue = 0, onvalue = 64, variable = value_R5C7)
        cb_R5C7.grid(row = 5, column = 7, sticky=W+E)
        if fl[4] & 64:
            cb_R5C7.select()
        self.vars.append(value_R5C7) # 42
        # Checkbutton R5C8 = SDTM_SC
        value_R5C8 = IntVar()
        cb_R5C8 = Checkbutton(self, anchor='w', text='SC', offvalue = 0, onvalue = 128, variable = value_R5C8)
        cb_R5C8.grid(row = 5, column = 8, sticky=W+E)
        if fl[4] & 128:
            cb_R5C8.select()
        self.vars.append(value_R5C8) # 43
        # Checkbutton R5C9 = SDTM_SS
        value_R5C9 = IntVar()
        cb_R5C9 = Checkbutton(self, anchor='w', text='SS', offvalue = 0, onvalue = 256, variable = value_R5C9)
        cb_R5C9.grid(row = 5, column = 9, sticky=W+E)
        if fl[4] & 256:
            cb_R5C9.select()
        self.vars.append(value_R5C9) # 44
        # Checkbutton R5C10 = SDTM_TU
        value_R5C10 = IntVar()
        cb_R5C10 = Checkbutton(self, anchor='w', text='TU', offvalue = 0, onvalue = 512, variable = value_R5C10)
        cb_R5C10.grid(row = 5, column = 10, sticky=W+E)
        if fl[4] & 512:
            cb_R5C10.select()
        self.vars.append(value_R5C10) # 45
        # Checkbutton R5C11 = SDTM_TR
        value_R5C11 = IntVar()
        cb_R5C11 = Checkbutton(self, anchor='w', text='TR', offvalue = 0, onvalue = 1024, variable = value_R5C11)
        cb_R5C11.grid(row = 5, column = 11, sticky=W+E)
        if fl[4] & 1024:
            cb_R5C11.select()
        self.vars.append(value_R5C11) # 46
        # Checkbutton R5C12 = SDTM_VS
        value_R5C12 = IntVar()
        cb_R5C12 = Checkbutton(self, anchor='w', text='VS', offvalue = 0, onvalue = 2048, variable = value_R5C12)
        cb_R5C12.grid(row = 5, column = 12, sticky=W+E)
        if fl[4] & 2048:
            cb_R5C12.select()
        self.vars.append(value_R5C12) # 47

        # =============================================================================================================
        # Label R6 = ADAM
        label_R6C0 = Label(self, bg = '#80CCFF', text = 'ADAM')
        label_R6C0.grid(row = 6, column = 0, padx = '5', pady = '5', sticky = 'ew')
        # Checkbutton R6C1 = ADSL
        value_R6C1 = IntVar()
        cb_R6C1 = Checkbutton(self, anchor='w', text='ADSL', offvalue = 0, onvalue = 1, variable = value_R6C1)
        cb_R6C1.grid(row = 6, column = 1, sticky=W+E)
        if fl[5] & 1:
            cb_R6C1.select()
        self.vars.append(value_R6C1) # 48
        # Checkbutton R6C2 = ADEX
        value_R6C2 = IntVar()
        cb_R6C2 = Checkbutton(self, anchor='w', text='ADEX', offvalue = 0, onvalue = 2, variable = value_R6C2)
        cb_R6C2.grid(row = 6, column = 2, sticky=W+E)
        if fl[5] & 2:
            cb_R6C2.select()
        self.vars.append(value_R6C2) # 49
        # Checkbutton R6C3 = ADLB
        value_R6C3 = IntVar()
        cb_R6C3 = Checkbutton(self, anchor='w', text='ADLB', offvalue = 0, onvalue = 4, variable = value_R6C3)
        cb_R6C3.grid(row = 6, column = 3, sticky=W+E)
        if fl[5] & 4:
            cb_R6C3.select()
        self.vars.append(value_R6C3) # 50
        # Checkbutton R6C4 = ADQS
        value_R6C4 = IntVar()
        cb_R6C4 = Checkbutton(self, anchor='w', text='ADQS', offvalue = 0, onvalue = 8, variable = value_R6C4)
        cb_R6C4.grid(row = 6, column = 4, sticky=W+E)
        if fl[5] & 8:
            cb_R6C4.select()
        self.vars.append(value_R6C4) # 51
        # Checkbutton R6C5 = ADTTE
        value_R6C5 = IntVar()
        cb_R6C5 = Checkbutton(self, anchor='w', text='ADTTE', offvalue = 0, onvalue = 16, variable = value_R6C5)
        cb_R6C5.grid(row = 6, column = 5, sticky=W+E)
        if fl[5] & 16:
            cb_R6C5.select()
        self.vars.append(value_R6C5) # 52
        # Checkbutton R6C6 = ADCM
        value_R6C6 = IntVar()
        cb_R6C6 = Checkbutton(self, anchor='w', text='ADCM', offvalue = 0, onvalue = 32, variable = value_R6C6)
        cb_R6C6.grid(row = 6, column = 6, sticky=W+E)
        if fl[5] & 32:
            cb_R6C6.select()
        self.vars.append(value_R6C6) # 53
        # Checkbutton R6C7 = ADPR
        value_R6C7 = IntVar()
        cb_R6C7 = Checkbutton(self, anchor='w', text='ADPR', offvalue = 0, onvalue = 64, variable = value_R6C7)
        cb_R6C7.grid(row = 6, column = 7, sticky=W+E)
        if fl[5] & 64:
            cb_R6C7.select()
        self.vars.append(value_R6C7) # 54
        # Checkbutton R6C8 = ADAE
        value_R6C8 = IntVar()
        cb_R6C8 = Checkbutton(self, anchor='w', text='ADAE', offvalue = 0, onvalue = 128, variable = value_R6C8)
        cb_R6C8.grid(row = 6, column = 8, sticky=W+E)
        if fl[5] & 128:
            cb_R6C8.select()
        self.vars.append(value_R6C8) # 55
        # Checkbutton R6C9 = ADDS
        value_R6C9 = IntVar()
        cb_R6C9 = Checkbutton(self, anchor='w', text='ADDS', offvalue = 0, onvalue = 256, variable = value_R6C9)
        cb_R6C9.grid(row = 6, column = 9, sticky=W+E)
        if fl[5] & 256:
            cb_R6C9.select()
        self.vars.append(value_R6C9) # 56
        # Checkbutton R6C10 = ADDV
        value_R6C10 = IntVar()
        cb_R6C10 = Checkbutton(self, anchor='w', text='ADMH', offvalue = 0, onvalue = 512, variable = value_R6C10)
        cb_R6C10.grid(row = 6, column = 10, sticky=W+E)
        if fl[5] & 512:
            cb_R6C10.select()
        self.vars.append(value_R6C10) # 57
        # Checkbutton R6C11 = ADHO
        value_R6C11 = IntVar()
        cb_R6C11 = Checkbutton(self, anchor='w', text='ADHO', offvalue = 0, onvalue = 1024, variable = value_R6C11)
        cb_R6C11.grid(row = 6, column = 11, sticky=W+E)
        if fl[5] & 1024:
            cb_R6C11.select()
        self.vars.append(value_R6C11) # 58
        # Checkbutton R6C12 = ADMI
        value_R6C12 = IntVar()
        cb_R6C12 = Checkbutton(self, anchor='w', text='ADMI', offvalue = 0, onvalue = 2048, variable = value_R6C12)
        cb_R6C12.grid(row = 6, column = 12, sticky=W+E)
        if fl[5] & 2048:
            cb_R6C12.select()
        self.vars.append(value_R6C12) # 59

        # =============================================================================================================
        # Label R7 = ADAM 2
        # label_R7C0 = Label(self, bg = '#80CCFF', text = 'ADAM')
        # label_R7C0.grid(row = 7, column = 0, padx = '5', pady = '5', sticky = 'ew')
        # Checkbutton R7C1 = AD 13
        value_R7C1 = IntVar()
        cb_R7C1 = Checkbutton(self, anchor='w', text='AD 13', offvalue = 0, onvalue = 1, variable = value_R7C1)
        cb_R7C1.grid(row = 7, column = 1, sticky=W+E)
        if fl[6] & 1:
            cb_R7C1.select()
        self.vars.append(value_R7C1) # 60
        # Checkbutton R7C2 = AD 14
        value_R7C2 = IntVar()
        cb_R7C2 = Checkbutton(self, anchor='w', text='AD 14', offvalue = 0, onvalue = 2, variable = value_R7C2)
        cb_R7C2.grid(row = 7, column = 2, sticky=W+E)
        if fl[6] & 2:
            cb_R7C2.select()
        self.vars.append(value_R7C2) # 61
        # Checkbutton R7C3 = AD 15
        value_R7C3 = IntVar()
        cb_R7C3 = Checkbutton(self, anchor='w', text='AD 15', offvalue = 0, onvalue = 4, variable = value_R7C3)
        cb_R7C3.grid(row = 7, column = 3, sticky=W+E)
        if fl[6] & 4:
            cb_R7C3.select()
        self.vars.append(value_R7C3) # 62
        # Checkbutton R7C4 = AD 16
        value_R7C4 = IntVar()
        cb_R7C4 = Checkbutton(self, anchor='w', text='AD 16', offvalue = 0, onvalue = 8, variable = value_R7C4)
        cb_R7C4.grid(row = 7, column = 4, sticky=W+E)
        if fl[6] & 8:
            cb_R7C4.select()
        self.vars.append(value_R7C4) # 63
        # Checkbutton R7C5 = AD 17
        value_R7C5 = IntVar()
        cb_R7C5 = Checkbutton(self, anchor='w', text='AD 17', offvalue = 0, onvalue = 16, variable = value_R7C5)
        cb_R7C5.grid(row = 7, column = 5, sticky=W+E)
        if fl[6] & 16:
            cb_R7C5.select()
        self.vars.append(value_R7C5) # 64
        # Checkbutton R7C6 = AD 18
        value_R7C6 = IntVar()
        cb_R7C6 = Checkbutton(self, anchor='w', text='AD 18', offvalue = 0, onvalue = 32, variable = value_R7C6)
        cb_R7C6.grid(row = 7, column = 6, sticky=W+E)
        if fl[6] & 32:
            cb_R7C6.select()
        self.vars.append(value_R7C6) # 65
        # Checkbutton R7C7 = AD 19
        value_R7C7 = IntVar()
        cb_R7C7 = Checkbutton(self, anchor='w', text='AD 19', offvalue = 0, onvalue = 64, variable = value_R7C7)
        cb_R7C7.grid(row = 7, column = 7, sticky=W+E)
        if fl[6] & 64:
            cb_R7C7.select()
        self.vars.append(value_R7C7) # 66
        # Checkbutton R7C8 = AD 20
        value_R7C8 = IntVar()
        cb_R7C8 = Checkbutton(self, anchor='w', text='AD 20', offvalue = 0, onvalue = 128, variable = value_R7C8)
        cb_R7C8.grid(row = 7, column = 8, sticky=W+E)
        if fl[6] & 128:
            cb_R7C8.select()
        self.vars.append(value_R7C8) # 67
        # Checkbutton R7C9 = AD 21
        value_R7C9 = IntVar()
        cb_R7C9 = Checkbutton(self, anchor='w', text='AD 21', offvalue = 0, onvalue = 256, variable = value_R7C9)
        cb_R7C9.grid(row = 7, column = 9, sticky=W+E)
        if fl[6] & 256:
            cb_R7C9.select()
        self.vars.append(value_R7C9) # 68
        # Checkbutton R7C10 = AD 22
        value_R7C10 = IntVar()
        cb_R7C10 = Checkbutton(self, anchor='w', text='AD 22', offvalue = 0, onvalue = 512, variable = value_R7C10)
        cb_R7C10.grid(row = 7, column = 10, sticky=W+E)
        if fl[6] & 512:
            cb_R7C10.select()
        self.vars.append(value_R7C10) # 69
        # Checkbutton R7C11 = AD 23
        value_R7C11 = IntVar()
        cb_R7C11 = Checkbutton(self, anchor='w', text='AD 23', offvalue = 0, onvalue = 1024, variable = value_R7C11)
        cb_R7C11.grid(row = 7, column = 11, sticky=W+E)
        if fl[6] & 1024:
            cb_R7C11.select()
        self.vars.append(value_R7C11) # 70
        # Checkbutton R7C12 = AD 24
        value_R7C12 = IntVar()
        cb_R7C12 = Checkbutton(self, anchor='w', text='AD 24', offvalue = 0, onvalue = 2048, variable = value_R7C12)
        cb_R7C12.grid(row = 7, column = 12, sticky=W+E)
        if fl[6] & 2048:
            cb_R7C12.select()
        self.vars.append(value_R7C12) # 71

        # =============================================================================================================
        # Label R8 = SGPLOT 1
        label_R8C0 = Label(self, bg = '#80CCFF', text = 'SGPLOT')
        label_R8C0.grid(row = 8, column = 0, padx = '5', pady = '5', sticky = 'ew')
        # Checkbutton R8C1 = Band
        value_R8C1 = IntVar()
        cb_R8C1 = Checkbutton(self, anchor='w', text='Band', offvalue = 0, onvalue = 1, variable = value_R8C1)
        cb_R8C1.grid(row = 8, column = 1, sticky=W+E)
        if fl[7] & 1:
            cb_R8C1.select()
        self.vars.append(value_R8C1) # 72
        # Checkbutton R8C2 = Block
        value_R8C2 = IntVar()
        cb_R8C2 = Checkbutton(self, anchor='w', text='Block', offvalue = 0, onvalue = 2, variable = value_R8C2)
        cb_R8C2.grid(row = 8, column = 2, sticky=W+E)
        if fl[7] & 2:
            cb_R8C2.select()
        self.vars.append(value_R8C2) # 73
        # Checkbutton R8C3 = Bubble
        value_R8C3 = IntVar()
        cb_R8C3 = Checkbutton(self, anchor='w', text='Bubble', offvalue = 0, onvalue = 4, variable = value_R8C3)
        cb_R8C3.grid(row = 8, column = 3, sticky=W+E)
        if fl[7] & 4:
            cb_R8C3.select()
        self.vars.append(value_R8C3) # 74
        # Checkbutton R8C4 = Density
        value_R8C4 = IntVar()
        cb_R8C4 = Checkbutton(self, anchor='w', text='Density', offvalue = 0, onvalue = 8, variable = value_R8C4)
        cb_R8C4.grid(row = 8, column = 4, sticky=W+E)
        if fl[7] & 8:
            cb_R8C4.select()
        self.vars.append(value_R8C4) # 75
        # Checkbutton R8C5 = Dot
        value_R8C5 = IntVar()
        cb_R8C5 = Checkbutton(self, anchor='w', text='Dot', offvalue = 0, onvalue = 16, variable = value_R8C5)
        cb_R8C5.grid(row = 8, column = 5, sticky=W+E)
        if fl[7] & 16:
            cb_R8C5.select()
        self.vars.append(value_R8C5) # 76
        # Checkbutton R8C6 = Dropline
        value_R8C6 = IntVar()
        cb_R8C6 = Checkbutton(self, anchor='w', text='Dropline', offvalue = 0, onvalue = 32, variable = value_R8C6)
        cb_R8C6.grid(row = 8, column = 6, sticky=W+E)
        if fl[7] & 32:
            cb_R8C6.select()
        self.vars.append(value_R8C6) # 77
        # Checkbutton R8C7 = Ellipse
        value_R8C7 = IntVar()
        cb_R8C7 = Checkbutton(self, anchor='w', text='Ellipse', offvalue = 0, onvalue = 64, variable = value_R8C7)
        cb_R8C7.grid(row = 8, column = 7, sticky=W+E)
        if fl[7] & 64:
            cb_R8C7.select()
        self.vars.append(value_R8C7) # 78
        # Checkbutton R8C8 = Fringe
        value_R8C8 = IntVar()
        cb_R8C8 = Checkbutton(self, anchor='w', text='Fringe', offvalue = 0, onvalue = 128, variable = value_R8C8)
        cb_R8C8.grid(row = 8, column = 8, sticky=W+E)
        if fl[7] & 128:
            cb_R8C8.select()
        self.vars.append(value_R8C8) # 79
        # Checkbutton R8C9 = Hbar
        value_R8C9 = IntVar()
        cb_R8C9 = Checkbutton(self, anchor='w', text='Hbar', offvalue = 0, onvalue = 256, variable = value_R8C9)
        cb_R8C9.grid(row = 8, column = 9, sticky=W+E)
        if fl[7] & 256:
            cb_R8C9.select()
        self.vars.append(value_R8C9) # 80
        # Checkbutton R8C10 = Hbox
        value_R8C10 = IntVar()
        cb_R8C10 = Checkbutton(self, anchor='w', text='Hbox', offvalue = 0, onvalue = 512, variable = value_R8C10)
        cb_R8C10.grid(row = 8, column = 10, sticky=W+E)
        if fl[7] & 512:
            cb_R8C10.select()
        self.vars.append(value_R8C10) # 81
        # Checkbutton R8C11 = Heatmap
        value_R8C11 = IntVar()
        cb_R8C11 = Checkbutton(self, anchor='w', text='Heatmap', offvalue = 0, onvalue = 1024, variable = value_R8C11)
        cb_R8C11.grid(row = 8, column = 11, sticky=W+E)
        if fl[7] & 1024:
            cb_R8C11.select()
        self.vars.append(value_R8C11) # 82
        # Checkbutton R8C12 = Highlow
        value_R8C12 = IntVar()
        cb_R8C12 = Checkbutton(self, anchor='w', text='Highlow', offvalue = 0, onvalue = 2048, variable = value_R8C12)
        cb_R8C12.grid(row = 8, column = 12, sticky=W+E)
        if fl[7] & 2048:
            cb_R8C12.select()
        self.vars.append(value_R8C12) # 83
        # Checkbutton R8C13 = Histo
        value_R8C13 = IntVar()
        cb_R8C13 = Checkbutton(self, anchor='w', text='Histogram', offvalue = 0, onvalue = 4096, variable = value_R8C13)
        cb_R8C13.grid(row = 8, column = 13, sticky=W+E)
        if fl[7] & 4096:
            cb_R8C13.select()
        self.vars.append(value_R8C13) # 84
        # Checkbutton R8C14 = Hline
        value_R8C14 = IntVar()
        cb_R8C14 = Checkbutton(self, anchor='w', text='Hline', offvalue = 0, onvalue = 8192, variable = value_R8C14)
        cb_R8C14.grid(row = 8, column = 14, sticky=W+E)
        if fl[7] & 8192:
            cb_R8C14.select()
        self.vars.append(value_R8C14) # 85

        # =============================================================================================================
        # Label R9 = SGPLOT 2
        #label_R9C0 = Label(self, bg = '#80CCFF', text = 'SGPLOT 2')
        #label_R9C0.grid(row = 9, column = 0, padx = '5', pady = '5', sticky = 'ew')
        # Checkbutton R9C1 = Inset
        value_R9C1 = IntVar()
        cb_R9C1 = Checkbutton(self, anchor='w', text='Inset', offvalue = 0, onvalue = 1, variable = value_R9C1)
        cb_R9C1.grid(row = 9, column = 1, sticky=W+E)
        if fl[8] & 1:
            cb_R9C1.select()
        self.vars.append(value_R9C1) # 86
        # Checkbutton R9C2 = Loess
        value_R9C2 = IntVar()
        cb_R9C2 = Checkbutton(self, anchor='w', text='Loess', offvalue = 0, onvalue = 2, variable = value_R9C2)
        cb_R9C2.grid(row = 9, column = 2, sticky=W+E)
        if fl[8] & 2:
            cb_R9C2.select()
        self.vars.append(value_R9C2) # 87
        # Checkbutton R9C3 = Needle
        value_R9C3 = IntVar()
        cb_R9C3 = Checkbutton(self, anchor='w', text='Needle', offvalue = 0, onvalue = 4, variable = value_R9C3)
        cb_R9C3.grid(row = 9, column = 3, sticky=W+E)
        if fl[8] & 4:
            cb_R9C3.select()
        self.vars.append(value_R9C3) # 88
        # Checkbutton R9C4 = Pbspline
        value_R9C4 = IntVar()
        cb_R9C4 = Checkbutton(self, anchor='w', text='Pbspline', offvalue = 0, onvalue = 8, variable = value_R9C4)
        cb_R9C4.grid(row = 9, column = 4, sticky=W+E)
        if fl[8] & 8:
            cb_R9C4.select()
        self.vars.append(value_R9C4) # 89
        # Checkbutton R9C5 = Polygon
        value_R9C5 = IntVar()
        cb_R9C5 = Checkbutton(self, anchor='w', text='Polygon', offvalue = 0, onvalue = 16, variable = value_R9C5)
        cb_R9C5.grid(row = 9, column = 5, sticky=W+E)
        if fl[8] & 16:
            cb_R9C5.select()
        self.vars.append(value_R9C5) # 90
        # Checkbutton R9C6 = Refline
        value_R9C6 = IntVar()
        cb_R9C6 = Checkbutton(self, anchor='w', text='Refline', offvalue = 0, onvalue = 32, variable = value_R9C6)
        cb_R9C6.grid(row = 9, column = 6, sticky=W+E)
        if fl[8] & 32:
            cb_R9C6.select()
        self.vars.append(value_R9C6) # 91
        # Checkbutton R9C7 = Reg
        value_R9C7 = IntVar()
        cb_R9C7 = Checkbutton(self, anchor='w', text='Reg', offvalue = 0, onvalue = 64, variable = value_R9C7)
        cb_R9C7.grid(row = 9, column = 7, sticky=W+E)
        if fl[8] & 64:
            cb_R9C7.select()
        self.vars.append(value_R9C7) # 92
        # Checkbutton R9C8 = Scatter
        value_R9C8 = IntVar()
        cb_R9C8 = Checkbutton(self, anchor='w', text='Scatter', offvalue = 0, onvalue = 128, variable = value_R9C8)
        cb_R9C8.grid(row = 9, column = 8, sticky=W+E)
        if fl[8] & 128:
            cb_R9C8.select()
        self.vars.append(value_R9C8) # 93
        # Checkbutton R9C9 = Series
        value_R9C9 = IntVar()
        cb_R9C9 = Checkbutton(self, anchor='w', text='Series', offvalue = 0, onvalue = 256, variable = value_R9C9)
        cb_R9C9.grid(row = 9, column = 9, sticky=W+E)
        if fl[8] & 256:
            cb_R9C9.select()
        self.vars.append(value_R9C9) # 94
        # Checkbutton R9C10 = Step
        value_R9C10 = IntVar()
        cb_R9C10 = Checkbutton(self, anchor='w', text='Step', offvalue = 0, onvalue = 512, variable = value_R9C10)
        cb_R9C10.grid(row = 9, column = 10, sticky=W+E)
        if fl[8] & 512:
            cb_R9C10.select()
        self.vars.append(value_R9C10) # 95
        # Checkbutton R9C11 = Text
        value_R9C11 = IntVar()
        cb_R9C11 = Checkbutton(self, anchor='w', text='Text', offvalue = 0, onvalue = 1024, variable = value_R9C11)
        cb_R9C11.grid(row = 9, column = 11, sticky=W+E)
        if fl[8] & 1024:
            cb_R9C11.select()
        self.vars.append(value_R9C11) # 96
        # Checkbutton R9C12 = Vbar
        value_R9C12 = IntVar()
        cb_R9C12 = Checkbutton(self, anchor='w', text='Vbar', offvalue = 0, onvalue = 2048, variable = value_R9C12)
        cb_R9C12.grid(row = 9, column = 12, sticky=W+E)
        if fl[8] & 2048:
            cb_R9C12.select()
        self.vars.append(value_R9C12) # 97
        # Checkbutton R9C13 = Vbox
        value_R9C13 = IntVar()
        cb_R9C13 = Checkbutton(self, anchor='w', text='Vbox', offvalue = 0, onvalue = 4096, variable = value_R9C13)
        cb_R9C13.grid(row = 9, column = 13, sticky=W+E)
        if fl[8] & 4096:
            cb_R9C13.select()
        self.vars.append(value_R9C13) # 98
        # Checkbutton R9C14 = Vector
        value_R9C14 = IntVar()
        cb_R9C14 = Checkbutton(self, anchor='w', text='Vector', offvalue = 0, onvalue = 8192, variable = value_R9C14)
        cb_R9C14.grid(row = 9, column = 14, sticky=W+E)
        if fl[8] & 8192:
            cb_R9C14.select()
        self.vars.append(value_R9C14) # 99

        # =============================================================================================================
        # Label R10 = SGPLOT 3
        #label_R10C0 = Label(self, bg = '#80CCFF', text = 'SGPLOT 3')
        #label_R10C0.grid(row = 10, column = 0, padx = '5', pady = '5', sticky = 'ew')
        # Checkbutton R10C1 = Vline	
        value_R10C1 = IntVar()
        cb_R10C1 = Checkbutton(self, anchor='w', text='Vline', offvalue = 0, onvalue = 1, variable = value_R10C1)
        cb_R10C1.grid(row = 10, column = 1, sticky=W+E)
        if fl[9] & 1:
            cb_R10C1.select()
        self.vars.append(value_R10C1) # 100
        # Checkbutton R10C2 = Waterfall
        value_R10C2 = IntVar()
        cb_R10C2 = Checkbutton(self, anchor='w', text='Waterfall', offvalue = 0, onvalue = 2, variable = value_R10C2)
        cb_R10C2.grid(row = 10, column = 2, sticky=W+E)
        if fl[9] & 2:
            cb_R10C2.select()
        self.vars.append(value_R10C2) # 101
        # Checkbutton R10C3 = Xaxis
        value_R10C3 = IntVar()
        cb_R10C3 = Checkbutton(self, anchor='w', text='Xaxis', offvalue = 0, onvalue = 4, variable = value_R10C3)
        cb_R10C3.grid(row = 10, column = 3, sticky=W+E)
        if fl[9] & 4:
            cb_R10C3.select()
        self.vars.append(value_R10C3) # 102
        # Checkbutton R10C4 = X2axis
        value_R10C4 = IntVar()
        cb_R10C4 = Checkbutton(self, anchor='w', text='X2axis', offvalue = 0, onvalue = 8, variable = value_R10C4)
        cb_R10C4.grid(row = 10, column = 4, sticky=W+E)
        if fl[9] & 8:
            cb_R10C4.select()
        self.vars.append(value_R10C4) # 103
        # Checkbutton R10C5 = Xaxistable
        value_R10C5 = IntVar()
        cb_R10C5 = Checkbutton(self, anchor='w', text='Xaxistable', offvalue = 0, onvalue = 16, variable = value_R10C5)
        cb_R10C5.grid(row = 10, column = 5, sticky=W+E)
        if fl[9] & 16:
            cb_R10C5.select()
        self.vars.append(value_R10C5) # 104
        # Checkbutton R10C6 = Yaxis
        value_R10C6 = IntVar()
        cb_R10C6 = Checkbutton(self, anchor='w', text='Yaxis', offvalue = 0, onvalue = 32, variable = value_R10C6)
        cb_R10C6.grid(row = 10, column = 6, sticky=W+E)
        if fl[9] & 32:
            cb_R10C6.select()
        self.vars.append(value_R10C6) # 105
        # Checkbutton R10C7 = Y2axis
        value_R10C7 = IntVar()
        cb_R10C7 = Checkbutton(self, anchor='w', text='Y2axis', offvalue = 0, onvalue = 64, variable = value_R10C7)
        cb_R10C7.grid(row = 10, column = 7, sticky=W+E)
        if fl[9] & 64:
            cb_R10C7.select()
        self.vars.append(value_R10C7) # 106
        # Checkbutton R10C8 = Yaxistable
        value_R10C8 = IntVar()
        cb_R10C8 = Checkbutton(self, anchor='w', text='Yaxistable', offvalue = 0, onvalue = 128, variable = value_R10C8)
        cb_R10C8.grid(row = 10, column = 8, sticky=W+E)
        if fl[9] & 128:
            cb_R10C8.select()
        self.vars.append(value_R10C8) # 107
        # Checkbutton R10C9 = Plot 1
        value_R10C9 = IntVar()
        cb_R10C9 = Checkbutton(self, anchor='w', text='Plot 1', offvalue = 0, onvalue = 256, variable = value_R10C9)
        cb_R10C9.grid(row = 10, column = 9, sticky=W+E)
        if fl[9] & 256:
            cb_R10C9.select()
        self.vars.append(value_R10C9) # 108
        # Checkbutton R10C10 = Plot 2
        value_R10C10 = IntVar()
        cb_R10C10 = Checkbutton(self, anchor='w', text='Plot 2', offvalue = 0, onvalue = 512, variable = value_R10C10)
        cb_R10C10.grid(row = 10, column = 10, sticky=W+E)
        if fl[9] & 512:
            cb_R10C10.select()
        self.vars.append(value_R10C10) # 109
        # Checkbutton R10C11 = Plot 3
        value_R10C11 = IntVar()
        cb_R10C11 = Checkbutton(self, anchor='w', text='Plot 3', offvalue = 0, onvalue = 1024, variable = value_R10C11)
        cb_R10C11.grid(row = 10, column = 11, sticky=W+E)
        if fl[9] & 1024:
            cb_R10C11.select()
        self.vars.append(value_R10C11) # 110
        # Checkbutton R10C12 = Plot 4
        value_R10C12 = IntVar()
        cb_R10C12 = Checkbutton(self, anchor='w', text='Plot 4', offvalue = 0, onvalue = 2048, variable = value_R10C12)
        cb_R10C12.grid(row = 10, column = 12, sticky=W+E)
        if fl[9] & 2048:
            cb_R10C12.select()
        self.vars.append(value_R10C12) # 111
        # Checkbutton R10C13 = Plot 5
        value_R10C13 = IntVar()
        cb_R10C13 = Checkbutton(self, anchor='w', text='Plot 5', offvalue = 0, onvalue = 4096, variable = value_R10C13)
        cb_R10C13.grid(row = 10, column = 13, sticky=W+E)
        if fl[9] & 4096:
            cb_R10C13.select()
        self.vars.append(value_R10C13) # 112
        # Checkbutton R10C14 = Plot 6
        value_R10C14 = IntVar()
        cb_R10C14 = Checkbutton(self, anchor='w', text='Plot 6', offvalue = 0, onvalue = 8192, variable = value_R10C14)
        cb_R10C14.grid(row = 10, column = 14, sticky=W+E)
        if fl[9] & 8192:
            cb_R10C14.select()
        self.vars.append(value_R10C14) # 113


        # =============================================================================================================
        # Label R11 = Modelling
        label_R11C0 = Label(self, bg = '#80CCFF', text = 'Modelling')
        label_R11C0.grid(row = 11, column = 0, padx = '5', pady = '5', sticky = 'ew')
        # Checkbutton R11C1 = GENMOD
        value_R11C1 = IntVar()
        cb_R11C1 = Checkbutton(self, anchor='w', text='GENMOD', offvalue = 0, onvalue = 1, variable = value_R11C1)
        cb_R11C1.grid(row = 11, column = 1, sticky=W+E)
        if fl[10] & 1:
            cb_R11C1.select()
        self.vars.append(value_R11C1) # 114
        # Checkbutton R11C2 = GLIMMIX
        value_R11C2 = IntVar()
        cb_R11C2 = Checkbutton(self, anchor='w', text='GLIMMIX', offvalue = 0, onvalue = 2, variable = value_R11C2)
        cb_R11C2.grid(row = 11, column = 2, sticky=W+E)
        if fl[10] & 2:
            cb_R11C2.select()
        self.vars.append(value_R11C2) # 115
        # Checkbutton R11C3 = GLM
        value_R11C3 = IntVar()
        cb_R11C3 = Checkbutton(self, anchor='w', text='GLM', offvalue = 0, onvalue = 4, variable = value_R11C3)
        cb_R11C3.grid(row = 11, column = 3, sticky=W+E)
        if fl[10] & 4:
            cb_R11C3.select()
        self.vars.append(value_R11C3) # 116
        # Checkbutton R11C4 = LIFEREG
        value_R11C4 = IntVar()
        cb_R11C4 = Checkbutton(self, anchor='w', text='LIFEREG', offvalue = 0, onvalue = 8, variable = value_R11C4)
        cb_R11C4.grid(row = 11, column = 4, sticky=W+E)
        if fl[10] & 8:
            cb_R11C4.select()
        self.vars.append(value_R11C4) # 117
        # Checkbutton R11C5 = LOESS
        value_R11C5 = IntVar()
        cb_R11C5 = Checkbutton(self, anchor='w', text='LOESS', offvalue = 0, onvalue = 16, variable = value_R11C5)
        cb_R11C5.grid(row = 11, column = 5, sticky=W+E)
        if fl[10] & 16:
            cb_R11C5.select()
        self.vars.append(value_R11C5) # 118
        # Checkbutton R11C6 = LOGISTIC
        value_R11C6 = IntVar()
        cb_R11C6 = Checkbutton(self, anchor='w', text='LOGISTIC', offvalue = 0, onvalue = 32, variable = value_R11C6)
        cb_R11C6.grid(row = 11, column = 6, sticky=W+E)
        if fl[10] & 32:
            cb_R11C6.select()
        self.vars.append(value_R11C6) # 119
        # Checkbutton R11C7 = MIXED
        value_R11C7 = IntVar()
        cb_R11C7 = Checkbutton(self, anchor='w', text='MIXED', offvalue = 0, onvalue = 64, variable = value_R11C7)
        cb_R11C7.grid(row = 11, column = 7, sticky=W+E)
        if fl[10] & 64:
            cb_R11C7.select()
        self.vars.append(value_R11C7) # 120
        # Checkbutton R11C8 = NLIN
        value_R11C8 = IntVar()
        cb_R11C8 = Checkbutton(self, anchor='w', text='NLIN', offvalue = 0, onvalue = 128, variable = value_R11C8)
        cb_R11C8.grid(row = 11, column = 8, sticky=W+E)
        if fl[10] & 128:
            cb_R11C8.select()
        self.vars.append(value_R11C8) # 121
        # Checkbutton R11C9 = NLMIXED
        value_R11C9 = IntVar()
        cb_R11C9 = Checkbutton(self, anchor='w', text='NLMIXED', offvalue = 0, onvalue = 256, variable = value_R11C9)
        cb_R11C9.grid(row = 11, column = 9, sticky=W+E)
        if fl[10] & 256:
            cb_R11C1.select()
        self.vars.append(value_R11C1) # 122
        # Checkbutton R11C10 = PHREG
        value_R11C10 = IntVar()
        cb_R11C10 = Checkbutton(self, anchor='w', text='PHREG', offvalue = 0, onvalue = 512, variable = value_R11C10)
        cb_R11C10.grid(row = 11, column = 10, sticky=W+E)
        if fl[10] & 512:
            cb_R11C10.select()
        self.vars.append(value_R11C10) # 123
        # Checkbutton R11C11 = REG
        value_R11C11 = IntVar()
        cb_R11C11 = Checkbutton(self, anchor='w', text='REG', offvalue = 0, onvalue = 1024, variable = value_R11C11)
        cb_R11C11.grid(row = 11, column = 11, sticky=W+E)
        if fl[10] & 1024:
            cb_R11C11.select()
        self.vars.append(value_R11C11) # 124
        # Checkbutton R11C12 = SURVEYxxx
        value_R11C12 = IntVar()
        cb_R11C12 = Checkbutton(self, anchor='w', text='SURVEYxxx', offvalue = 0, onvalue = 2048, variable = value_R11C12)
        cb_R11C12.grid(row = 11, column = 12, sticky=W+E)
        if fl[10] & 2048:
            cb_R11C12.select()
        self.vars.append(value_R11C12) # 125
         # Checkbutton R11C13 = Model 1
        value_R11C13 = IntVar()
        cb_R11C13 = Checkbutton(self, anchor='w', text='Model 1', offvalue = 0, onvalue = 4096, variable = value_R11C13)
        cb_R11C13.grid(row = 11, column = 13, sticky=W+E)
        if fl[10] & 4096:
            cb_R11C13.select()
        self.vars.append(value_R11C13) # 126
        # Checkbutton R11C14 = Model 2
        value_R11C14 = IntVar()
        cb_R11C14 = Checkbutton(self, anchor='w', text='Model 2', offvalue = 0, onvalue = 8192, variable = value_R11C14)
        cb_R11C14.grid(row = 11, column = 14, sticky=W+E)
        if fl[10] & 8192:
            cb_R11C14.select()
        self.vars.append(value_R11C14) # 127

        # =============================================================================================================
        # Label R12 = Document
        label_R12C0 = Label(self, bg = '#80CCFF', text = 'Document')
        label_R12C0.grid(row = 12, column = 0, padx = '5', pady = '5', sticky = 'ew')
        # Checkbutton R12C1 = Program
        value_R12C1 = IntVar()
        cb_R12C1 = Checkbutton(self, anchor='w', text='Program', offvalue = 0, onvalue = 1, variable = value_R12C1)
        cb_R12C1.grid(row = 12, column = 1, sticky=W+E)
        if fl[11] & 1:
            cb_R12C1.select()
        self.vars.append(value_R12C1) # 128
        # Checkbutton R12C2 = Manual
        value_R12C2 = IntVar()
        cb_R12C2 = Checkbutton(self, anchor='w', text='Manual', offvalue = 0, onvalue = 2, variable = value_R12C2)
        cb_R12C2.grid(row = 12, column = 2, sticky=W+E)
        if fl[11] & 2:
            cb_R12C2.select()
        self.vars.append(value_R12C2) # 129
        # Checkbutton R12C3 = Tutorial
        value_R12C3 = IntVar()
        cb_R12C3 = Checkbutton(self, anchor='w', text='Tutorial', offvalue = 0, onvalue = 4, variable = value_R12C3)
        cb_R12C3.grid(row = 12, column = 3, sticky=W+E)
        if fl[11] & 4:
            cb_R12C3.select()
        self.vars.append(value_R12C3) # 130
        # Checkbutton R12C4 = Publication
        value_R12C4 = IntVar()
        cb_R12C4 = Checkbutton(self, anchor='w', text='Publication', offvalue = 0, onvalue = 8, variable = value_R12C4)
        cb_R12C4.grid(row = 12, column = 4, sticky=W+E)
        if fl[11] & 8:
            cb_R12C4.select()
        self.vars.append(value_R12C4) # 131
        # Checkbutton R12C5 = Web document
        value_R12C5 = IntVar()
        cb_R12C5 = Checkbutton(self, anchor='w', text='Web document', offvalue = 0, onvalue = 16, variable = value_R12C5)
        cb_R12C5.grid(row = 12, column = 5, sticky=W+E)
        if fl[11] & 16:
            cb_R12C5.select()
        self.vars.append(value_R12C5) # 132
        # Checkbutton R12C6 = Table
        value_R12C6 = IntVar()
        cb_R12C6 = Checkbutton(self, anchor='w', text='Output Table', offvalue = 0, onvalue = 32, variable = value_R12C6)
        cb_R12C6.grid(row = 12, column = 6, sticky=W+E)
        if fl[11] & 32:
            cb_R12C6.select()
        self.vars.append(value_R12C6) # 133
        # Checkbutton R12C7 = Figure
        value_R12C7 = IntVar()
        cb_R12C7 = Checkbutton(self, anchor='w', text='Output Figure', offvalue = 0, onvalue = 64, variable = value_R12C7)
        cb_R12C7.grid(row = 12, column = 7, sticky=W+E)
        if fl[11] & 64:
            cb_R12C7.select()
        self.vars.append(value_R12C7) # 134
        # Checkbutton R12C8 = Listing
        value_R12C8 = IntVar()
        cb_R12C8 = Checkbutton(self, anchor='w', text='Output Listing', offvalue = 0, onvalue = 128, variable = value_R12C8)
        cb_R12C8.grid(row = 12, column = 8, sticky=W+E)
        if fl[11] & 128:
            cb_R12C8.select()
        self.vars.append(value_R12C8) # 135
        # Checkbutton R12C9 = Document 1
        value_R12C9 = IntVar()
        cb_R12C9 = Checkbutton(self, anchor='w', text='Document 1', offvalue = 0, onvalue = 256, variable = value_R12C9)
        cb_R12C9.grid(row = 12, column = 9, sticky=W+E)
        if fl[11] & 256:
            cb_R12C1.select()
        self.vars.append(value_R12C1) # 136
        # Checkbutton R12C10 = Document 2
        value_R12C10 = IntVar()
        cb_R12C10 = Checkbutton(self, anchor='w', text='Document 2', offvalue = 0, onvalue = 512, variable = value_R12C10)
        cb_R12C10.grid(row = 12, column = 10, sticky=W+E)
        if fl[11] & 512:
            cb_R12C10.select()
        self.vars.append(value_R12C10) # 137
        # Checkbutton R12C11 = Document 3
        value_R12C11 = IntVar()
        cb_R12C11 = Checkbutton(self, anchor='w', text='Document 3', offvalue = 0, onvalue = 1024, variable = value_R12C11)
        cb_R12C11.grid(row = 12, column = 11, sticky=W+E)
        if fl[11] & 1024:
            cb_R12C11.select()
        self.vars.append(value_R12C11) # 138
        # Checkbutton R12C12 = Document 4
        value_R12C12 = IntVar()
        cb_R12C12 = Checkbutton(self, anchor='w', text='Document 4', offvalue = 0, onvalue = 2048, variable = value_R12C12)
        cb_R12C12.grid(row = 12, column = 12, sticky=W+E)
        if fl[11] & 2048:
            cb_R12C12.select()
        self.vars.append(value_R12C12) # 139
         # Checkbutton R12C13 = Document 5
        value_R12C13 = IntVar()
        cb_R12C13 = Checkbutton(self, anchor='w', text='Document 5', offvalue = 0, onvalue = 4096, variable = value_R12C13)
        cb_R12C13.grid(row = 12, column = 13, sticky=W+E)
        if fl[11] & 4096:
            cb_R12C13.select()
        self.vars.append(value_R12C13) # 140
        # Checkbutton R12C14 = Document 6
        value_R12C14 = IntVar()
        cb_R12C14 = Checkbutton(self, anchor='w', text='Document 6', offvalue = 0, onvalue = 8192, variable = value_R12C14)
        cb_R12C14.grid(row = 12, column = 14, sticky=W+E)
        if fl[11] & 8192:
            cb_R12C14.select()
        self.vars.append(value_R12C14) # 141

        # =============================================================================================================
        # Load file
        buttonLoad = Button(self, text = 'Choose', command=buttonChooseClick)
        buttonLoad.grid(row = 15, column = 1, padx = '5', pady = '5')
        # Save file
        buttonSave = Button(self, text = 'Save', command=partial(buttonSaveClick, self.vars, myfilepath, fl[20]))
        buttonSave.grid(row = 15, column = 2, padx = '5', pady = '5')
        # Search files
        buttonSearch = Button(self, text = 'Search', command=partial(buttonSearchClick, self.vars))
        buttonSearch.grid(row = 15, column = 3, padx = '5', pady = '5')
        # Close
        buttonClose = Button(self, text = 'Close', command = partial(buttonCloseClick, 0))
        buttonClose.grid(row = 15, column = 4, padx = '5', pady = '5')


        col_count, row_count = self.grid_size()

        for col in range(col_count):
            self.grid_columnconfigure(col, minsize = 100)

        for row in range(row_count):
            self.grid_rowconfigure(row, minsize = 20)

        self.pack()

def main():
    if len(sys.argv) < 2:
        # Called without parameter
        print("Parameter missing")
        sys.exit()
    myfilepath = sys.argv[1]
    print(myfilepath)
    root = Tk()
    PrgSieve(myfilepath)
    root.mainloop()


if __name__ == '__main__':
    main()