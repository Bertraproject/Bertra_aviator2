def calculate_prediction(multipliers):
    values = [float(m.replace("x", "")) for m in multipliers if "x" in m]
    low_streak = 0
    for v in reversed(values[-10:]):
        if v < 2.0:
            low_streak += 1
        else:
            break
    probability = min(100, low_streak * 10 + len([v for v in values[-10:] if v > 10]) * 5)
    return {
        "low_streak": low_streak,
        "high_count": len([v for v in values[-10:] if v > 10]),
        "probability": probability,
    }
