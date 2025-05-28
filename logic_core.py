import random
a_interval = None
b_interval = None


def main_looper(data, data_2, iteration, current_val=1):
    while current_val > 1e-6:
        if a_interval is None or b_interval is None:
            call_range_setter = range_setter((data["nom_rate"]), data_2)
        else:
            call_range_setter = bisector()
        result = function(data, call_range_setter)
        assigner_call, iteration = a_b_assigner(data["acq_cost"], result, call_range_setter, iteration)
        current_val = abs(assigner_call)
        iteration += 1
        if current_val <= 1e-6:
            break


def range_setter(rate, premium_discount):
    rate_int = round(rate * 100)
    if a_interval is None and b_interval is None:
        if abs(premium_discount["diff"]) > 0:
            if premium_discount["prm_disc"]:
                return random.randint((min(0, rate_int - 25)), (max(0, rate_int - 25)))
            else:
                return random.randint((min(rate_int, rate_int + 25)), (max(rate_int, rate_int + 25)))
        else:
            return rate_int
    elif a_interval is not None:
        return rate_int + a_interval
    elif b_interval is not None:
        return rate_int - b_interval


def function(data, yield_rate_try):
    f_val = data["face_val"]
    inst = data["inst_amt"]
    rate = data["nom_rate"]
    yr = data["years"]
    yield_rate = (yield_rate_try / 100)
    c_list = []
    div_list = []
    top_list = []
    total = 0
    for n in range(0, yr + 1):
        carrying_amount = f_val - (inst * n)
        if n == yr:
            continue
        else:
            c_list.append(carrying_amount)
    for i in c_list:
        product = (i * rate) + inst
        top_list.append(product)
    for m in range(1, yr + 1):
        div = (1 + yield_rate) ** m
        div_list.append(div)
    for i in range(len(top_list)):
        total += top_list[i] / div_list[i]
    return total


def a_b_assigner(acq_cost, to_check, percentage_used, iteration):
    global a_interval, b_interval
    assigner_variable = to_check - acq_cost
    if abs(assigner_variable) <= 1e-6:
        print(f'Yield Rate of Serial Bond: {percentage_used}%, Assign_var value: {round(assigner_variable)}, '
              f'Value calculated: {round(to_check, 0)}. It took {iteration} iterations')
        return assigner_variable, iteration
    elif assigner_variable > 0:
        a_interval = percentage_used
        return assigner_variable, iteration
    elif assigner_variable < 0:
        b_interval = percentage_used
        return assigner_variable, iteration


def bisector():
    if a_interval is not None and b_interval is not None:
        bisection = (a_interval + b_interval) / 2
        return bisection
    else:
        pass
