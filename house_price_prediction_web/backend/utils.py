import numpy as np

def confidence_interval(pred, std):
    return {
        "min": round(pred - 1.96 * std, 2),
        "max": round(pred + 1.96 * std, 2)
    }
