import time
import urwid

progbar = urwid.ProgressBar('a','b',satt=u' ▏▎▍▌▋▊▉')
progbar.render((100,),focus=True)

def pbar(*args):
    global progbar
    global loop
    for i in range(1, 100):
        progbar.set_completion(i)

        # progbar.render((10,))
        loop.draw_screen()
        time.sleep(0.1)


btn = urwid.Button('Go', on_press=pbar)
frame = urwid.Frame(urwid.Filler(urwid.Pile([progbar, btn])))
loop = urwid.MainLoop(frame)

if __name__ == '__main__':
    loop.run()
