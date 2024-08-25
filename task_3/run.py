import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from PIL import Image
import json
import convert_data

# Function to read Velodyne binary files (point cloud data)
def read_bin_velodyne(path):
    points = np.fromfile(path, dtype=np.float32).reshape(-1, 4)
    return points[:, :3]  # return x, y, z

# Function to filter 3D bounding box corners based on distance
def filter_bbox_points(corners_3d, threshold=400):
    distances = np.linalg.norm(corners_3d, axis=0)
    return corners_3d[:, distances <= threshold]

# Function to create a rotation matrix for the Y axis
def create_rotation_matrix_y(t):
    c = np.cos(t)
    s = np.sin(t)
    return np.array([[c, 0, s], [0, 1, 0], [-s, 0, c]])

# Function to draw 3D bounding boxes on the plot
def draw_3d_bounding_box(fig, dimension, center, rotation, threshold=400):
    h, w, l = dimension
    x, y, z = center
    t = rotation

    R = create_rotation_matrix_y(t)
    x_corners = [l/2, l/2, -l/2, -l/2, l/2, l/2, -l/2, -l/2]
    y_corners = [0, 0, 0, 0, -h, -h, -h, -h]
    z_corners = [w/2, -w/2, -w/2, w/2, w/2, -w/2, -w/2, w/2]
    corners_3d = np.vstack([x_corners, y_corners, z_corners])

    corners_3d = R.dot(corners_3d)
    corners_3d += np.array([x, y, z]).reshape(3, 1)

    corners_3d = filter_bbox_points(corners_3d, threshold)

    if corners_3d.shape[1] == 0:
        return np.inf, -np.inf, np.inf, -np.inf, np.inf, -np.inf

    edges = [
        [0, 1], [1, 2], [2, 3], [3, 0],
        [4, 5], [5, 6], [6, 7], [7, 4],
        [0, 4], [1, 5], [2, 6], [3, 7]
    ]

    y, z, x = corners_3d
    y *= -1
    z *= -1

    for edge in edges:
        if all(idx < corners_3d.shape[1] for idx in edge):
            fig.add_trace(go.Scatter3d(
                x=[x[edge[0]], x[edge[1]]],
                y=[y[edge[0]], y[edge[1]]],
                z=[z[edge[0]], z[edge[1]]],
                mode='lines',
                line=dict(color='blue', width=3),
                name='Bounding Box'
            ))

    return np.min(x), np.max(x), np.min(y), np.max(y), np.min(z), np.max(z)

# Function to print the encoded data structure and data (only the first item in lists)
def print_encoded_data(data):
    # Make a copy of the data but only keep the first element in each list
    data_copy = {
        "object_2d": {"objects": [data["object_2d"]["objects"][0]]} if data["object_2d"]["objects"] else {"objects": []},
        "object_3d": {"objects": [data["object_3d"]["objects"][0]]} if data["object_3d"]["objects"] else {"objects": []}
    }
    print("\nEncoded Data Structure (with first item only):")
    print(json.dumps(data_copy, indent=4))

# File paths
label_path = 'data/labels/000010.txt'  # Replace with your actual label file path
pcd_path = 'data/pcd/000010.bin'  # Replace with your actual point cloud file path
image_path = 'data/images/000010.png'  # Replace with your actual image file path
camera_position_path = 'data/camera_settings.json'  # Replace with your actual JSON file path

# Read point cloud data
pcd = read_bin_velodyne(pcd_path)

# Encode the data by parsing the KITTI label file using the function from convert_data.py
data = convert_data.parse_kitti_label_file(label_path)

# Print the encoded data structure and contents (only the first item in lists)
print_encoded_data(data)

# Load the image
image = Image.open(image_path)

# Load camera positions from JSON file
with open(camera_position_path, 'r') as f:
    camera_positions = json.load(f)

# Create a subplot with 2 rows and 1 column
fig = make_subplots(rows=2, cols=1, subplot_titles=("2D Bounding Boxes on Image", "3D Point Cloud with Bounding Boxes"),
                    specs=[[{"type": "xy"}], [{"type": "scatter3d"}]])

# Add 2D image with bounding boxes to the first subplot
fig.add_trace(go.Image(z=np.array(image)), row=1, col=1)

for obj in data["object_2d"]["objects"]:
    x_min_2d, y_min_2d, x_max_2d, y_max_2d = obj["2d bb"]
    fig.add_trace(go.Scatter(
        x=[x_min_2d, x_max_2d, x_max_2d, x_min_2d, x_min_2d],
        y=[y_min_2d, y_min_2d, y_max_2d, y_max_2d, y_min_2d],
        mode='lines',
        line=dict(color='red', width=2),
        name='2D Bounding Box'
    ), row=1, col=1)

# Add point cloud and 3D bounding boxes to the second subplot
fig.add_trace(go.Scatter3d(
    x=pcd[:, 0], y=pcd[:, 1], z=pcd[:, 2],
    mode='markers',
    marker=dict(size=1, color=pcd[:, 0], colorscale='Viridis', showscale=True),  # Color by x-axis
    name='Point Cloud'
), row=2, col=1)

x_min, x_max = np.min(pcd[:, 0]), np.max(pcd[:, 0])
y_min, y_max = np.min(pcd[:, 1]), np.max(pcd[:, 1])
z_min, z_max = np.min(pcd[:, 2]), np.max(pcd[:, 2])

for obj in data["object_3d"]["objects"]:
    dimension = obj["3d bb"]["dimension"]
    center = obj["3d bb"]["center"]
    rotation = obj["3d bb"]["rotation"]
    bx_min, bx_max, by_min, by_max, bz_min, bz_max = draw_3d_bounding_box(fig, dimension, center, rotation)
    x_min, x_max = min(x_min, bx_min), max(x_max, bx_max)
    y_min, y_max = min(y_min, by_min), max(y_max, by_max)
    z_min, z_max = min(z_min, bz_min), max(z_max, bz_max)

# Apply the first camera position as the default
fig.update_layout(
    scene=dict(
        camera=camera_positions[0],
        xaxis=dict(title='X', range=[x_min, x_max]),
        yaxis=dict(title='Y', range=[y_min, y_max]),
        zaxis=dict(title='Z', range=[z_min, z_max]),
        aspectmode='data'
    ),
    height=2000,  # Increased height for the 3D plot
    showlegend=False
)

# Display the combined plot in the browser
fig.show()
