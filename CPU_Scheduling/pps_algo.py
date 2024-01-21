# <!DOCTYPE PREEMPTIVE PRIORITY SCHEDULING>
# needed to add: exception catchers (maybe)


def algo_pps(processes):
    processlist = {}
    # Creates split dictionaries for arrival times and burst times (sorts them as well)
    arrival_times = {key: value[0] for key, value in sorted(processes.items(), key=lambda item: item[1][0])}
    burst_times = {key: value[1] for key, value in sorted(processes.items(), key=lambda item: item[1][1])}
    priority_numbers = {key: value[2] for key, value in sorted(processes.items(), key=lambda item: item[1][2])}

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
    while need_shorthair_polsci_slash_arki_chinita_gf:
        for key, value in arrival_times.items():
            if value == process_time:
                if current_process == "IDLE":
                    if process_time > 0 and start_time < process_time:
                        end_time = process_time
                        gantt_chart[gantt_ctr] = [current_process, start_time, end_time]
                        gantt_ctr += 1
                    current_process = key
                    start_time = process_time
                else: 
                    waitlist.append(key)
                    waitlist= sorted(waitlist, key=lambda value: priority_numbers[value])
        if len(waitlist) > 0 and burst_times[current_process] > 0:
            if priority_numbers[current_process] > priority_numbers[waitlist[0]]:
                if start_time < process_time:
                    end_time = process_time
                    gantt_chart[gantt_ctr] = [current_process, start_time, end_time]
                    gantt_ctr += 1
                waitlist.append(current_process)
                waitlist= sorted(waitlist, key=lambda value: priority_numbers[value])
                current_process = waitlist[0]
                start_time = process_time
                waitlist.remove(current_process)
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
list_process = {"Process_1": [0, 4, 4], "Process_2": [2, 10, 2], "Process_3": [4, 2, 1], "Process_4": [6, 20, 3], "Process_5": [8, 2, 5]}

# n = int(input("Number of processes: "))
# print()
# for i in range(n):
#     at = int(input(f"P{i+1} Arrival Time: "))
#     bt = int(input(f"P{i+1} Burst Time: "))
#     pn = int(input(f"P{i+1} Priority Number: "))
#     processlist[f"P{i+1}"] = [at, bt, pn]
#     print()
# print(processlist)

gantt_chart, waiting_times, turnaround_times  = algo_pps(list_process)
print(f"GANTT CHART: {gantt_chart}\n")
print(f"WAITING TIMES: {waiting_times}\n")
print(f"TURNAROUND TIMES: {turnaround_times}\n")