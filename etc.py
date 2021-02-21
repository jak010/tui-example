import urwid

def bar_graph(self, smooth=False):
    satt = None
    if smooth:
        satt = {(1,0): 'bg 1 smooth', (2,0): 'bg 2 smooth'}
    w = urwid.BarGraph(['bg background','bg 1','bg 2'], satt=satt)
    return w

bar_graph()