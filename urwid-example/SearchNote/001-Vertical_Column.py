#  세로로 화면 그리기
import urwid

text1 = urwid.Text("text1", 'center')
text2 = urwid.Text("text2", 'center')
text3 = urwid.Text("text3", 'center')

childs = urwid.Columns([('fixed', 20, text1), ('fixed', 10, text2), ('fixed', 10, text3)], )

menuList = urwid.SimpleListWalker([childs])

lb = urwid.ListBox(menuList)

main_loop = urwid.MainLoop(lb)
main_loop.run()
