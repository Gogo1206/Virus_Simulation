import xlwt

_wb = None
_sheet1 = None


def _init():
    """Lazy-initialize workbook so import doesn't require xlwt installed."""
    global _wb, _sheet1
    if _wb is None:
        _wb = xlwt.Workbook()
        _sheet1 = _wb.add_sheet('Data')


def write(row, column, context):
    """Write a cell and save the workbook."""
    _init()
    _sheet1.write(row, column, context)
    _wb.save('Data.xls')