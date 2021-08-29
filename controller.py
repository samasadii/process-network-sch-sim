import rr
import fcfs
import sjf
import csv
import threading
import matplotlib.pyplot as plt

processes = []
arrivalTime = []
burstTime = []

quantum = 5

with open('data.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        processes.append(int(row['Process']))
        arrivalTime.append(int(row['Arrival']))
        burstTime.append(int(row['Burst']))
        if (row['Quantum'] != ''):
            quantum = int(row['Quantum'])

# threading.Thread(target=rr.roundRobin, args=(processes, arrivalTime, burstTime, quantum,)).start()
# threading.Thread(target=fcfs.firstComeFirstServe, args=(processes, arrivalTime, burstTime,)).start()
# threading.Thread(target=sjf.shortestJobFirst, args=(processes, arrivalTime, burstTime,)).start()

rr.roundRobin(processes, arrivalTime, burstTime, quantum)
fcfs.firstComeFirstServe(processes, arrivalTime, burstTime)
sjf.shortestJobFirst(processes, arrivalTime, burstTime)
