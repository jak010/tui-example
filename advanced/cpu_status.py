
import psutil
from progress.bar import Bar
from pprint import pprint
from time import sleep

<<<<<<< HEAD
bar = Bar("Processing", max=100, suffix="%(index).1f%% - %(max)d%% cpu  ")

while True:
    p = psutil.cpu_percent()
    bar.index = float(p)
    bar.next()
    sleep(0.2)
bar.finish()
=======
    # Stat Check
    current_stat = int()

    bar1 = TimedProgressBar('normal', 'complete', label='Current Input',
                            label_width=100, done=10)

    footer = uw.Text('q to exit, any other key adds to progress')


    # progress = uw.Frame(uw.ListBox([bar1, uw.Divider()]), footer=footer)

    def keypress(key):
        p = psutil.Process(33362)
        memory = p.as_dict()['memory_percent']
        current_stat = memory

        # bar1.add_progress(memory)
        time.sleep(0.1)

        if key in ('q', 'Q'):
            raise uw.ExitMainLoop()

        bar1.current = memory


    # def press_test(*args):
    #     p = psutil.Process(560)
    #     memory = p.as_dict()['memory_percent']
    #     current_stat = memory
    #     bar1.add_progress(memory)
    #     time.sleep(0.1)

    # btn = uw.Button("Go", on_press=press_test)
    frame = uw.Frame(uw.Filler(uw.Pile([bar1])))

    loop = uw.MainLoop(frame, unhandled_input=keypress)
    loop.run()
>>>>>>> f4ce96cc7f2bf08d96c37a44be9fd255372a0ab9
