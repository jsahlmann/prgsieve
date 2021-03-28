
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
        entryFile.grid(row = 0, column = 1, columnspan = 4, padx = '5', pady = '5', sticky = 'ew')
        entryFileText.set(myfilepath)

        # Label Language
        labelLanguage = Label(self, bg = '#80CCFF', text = 'Language')
        labelLanguage.grid(row = 2, column = 0, padx = '5', pady = '5', sticky = 'ew')
        # Checkbutton Lang_SAS
        valueLang_SAS = IntVar()
        cbLang_SAS = Checkbutton(self, anchor='w', text='SAS', offvalue = 0, onvalue = 1, variable = valueLang_SAS)
        cbLang_SAS.grid(row = 2, column = 1)
        # Checkbutton Lang_R
        valueLang_R = IntVar()
        cbLang_R = Checkbutton(self, anchor='w', text='R', offvalue = 0, onvalue = 1, variable = valueLang_R)
        cbLang_R.grid(row = 2, column = 2)
        # Checkbutton Lang_Python
        valueLang_Python = IntVar()
        cbLang_Python = Checkbutton(self, anchor='w', text='Python', offvalue = 0, onvalue = 1, variable = valueLang_Python)
        cbLang_Python.grid(row = 2, column = 3)
        # Checkbutton Lang_SQL
        valueLang_SQL = IntVar()
        cbLang_SQL = Checkbutton(self, anchor='w', text='SQL', offvalue = 0, onvalue = 1, variable = valueLang_SQL)
        cbLang_SQL.grid(row = 2, column = 4)



        # Label SDTM 1
        labelSDTM = Label(self, bg = '#80CCFF', text = 'SDTM 1')
        labelSDTM.grid(row = 3, column = 0, padx = '5', pady = '5', sticky = 'ew')
        # Checkbutton SDTM_CO
        valueSDTM_CO = IntVar()
        cbSDTM_CO = Checkbutton(self, anchor='w', text='CO', offvalue = 0, onvalue = 1, variable = valueSDTM_CO)
        cbSDTM_CO.grid(row = 3, column = 1)
        # Checkbutton SDTM_DM
        valueSDTM_DM = IntVar()
        cbSDTM_DM = Checkbutton(self, anchor='w', text='DM', offvalue = 0, onvalue = 2, variable = valueSDTM_DM)
        cbSDTM_DM.grid(row = 3, column = 2)
        # Checkbutton SDTM_SE
        valueSDTM_SE = IntVar()
        cbSDTM_SE = Checkbutton(self, anchor='w', text='SE', offvalue = 0, onvalue = 4, variable = valueSDTM_SE)
        cbSDTM_SE.grid(row = 3, column = 3)
        # Checkbutton SDTM_SV
        valueSDTM_SV = IntVar()
        cbSDTM_SV = Checkbutton(self, anchor='w', text='SV', offvalue = 0, onvalue = 8, variable = valueSDTM_SV)
        cbSDTM_SV.grid(row = 3, column = 4)
        # Checkbutton SDTM_CM
        valueSDTM_CM = IntVar()
        cbSDTM_CM = Checkbutton(self, anchor='w', text='CM', offvalue = 0, onvalue = 16, variable = valueSDTM_CM)
        cbSDTM_CM.grid(row = 3, column = 5)
        # Checkbutton SDTM_EC
        valueSDTM_EC = IntVar()
        cbSDTM_EC = Checkbutton(self, anchor='w', text='EC', offvalue = 0, onvalue = 32, variable = valueSDTM_EC)
        cbSDTM_EC.grid(row = 3, column = 6)
        # Checkbutton SDTM_EX
        valueSDTM_EX = IntVar()
        cbSDTM_EX = Checkbutton(self, anchor='w', text='EX', offvalue = 0, onvalue = 64, variable = valueSDTM_EX)
        cbSDTM_EX.grid(row = 3, column = 7)
        # Checkbutton SDTM_SU
        valueSDTM_SU = IntVar()
        cbSDTM_SU = Checkbutton(self, anchor='w', text='SU', offvalue = 0, onvalue = 128, variable = valueSDTM_SU)
        cbSDTM_SU.grid(row = 3, column = 8)
        # Checkbutton SDTM_PR
        valueSDTM_PR = IntVar()
        cbSDTM_PR = Checkbutton(self, anchor='w', text='PR', offvalue = 0, onvalue = 256, variable = valueSDTM_PR)
        cbSDTM_PR.grid(row = 3, column = 9)
        # Checkbutton SDTM_AE
        valueSDTM_AE = IntVar()
        cbSDTM_AE = Checkbutton(self, anchor='w', text='AE', offvalue = 0, onvalue = 512, variable = valueSDTM_AE)
        cbSDTM_AE.grid(row = 3, column = 10)
        # Checkbutton SDTM_CE
        valueSDTM_CE = IntVar()
        cbSDTM_CE = Checkbutton(self, anchor='w', text='CE', offvalue = 0, onvalue = 1024, variable = valueSDTM_CE)
        cbSDTM_CE.grid(row = 3, column = 11)
        # Checkbutton SDTM_DS
        valueSDTM_DS = IntVar()
        cbSDTM_DS = Checkbutton(self, anchor='w', text='DS', offvalue = 0, onvalue = 2048, variable = valueSDTM_DS)
        cbSDTM_DS.grid(row = 3, column = 12)

        # DV MH HO 
        # DA DD EG IE IS LB MB MI MO MS PC PP PE QS RP RS SC SS TU TR VS 
        # FA SR
        # TA TD TE TV  TI TS
        # SUPP RELREC

        # Label SDTM 2
        labelSDTM = Label(self, bg = '#80CCFF', text = 'SDTM 2')
        labelSDTM.grid(row = 4, column = 0, padx = '5', pady = '5', sticky = 'ew')


        # Label ADS
        labelADS = Label(self, bg = '#80CCFF', text = 'ADS')
        labelADS.grid(row = 6, column = 0, padx = '5', pady = '5', sticky = 'ew')
        # Checkbutton ADS_ADSL
        valueADS_ADSL = IntVar()
        cbADS_ADSL = Checkbutton(self, anchor='w', text='ADSL', offvalue = 0, onvalue = 1, variable = valueADS_ADSL)
        cbADS_ADSL.grid(row = 6, column = 1)


        # Label Plot
        labelPlot = Label(self, bg = '#80CCFF', text = 'SGPLOT 1')
        labelPlot.grid(row = 7, column = 0, padx = '5', pady = '5', sticky = 'ew')
        # Checkbutton Plot_Band
        valuePlot_Band = IntVar()
        cbPlot_Band = Checkbutton(self, anchor='w', text='Band', offvalue = 0, onvalue = 1, variable = valuePlot_Band)
        cbPlot_Band.grid(row = 7, column = 1)
        # Checkbutton Plot_Block
        valuePlot_Block = IntVar()
        cbPlot_Block = Checkbutton(self, anchor='w', text='Block', offvalue = 0, onvalue = 2, variable = valuePlot_Block)
        cbPlot_Block.grid(row = 7, column = 2)
        # Checkbutton Plot_Bubble
        valuePlot_Bubble = IntVar()
        cbPlot_Bubble = Checkbutton(self, anchor='w', text='Bubble', offvalue = 0, onvalue = 4, variable = valuePlot_Bubble)
        cbPlot_Bubble.grid(row = 7, column = 3)
        # Checkbutton Plot_Density
        valuePlot_Density = IntVar()
        cbPlot_Density = Checkbutton(self, anchor='w', text='Density', offvalue = 0, onvalue = 8, variable = valuePlot_Density)
        cbPlot_Density.grid(row = 7, column = 4)
        # Checkbutton Plot_Dot
        valuePlot_Dot = IntVar()
        cbPlot_Dot = Checkbutton(self, anchor='w', text='Dot', offvalue = 0, onvalue = 16, variable = valuePlot_Dot)
        cbPlot_Dot.grid(row = 7, column = 5)
        # Checkbutton Plot_Dropline
        valuePlot_Dropline = IntVar()
        cbPlot_Dropline = Checkbutton(self, anchor='w', text='Dropline', offvalue = 0, onvalue = 32, variable = valuePlot_Dropline)
        cbPlot_Dropline.grid(row = 7, column = 6)
        # Checkbutton Plot_Ellipse
        valuePlot_Ellipse = IntVar()
        cbPlot_Ellipse = Checkbutton(self, anchor='w', text='Ellipse', offvalue = 0, onvalue = 64, variable = valuePlot_Ellipse)
        cbPlot_Ellipse.grid(row = 7, column = 7)
        # Checkbutton Plot_Fringe
        valuePlot_Fringe = IntVar()
        cbPlot_Fringe = Checkbutton(self, anchor='w', text='Fringe', offvalue = 0, onvalue = 128, variable = valuePlot_Fringe)
        cbPlot_Fringe.grid(row = 7, column = 8)
        # Checkbutton Plot_Hbar
        valuePlot_Hbar = IntVar()
        cbPlot_Hbar = Checkbutton(self, anchor='w', text='Hbar', offvalue = 0, onvalue = 256, variable = valuePlot_Hbar)
        cbPlot_Hbar.grid(row = 7, column = 9)
        # Checkbutton Plot_Hbox
        valuePlot_Hbox = IntVar()
        cbPlot_Hbox = Checkbutton(self, anchor='w', text='Hbox', offvalue = 0, onvalue = 512, variable = valuePlot_Hbox)
        cbPlot_Hbox.grid(row = 7, column = 10)
        # Checkbutton Plot_Heatmap
        valuePlot_Heatmap = IntVar()
        cbPlot_Heatmap = Checkbutton(self, anchor='w', text='Heatmap', offvalue = 0, onvalue = 1024, variable = valuePlot_Heatmap)
        cbPlot_Heatmap.grid(row = 7, column = 11)
        # Checkbutton Plot_Highlow
        valuePlot_Highlow = IntVar()
        cbPlot_Highlow = Checkbutton(self, anchor='w', text='Highlow', offvalue = 0, onvalue = 2048, variable = valuePlot_Highlow)
        cbPlot_Highlow.grid(row = 7, column = 12)
        # Checkbutton Plot_Histo
        valuePlot_Histo = IntVar()
        cbPlot_Histo = Checkbutton(self, anchor='w', text='Histogram', offvalue = 0, onvalue = 4096, variable = valuePlot_Histo)
        cbPlot_Histo.grid(row = 7, column = 13)
        # Checkbutton Plot_Hline
        valuePlot_Hline = IntVar()
        cbPlot_Hline = Checkbutton(self, anchor='w', text='Hline', offvalue = 0, onvalue = 8192, variable = valuePlot_Hline)
        cbPlot_Hline.grid(row = 7, column = 14)

        # Label SGPLOT 2
        labelPlot2 = Label(self, bg = '#80CCFF', text = 'SGPLOT 2')
        labelPlot2.grid(row = 8, column = 0, padx = '5', pady = '5', sticky = 'ew')
        # Checkbutton Plot_Scatter
        valuePlot_Scatter = IntVar()
        cbPlot_Scatter = Checkbutton(self, anchor='w', text='Scatter', offvalue = 0, onvalue = 1, variable = valuePlot_Scatter)
        cbPlot_Scatter.grid(row = 8, column = 1)


        # Load file
        buttonLoad = Button(self, text = 'Choose', command=buttonChooseClick)
        buttonLoad.grid(row = 20, column = 1, padx = '5', pady = '5')
        # Save file
        buttonSave = Button(self, text = 'Save', command=buttonSaveClick)
        buttonSave.grid(row = 20, column = 2, padx = '5', pady = '5')
        # Search files
        buttonSearch = Button(self, text = 'Search', command=buttonSearchClick)
        buttonSearch.grid(row = 20, column = 3, padx = '5', pady = '5')
        # Close
        buttonClose = Button(self, text = 'Close', command = partial(buttonCloseClick, 3))
        buttonClose.grid(row = 20, column = 4, padx = '5', pady = '5')


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