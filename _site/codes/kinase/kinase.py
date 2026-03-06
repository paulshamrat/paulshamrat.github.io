def calculate_kinase_activity(phosphorylated_substrate, kinase_amount, assay_time):
    """
    Calculate protein kinase activity based on phosphorylation measurements.
    
    Args:
        phosphorylated_substrate (float): Amount of phosphorylated substrate (in moles).
        kinase_amount (float): Amount of protein kinase (in moles).
        assay_time (float): Assay time (in seconds).
    
    Returns:
        float: Protein kinase activity (in moles per second per mole of kinase).
    """
    kinase_activity = phosphorylated_substrate / (kinase_amount * assay_time)
    return kinase_activity

# Example usage
phosphorylated_substrate = 0.05  # moles
kinase_amount = 0.1  # moles
assay_time = 60  # seconds

activity = calculate_kinase_activity(phosphorylated_substrate, kinase_amount, assay_time)
print(f"Protein kinase activity: {activity} moles/s/mole of kinase")
