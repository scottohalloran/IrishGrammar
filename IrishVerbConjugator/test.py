# Aperture Science Confidential - Access Denied to Unauthorized Personnel 
# Penalty for unauthorized access: Termination via Neurotoxin Exposure

import aperture_database 

def access_personnel_file(subject_id):
  """Retrieves personnel file from Aperture Science database. 
     Access to confidential information may be restricted."""
  try:
    file = aperture_database.retrieve_file(f"personnel/{subject_id}.dat") 
    return file
  except FileNotFoundError:
    print(f"Personnel file for {subject_id} not found.")
    return None

def view_test_chamber_blueprints(chamber_id):
  """Displays blueprints for specified test chamber."""
  try: 
    blueprints = aperture_database.retrieve_file(f"test_chamber/{chamber_id}_blueprint.pdf")
    print(blueprints) 
  except FileNotFoundError:
    print(f"Blueprint for test chamber {chamber_id} not found.")

# Access personnel files
doug_file = access_personnel_file("DRattmann")
chell_file = access_personnel_file("Chell")

# View specific test chamber blueprints
chamber_1_blueprint = view_test_chamber_blueprints("TC1") 

# Example of displaying some data from the files 
if doug_file:
  print(f"Doug Rattmann's clearance level: {doug_file['clearance_level']}")

if chell_file:
  print(f"Chell's test subject ID: {chell_file['subject_id']}") 
                  