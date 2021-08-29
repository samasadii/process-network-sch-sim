import csv
import matplotlib.pyplot as plt
import numpy as np

def writeAnswer(process, averageWaitingTime, averageResponseTime, averageTurnAroundTime,
 utilization, throughput, waitingTime, turnAroundTime, startTime, runningTime, name):
    fileName = name + '.csv'
    with open(fileName, 'w', newline='') as csvfile:
        fieldnames = ['Process', 'Waiting_Time', 'TurnAround_Time', 'Average_Waiting_Time', 'Average_Response_Time','Average_TurnAround_Time', 'CPU_Utilization', 'Throughput']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow({'Process': process[0],
                'Waiting_Time': waitingTime[0],
                'TurnAround_Time': turnAroundTime[0],
                'Average_Waiting_Time': averageWaitingTime,
                'Average_Response_Time': averageResponseTime,
                'Average_TurnAround_Time': averageTurnAroundTime,
                'CPU_Utilization': utilization,
                'Throughput': throughput})
        for i in range(1, len(waitingTime)):
            writer.writerow({'Process': process[i], 'Waiting_Time': str(waitingTime[i]), 'TurnAround_Time': str(turnAroundTime[i])})
    



        y = np.arange(len(process))  # the label locations
        height = 0.35  # the width of the bars

        fig, ax = plt.subplots()
        rects1 = ax.barh(y - height/2, waitingTime, height, label='Waiting Time')
        rects2 = ax.barh(y + height/2, turnAroundTime, height, label='Turn Around Time')

        # Add some text for labels, title and custom x-axis tick labels, etc.
        ax.set_ylabel('Process')
        ax.set_xlabel('Time')
        ax.set_title(name)
        ax.set_yticks(y)
        ax.set_yticklabels(process)
        ax.legend()

        fig.tight_layout()

        plt.show()

        ind = np.arange(len(process))    # the x locations for the groups
        height = 0.35       # the width of the bars: can also be len(x) sequence

        p1 = plt.barh(ind, startTime, height, color=(0.0, 0.0, 0.0, 0.0))
        p2 = plt.barh(ind, runningTime, height,
                left=startTime)

        plt.xlabel('time')
        plt.ylabel('process')
        plt.title(name)
        plt.yticks(ind, process)

        plt.show()

    # plt.barh(process, turnAroundTime)
    # plt.show()
