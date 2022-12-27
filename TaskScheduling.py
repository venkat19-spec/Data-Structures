class TaskNode:
    def __init__(self, start=None, finish=None):
        self.start_time = start
        self.finish_time = finish

class TaskScheduling:

    def solution(self, arr):

        #sort by order of finish time
        sorted(arr, key=lambda x: x.finish_time)

        #maintain a list for scheduled tasks
        res = list()
        #append first task
        res.append(arr[0])
        count = 1
        #if start time of next task > finish time of previous task , add it to scheduled tasks
        for i in range(1, len(arr)):
            if res[-1].finish_time <= arr[i].start_time:
                res.append(arr[i])
                count += 1

        #print the tasks
        print("Task \t Start \t Finish")
        for i in range(len(res)):
            print((i+1), '\t', res[i].start_time, '\t', res[i].finish_time)
        print("Max tasks: ", count)

if __name__ == "__main__":
    arr = list()
    arr.append(TaskNode(2, 3))
    arr.append(TaskNode(1, 5))
    arr.append(TaskNode(4, 5))
    arr.append(TaskNode(6, 7))
    arr.append(TaskNode(9, 10))

    ts = TaskScheduling()
    ts.solution(arr)