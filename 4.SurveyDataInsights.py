# Let's use string comparisons to label data acquired through a fitness app's user survey.

frequency = "once a week"
intensity = "low"

highly_active = frequency == "daily"
print("Highly active user:")
print(highly_active)

high_intensity = intensity == "high"
print("High intensity activity:")
print(high_intensity)
