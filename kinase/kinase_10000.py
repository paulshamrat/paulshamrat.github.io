def calculate_kinase_activity(phosphorylated_substrate, kinase_amount, assay_time):
    """
    Calculate protein kinase activity based on phosphorylation measurements.
    
    Args:
        phosphorylated_substrate (list): List of amounts of phosphorylated substrate (in moles).
        kinase_amount (list): List of amounts of protein kinase (in moles).
        assay_time (list): List of assay times (in seconds).
    
    Returns:
        list: List of protein kinase activities (in moles per second per mole of kinase).
    """
    kinase_activities = []
    
    for p_substrate, k_amount, a_time in zip(phosphorylated_substrate, kinase_amount, assay_time):
        kinase_activity = p_substrate / (k_amount * a_time)
        kinase_activities.append(kinase_activity)
    
    return kinase_activities

# Example usage with 10,000 samples
phosphorylated_substrate = [0.05, 0.03, 0.07, 0.02, 0.01, 0.09, 0.04, 0.06, 0.03, 0.08] * 1000  # moles
kinase_amount = [0.1, 0.2, 0.15, 0.08, 0.12, 0.25, 0.09, 0.18, 0.1, 0.22] * 1000  # moles
assay_time = [60, 90, 120, 60, 90, 120, 60, 90, 120, 60] * 1000  # seconds

activities = calculate_kinase_activity(phosphorylated_substrate, kinase_amount, assay_time)

for i, activity in enumerate(activities):
    print(f"Sample {i+1}: Protein kinase activity = {activity} moles/s/mole of kinase")
