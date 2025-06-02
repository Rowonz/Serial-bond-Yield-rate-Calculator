import logic_core as main
inputs = None


def inputs_main(data):
    global inputs
    inputs = data
    try:
        inputs["years"] = round(inputs["face_val"] / inputs["inst_amt"])
    except ZeroDivisionError:
        inputs["years"] = 0
        print('Placeholder')

    difference = inputs["acq_cost"] - inputs["face_val"]
    prm_disc = difference >= 0
    amort_details_data = {"prm_disc": prm_disc, "diff": difference}
    main.main_looper(inputs, amort_details_data, iteration=0)
