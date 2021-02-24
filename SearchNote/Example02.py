import urwid

class SelectableText(urwid.Text):
    def selectable(self):
        return True

    def keypress(self, size, key):
        return key

content = urwid.SimpleListWalker([
    urwid.AttrMap(SelectableText('foo'), '',  'reveal focus'),
    urwid.AttrMap(SelectableText('bar'), '',  'reveal focus'),
    urwid.AttrMap(SelectableText('baz'), '',  'reveal focus'),
])

listbox = urwid.ListBox(content)
wrapped = listbox

palette = [
    ('reveal focus', 'black', 'dark cyan', 'standout')
   ]

loop = urwid.MainLoop(wrapped, palette=palette)
loop.run()