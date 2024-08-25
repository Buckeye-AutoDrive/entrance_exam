# Task 3: Data Conversion and Visualization

In this task, you'll work with KITTI data to convert its format into our custom data structure and visualize the converted data. The purpose of this task is to test your data processing skills.

## Steps to Complete the Task

### 1. Understand the Provided Base Code and Data Structure

- The provided base code (`run.py`) handles reading the point cloud data from a `.bin` file, converting the KITTI data format, and visualizing both the raw and processed data. It also contains the necessary logic to decode the custom data structure for visualization.


- The KITTI data format provides labels in the following structure (example):

  ```
  Car 0.80 0 -2.09 1013.39 182.46 1241.00 374.00 1.57 1.65 3.35 4.43 1.65 5.20 -1.42
  ```

- This line represents a single object in the scene, where:
  
  - `Car`: The object class.
  - `0.80`: The truncation level (0 = non-truncated, 1 = truncated).
  - `0`: The occlusion level (0 = fully visible, 1 = partly occluded).
  - `-2.09`: The observation angle (in radians).
  - `1013.39 182.46 1241.00 374.00`: The 2D bounding box coordinates in the image (left, top, right, bottom).
  - `1.57 1.65 3.35`: The dimensions of the 3D bounding box (height, width, length).
  - `4.43 1.65 5.20`: The center of the 3D bounding box in the camera coordinate system (x, y, z).
  - `-1.42`: The rotation angle around the Y-axis.

  You can view more examples in the `data/labels` directory.

### 2. Implement Data Conversion

- Your task is to implement the `convert_data.py` file inside the `task_3` directory. This file should convert the KITTI label data into the following custom data structure:
    ```
    data  
    ├── object_2d  
    │   └── objects (list)  
    │       ├── class  
    │       └── 2d bb  
    └── object_3d   
        └── objects (list)  
            ├── class  
            └── 3d bb  
                ├── dimension  
                ├── center  
                └── rotation  
    ```

- Once you've implemented the conversion, you can run `convert_data.py` to view the full data structure with data included, which will help you debug your implementation.

    ```
    cd task_3
    python convert_data.py
    ```


### 3. Run the Code and Visualize the Results

- After implementing the conversion, you can run the following command from the `task_3` directory:

    ```
    python run.py
    ```

    This will visualize the processed data. The script includes a built-in data decoder that expects the above custom data structure. If your conversion is correct, the visualization should work and display the output correctly. If there are errors in your conversion, the script will raise an error.

### 4. Check Sample Results

- To better understand the expected output and data structure, refer to the `sample_result/sample_data_structure` file, which shows a correctly implemented data structure. Additionally, view the `sample_result/sample_result.png` to see what the correct visualization output should look like.

### 5. Create the Result Directory
   - Create a result directory with this code:

     ```
     mkdir result
     ```

### 6. Save and Document Your Results

- Save the results of your visualization by clicking the "Download plot as png" button on the visualization webpage (located in the top right corner). Save this file in the `result` directory inside `task_3`.

- Make an empty `data.txt` file in the `result` directory. Copy the terminal output showing your converted data structure and paste it to the `data.txt`.
