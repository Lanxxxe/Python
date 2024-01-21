# <!DOCTYPE SHORTEST JOB FIRST>
# needed to add: exception catchers (maybe)



def algo_sjf(processes):
    processlist = {}
    # Creates split dictionaries for arrival times and burst times (sorts them as well)
    arrival_times = {key: value[0] for key, value in sorted(processes.items(), key=lambda item: item[1][0])}
    burst_times = {key: value[1] for key, value in sorted(processes.items(), key=lambda item: item[1][1])}

    # Initializes dictionaries and variables
    waiting_times = {key: 0 for key in processes.keys()}    
    turnaround_times = {key: 0 for key in processes.keys()}
    waitlist = []
    current_process = "IDLE"
    process_time = 0
    burst_total = 0
    for value in burst_times.values():
        burst_total += value

    # gantt chart format : PROCESS_COUNT: [PROCESS_ID, START_TIME, END_TIME]
    gantt_chart = {}
    gantt_ctr = 0
    start_time = 0

    # ong please
    need_shorthair_polsci_slash_arki_chinita_gf = True
    while True:
        for key, value in arrival_times.items():
            if value == process_time:
                if current_process == "IDLE":
                    if process_time > 0:
                        end_time = process_time
                        gantt_chart[gantt_ctr] = [current_process, start_time, end_time]
                        gantt_ctr += 1
                    current_process = key
                    start_time = process_time
                else: 
                    waitlist.append(key)
        process_time += 1
        if current_process != "IDLE":
            burst_times[current_process] -= 1
            turnaround_times[current_process] += 1
            for process in waitlist:
                waiting_times[process] += 1
                turnaround_times[process] += 1
        if current_process != "IDLE" and burst_times[current_process] == 0:
            end_time = process_time
            gantt_chart[gantt_ctr] = [current_process, start_time, end_time]
            gantt_ctr += 1
            if len(waitlist) > 0:
                current_process = waitlist[0]
                start_time = process_time
                waitlist.remove(current_process)
            else: 
                current_process = "IDLE"
                start_time = process_time
        for value in burst_times.values():
            burst_total += value
        if burst_total == 0:
            break
        else: 
            burst_total = 0
    return gantt_chart, waiting_times, turnaround_times





processlist = {}
n = int(input("Number of processes: "))
print()
for i in range(n):
    at = int(input(f"P{i+1} Arrival Time: "))
    bt = int(input(f"P{i+1} Burst Time: "))
    print()
    processlist[f"P{i+1}"] = [at, bt]
print(processlist)

gantt_chart, waiting_times, turnaround_times  = algo_sjf(processlist)
print(f"GANTT CHART: {gantt_chart}\n")
print(f"WAITING TIMES: {waiting_times}\n")
print(f"TURNAROUND TIMES: {turnaround_times}\n")