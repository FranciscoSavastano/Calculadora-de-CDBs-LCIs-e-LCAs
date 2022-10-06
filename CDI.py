import getopt
import math
import sys


class conta:
    # realiza verificação do valor do IR, e ajusta/ corrige para incindir com os meses dados.
    def irrecalc(self, alIR: float, mes):
        if mes <= 6:
            alIR = 22.5
        elif mes <= 12:
            alIR = 20.0
        elif mes <= 24:
            alIR = 17.5
        elif mes > 24:
            alIR = 15.0
        return alIR

    def jc(self, r: float, t: int, n: int = 1) -> float:  # realiza o calculo de juros compostos
        return (1 + r / float(n))**(n * t) - 1

    # converte anos para dias ultilizando a funcão de juros compostos
    def year2days(self, a, wd: int = 252) -> float:
        return 100 * conta.jc(conta, a, 1 / wd)

    # converte anos para meses ultilizando a funcão de juros compostos
    def year2month(self, a: float) -> float:
        return 100 * conta.jc(conta, a, 1 / 12.0)

    def txpoup(self, s: float):  # realiza calculo da taxa anual e mensal
        if s <= 8.5:
            txanu = s * 0.7
        else:
            txanu = 6.17
        txmes = conta.year2month(conta, txanu / 100)
        return txanu, txmes

    # É usada para calcular o tempo necess á rio para dobrar o principal quando sujeito uma taxa de juros dada
    def doublePrincipal(self, r: float) -> float:
        return math.log(2, 1 + r)

    def imposto(self, alIR: float, taxacdi: float, cdi: float):  # realiza calculo dos impostos
        impcdi = (100 - alIR) * (taxacdi / 100)
        imprent = impcdi * cdi
        impmes = conta.year2month(conta, imprent / 100)
        return impcdi, imprent, impmes

    # realiza calculo dos montantes aplicados e de poupança e imposto
    def montapl(self, capital: float, impostmes: float, mes, txm, rentanu: float):
        montap = capital + (impostmes / 100 * capital) * mes
        montpoup = (((txm / 100) * mes) * capital) + capital
        submont = montap - montpoup
        rentmen = conta.year2month(conta, rentanu)
        impapl = (((capital * rentmen / 100) * mes) + capital) - montap
        rendmes = ((montap - capital)*100) / capital
        return montap, montpoup, submont, impapl, rendmes

    # realiza calculos do subtração de aplicação e aplicação de poupança
    def aplcalc(self, montapl: float, montpoup: float, mes, capital, alIR: float, taxaanual, cdi):
        aplsub = (montapl - montpoup)*100 / capital
        aplpoup = taxaanual / (cdi * (1-(alIR / 100)))
        return aplsub, aplpoup

    def porcentagem(self, x):  # Converte um valor X decimal em uma porcentagem
        return x * 100


class main:
    # recebe os argumentos da linha de comando e armazena-os em variaveis
    def principal(self, capital, cdi, selic, alIR, taxacdi, mes):
        print(taxacdi)
        argumentos = 'c:a:s:i:t:m:h'
        if mes == None:
            mes = 0
        else:
            mes = int(mes)
        try:
            opts, args = getopt.getopt(sys.argv[1:], argumentos)
            for opt, arg in opts:
                if opt in '-c':
                    capital = arg

                elif opt in '-a':
                    cdi = arg

                elif opt in '-t':
                    taxacdi = arg

                elif opt in '-s':
                    selic = arg

                elif opt in '-i':
                    alIR = arg

                elif opt in '-m':
                    mes = arg

                elif opt in '-h':
                    print(
                        f'Argumentos \n-c -> capital \n-a -> CDI \n-t -> taxa cdi \n-s -> selic \n-i -> IR \n-m -> mes')

        except getopt.GetoptError as erro:  # encerra programa em caso de erro
            exit(erro)
        print(cdi, taxacdi)
        # verifica se existem argumentos para execução
        if capital == None and cdi == None and taxacdi == None and selic == None and alIR == None:
            exit('não ha argumentos para execução, ultilize a função "-h"')
        else:
            selic = float(selic)
            taxacdi = float(taxacdi)
            capital = float(capital)
            cdi = float(cdi)
            alIR = float(alIR)


        # chamada de funçoes da classe 'conta' para receber os valores para o print
        cdipct = cdi * 100

        alIR = conta.irrecalc(conta, alIR, mes)  # corrige o IR em caso de erro
        rent = taxacdi * cdi / 100
        cdimen = conta.year2month(conta, cdi)  # converte o cdi em meses
        cdidia = conta.year2days(conta, cdi)  # converte o cdi em dias
        impostcdi, impostrent, impostmes = conta.imposto(
            conta, alIR, taxacdi, cdi)
        impostmen = conta.year2month(conta, impostrent / 100)
        # transforma selic de decimal em porcentagem
        selicpct = conta.porcentagem(conta, selic)
        txy, txm = conta.txpoup(conta, selicpct)  # taxa poup
        montanteapl, montpoupanca, submontante, impostoapl, rendmes = conta.montapl(conta,
                                                                                    capital, impostmes, mes, txm, rent)
        aplsub, aplpoup = conta.aplcalc(conta,
                                        montanteapl, montpoupanca, mes, capital, alIR, txy, cdi)
        poupancadv = conta.doublePrincipal(conta, txy / 100)
        aplicadv = conta.doublePrincipal(conta, impostrent / 100)
        impostdv = conta.doublePrincipal(conta, impostmen / 100)
        poupmen = conta.doublePrincipal(conta, txm / 100)

        # conversao de decimal para porcentagem
        cdipct = conta.porcentagem(conta, cdi)
        # conversao de decimal para porcentagem
        rentpct = conta.porcentagem(conta, rent)

        print(f'\ncapital = {capital:.2f}')
        print(f'selic = {selicpct}%')
        print(
            f'CDI = {cdipct}% ao ano = {cdimen:.4f}% ao mês = {cdidia:.6f}% ao dia')
        print(f'Taxa Poup = {txy:.2f}% ao ano = {txm:.4f}% ao mês')
        print(f'\nIR = {alIR}%')
        print(f'\nRentabilidade = {taxacdi:.2f}% CDI = {rentpct:.2f}%')
        print(
            f'Com impostos = {impostcdi:.2f}%  CDI = {impostrent:.2f}%')
        print(f'\nMeses = {mes}')
        print(f'\nMontante Aplicação = {montanteapl:.2f}$')
        print(f'Montante Poupança = {montpoupanca:.2f}$')
        print(f'Apl - Poup ({mes} meses) = {submontante:.2f}$')
        print(f'Imposto = ${impostoapl:.4f}')
        print(f'Rendimento em {mes} meses = {rendmes:.4f}%')
        print(f'\nApl - Poup ({mes}) meses = {aplsub:.4f} %')
        print(f'Apl = Poup = {aplpoup:.2f}% CDI')
        print(
            f'Tempo 2 x Poupança = {poupancadv:.2f} anos = {poupmen:.2f} meses')
        print(
            f'Tempo 2 x Aplicação = {aplicadv:.2f} anos =  {impostdv:.2f} meses')
        return capital, selicpct, cdipct, cdimen, cdidia, txy, txm, alIR, taxacdi, rentpct, impostcdi, impostrent, mes, montanteapl, montpoupanca, submontante,impostoapl, rendmes, aplsub, poupancadv, poupmen,aplicadv, impostdv, aplpoup


capital = taxacdi = selic = alIR = cdi = mes = None
if __name__ == '__main__':
    main.principal(main, capital, taxacdi, selic, alIR, cdi, mes)
