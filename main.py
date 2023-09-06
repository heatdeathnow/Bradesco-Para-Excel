from format import clean_df, xlsx_format, add_formulaic_cols
from concurrent.futures import ThreadPoolExecutor
from argparse import ArgumentParser
from time import perf_counter
from extract import get_info
import pandas as pd
import pdfplumber
import var


if __name__ == '__main__':
    runtime = perf_counter()
    parse = ArgumentParser()
    parse.add_argument('input')
    args = parse.parse_args()

    if args.input[args.input.rfind('.'):] != '.pdf' and args.input[args.input.rfind('.'):] != '.PDF':
        raise TypeError(f'Apenas arquivos .pdf são permitidos, porém foi passado um arquivo com a extensão {args.input[args.input.rfind("."):]}')
    
    else:
        file = args.input

    output = file.replace('.pdf', '.xlsx').replace('.PDF', '.xlsx')

    with pdfplumber.open(file) as pdf:
        size = len(pdf.pages)  # Nunca vai ser menor que 3. A primeira e a última página são inúteis.
        pages = pdf.pages[1:-1]

        with ThreadPoolExecutor(thread_name_prefix = 'Thread_número', max_workers = var.main_threads) as tpx:
            dfs = tpx.map(get_info, pages)

        base = pd.concat(dfs)

        #for i, page in enumerate(pdf.pages):
         #   if i == 0 or i == size - 1: continue  # Ignore a primeira e a última página.
          #  
           # elif i == 1:  # Caso especial para a primeira página
            #    start_time = perf_counter()
             #   print(f'Lendo a {i + 1}ª página... ', end = '')
              #  base = get_info(page)
               # print(f'tempo percorrido: {perf_counter() - start_time:.2f} segundos.')

            #else:
             #   start_time = perf_counter()
              #  print(f'Lendo a {i + 1}ª página... ', end = '')
               # base = pd.concat([base, get_info(page)])
                #print(f'tempo percorrido: {perf_counter() - start_time:.2f} segundos.')
    
    clean_df(base)
    writer = pd.ExcelWriter(output, engine = 'openpyxl')
    base.to_excel(writer, 'Faturamento', index = False, startrow = 1)
    add_formulaic_cols(writer.sheets['Faturamento'])
    xlsx_format(writer.sheets['Faturamento'])
    writer.close()
    print(f'Tempo total de execução: {perf_counter() - runtime:.2f} segundos.')
