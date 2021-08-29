import output

def roundRobin(processes, arrivalTime, burstTime, quantum):
	
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
		remainingBurstTime = [0] * n
		response = [0] * n
		queue = []
		
		for i in range(n): 
			remainingBurstTime[i] = burstTime[i]

		for i in range(n):
			if (arrivalTime[i] == 0):
				queue.append(i)
		
		t = 0
		numDoneProcesses = 0
		
		while(1):

			i = 0
			queueLen = len(queue)

			while (i < queueLen):
				processDone = False 

				for j in range(quantum):

					if(response[queue[i]] == 0):
						response[queue[i]] = 1
						responseTime[queue[i]] = t - arrivalTime[queue[i]]	
					
					t += 1 
					remainingBurstTime[queue[i]] -= 1

					for k in range(n):
						if (arrivalTime[k] == t):
							queue.append(k)
							queueLen = len(queue)

					if (remainingBurstTime[queue[i]] == 0):
						waitingTime[queue[i]] = t - burstTime[queue[i]] - arrivalTime[queue[i]]
						queue.pop(i)
						queueLen = len(queue)
						processDone = True
						numDoneProcesses += 1
						break
			
				if(processDone):
					i -= 1
				i += 1
				
			if (numDoneProcesses == n):
				break

			if (queueLen == 0):
				t += 1
				for k in range(n):
					if (arrivalTime[k] == t):
						queue.append(k)
						queueLen = len(queue)		 
				
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
	responseTime = [0] * n 
	startTime = [0] * n
	runningTime = [0] * n
	
	totalWaitingTime = 0
	totalTurnAroundTime = 0
	totalBurstTime = 0

	sort() 
	findWaitingTime()
	findTurnAroundTime() 

	for i in range(n):
		totalBurstTime += burstTime[i]
		totalWaitingTime += waitingTime[i] 
		totalTurnAroundTime += turnAroundTime[i]
		startTime[i] = responseTime[i] + arrivalTime[i]
		runningTime[i] = turnAroundTime[i] - responseTime[i]  

	throughput = findThroughput()
	utilization = findUtilization()

	output.writeAnswer(processes, totalWaitingTime / n, totalWaitingTime / n, totalTurnAroundTime / n, utilization, throughput, waitingTime, turnAroundTime, startTime, runningTime, "rr")
