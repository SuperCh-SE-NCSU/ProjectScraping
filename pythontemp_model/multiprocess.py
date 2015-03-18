from multiprocessing import Process
import os
import sendEmail_v0

def info(title):
    print(title)
    
    print('module name:', __name__)
    if hasattr(os, 'getppid'):  # only available on Unix
        print('parent process:', os.getppid())
    print('process id:', os.getpid())

def f(name):
    info('function f')
    print('hello', name)
    sendEmail_v0.Task=namedtuple('task','name,time,task')
    sendEmail_v0.Tasks = [Task("testtask", "21:28", sendgridEmail)]
    sendEmail_v0.run(Tasks)

if __name__ == '__main__':
    info('main line')
    p = Process(target=f, args=('bob',))
    p.start()
    p.join()
