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

print(pandas.__version__)

G = 9.81
ACCELERATION_IMPACT_COEFFICIENT = 2.5
ACCELERATION_FREE_FALL_COEFFICIENT = 0.3
ACCELERATION_IMPACT = ACCELERATION_IMPACT_COEFFICIENT * G
ACCELERATION_FREE_FALL = ACCELERATION_FREE_FALL_COEFFICIENT * G

MIN_SQM = 1.0

MAX_SPIKES = 2

MEDIANA_INTERVAL_SIZE = 17
LOWER_BOUND_MEDIANA = 0.93
UPPER_BOUND_MEDIANA = 1.03

MIN_MEDIANA = G * 0.93;
MAX_MEDIANA = G * 1.03;

acceleration_impact_analyzed = 0

# print('_G: {}'.format(G))
# print('_ACCELERATION_IMPACT: {} ({})'.format(ACCELERATION_IMPACT, ACCELERATION_IMPACT_COEFFICIENT))
# print('_ACCELERATION_FREE_FALL: {} ({})'.format(ACCELERATION_FREE_FALL, ACCELERATION_FREE_FALL_COEFFICIENT))
# print('_MIN_SQM: {}'.format(MIN_SQM))
# print('_MAX_SPIKES: {}'.format(MAX_SPIKES))
# print('_MEDIANA_INTERVAL_SIZE: {}'.format(MEDIANA_INTERVAL_SIZE))
# print('_LOWER_BOUND_MEDIANA: {}'.format(LOWER_BOUND_MEDIANA))
# print('_UPPER_BOUND_MEDIANA: {}'.format(UPPER_BOUND_MEDIANA))

def plot_dataframe(df, title):
    global acceleration_impact_analyzed
    print('\n__dataframe: {}__'.format(title))
    # df.plot.line()
    a = df['a']
    spike = a[a >= ACCELERATION_IMPACT]
    print('\n__over ACCELERATION_IMPACT {}: {}'.format(ACCELERATION_IMPACT, spike.size))
    print('over ACCELERATION_IMPACT:\n{}'.format(spike.index))
    print('\n__under ACCELERATION_FREE_FALL {}: {}'.format(ACCELERATION_FREE_FALL, a[a <= ACCELERATION_FREE_FALL].size))
    print('{}'.format(a[a <= ACCELERATION_FREE_FALL]))


def analyze_dataframe(df, title):
    print('\n__dataframe: {}__'.format(title))
    a = df['a']
    print('___a: {}__'.format(a.size))
    a = a[2:]

    print('___fall evaluation___')
    mediana = a.median()
    result = False

    if a.size == 12:
        print('___free fall___')
        result_mediana = mediana <= MAX_MEDIANA and mediana >= MIN_MEDIANA

        filtered = a[a >= MIN_MEDIANA]
        filtered = filtered[filtered <= MAX_MEDIANA]
        result_filtered = filtered.size >= (MEDIANA_INTERVAL_SIZE / 2)

        result = result_mediana and result_filtered

        print('__mediana\ncurrent: {}; result: {}; MAX_MEDIANA: {}; MIN_MEDIANA: {}'.format(mediana, result_mediana, MAX_MEDIANA, MIN_MEDIANA))
        print('__filter\nmin: {}; max: {}; current: {}; got: {}: result: {}'.format(MIN_MEDIANA, MAX_MEDIANA, a.size, filtered.size, result_filtered))
        print(filtered)
    else:
        std = a.std()

        print('___shock___')
        result_mediana = True
        result_std = std >= MIN_SQM
        spike = a[a > ACCELERATION_IMPACT]
        result_spikes = spike.size <= MAX_SPIKES

        filtered = a[a >= LOWER_BOUND_MEDIANA * mediana]
        filtered = filtered[filtered <= UPPER_BOUND_MEDIANA * mediana]
        result_filtered = filtered.size >= MEDIANA_INTERVAL_SIZE

        print(a.describe())
        print('__mediana: {}__'.format(mediana))
        print('__mediana__\ncurrent: {}; result: {}; MAX_MEDIANA: {}; MIN_MEDIANA: {}'.format(mediana, result_mediana, MAX_MEDIANA, MIN_MEDIANA))
        print('__dev standard__\nmin: {}; current: {}; result: {}'.format(MIN_SQM, std, result_std))
        print('__spikes__\nthreshold: {}; max: {}; current: {}; result: {}'.format(ACCELERATION_IMPACT, MAX_SPIKES, spike.size, result_spikes))
        print('__filter__\nmin: {}; max: {}; current: {}; got: {}: result: {}'.format(LOWER_BOUND_MEDIANA * mediana, UPPER_BOUND_MEDIANA * mediana, a.size, filtered.size, result_filtered))
        result = result_mediana and result_spikes and result_filtered and result_std

    if result:
        print('_Fall detected')
    else:
        print('_No fall detected')

    print(a.sort_values())
    sorted = a.sort_values()
    sorted.plot.line(title='sorted', use_index=False)


def analyze_dataframe_from_csv_name(csv_name):
    riposo = pandas.read_csv(csv_name, sep=';')
    analyze_dataframe(riposo, csv_name)


# csv_name='paragone/test-4/101/FP-test4'
csv_name='test-notturno/FP/camminata.freefall.1'
riposo = pandas.read_csv('{}.csv'.format(csv_name), sep=';')
# plot_dataframe(riposo, csv_name)
analyze_dataframe(riposo, csv_name)

csv_name='test-notturno/FP/tp1'
riposo = pandas.read_csv('{}.csv'.format(csv_name), sep=';')
# plot_dataframe(riposo, csv_name)
analyze_dataframe(riposo, csv_name)

plt.savefig('{}.png'.format('confronto'))
plt.show()
