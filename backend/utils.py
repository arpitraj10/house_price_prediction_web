

def confidence_interval(prediction, margin=0.1):
    lower = prediction * (1 - margin)
    upper = prediction * (1 + margin)
    return lower, upper
