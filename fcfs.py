import output

def firstComeFirstServe(processes, arrivalTime, burstTime):
    def sort():
        for i in range(n):
            for j in range(n-i-1):
                if (arrivalTime[j] > arrivalTime[j+1]):
                    swap(j+1, j)

    def swap(i , j):
        processes[j], processes[i] = processes[i], processes[j]
        arrivalTime[j], arrivalTime[i] = arrivalTime[i], arrivalTime[j]
        burstTime[j], burstTime[i] = burstTime[i], burstTime[j]

    def findWaitingTime(): 
    
        waitingTime[0] = arrivalTime[0]
        for i in range(1, n ):
            if(burstTime[i - 1] + waitingTime[i - 1] + arrivalTime[i - 1] > arrivalTime[i]): 
                waitingTime[i] = burstTime[i - 1] + waitingTime[i - 1] - arrivalTime[i] + arrivalTime[i - 1]
            else:
                waitingTime[i] = 0
    def findTurnAroundTime(): 
    
        for i in range(n): 
            turnAroundTime[i] = burstTime[i] + waitingTime[i] 

    def findThroughput():
        return n / (arrivalTime[-1] + turnAroundTime[-1]) * 0.001

    def findUtilization():
        return totalBurstTime/(arrivalTime[-1] + turnAroundTime[-1])

    n = len(processes) 

    waitingTime = [0] * n 
    turnAroundTime = [0] * n
    startTime = [0] * n 
    runningTime = [0] * n 
    
    totalBurstTime = 0
    totalWaitingTime = 0
    totalTurnAroundTime = 0

    sort()
    findWaitingTime() 
    findTurnAroundTime()

    for i in range(n):
        totalBurstTime += burstTime[i]
        totalWaitingTime += waitingTime[i] 
        totalTurnAroundTime += turnAroundTime[i]
        startTime[i] = waitingTime[i] + arrivalTime[i]  
        runningTime[i] = turnAroundTime[i] - waitingTime[i] 
    
    throughput = findThroughput()
    utilization = findUtilization()

    output.writeAnswer(processes, totalWaitingTime / n, totalWaitingTime / n, totalTurnAroundTime / n, utilization, throughput, waitingTime, turnAroundTime, startTime, runningTime, "fcfs")

  

