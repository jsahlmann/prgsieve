
"""
Program Sieve

Main class for application
Author: Jörg Sahlmann

"""


from tkinter import *
from functools import partial

def buttonCloseClick(vn):
    print(vn)
    print("Close")
    sys.exit()


def buttonChooseClick():
    print("Choose")


def buttonSaveClick():
    print("Save")


def buttonSearchClick():
    print("Search")


class PrgSieve(Frame):

    def __init__(self, mfp):
        super().__init__()
        self.initUI(mfp)
    
    def initUI(self, myfilepath):

        self.master.title("Program Sieve")

        # Label File
        labelFile = Label(self, text = 'File')
        labelFile.grid(row = 0, column = 0, padx = '5', pady = '5', sticky = 'ew')
        # Entry for path and filename
        entryFileText = StringVar()
        entryFile = Entry(self, bg = 'white', width = '8', textvariable = entryFileText)
        entryFile.grid(row = 0, column = 1, columnspan = 10, padx = '5', pady = '5', sticky = 'ew')
        entryFileText.set(myfilepath)

        # Label R2 = Language 
        label_R2C0 = Label(self, bg = '#80CCFF', text = 'Language')
        label_R2C0.grid(row = 2, column = 0, padx = '5', pady = '5', sticky = 'ew')
        # Checkbutton R2C1 = SAS
        value_R2C1 = IntVar()
        cbLang_R2C1 = Checkbutton(self, anchor='w', text='SAS', offvalue = 0, onvalue = 1, variable = value_R2C1)
        cbLang_R2C1.grid(row = 2, column = 1, sticky=W+E)
        # Checkbutton R2C2 = R
        value_R2C2 = IntVar()
        cbLang_R2C2 = Checkbutton(self, anchor='w', text='R', offvalue = 0, onvalue = 1, variable = value_R2C2)
        cbLang_R2C2.grid(row = 2, column = 2, sticky=W+E)
        # Checkbutton R2C3 = Python
        value_R2C3 = IntVar()
        cbLang_R2C3 = Checkbutton(self, anchor='w', text='Python', offvalue = 0, onvalue = 1, variable = value_R2C3)
        cbLang_R2C3.grid(row = 2, column = 3, sticky=W+E)
        # Checkbutton R2C4 = SQL
        value_R2C4 = IntVar()
        cbLang_R2C4 = Checkbutton(self, anchor='w', text='SQL', offvalue = 0, onvalue = 1, variable = value_R2C4)
        cbLang_R2C4.grid(row = 2, column = 4, sticky=W+E)

        # Label R3 = SDTM 1
        label_R3C0 = Label(self, bg = '#80CCFF', text = 'SDTM')
        label_R3C0.grid(row = 3, column = 0, padx = '5', pady = '5', sticky = 'ew')
        # Checkbutton R3C1 = SDTM_CO
        value_R3C1 = IntVar()
        cbSDTM_R3C1 = Checkbutton(self, anchor='w', text='CO', offvalue = 0, onvalue = 1, variable = value_R3C1)
        cbSDTM_R3C1.grid(row = 3, column = 1, sticky=W+E)
        # Checkbutton R3C2 = SDTM_DM
        value_R3C2 = IntVar()
        cbSDTM_R3C2 = Checkbutton(self, anchor='w', text='DM', offvalue = 0, onvalue = 2, variable = value_R3C2)
        cbSDTM_R3C2.grid(row = 3, column = 2, sticky=W+E)
        # Checkbutton R3C3 = SDTM_SE
        value_R3C3 = IntVar()
        cbSDTM_R3C3 = Checkbutton(self, anchor='w', text='SE', offvalue = 0, onvalue = 4, variable = value_R3C3)
        cbSDTM_R3C3.grid(row = 3, column = 3, sticky=W+E)
        # Checkbutton R3C4 = SDTM_SV
        value_R3C4 = IntVar()
        cbSDTM_R3C4 = Checkbutton(self, anchor='w', text='SV', offvalue = 0, onvalue = 8, variable = value_R3C4)
        cbSDTM_R3C4.grid(row = 3, column = 4, sticky=W+E)
        # Checkbutton R3C5 = SDTM_CM
        value_R3C5 = IntVar()
        cbSDTM_R3C5 = Checkbutton(self, anchor='w', text='CM', offvalue = 0, onvalue = 16, variable = value_R3C5)
        cbSDTM_R3C5.grid(row = 3, column = 5, sticky=W+E)
        # Checkbutton R3C6 = SDTM_EC
        value_R3C6 = IntVar()
        cbSDTM_R3C6 = Checkbutton(self, anchor='w', text='EC', offvalue = 0, onvalue = 32, variable = value_R3C6)
        cbSDTM_R3C6.grid(row = 3, column = 6, sticky=W+E)
        # Checkbutton R3C7 = SDTM_EX
        value_R3C7 = IntVar()
        cbSDTM_R3C7 = Checkbutton(self, anchor='w', text='EX', offvalue = 0, onvalue = 64, variable = value_R3C7)
        cbSDTM_R3C7.grid(row = 3, column = 7, sticky=W+E)
        # Checkbutton R3C8 = SDTM_SU
        value_R3C8 = IntVar()
        cbSDTM_R3C8 = Checkbutton(self, anchor='w', text='SU', offvalue = 0, onvalue = 128, variable = value_R3C8)
        cbSDTM_R3C8.grid(row = 3, column = 8, sticky=W+E)
        # Checkbutton R3C9 = SDTM_PR
        value_R3C9 = IntVar()
        cbSDTM_R3C9 = Checkbutton(self, anchor='w', text='PR', offvalue = 0, onvalue = 256, variable = value_R3C9)
        cbSDTM_R3C9.grid(row = 3, column = 9, sticky=W+E)
        # Checkbutton R3C10 = SDTM_AE
        value_R3C10 = IntVar()
        cbSDTM_R3C10 = Checkbutton(self, anchor='w', text='AE', offvalue = 0, onvalue = 512, variable = value_R3C10)
        cbSDTM_R3C10.grid(row = 3, column = 10, sticky=W+E)
        # Checkbutton R3C11 = SDTM_CE
        value_R3C11 = IntVar()
        cbSDTM_R3C11 = Checkbutton(self, anchor='w', text='CE', offvalue = 0, onvalue = 1024, variable = value_R3C11)
        cbSDTM_R3C11.grid(row = 3, column = 11, sticky=W+E)
        # Checkbutton R3C12 = SDTM_R3C12
        value_R3C12 = IntVar()
        cbSDTM_R3C12 = Checkbutton(self, anchor='w', text='DS', offvalue = 0, onvalue = 2048, variable = value_R3C12)
        cbSDTM_R3C12.grid(row = 3, column = 12, sticky=W+E)

        # Label R4 = SDTM 2
        #label_R4C0 = Label(self, bg = '#80CCFF', text = 'SDTM 2')
        #label_R4C0.grid(row = 4, column = 0, padx = '5', pady = '5', sticky = 'ew')
        # Checkbutton R4C1 = SDTM_DV
        value_R4C1 = IntVar()
        cbSDTM_R4C1 = Checkbutton(self, anchor='w', text='DV', offvalue = 0, onvalue = 1, variable = value_R4C1)
        cbSDTM_R4C1.grid(row = 4, column = 1, sticky=W+E)
        # Checkbutton R4C2 = SDTM_MH
        value_R4C2 = IntVar()
        cbSDTM_R4C2 = Checkbutton(self, anchor='w', text='MH', offvalue = 0, onvalue = 2, variable = value_R4C2)
        cbSDTM_R4C2.grid(row = 4, column = 2, sticky=W+E)
        # Checkbutton R4C3 = SDTM_HO
        value_R4C3 = IntVar()
        cbSDTM_R4C3 = Checkbutton(self, anchor='w', text='HO', offvalue = 0, onvalue = 4, variable = value_R4C3)
        cbSDTM_R4C3.grid(row = 4, column = 3, sticky=W+E)
        # Checkbutton R4C4 = SDTM_DA
        value_R4C4 = IntVar()
        cbSDTM_R4C4 = Checkbutton(self, anchor='w', text='DA', offvalue = 0, onvalue = 8, variable = value_R4C4)
        cbSDTM_R4C4.grid(row = 4, column = 4, sticky=W+E)
        # Checkbutton R4C5 = SDTM_DD
        value_R4C5 = IntVar()
        cbSDTM_R4C5 = Checkbutton(self, anchor='w', text='DD', offvalue = 0, onvalue = 16, variable = value_R4C5)
        cbSDTM_R4C5.grid(row = 4, column = 5, sticky=W+E)
        # Checkbutton R4C6 = SDTM_EG
        value_R4C6 = IntVar()
        cbSDTM_R4C6 = Checkbutton(self, anchor='w', text='EG', offvalue = 0, onvalue = 32, variable = value_R4C6)
        cbSDTM_R4C6.grid(row = 4, column = 6, sticky=W+E)
        # Checkbutton R4C7 = SDTM_IE
        value_R4C7 = IntVar()
        cbSDTM_R4C7 = Checkbutton(self, anchor='w', text='IE', offvalue = 0, onvalue = 64, variable = value_R4C7)
        cbSDTM_R4C7.grid(row = 4, column = 7, sticky=W+E)
        # Checkbutton R4C8 = SDTM_IS
        value_R4C8 = IntVar()
        cbSDTM_R4C8 = Checkbutton(self, anchor='w', text='IS', offvalue = 0, onvalue = 128, variable = value_R4C8)
        cbSDTM_R4C8.grid(row = 4, column = 8, sticky=W+E)
        # Checkbutton R4C9 = SDTM_LB
        value_R4C9 = IntVar()
        cbSDTM_R4C9 = Checkbutton(self, anchor='w', text='LB', offvalue = 0, onvalue = 256, variable = value_R4C9)
        cbSDTM_R4C9.grid(row = 4, column = 9, sticky=W+E)
        # Checkbutton R4C10 = SDTM_MB
        value_R4C10 = IntVar()
        cbSDTM_R4C10 = Checkbutton(self, anchor='w', text='MB', offvalue = 0, onvalue = 512, variable = value_R4C10)
        cbSDTM_R4C10.grid(row = 4, column = 10, sticky=W+E)
        # Checkbutton R4C11 = SDTM_MI
        value_R4C11 = IntVar()
        cbSDTM_R4C11 = Checkbutton(self, anchor='w', text='MI', offvalue = 0, onvalue = 1024, variable = value_R4C11)
        cbSDTM_R4C11.grid(row = 4, column = 11, sticky=W+E)
        # Checkbutton R4C12 = SDTM_MO
        value_R4C12 = IntVar()
        cbSDTM_R4C12 = Checkbutton(self, anchor='w', text='MO', offvalue = 0, onvalue = 2048, variable = value_R4C12)
        cbSDTM_R4C12.grid(row = 4, column = 12, sticky=W+E)

        # Label R5 = SDTM 3
        #label_R5C0 = Label(self, bg = '#80CCFF', text = 'SDTM 3')
        #label_R5C0.grid(row = 5, column = 0, padx = '5', pady = '5', sticky = 'ew')
        # Checkbutton R5C1 = SDTM_MS
        value_R5C1 = IntVar()
        cbSDTM_R5C1 = Checkbutton(self, anchor='w', text='MS', offvalue = 0, onvalue = 1, variable = value_R5C1)
        cbSDTM_R5C1.grid(row = 5, column = 1, sticky=W+E)
        # Checkbutton R5C2 = SDTM_PC
        value_R5C2 = IntVar()
        cbSDTM_R5C2 = Checkbutton(self, anchor='w', text='PC', offvalue = 0, onvalue = 2, variable = value_R5C2)
        cbSDTM_R5C2.grid(row = 5, column = 2, sticky=W+E)
        # Checkbutton R5C3 = SDTM_PP
        value_R5C3 = IntVar()
        cbSDTM_R5C3 = Checkbutton(self, anchor='w', text='PP', offvalue = 0, onvalue = 4, variable = value_R5C3)
        cbSDTM_R5C3.grid(row = 5, column = 3, sticky=W+E)
        # Checkbutton R5C4 = SDTM_PE
        value_R5C4 = IntVar()
        cbSDTM_R5C4 = Checkbutton(self, anchor='w', text='PE', offvalue = 0, onvalue = 8, variable = value_R5C4)
        cbSDTM_R5C4.grid(row = 5, column = 4, sticky=W+E)
        # Checkbutton R5C5 = SDTM_QS
        value_R5C5 = IntVar()
        cbSDTM_R5C5 = Checkbutton(self, anchor='w', text='QS', offvalue = 0, onvalue = 16, variable = value_R5C5)
        cbSDTM_R5C5.grid(row = 5, column = 5, sticky=W+E)
        # Checkbutton R5C6 = SDTM_RP
        value_R5C6 = IntVar()
        cbSDTM_R5C6 = Checkbutton(self, anchor='w', text='RP', offvalue = 0, onvalue = 32, variable = value_R5C6)
        cbSDTM_R5C6.grid(row = 5, column = 6, sticky=W+E)
        # Checkbutton R5C7 = SDTM_RS
        value_R5C7 = IntVar()
        cbSDTM_R5C7 = Checkbutton(self, anchor='w', text='RS', offvalue = 0, onvalue = 64, variable = value_R5C7)
        cbSDTM_R5C7.grid(row = 5, column = 7, sticky=W+E)
        # Checkbutton R5C8 = SDTM_SC
        value_R5C8 = IntVar()
        cbSDTM_R5C8 = Checkbutton(self, anchor='w', text='SC', offvalue = 0, onvalue = 128, variable = value_R5C8)
        cbSDTM_R5C8.grid(row = 5, column = 8, sticky=W+E)
        # Checkbutton R5C9 = SDTM_SS
        value_R5C9 = IntVar()
        cbSDTM_R5C9 = Checkbutton(self, anchor='w', text='SS', offvalue = 0, onvalue = 256, variable = value_R5C9)
        cbSDTM_R5C9.grid(row = 5, column = 9, sticky=W+E)
        # Checkbutton R5C10 = SDTM_TU
        value_R5C10 = IntVar()
        cbSDTM_R5C10 = Checkbutton(self, anchor='w', text='TU', offvalue = 0, onvalue = 512, variable = value_R5C10)
        cbSDTM_R5C10.grid(row = 5, column = 10, sticky=W+E)
        # Checkbutton R5C11 = SDTM_TR
        value_R5C11 = IntVar()
        cbSDTM_R5C11 = Checkbutton(self, anchor='w', text='TR', offvalue = 0, onvalue = 1024, variable = value_R5C11)
        cbSDTM_R5C11.grid(row = 5, column = 11, sticky=W+E)
        # Checkbutton R5C12 = SDTM_VS
        value_R5C12 = IntVar()
        cbSDTM_R5C12 = Checkbutton(self, anchor='w', text='VS', offvalue = 0, onvalue = 2048, variable = value_R5C12)
        cbSDTM_R5C12.grid(row = 5, column = 12, sticky=W+E)





        # Label R6 = Document
        label_R6C0 = Label(self, bg = '#80CCFF', text = 'Document')
        label_R6C0.grid(row = 6, column = 0, padx = '5', pady = '5', sticky = 'ew')
        # Checkbutton R6C1 = ADSL
        value_R6C1 = IntVar()
        cbSDTM_R6C1 = Checkbutton(self, anchor='w', text='ADSL', offvalue = 0, onvalue = 1, variable = value_R6C1)
        cbSDTM_R6C1.grid(row = 6, column = 1, sticky=W+E)
        # Checkbutton R6C2 = ADEX
        value_R6C2 = IntVar()
        cbSDTM_R6C2 = Checkbutton(self, anchor='w', text='ADEX', offvalue = 0, onvalue = 2, variable = value_R6C2)
        cbSDTM_R6C2.grid(row = 6, column = 2, sticky=W+E)
        # Checkbutton R6C3 = ADLB
        value_R6C3 = IntVar()
        cbSDTM_R6C3 = Checkbutton(self, anchor='w', text='ADLB', offvalue = 0, onvalue = 4, variable = value_R6C3)
        cbSDTM_R6C3.grid(row = 6, column = 3, sticky=W+E)
        # Checkbutton R6C4 = ADQS
        value_R6C4 = IntVar()
        cbSDTM_R6C4 = Checkbutton(self, anchor='w', text='ADQS', offvalue = 0, onvalue = 8, variable = value_R6C4)
        cbSDTM_R6C4.grid(row = 6, column = 4, sticky=W+E)
        # Checkbutton R6C5 = ADTTE
        value_R6C5 = IntVar()
        cbSDTM_R6C5 = Checkbutton(self, anchor='w', text='ADTTE', offvalue = 0, onvalue = 16, variable = value_R6C5)
        cbSDTM_R6C5.grid(row = 6, column = 5, sticky=W+E)

        # Label R16 = SGPLOT 1
        label_R16C0 = Label(self, bg = '#80CCFF', text = 'SGPLOT')
        label_R16C0.grid(row = 16, column = 0, padx = '5', pady = '5', sticky = 'ew')
        # Checkbutton R16C1 = Band
        value_R16C1 = IntVar()
        cb_R16C1 = Checkbutton(self, anchor='w', text='Band', offvalue = 0, onvalue = 1, variable = value_R16C1)
        cb_R16C1.grid(row = 16, column = 1, sticky=W+E)
        # Checkbutton R16C2 = Block
        value_R16C2 = IntVar()
        cb_R16C2 = Checkbutton(self, anchor='w', text='Block', offvalue = 0, onvalue = 2, variable = value_R16C2)
        cb_R16C2.grid(row = 16, column = 2, sticky=W+E)
        # Checkbutton R16C3 = Bubble
        value_R16C3 = IntVar()
        cb_R16C3 = Checkbutton(self, anchor='w', text='Bubble', offvalue = 0, onvalue = 4, variable = value_R16C3)
        cb_R16C3.grid(row = 16, column = 3, sticky=W+E)
        # Checkbutton R16C4 = Density
        value_R16C4 = IntVar()
        cb_R16C4 = Checkbutton(self, anchor='w', text='Density', offvalue = 0, onvalue = 8, variable = value_R16C4)
        cb_R16C4.grid(row = 16, column = 4, sticky=W+E)
        # Checkbutton R16C5 = Dot
        value_R16C5 = IntVar()
        cb_R16C5 = Checkbutton(self, anchor='w', text='Dot', offvalue = 0, onvalue = 16, variable = value_R16C5)
        cb_R16C5.grid(row = 16, column = 5, sticky=W+E)
        # Checkbutton R16C6 = Dropline
        value_R16C6 = IntVar()
        cb_R16C6 = Checkbutton(self, anchor='w', text='Dropline', offvalue = 0, onvalue = 32, variable = value_R16C6)
        cb_R16C6.grid(row = 16, column = 6, sticky=W+E)
        # Checkbutton R16C7 = Ellipse
        value_R16C7 = IntVar()
        cb_R16C7 = Checkbutton(self, anchor='w', text='Ellipse', offvalue = 0, onvalue = 64, variable = value_R16C7)
        cb_R16C7.grid(row = 16, column = 7, sticky=W+E)
        # Checkbutton R16C8 = Fringe
        value_R16C8 = IntVar()
        cb_R16C8 = Checkbutton(self, anchor='w', text='Fringe', offvalue = 0, onvalue = 128, variable = value_R16C8)
        cb_R16C8.grid(row = 16, column = 8, sticky=W+E)
        # Checkbutton R16C9 = Hbar
        value_R16C9 = IntVar()
        cb_R16C9 = Checkbutton(self, anchor='w', text='Hbar', offvalue = 0, onvalue = 256, variable = value_R16C9)
        cb_R16C9.grid(row = 16, column = 9, sticky=W+E)
        # Checkbutton R16C10 = Hbox
        value_R16C10 = IntVar()
        cb_R16C10 = Checkbutton(self, anchor='w', text='Hbox', offvalue = 0, onvalue = 512, variable = value_R16C10)
        cb_R16C10.grid(row = 16, column = 10, sticky=W+E)
        # Checkbutton R16C11 = Heatmap
        value_R16C11 = IntVar()
        cb_R16C11 = Checkbutton(self, anchor='w', text='Heatmap', offvalue = 0, onvalue = 1024, variable = value_R16C11)
        cb_R16C11.grid(row = 16, column = 11, sticky=W+E)
        # Checkbutton R16C12 = Highlow
        value_R16C12 = IntVar()
        cb_R16C12 = Checkbutton(self, anchor='w', text='Highlow', offvalue = 0, onvalue = 2048, variable = value_R16C12)
        cb_R16C12.grid(row = 16, column = 12, sticky=W+E)
        # Checkbutton R16C13 = Histo
        value_R16C13 = IntVar()
        cb_R16C13 = Checkbutton(self, anchor='w', text='Histogram', offvalue = 0, onvalue = 4096, variable = value_R16C13)
        cb_R16C13.grid(row = 16, column = 13, sticky=W+E)
        # Checkbutton R16C14 = Hline
        value_R16C14 = IntVar()
        cb_R16C14 = Checkbutton(self, anchor='w', text='Hline', offvalue = 0, onvalue = 8192, variable = value_R16C14)
        cb_R16C14.grid(row = 16, column = 14, sticky=W+E)

        # Label R17 = SGPLOT 2
        #label_R17C0 = Label(self, bg = '#80CCFF', text = 'SGPLOT 2')
        #label_R17C0.grid(row = 17, column = 0, padx = '5', pady = '5', sticky = 'ew')
        # Checkbutton R17C1 = Inset
        value_R17C1 = IntVar()
        cb_R17C1 = Checkbutton(self, anchor='w', text='Inset', offvalue = 0, onvalue = 1, variable = value_R17C1)
        cb_R17C1.grid(row = 17, column = 1, sticky=W+E)
        # Checkbutton R17C2 = Loess
        value_R17C2 = IntVar()
        cb_R17C2 = Checkbutton(self, anchor='w', text='Loess', offvalue = 0, onvalue = 2, variable = value_R17C2)
        cb_R17C2.grid(row = 17, column = 2, sticky=W+E)
        # Checkbutton R17C3 = Needle
        value_R17C3 = IntVar()
        cb_R17C3 = Checkbutton(self, anchor='w', text='Needle', offvalue = 0, onvalue = 4, variable = value_R17C3)
        cb_R17C3.grid(row = 17, column = 3, sticky=W+E)
        # Checkbutton R17C4 = Pbspline
        value_R17C4 = IntVar()
        cb_R17C4 = Checkbutton(self, anchor='w', text='Pbspline', offvalue = 0, onvalue = 8, variable = value_R17C4)
        cb_R17C4.grid(row = 17, column = 4, sticky=W+E)
        # Checkbutton R17C5 = Polygon
        value_R17C5 = IntVar()
        cb_R17C5 = Checkbutton(self, anchor='w', text='Polygon', offvalue = 0, onvalue = 16, variable = value_R17C5)
        cb_R17C5.grid(row = 17, column = 5, sticky=W+E)
        # Checkbutton R17C6 = Refline
        value_R17C6 = IntVar()
        cb_R17C6 = Checkbutton(self, anchor='w', text='Refline', offvalue = 0, onvalue = 32, variable = value_R17C6)
        cb_R17C6.grid(row = 17, column = 6, sticky=W+E)
        # Checkbutton R17C7 = Reg
        value_R17C7 = IntVar()
        cb_R17C7 = Checkbutton(self, anchor='w', text='Reg', offvalue = 0, onvalue = 64, variable = value_R17C7)
        cb_R17C7.grid(row = 17, column = 7, sticky=W+E)
        # Checkbutton R17C8 = Scatter
        value_R17C8 = IntVar()
        cb_R17C8 = Checkbutton(self, anchor='w', text='Scatter', offvalue = 0, onvalue = 128, variable = value_R17C8)
        cb_R17C8.grid(row = 17, column = 8, sticky=W+E)
        # Checkbutton R17C9 = Series
        value_R17C9 = IntVar()
        cb_R17C9 = Checkbutton(self, anchor='w', text='Series', offvalue = 0, onvalue = 256, variable = value_R17C9)
        cb_R17C9.grid(row = 17, column = 9, sticky=W+E)
        # Checkbutton R17C10 = Step
        value_R17C10 = IntVar()
        cb_R17C10 = Checkbutton(self, anchor='w', text='Step', offvalue = 0, onvalue = 512, variable = value_R17C10)
        cb_R17C10.grid(row = 17, column = 10, sticky=W+E)
        # Checkbutton R17C11 = Text
        value_R17C11 = IntVar()
        cb_R17C11 = Checkbutton(self, anchor='w', text='Text', offvalue = 0, onvalue = 1024, variable = value_R17C11)
        cb_R17C11.grid(row = 17, column = 11, sticky=W+E)
        # Checkbutton R17C12 = Vbar
        value_R17C12 = IntVar()
        cb_R17C12 = Checkbutton(self, anchor='w', text='Vbar', offvalue = 0, onvalue = 2048, variable = value_R17C12)
        cb_R17C12.grid(row = 17, column = 12, sticky=W+E)
        # Checkbutton R17C13 = Vbox
        value_R17C13 = IntVar()
        cb_R17C13 = Checkbutton(self, anchor='w', text='Vbox', offvalue = 0, onvalue = 4096, variable = value_R17C13)
        cb_R17C13.grid(row = 17, column = 13, sticky=W+E)
        # Checkbutton R17C14 = Vector
        value_R17C14 = IntVar()
        cb_R17C14 = Checkbutton(self, anchor='w', text='Vector', offvalue = 0, onvalue = 8192, variable = value_R17C14)
        cb_R17C14.grid(row = 17, column = 14, sticky=W+E)

        # Label R18 = SGPLOT 3
        #label_R18C0 = Label(self, bg = '#80CCFF', text = 'SGPLOT 3')
        #label_R18C0.grid(row = 18, column = 0, padx = '5', pady = '5', sticky = 'ew')
        # Checkbutton R18C1 = Vline	
        value_R18C1 = IntVar()
        cb_R18C1 = Checkbutton(self, anchor='w', text='Vline', offvalue = 0, onvalue = 1, variable = value_R18C1)
        cb_R18C1.grid(row = 18, column = 1, sticky=W+E)
        # Checkbutton R18C2 = Waterfall
        value_R18C2 = IntVar()
        cb_R18C2 = Checkbutton(self, anchor='w', text='Waterfall', offvalue = 0, onvalue = 2, variable = value_R18C2)
        cb_R18C2.grid(row = 18, column = 2, sticky=W+E)
        # Checkbutton R18C3 = Xaxis
        value_R18C3 = IntVar()
        cb_R18C3 = Checkbutton(self, anchor='w', text='Xaxis', offvalue = 0, onvalue = 4, variable = value_R18C3)
        cb_R18C3.grid(row = 18, column = 3, sticky=W+E)
        # Checkbutton R18C4 = X2axis
        value_R18C4 = IntVar()
        cb_R18C4 = Checkbutton(self, anchor='w', text='X2axis', offvalue = 0, onvalue = 8, variable = value_R18C4)
        cb_R18C4.grid(row = 18, column = 4, sticky=W+E)
        # Checkbutton R18C5 = Xaxistable
        value_R18C5 = IntVar()
        cb_R18C5 = Checkbutton(self, anchor='w', text='Xaxistable', offvalue = 0, onvalue = 16, variable = value_R18C5)
        cb_R18C5.grid(row = 18, column = 5, sticky=W+E)
        # Checkbutton R18C6 = Yaxis
        value_R18C6 = IntVar()
        cb_R18C6 = Checkbutton(self, anchor='w', text='Yaxis', offvalue = 0, onvalue = 32, variable = value_R18C6)
        cb_R18C6.grid(row = 18, column = 6, sticky=W+E)
        # Checkbutton R18C7 = Y2axis
        value_R18C7 = IntVar()
        cb_R18C7 = Checkbutton(self, anchor='w', text='Y2axis', offvalue = 0, onvalue = 64, variable = value_R18C7)
        cb_R18C7.grid(row = 18, column = 7, sticky=W+E)
        # Checkbutton R18C8 = Yaxistable
        value_R18C8 = IntVar()
        cb_R18C8 = Checkbutton(self, anchor='w', text='Yaxistable', offvalue = 0, onvalue = 128, variable = value_R18C8)
        cb_R18C8.grid(row = 18, column = 8, sticky=W+E)


        # Label R19 = Modelling
        label_R19C0 = Label(self, bg = '#80CCFF', text = 'Modelling')
        label_R19C0.grid(row = 19, column = 0, padx = '5', pady = '5', sticky = 'ew')
        # Checkbutton R19C1 = GENMOD
        value_R19C1 = IntVar()
        cbSDTM_R19C1 = Checkbutton(self, anchor='w', text='GENMOD', offvalue = 0, onvalue = 1, variable = value_R19C1)
        cbSDTM_R19C1.grid(row = 19, column = 1, sticky=W+E)
        # Checkbutton R19C2 = GLIMMIX
        value_R19C2 = IntVar()
        cbSDTM_R19C2 = Checkbutton(self, anchor='w', text='GLIMMIX', offvalue = 0, onvalue = 2, variable = value_R19C2)
        cbSDTM_R19C2.grid(row = 19, column = 2, sticky=W+E)
        # Checkbutton R19C3 = GLM
        value_R19C3 = IntVar()
        cbSDTM_R19C3 = Checkbutton(self, anchor='w', text='GLM', offvalue = 0, onvalue = 4, variable = value_R19C3)
        cbSDTM_R19C3.grid(row = 19, column = 3, sticky=W+E)
        # Checkbutton R19C4 = LIFEREG
        value_R19C4 = IntVar()
        cbSDTM_R19C4 = Checkbutton(self, anchor='w', text='LIFEREG', offvalue = 0, onvalue = 8, variable = value_R19C4)
        cbSDTM_R19C4.grid(row = 19, column = 4, sticky=W+E)
        # Checkbutton R19C5 = LOESS
        value_R19C5 = IntVar()
        cbSDTM_R19C5 = Checkbutton(self, anchor='w', text='LOESS', offvalue = 0, onvalue = 16, variable = value_R19C5)
        cbSDTM_R19C5.grid(row = 19, column = 5, sticky=W+E)
        # Checkbutton R19C6 = LOGISTIC
        value_R19C6 = IntVar()
        cbSDTM_R19C6 = Checkbutton(self, anchor='w', text='LOGISTIC', offvalue = 0, onvalue = 32, variable = value_R19C6)
        cbSDTM_R19C6.grid(row = 19, column = 6, sticky=W+E)
        # Checkbutton R19C7 = MIXED
        value_R19C7 = IntVar()
        cbSDTM_R19C7 = Checkbutton(self, anchor='w', text='MIXED', offvalue = 0, onvalue = 64, variable = value_R19C7)
        cbSDTM_R19C7.grid(row = 19, column = 7, sticky=W+E)
        # Checkbutton R19C8 = NLIN
        value_R19C8 = IntVar()
        cbSDTM_R19C8 = Checkbutton(self, anchor='w', text='NLIN', offvalue = 0, onvalue = 128, variable = value_R19C8)
        cbSDTM_R19C8.grid(row = 19, column = 8, sticky=W+E)
        # Checkbutton R19C9 = NLMIXED
        value_R19C9 = IntVar()
        cbSDTM_R19C9 = Checkbutton(self, anchor='w', text='NLMIXED', offvalue = 0, onvalue = 256, variable = value_R19C9)
        cbSDTM_R19C9.grid(row = 19, column = 9, sticky=W+E)
        # Checkbutton R19C10 = PHREG
        value_R19C10 = IntVar()
        cbSDTM_R19C10 = Checkbutton(self, anchor='w', text='PHREG', offvalue = 0, onvalue = 512, variable = value_R19C10)
        cbSDTM_R19C10.grid(row = 19, column = 10, sticky=W+E)
        # Checkbutton R19C11 = REG
        value_R19C11 = IntVar()
        cbSDTM_R19C11 = Checkbutton(self, anchor='w', text='REG', offvalue = 0, onvalue = 1024, variable = value_R19C11)
        cbSDTM_R19C11.grid(row = 19, column = 11, sticky=W+E)
        # Checkbutton R19C12 = SURVEYxxx
        value_R19C12 = IntVar()
        cbSDTM_R19C12 = Checkbutton(self, anchor='w', text='SURVEYxxx', offvalue = 0, onvalue = 2048, variable = value_R19C12)
        cbSDTM_R19C12.grid(row = 19, column = 12, sticky=W+E)

        # Label R20 = Document
        label_R20C0 = Label(self, bg = '#80CCFF', text = 'Document')
        label_R20C0.grid(row = 20, column = 0, padx = '5', pady = '5', sticky = 'ew')
        # Checkbutton R20C1 = Program
        value_R20C1 = IntVar()
        cbSDTM_R20C1 = Checkbutton(self, anchor='w', text='Program', offvalue = 0, onvalue = 1, variable = value_R20C1)
        cbSDTM_R20C1.grid(row = 20, column = 1, sticky=W+E)
        # Checkbutton R20C2 = Manual
        value_R20C2 = IntVar()
        cbSDTM_R20C2 = Checkbutton(self, anchor='w', text='Manual', offvalue = 0, onvalue = 2, variable = value_R20C2)
        cbSDTM_R20C2.grid(row = 20, column = 2, sticky=W+E)
        # Checkbutton R20C3 = Tutorial
        value_R20C3 = IntVar()
        cbSDTM_R20C3 = Checkbutton(self, anchor='w', text='Tutorial', offvalue = 0, onvalue = 4, variable = value_R20C3)
        cbSDTM_R20C3.grid(row = 20, column = 3, sticky=W+E)
        # Checkbutton R20C4 = Publication
        value_R20C4 = IntVar()
        cbSDTM_R20C4 = Checkbutton(self, anchor='w', text='Publication', offvalue = 0, onvalue = 8, variable = value_R20C4)
        cbSDTM_R20C4.grid(row = 20, column = 4, sticky=W+E)
        # Checkbutton R20C5 = Web document
        value_R20C5 = IntVar()
        cbSDTM_R20C5 = Checkbutton(self, anchor='w', text='Web document', offvalue = 0, onvalue = 16, variable = value_R20C5)
        cbSDTM_R20C5.grid(row = 20, column = 5, sticky=W+E)
        

        # Load file
        buttonLoad = Button(self, text = 'Choose', command=buttonChooseClick)
        buttonLoad.grid(row = 22, column = 1, padx = '5', pady = '5')
        # Save file
        buttonSave = Button(self, text = 'Save', command=buttonSaveClick)
        buttonSave.grid(row = 22, column = 2, padx = '5', pady = '5')
        # Search files
        buttonSearch = Button(self, text = 'Search', command=buttonSearchClick)
        buttonSearch.grid(row = 22, column = 3, padx = '5', pady = '5')
        # Close
        buttonClose = Button(self, text = 'Close', command = partial(buttonCloseClick, 3))
        buttonClose.grid(row = 22, column = 4, padx = '5', pady = '5')


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