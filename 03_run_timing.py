"""
Write a function that asks how long it took to run 10k.
the function continues to as how long (in min) it took for additional runs.
until the user press enter
at that point the function exits but only after calculating and displaying
the average time of runs and how many.
"""

def run_timming():
    number_of_runs = 0
    total_time= 0

    while True:
        one_run = input("Enter 10k run time: ")
        if not one_run:
            break
        number_of_runs += 1
        total_time += float(one_run) 
    average = total_time/number_of_runs
    print(f'average of {average:.1f}, over {number_of_runs} runs')



run_timming()
