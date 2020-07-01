import pandas as pd
import time
from SIIConfig import info_sii

dataset = pd.read_csv('../csv/compilado_ruts_unicos.txt', sep = '\n', header = None)

data_sii = pd.DataFrame()

for r in range(dataset.shape[0]):
    try:
        rut = dataset[0][r].split('-')
        data_sii = data_sii.append(info_sii(rut[0],rut[1]), ignore_index = True)
        time.sleep(2)
    except:
        pass
    print(r)

data_sii.to_csv('../csv/compilado_reducción_jornada_info_sii.csv', encoding = 'utf-8', index = False)