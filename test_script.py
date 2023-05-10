#path.append("./")  # look at path & append folder - contains current directory
#from data.load_engineering_data import get_project_data
import utils.load_engineering_data

# call the function
data = utils.load_engineering_data.get_project_data()
print("Data was loaded successfully.")
print(f"Data dimensions are {data.shape}")

# Address the input and output stipulations requested in the Project Description

"""
Inputs: Layer Height, Wall Thickness, Infill Density, Infill Pattern, 
Nozzle Temperature, Bed Temperature, Print Speed, Material (PLA or ABS), Fan Speed

Output: Tension Strength (the maximum stress that a material
can withstand while being stretched or pulled before breaking).

After the part was manufactured, the following three parameters 
were measured for each product.  Since only Tension Strength is 
required for this analysis, we will eliminate Roughness and Elongation
from the dataset

- Roughness (µm)
- Tension Strength (MPa)
- Elongation (%)

"""

# dropping unwanted columns
data = data.drop(columns=['roughness', 'elongation'])
print(f"The dimensions of the data after dropping two output columns are {data.shape}")