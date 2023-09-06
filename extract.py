from concurrent.futures import ThreadPoolExecutor
from threading import current_thread
from pdfplumber.page import Page
from time import perf_counter
from pandas import DataFrame
from crop import *
import var


def get_cells(page: Page, rel_pos: list[int]) -> list:
    cells = [''] * len(rel_pos)

    for line in page.extract_text_lines(return_chars = False):
        index = rel_pos.index(round(line['top']))
        cells[index] = line['text']

    return cells

def get_rel_pos(page: Page) -> list:  # Passar idade pois é mais fácil
    positions = []
    lines = page.extract_text_lines(return_chars = False)

    for line in lines:
        positions.append(round(line['top']))

    return positions

def get_info(page: Page) -> DataFrame:
    start_time = perf_counter()
    cropped_data = crop_data(page)
    rp = get_rel_pos(cropped_data)

    with ThreadPoolExecutor(var.max_threads / var.main_threads) as tpx:
        cropped = tpx.map(crop_any, [page] * 11, (0, 1, 2, 3, 4, 5, 6, 8, 9, 10, 11))
        data = tpx.submit(get_cells, cropped_data, rp)
        info = list(tpx.map(get_cells, cropped, [rp] * 11))

    df = DataFrame({'Certificado': info[0],
                    'Nome do beneficiário': info[1],
                    'Data de nascimento': info[2],
                    'Sexo': info[3],
                    'Estado civil': info[4],
                    'Parentesco': info[5],
                    'Plano': info[6],
                    'Data de início': data.result(),
                    'Movimentação': info[7],
                    'Mês/Ano': info[8],
                    'Valor': info[9],
                    'Part. Seg.': info[10]})
    
    print(f'{current_thread().name}: informação da página {page.page_number:02} extraída em {perf_counter() - start_time:.2f} segundos.')
    return df
