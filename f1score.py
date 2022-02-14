def f1_score(recall: dict, precision: dict):
    rc_ = [v for k, v in recall.items()]
    r = rc_[-1]  # last recall
    pr_ = [v for k, v in precision.items()]
    p = pr_[-1]  # last precision
    f1 = round(2 * (p * r) / (p + r), 4)
    return f1
