arrival_time=[5,5,10,20]
start_time =[5,7,11,20]
end_time=[7,11,14,21]

def waiting_time(arrival_time,end_time):
    waiting_times=[]
    for arrival, end in zip(arrival_time, end_time):
        wait = end - arrival
        waiting_times.append(wait)
        avg_time=sum(waiting_times)/len(waiting_times)
    return avg_time

final_time=waiting_time(arrival_time,end_time)
print("The average waiting time is: ")
print(final_time)