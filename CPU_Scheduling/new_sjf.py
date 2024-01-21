def sjf_algorithm(processes):
    sorted_processes = sorted(processes.items(), key=lambda item: (item[1][0], item[1][1]))
    
    waiting_times = {key: 0 for key in processes.keys()}
    turnaround_times = {key: 0 for key in processes.keys()}
    burst_times = {key: value[1] for key, value in processes.items()}  # Define burst_times

    waitlist = []
    current_process = "IDLE"
    process_time = 0

    gantt_chart = {}
    gantt_ctr = 0
    start_time = 0

    while True:
        for key, (arrival_time, burst_time) in sorted_processes:
            if arrival_time == process_time:
                if current_process == "IDLE" or burst_time < burst_times[current_process]:
                    if process_time > 0 and start_time < process_time:
                        end_time = process_time
                        gantt_chart[gantt_ctr] = [current_process, start_time, end_time]
                        gantt_ctr += 1

                    current_process = key
                    start_time = process_time
                else:
                    waitlist.append(key)
                    waitlist = sorted(waitlist, key=lambda val: (burst_times[val], val))

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

            if waitlist:
                current_process = waitlist.pop(0)
                start_time = process_time
            else:
                current_process = "IDLE"
                start_time = process_time

        if all(burst == 0 for burst in burst_times.values()):
            break

    return gantt_chart, waiting_times, turnaround_times

def main():
    processlist = {}
    n = int(input("Number of processes: "))
    print()
    
    for i in range(n):
        at = int(input(f"P{i+1} Arrival Time: "))
        bt = int(input(f"P{i+1} Burst Time: "))
        print()
        processlist[f"P{i+1}"] = [at, bt]

    gantt_chart, waiting_times, turnaround_times = sjf_algorithm(processlist)

    print(f"GANTT CHART: {gantt_chart}\n")
    print(f"WAITING TIMES: {waiting_times}\n")
    print(f"TURNAROUND TIMES: {turnaround_times}\n")

if __name__ == "__main__":
    main()
