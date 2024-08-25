## Task 2: 3D Point Cloud Ground Removal

In this task, you'll work with 3D point cloud data (PCD) to remove the ground portion of the point cloud without using neural network-based methods. You can use any Python modules or algorithms you are familiar with to achieve this.

### Steps to Complete the Task

#### 1. Understand the Provided Base Code

- The provided base code (`run.py`) handles reading the point cloud data from a `.bin` file and visualizing both the raw and filtered point clouds. It also measures and displays the inference time for the ground removal algorithm.

  To run the script, navigate to the `task_2` directory and execute the script:
  
  ```
  cd task_2  
  python run.py
  ```

  This ensures that the script can correctly access all necessary data and resources within the `task_2` directory.

- There are four data visualizations included: the raw PCD in blue and the filtered (ground removed) PCD in red. Example outputs are available in the `sample_result` directory within `task_2` to help you understand the expected outcome.

#### 2. Implement Ground Removal

- Locate the `ground_removal.py` file inside the `task_2` directory and implement your ground removal algorithm within the `ground_removal` function. Your task is to effectively remove the ground points from the point cloud data.

- You can use any Python modules or algorithms you are comfortable with to achieve this.

#### 3. Run the Code and Visualize the Results

- After implementing your algorithm, run the following command from the `task_2` directory:

  ```
  python run.py
  ```
  
  This will visualize both the raw and filtered point clouds. The visualization will automatically display the raw PCD in blue and the filtered PCD (with the ground removed) in red.

- If you haven't implemented the ground removal yet, you can still run `run.py` to see the raw PCD.

#### 4. Measure Inference Time

- The `run.py` script will automatically measure and display the inference time for your ground removal algorithm in the terminal. Ensure that your implementation is efficient.

#### 5. Create the Result Directory
   - Create a result directory with this code:

     ```
     mkdir result
     ```

#### 6. Save and Document Your Results

- Save the results of your visualization by clicking the "Download plot as png" button on the visualization webpage (located in the top right corner). Save this file in the `result` directory inside `task_2`.

- Take a screenshot of the terminal output showing the inference speed and save it in the `result` directory as well.

 
