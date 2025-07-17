def heart_rate_zone(age, heart_rate): #define the function
    max_hr = 220 - age #calculate the maximum heart rate for the age group
    if heart_rate > max_hr:
        return "Error: Heart rate exceeds maximum safe value" #if heart rate exceeds maximum safe value, return error message
    if heart_rate < 0.5 * max_hr:
        return "Error: Heart rate below minimum exercise threshold" #if heart rate is below minimum exercise threshold, return error message
    percentages = [
        (0.5, 0.6, 1, "Very light exercise"),
        (0.6, 0.7, 2, "Light exercise"),
        (0.7, 0.8, 3, "Moderate exercise"),
        (0.8, 0.9, 4, "Hard exercise"),
        (0.9, 1.0, 5, "Maximum")
        ] #create a list of tuples containing the percentage ranges and zone descriptions
    for low, high, zone, description in percentages: #loop through the list of tuples
        if low <= heart_rate / max_hr < high:
            return f"Heart rate zone: {zone} ({description})" #if the heart rate falls within a percentage range, return the corresponding zone description
    return "Error: Heart rate not within any zone"  #if the heart rate does not fall within any percentage range, return error message

# Testing the function
print(heart_rate_zone(25, 150)) # Expected output: "Heart rate zone: 3 (Moderate exercise)"
    