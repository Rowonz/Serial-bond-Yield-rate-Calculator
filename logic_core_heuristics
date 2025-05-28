import random


# a > 0, b < 0
a_interval = None
b_interval = None
inputs = None


def inputs_main(iteration):
    global inputs
    if iteration == 0:
        inputs = {"acq_cost": float(input("Acquisition Cost: ").replace(',', '')),
                  "face_val": float(input("Face Value: ").replace(',', '')),
                  "inst_amt": float(input("Installment Amount: ").replace(',', '')),
                  "nom_rate": float(input("Nominal Rate (%): ").replace('%', '')) / 100}
        inputs["years"] = round(inputs["face_val"] / inputs["inst_amt"])
        starter(inputs, iteration, None)
        return inputs
    else:
        if inputs is not None:
            return inputs
        else:
            print("Warning: No existing inputs provided for iteration > 1.")
            return {}


def starter(data, iter_c, new_val):
    a_cost = data["acq_cost"]
    f_val = data["face_val"]
    inst = data["inst_amt"]
    rate = data["nom_rate"]
    yr = data["years"]
    if iter_c == 0:
        guess_formula_initial, prm_disc = scaled_guess(a_cost, f_val, iter_c)
        guess = range_setter(rate, guess_formula_initial, prm_disc)
        assign_var_result = function(a_cost, f_val, inst, rate, yr, guess, iter_c)
        return assign_var_result
    else:  # x, y, z, a, b, c
        assign_var_result = function(a_cost, f_val, inst, rate, yr, new_val, iter_c)
        return assign_var_result


def scaled_guess(acq_cost, face_val, iter_c):
    diff_steps = (acq_cost / face_val) - 1  # deviation from 1 (when acq_cost = face_val)
    prm_disc = diff_steps >= 0
    calculated = (abs(diff_steps) ** (1 / 4) * 10)
    check_call = scale_viability(calculated, iter_c)
    return check_call, prm_disc  # custom scaler based on ratio - 1


def range_setter(x, y, z):  # function to choose a random number based on input and guess
    percentage_int = round(x * 100)
    if a_interval is not None and b_interval is not None:
        midpoint_val = bisector()
        return midpoint_val
    elif a_interval is not None:
        b_try = percentage_int + a_interval
        return b_try
    elif b_interval is not None:
        a_try = percentage_int - b_interval
        return a_try
    else:
        if y > 0:
            if z:  # handles premium
                n = percentage_int - y
                return random.randint(min(percentage_int, n) + 1, max(percentage_int, n) + 1)
            else:  # handles discount
                n = percentage_int + y
                return random.randint(min(percentage_int, n) + 1, max(percentage_int, n) + 1)
        else:
            return percentage_int  # added to guard against/check if acq_cost = face_val, as
            # nominal rate may be excluded due to min(...) + 1 or max(...) + 1


def function(x, y, z, a, b, c, iteration):
    guess_dec = (c / 100)
    c_list = []
    div_list = []
    top_list = []
    total = 0  # final result from all calculations stored here
    for n in range(0, b + 1):  # carrying amount - installment
        carrying_amount = y - (z * n)
        if n == b:
            continue  # skip dummy year (0) to avoid adding (decrease complexity later)
        else:
            c_list.append(carrying_amount)
    for i in c_list:  # top part of the formula
        product = (i * a) + z  # ACTUAL CASH FLOWS
        top_list.append(product)
    for m in range(1, b + 1):  # bottom part of the formula
        div = (1 + guess_dec) ** m
        div_list.append(div)
    for i in range(len(top_list)):  # completed formula
        total += top_list[i] / div_list[i]
    return a_b_assigner(x, total, c, a, iteration)


def a_b_assigner(acq_cost, to_check, percentage_used, nom_rate, iter_c):  # iter count placeholder for now
    global a_interval, b_interval
    assign_var = to_check - acq_cost
    if abs(assign_var) <= 1e-6:  # circumvent floating point problem tolerance of 0.01 (legacy comment no tolerance now)
        print(f'Yield Rate of Serial Bond: {percentage_used}%, Assign_var value: {round(assign_var)}, '
              f'Value calculated: {round(to_check, 0)}. It took {iter_c} iterations')
        return assign_var
    elif assign_var > 0:
        iter_c += 1
        a_interval = percentage_used
        return looper(nom_rate, percentage_used, True, iter_c, assign_var)
    elif assign_var < 0:
        iter_c += 1
        b_interval = percentage_used
        return looper(nom_rate, percentage_used, False, iter_c, assign_var)


def bisector():
    if a_interval is not None and b_interval is not None:
        mid_point = (a_interval + b_interval) / 2
        return mid_point


def looper(rate, percent, prm_disc, iter_c, var):
    while abs(var) > 1e-6:
        inputs_looper = inputs_main(iter_c)
        new_val = range_setter(rate, percent, prm_disc)
        var = starter(inputs_looper, iter_c, new_val)
        if abs(var - inputs_looper["acq_cost"]) <= 1e-6:  # Compare PV to acq_cost
            break
    return var


def scale_viability(check, iter_c):
    call_inputs = inputs
    a_cost = call_inputs["acq_cost"]
    f_val = call_inputs["face_val"]
    inst = call_inputs["inst_amt"]
    rate = call_inputs["nom_rate"]
    yr = call_inputs["years"]
    check_result = function(a_cost, f_val, inst, rate, yr, check, iter_c)
    if check_result is a_interval:
        return check_result
    else:
        return check_result + 10


inputs_main(iteration=0)
