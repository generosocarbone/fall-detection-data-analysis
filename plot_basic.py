# python3 pandas_test.py
# idea:  in base a quanto e come varia il fall index possiamo stabilire se si è verificata una caduta
# Se c'è un picco che resta più o meno costante allora è possibile assumere che si sia verificata una caduta
# Se c'è un picco che non resta costante anzi tende a decrescere, allora è possibile assumere che la
# caduta non si sia verificata.
# Una cosa che ho notato è che l'accelerometro non è costantente nel fornire i valori, ma tende ad accelerare
# all'aumentare delle variazioni di accelerazione. Sembra valido per il mio samsung, non so se è un discorso
# comune a tutti i dispositivi.

# Fare un'implementazione per smartwatch in grado di fare dei run di misurazione molto lunghi e vedere come
# si comporta il Fall Index nel tempo



import pandas
import matplotlib.pyplot as plt
import math

G = 9.81
MIN_MEDIANA = G * 0.93;
MAX_MEDIANA = G * 1.05;

print('MIN_MEDIANA: {}'.format(MIN_MEDIANA))
print('MAX_MEDIANA: {}'.format(MAX_MEDIANA))

def plot_dataframe(df, title):
    global acceleration_impact_analyzed
    print('\n__dataframe: {}__'.format(title))
    x = df['x']
    x.plot.line()
    print(x.describe(percentiles = [.1, .5, .9]))

csv_name='102/movimenti_ii'
riposo = pandas.read_csv('{}.csv'.format(csv_name), sep=';')
plot_dataframe(riposo, csv_name)

plt.show()
