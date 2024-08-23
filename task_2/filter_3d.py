import numpy as np
import plotly.graph_objs as go
import plotly.io as pio
import time

def load_point_cloud(file_path):
    point_cloud = np.fromfile(file_path, dtype=np.float32).reshape(-1, 4)
    return point_cloud[:, :3]

def visualize_point_cloud(points, title="Point Cloud", color='blue'):
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

    camera = dict(
        up=dict(x=0, y=0, z=1),
        center=dict(x=-0.11, y=0.18, z=-0.19),
        eye=dict(x=-1, y=0.14, z=0.3),
        projection=dict(type='perspective')
    )

    layout = go.Layout(
        title=title,
        scene=dict(
            xaxis_title='X',
            yaxis_title='Y',
            zaxis_title='Z',
            camera=camera
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
    file_path = "000000.bin"
    points = load_point_cloud(file_path)
    visualize_point_cloud(points, title="Raw Point Cloud", color='blue')

    start_time = time.time()
    filtered_points = ground_removal(points)
    inference_time = time.time() - start_time

    visualize_point_cloud(filtered_points, title="Filtered Point Cloud", color='red')
    print(f"Ground removal algorithm inference time: {inference_time:.4f} seconds")

if __name__ == "__main__":
    main()
