import json
import numpy as np

# Read JSON data
with open('python_toolbox/evaluation/data/Ignatius/Ignatius.json') as f:
  data = json.load(f)

# Extract vertices 
vertices = np.array(data['bounding_polygon'])

# Create PLY header
header = '''ply
format ascii 1.0
element vertex %d
property float x
property float y
property float z
end_header
''' % len(vertices)

# Concatenate header and vertex coordinates
ply_data = header + '\n'.join([' '.join(map(str,v)) for v in vertices])

# Save to PLY file
with open('bbox.ply', 'w') as f:
  f.write(ply_data)