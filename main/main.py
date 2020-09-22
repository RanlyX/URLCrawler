# !usr/bin/python
# -*- coding:utf-8 -*-

import sys
import phider.task as task
import phider.task_manager as mtm
import argparse
from bs4 import BeautifulSoup

def main2():
    data = None
    with open('test.html', 'r') as f:
        data = f.read()
    soup = BeautifulSoup(data, 'html.parser')
    print(soup.h1.text.find('1015'))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-w", "--workers", type=int, help="number of workers")
    parser.add_argument("-d", "--default", help="Default PhishTank ID range", action="store_true")
    parser.add_argument("-s", "--start", type=int, help="start PhishTank ID")
    parser.add_argument("-e", "--end", type=int, help="end PhishTank ID")
    args = parser.parse_args()
    workers = 1
    start = 1
    end = task.Task(1).getMax()
    print(end)
    if args.workers:
        workers = args.workers
    if not args.default:
        if args.start:
            if args.end:
                if args.start>args.end:
                    print("Start must <= end")
                    sys.exit(1)
                else:
                    start = args.start 
                    end = args.end
            else:
                print("The beginning and the end must appear in pairs")
                sys.exit(1)
        else:
            if args.end:
                print("The beginning and the end must appear in pairs")
                sys.exit(1)
    else:
        if args.start or args.end:
            print("Default range cannot be set")
            sys.exit(1)
    
    m = mtm.TaskManager(workerNum=workers, start=start, end=end)
    m.doJobs()

if __name__ == '__main__':
    main()