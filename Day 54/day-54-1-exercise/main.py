import time
# print('First Time',current_time)

def speed_calc_decorator(function):
    def speed_timer():
        first_time = time.time()
        function()
        second_timer = time.time()
        final_runing_speed = second_timer - first_time

        print(f"{function.__name__} run Speed :{final_runing_speed}s")
    return speed_timer
 
    return fast_function

def fast_function():
    for i in range(10000000):
        i * i
        
def slow_function():
    for i in range(100000000):
        i * i

function_List = [fast_function, slow_function]

for n in function_List:
    decorator_function = speed_calc_decorator(n)