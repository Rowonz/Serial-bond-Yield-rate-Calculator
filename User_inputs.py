import logic_core as main
inputs = None


def inputs_main(iteration):
    global inputs
    inputs = {"acq_cost": float(input("Acquisition Cost: ").replace(',', '')),
              "face_val": float(input("Face Value: ").replace(',', '')),
              "inst_amt": float(input("Installment Amount: ").replace(',', '')),
              "nom_rate": float(input("Nominal Rate (%): ").replace('%', '')) / 100}
    inputs["years"] = round(inputs["face_val"] / inputs["inst_amt"])
    difference = inputs["acq_cost"] - inputs["face_val"]
    prm_disc = difference >= 0
    amort_details_data = {"prm_disc": prm_disc, "diff": difference}
    main.logic_core_heuristics(inputs, amort_details_data, iteration)  # not functioning as of right now, not all pos. args met
