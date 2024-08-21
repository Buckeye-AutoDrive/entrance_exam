import numpy as np
import plotly.graph_objs as go
import plotly.io as pio
import time

def load_point_cloud(file_path):
    # Load the point cloud data from a .bin file
    point_cloud = np.fromfile(file_path, dtype=np.float32).reshape(-1, 4)
    return point_cloud[:, :3]  # Return only XYZ coordinates

def visualize_point_cloud(points, title="Point Cloud", color='blue'):
    # Interactive 3D scatter plot using plotly
    trace = go.Scatter3d(
        x=points[:, 0],
        y=points[:, 1],
        z=points[:, 2],
        mode='markers',
        marker=dict(
            size=2,
            color=color,
        )
    )

    layout = go.Layout(
        title=title,
        scene=dict(
            xaxis_title='X',
            yaxis_title='Y',
            zaxis_title='Z'
        ),

    )

    fig = go.Figure(data=[trace], layout=layout)
    fig.update_layout(scene=dict(aspectmode='data'))
    pio.show(fig)

def ground_removal(points):
    # Implement your ground removal algorithm here
    # Return the filtered point cloud (without ground points)
    filtered_points = points  # Placeholder: replace with your algorithm
    return filtered_points

def main():
    # Load the point cloud data
    file_path = "000000.bin"  # Update this path
    points = load_point_cloud(file_path)

    # Visualize the raw point cloud
    print("Visualizing raw point cloud...")
    visualize_point_cloud(points, title="Raw Point Cloud", color='blue')

    # Measure inference time for ground removal
    start_time = time.time()
    filtered_points = ground_removal(points)
    inference_time = time.time() - start_time

    # Visualize the filtered point cloud
    print("Visualizing filtered point cloud...")
    visualize_point_cloud(filtered_points, title="Filtered Point Cloud", color='red')

    # Print inference time
    print(f"Ground removal algorithm inference time: {inference_time:.4f} seconds")

if __name__ == "__main__":
    main()
