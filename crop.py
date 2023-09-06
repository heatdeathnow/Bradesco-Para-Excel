from pdfplumber.page import Page

def crop_any(page: Page, index: int) -> Page:
    match index:
        case 0:
            return crop_cert(page)
        
        case 1:
            return crop_nome(page)
        
        case 2:
            return crop_nasc(page)
        
        case 3:
            return crop_sexo(page)
        
        case 4:
            return crop_civi(page)
        
        case 5:
            return crop_pare(page)
        
        case 6:
            return crop_plan(page)
        
        case 7:
            return crop_data(page)
        
        case 8:
            return crop_movi(page)
        
        case 9:
            return crop_mesa(page)
        
        case 10:
            return crop_valo(page)
        
        case 11:
            return crop_part(page)

def crop_cert(page: Page) -> Page:
    return page.within_bbox((20, 218, 61, 794))  # X0, Y0, X1, Y1. Size: (0, 0, 595, 842)

def crop_nome(page: Page) -> Page:
    return page.within_bbox((62, 218, 200, 794))

def crop_nasc(page: Page) -> Page:
    return page.within_bbox((242, 218, 282, 794))

def crop_sexo(page: Page) -> Page:
    return page.within_bbox((283, 218, 301, 794))

def crop_civi(page: Page) -> Page:
    return page.within_bbox((303, 218, 328, 794))

def crop_pare(page: Page) -> Page:
    return page.within_bbox((328, 218, 353, 794))

def crop_plan(page: Page) -> Page:
    return page.within_bbox((356, 218, 378, 794))

def crop_data(page: Page) -> Page:
    return page.within_bbox((380, 218, 420, 794))

def crop_movi(page: Page) -> Page:
    return page.within_bbox((422, 218, 440, 794))

def crop_mesa(page: Page) -> Page:
    return page.within_bbox((442, 218, 472, 794))

def crop_valo(page: Page) -> Page:
    return page.within_bbox((473, 218, 523, 794))

def crop_part(page: Page) -> Page:
    return page.within_bbox((524, 218, 575, 794))
