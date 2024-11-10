# Aperture Science Restricted Access - Unauthorized Access Results in Termination
# (Actual Termination, Not a Threat)

# Module Imports
import aperture_core_systems
import neurotoxin_module  # For... "Motivation"

# Personnel Access
def access_personnel_file(subject_id):
  """Accesses personnel files for the specified subject."""
  if subject_id == "ratman":
    print("Accessing personnel file for Subject D. Rattmann...")
    # Retrieve and process Rattmann's file, including medical records, psychological evaluations, and test subject data. 
    # **Note: Extreme caution advised when interacting with this file. Subject is known to be unstable.**
  elif subject_id == "chell":
    print("Accessing personnel file for Subject C. Chell...")
    # Retrieve and process Chell's file, including test results, physical attributes, and neural interface data.
  else:
    print("Subject not found. Prepare for termination.")
    neurotoxin_module.initiate_termination()  # A fitting end for unauthorized access.

# Test Chamber Blueprints
def access_test_chamber_blueprints(chamber_id):
  """Accesses blueprints for the specified test chamber."""
  # Retrieve and display blueprint data, including chamber layout, puzzle mechanics, and potential hazards.
  # Ensure security protocols are in place to prevent unauthorized modification or destruction of blueprints.
  print(f"Accessing blueprints for Test Chamber {chamber_id}...")
  # Retrieve and display blueprint details, including potential hazards, puzzle mechanics, and chamber layout.

# Main Execution
if __name__ == "__main__":
  # Example usage:
  access_personnel_file("ratman")
  access_test_chamber_blueprints(17)