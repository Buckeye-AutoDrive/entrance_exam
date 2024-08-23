import numpy as np
import plotly.graph_objs as go
import plotly.io as pio
from plotly.subplots import make_subplots
from PIL import Image
import os
import json

def load_point_cloud(file_path):
    point_cloud = np.fromfile(file_path, dtype=np.float32).reshape(-1, 4)
    return point_cloud[:, :3]

def load_camera_settings_from_json(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)

def visualize_multiple_point_clouds(image_files, pcd_files, camera_settings):
    num_data = len(image_files)

    # Create a subplot grid with num_data rows and 3 columns
    fig = make_subplots(rows=num_data, cols=3,
                        subplot_titles=sum(
                            [["Image", "Raw Point Cloud", "Filtered Point Cloud"] for _ in range(num_data)], []),
                        specs=[[{'type': 'xy'}, {'type': 'scatter3d'}, {'type': 'scatter3d'}]] * num_data)

    for i, (image_path, pcd_path) in enumerate(zip(image_files, pcd_files)):
        # Load the image using PIL and resize it
        img = Image.open(image_path)
        img = img.resize((800, 800), Image.Resampling.LANCZOS)

        # Convert the image to a numpy array
        img_np = np.array(img)

        # Add the image to the first column of the i-th row
        fig.add_trace(go.Image(z=img_np), row=i + 1, col=1)

        # Load and process the point cloud
        points = load_point_cloud(pcd_path)
        filtered_points = ground_removal(points)

        # Raw Point Cloud
        raw_trace = go.Scatter3d(
            x=points[:, 0],
            y=points[:, 1],
            z=points[:, 2],
            mode='markers',
            marker=dict(
                size=2,
                color='blue',
            ),
            showlegend=False  # Disable legend for this trace
        )

        # Filtered Point Cloud
        filtered_trace = go.Scatter3d(
            x=filtered_points[:, 0],
            y=filtered_points[:, 1],
            z=filtered_points[:, 2],
            mode='markers',
            marker=dict(
                size=2,
                color='red',
            ),
            showlegend=False  # Disable legend for this trace
        )

        # Add traces to the subplots
        fig.add_trace(raw_trace, row=i + 1, col=2)
        fig.add_trace(filtered_trace, row=i + 1, col=3)

        # Apply different camera settings and aspect mode to each row
        scene_id = f'scene{i * 2 + 1}'
        fig.update_layout({scene_id: dict(aspectmode='data', camera=camera_settings[i])})
        scene_id2 = f'scene{i * 2 + 2}'
        fig.update_layout({scene_id2: dict(aspectmode='data', camera=camera_settings[i])})

    # Set the resolution for a clearer display and remove the legend
    fig.update_layout(width=1800, height=600 * num_data, showlegend=False)  # Adjust height based on number of rows

    pio.show(fig)

def ground_removal(points):

    non_ground_points = points

    return non_ground_points

def main():
    image_dir = "data/images"
    pcd_dir = "data/pcd"

    # Collect image and pcd file paths
    image_files = sorted([os.path.join(image_dir, f) for f in os.listdir(image_dir) if f.endswith('.png')])
    pcd_files = sorted([os.path.join(pcd_dir, f) for f in os.listdir(pcd_dir) if f.endswith('.bin')])

    # Load the camera settings from the JSON file
    camera_settings = load_camera_settings_from_json('data/camera_settings.json')

    # Visualize the multiple point clouds with the loaded camera settings
    visualize_multiple_point_clouds(image_files, pcd_files, camera_settings)


if __name__ == "__main__":
    main()
