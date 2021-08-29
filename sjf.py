import output

def shortestJobFirst(processes, arrivalTime, burstTime):

    def sort():
        for i in range(n):
            for j in range(n-i-1):
                if (arrivalTime[j] > arrivalTime[j+1]):
                    swap(j+1, j)

    def swap(i , j):
        processes[j], processes[i] = processes[i], processes[j]
        arrivalTime[j], arrivalTime[i] = arrivalTime[i], arrivalTime[j]
        burstTime[j], burstTime[i] = burstTime[i], burstTime[j]
        completionTime[j], completionTime[i] = completionTime[i], completionTime[j]
        waitingTime[j], waitingTime[i] = waitingTime[i], waitingTime[j]
        turnAroundTime[j], turnAroundTime[i] = turnAroundTime[i], turnAroundTime[j]

    def findCompletionTime():

        for i in range(0, n):
            if(i == 0):
                temp = arrivalTime[0]
            else:
                temp = completionTime[i-1]
            
            minimumBurstTime = burstTime[i]
            done = 0

            for j in range(i, n):
                if(temp >= arrivalTime[j] and minimumBurstTime >= burstTime[j]):
                    minimumBurstTime = burstTime[j]
                    val = j
                    done = 1
            
            if(done == 0):
                temp = arrivalTime[i]
                for j in range(i, n):
                    if (temp >= arrivalTime[j] and minimumBurstTime >= burstTime[j]):
                        minimumBurstTime = burstTime[j]
                        val = j
            
            if(done == 1):
                completionTime[val] = temp + burstTime[val]
                turnAroundTime[val] = completionTime[val] - arrivalTime[val]
                waitingTime[val] = turnAroundTime[val] - burstTime[val]
            else:
                completionTime[val] = temp + burstTime[val]
                turnAroundTime[val] = burstTime[val]
                waitingTime[val] = 0
            

            swap(i, val)

    def findThroughput():
        return n / (arrivalTime[-1] + turnAroundTime[-1]) * 0.001

    def findUtilization():
        return totalBurstTime/(arrivalTime[-1] + turnAroundTime[-1])
    
    n = len(processes)

    completionTime = [0] * n
    waitingTime = [0] * n
    turnAroundTime = [0] * n
    startTime = [0] * n
    runningTime = [0] * n

    totalWaitingTime = 0
    totalTurnAroundTime = 0
    totalBurstTime = 0

    sort()
    findCompletionTime()

    for i in range(n):
        totalBurstTime += burstTime[i]
        totalWaitingTime += waitingTime[i] 
        totalTurnAroundTime += turnAroundTime[i]
        startTime[i] = waitingTime[i] + arrivalTime[i] 
        runningTime[i] = turnAroundTime[i] - waitingTime[i] 

    throughput = findThroughput()
    utilization = findUtilization()

    output.writeAnswer(processes, totalWaitingTime / n, totalWaitingTime / n, totalTurnAroundTime / n, utilization, throughput, waitingTime, turnAroundTime, startTime, runningTime, "sjf")

    