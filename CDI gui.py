import CDI
from tkinter import *

root = Tk()


class app(): 
    def __init__(self): #inicializa a interface
        self.root = root
        self.v = DoubleVar()
        self.window()
        self.subwindow()
        self.botoes()
        root.mainloop()

    def calcula(self): #recebe os valores das caixas de textos, e os prepara para calculo
        try:
            float(entryCap.get())
            cap = float(entryCap.get())
        except:
            respostacap.config(text='Insira um numero')
            return
        try:
            float(entryTaxSel.get())
            sel = float(entryTaxSel.get())
            sel = sel / 100
        except:
            respostasel.config(text='Insira um numero')
            return
        try:
            float(entryTaxCDI.get())
            taxcdi = float(entryTaxCDI.get())
            taxcdi = taxcdi / 100
        except:
            respostacdi.config(text='Insira um numero')
            return
        try:
            float(entryRent.get())
            rent = float(entryRent.get())
            print(rent)
        except:
            respostarent.config(text='Insira um numero')
            return
        mnths = entryMonths.get()
        if mnths == '':
            mnths = 0
        alIR = float(self.v.get())
        capital, selicpct, cdipct, cdimen, cdidia, txy, txm, alIR, taxacdi, rentpct, impostcdi, impostrent, mes, montanteapl, montpoupanca, submontante, impostoapl, rendmes, aplsub, poupancadv, poupmen, aplicadv, impostdv, aplpoup = CDI.main.principal(
            CDI.main, cap, taxcdi, sel, alIR, rent, mnths)
        self.ResWin(capital, selicpct, cdipct, cdimen, cdidia, txy, txm, alIR, taxacdi, rentpct, impostcdi, impostrent, mes,
                    montanteapl, montpoupanca, submontante, impostoapl, rendmes, aplsub, poupancadv, poupmen, aplicadv, impostdv, aplpoup)

        #import CDI

    def window(self): #cria a janela principal
        self.root.title('CDI')
        self.root.configure(background='#ffffff')
        self.root.geometry("500x730")
        self.root.resizable(False, False)

    def subwindow(self): #cria as subjanelas para os widgets, e os insere
        self.frame_1 = Frame()
        self.frame_1 = Label(
            bg='#cac3ba', bd=2, highlightbackground='#000000', highlightthickness=1)
        self.frame_1.place(relx=0.03, rely=0.07, relwidth=0.9, relheight=0.9)

        self.frame_2 = Frame()
        self.frame_2 = Label(
            bg='#faebd7', bd=4, highlightbackground='#add8e6', highlightthickness=3)
        self.frame_2.place(relx=0.05, rely=0.12, relwidth=0.8, relheight=0.7)

        entrytext = Label(
            text='Capital: \n\n\nTaxa Selic: \n\n\nTaxa CDI: \n\n\nRentabilidade: \n\n\nMeses: \n\n\nAlíquota IR:', bg='#faebd7', font=('verdana', 12))
        entrytext.place(relx=0.06, rely=0.15)

        self.frame_3 = Frame()
        self.frame_3 = Label(self.root, bg='#ff6347', bd=4, highlightbackground='#add8e6', highlightthickness=3, text=(
            'CDBs, LCIs e LCAs indexadas por \n Certificados de Depósitos Interbancários'), font=('verdana', 12, 'bold'))
        self.frame_3.place(relx=0.08, rely=0.0, relwidth=0.76, relheight=0.1)

        self.textentr1 = Frame(self.root)
        self.textentr1 = Label(text='$', bg='#faebd7', font=('verdana', 12))
        self.textentr1.place(relx=0.32, rely=0.148, relwidth=0.02)

        self.textentr2 = Frame(self.root)
        self.textentr2 = Label(
            text='% ano', bg='#faebd7', font=('verdana', 12))
        self.textentr2.place(relx=0.505, rely=0.226, relwidth=0.11)

        self.textentr3 = Frame(self.root)
        self.textentr3 = Label(
            text='% ano', bg='#faebd7', font=('verdana', 12))
        self.textentr3.place(relx=0.505, rely=0.3, relwidth=0.11)

        self.textentr4 = Frame(self.root)
        self.textentr4 = Label(
            text='% CDI', bg='#faebd7', font=('verdana', 12))
        self.textentr4.place(relx=0.466, rely=0.376, relwidth=0.11)

    def botoes(self): #realiza a criação dos botões.
        global entryCap, entryTaxSel, entryTaxCDI, entryRent, entryMonths, respostacap, respostacdi, respostarent, respostasel
        entryCap = Entry(self.frame_2)
        entryCap.place(relx=0.36, rely=0.034, relwidth=0.3)
        respostacap = Label(text='', bg='#faebd7')
        respostacap.place(relx=0.36, rely=0.18)
        entryTaxSel = Entry(self.frame_2)
        entryTaxSel.place(relx=0.36, rely=0.146, relwidth=0.2)
        respostasel = Label(text='', bg='#faebd7')
        respostasel.place(relx=0.36, rely=0.256)
        entryTaxCDI = Entry(self.frame_2)
        entryTaxCDI.place(relx=0.36, rely=0.254, relwidth=0.2)
        respostacdi = Label(text='', bg='#faebd7')
        respostacdi.place(relx=0.36, rely=0.33)
        entryRent = Entry(self.frame_2)
        entryRent.place(relx=0.36, rely=0.364, relwidth=0.15)
        respostarent = Label(text='', bg='#faebd7')
        respostarent.place(relx=0.36, rely=0.407)
        entryMonths = Entry(self.frame_2)
        entryMonths.place(relx=0.36, rely=0.47, relwidth=0.1)

        Ir = [('0.0 (LCA ou LCI)', float(0.0)), ('15.0 (Acima de 721 dias)', float(15.0)), ('17.5 (de 361 até 720)',
                                                                                            float(17.5)), ('20.0 (de 181 até 360 dias)', float(20.0)), ('22.5 (até 180 dias)', float(22.5))]
        relytemp = 0.57
        for Irv, val in Ir:
            Irrad = Radiobutton(self.root, bg='#faebd7',
                                text=Irv, variable=self.v, value=val, font=('verdana', 12))
            Irrad.place(relx=0.14, rely=relytemp)
            relytemp += 0.04

        calc = Button(text='Calcular', font=(
            'verdana', 12,), command=self.calcula)
        calc.config(fg='red')
        calc.place(relx=0.37, rely=0.86)
    #cria a janela de resultado apos realizar as contas.
    def ResWin(self, capital, selicpct, cdipct, cdimen, cdidia, txy, txm, alIR, taxacdi, rentpct, impostcdi, impostrent, mes, montanteapl, montpoupanca, submontante, impostoapl, rendmes, aplsub, poupancadv, poupmen, aplicadv, impostdv, aplpoup):
        win = Toplevel()
        win.geometry('800x580')
        win.resizable(False, False)
        res_1 = Frame(win)
        res_1.place(relx=0.02, rely=0.05, relheight=0.55, relwidth=0.55)
        lab_1 = Label(res_1, bg='#d3d3d3', highlightbackground='#008000', highlightthickness=8,
                      text=f'Capital: ${capital}\n\nTaxa Selic: {selicpct}% ao ano\n\nCDI: {cdipct}% ao ano = {cdimen:.4f}% ao mês = {cdidia:.6f}% ao dia\n\nTaxa Poupança: {txy:.2f}% ao ano = {txm:.4f}% ao mês\n\n IR: {alIR}%\n\nRentabilidade: {taxacdi:.2f}% CDI = {rentpct:.2f}%\nCom impostos: {impostcdi:.2f}%  CDI = {impostrent:.2f}%\n\nMeses = {mes}', font=('verdana', 10, 'bold'))
        lab_1.place(relheight=1, relwidth=1)

        res_2 = Frame(win)
        res_2.place(relx=0.60, rely=0.05, relheight=0.45, relwidth=0.36)
        lab_2 = Label(res_2, bg='#d3d3d3', bd=4,
                      highlightbackground='#ff0000', highlightthickness=8, text=f'Montante Aplicação: {montanteapl:.2f}$\n\nMontante Poupança: {montpoupanca:.2f}$\n\nApl - Poup ({mes} meses): {submontante:.2f}$\n\nImposto: ${impostoapl:.4f}\n\nRendimento em {mes} meses: {rendmes:.4f}%', font=('verdana', 10, 'bold'))
        lab_2.place(relheight=1, relwidth=1)

        res_3 = Frame(win)
        res_3.place(relx=0.07, rely=0.68, relheight=0.25, relwidth=0.55)
        lab_3 = Label(res_3, bg='#d3d3d3', bd=4,
                      highlightbackground='#0000ff', highlightthickness=8, text=f'Apl - Poup ({mes}) meses = {aplsub:.4f} %\n\nApl = Poup = {aplpoup:.2f}% CDI\n\nTempo 2 x Poupança = {poupancadv:.2f} anos = {poupmen:.2f} meses\n\nTempo 2 x Aplicação = {aplicadv:.2f} anos =  {impostdv:.2f} meses', font=('verdana', 10, 'bold'))
        lab_3.place(relheight=1, relwidth=1)


app()
