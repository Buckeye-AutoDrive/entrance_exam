## Task 2: 3D Point Cloud Ground Removal

In this task, you'll work with 3D point cloud data (PCD) to remove the ground portion of the point cloud without using neural network-based methods. You can use any Python modules or algorithms you are familiar with to achieve this.

### Steps to Complete the Task

#### 1. Set Up Your Environment

- Before starting on the task, you need to set up your Python environment and install the necessary dependencies. Follow the instructions below to create and configure your environment using either Conda or a virtual environment (venv).


1. **Create a new Conda environment:**

   ```conda create --name task2 python=3.8```


2. **Activate the environment:**

   ```conda activate task2```


3. **Install the required packages:**

   ```pip install -r requirements.txt```


<br>

#### 2. Understand the Provided Base Code

- The provided base code (`run.py`) handles reading the point cloud data from a `.bin` file and visualizing both the raw and filtered point clouds. It also measures and displays the inference time for the ground removal algorithm.

   ```python run.py```


- There are four data visualizations included: the raw PCD in blue and the filtered (ground removed) PCD in red. Example outputs are available in the `sample_result` directory to help you understand the expected outcome.

<br>

#### 3. Implement Ground Removal

- Locate the `ground_removal.py` file and implement your ground removal algorithm within the `ground_removal` function. Your task is to effectively remove the ground points from the point cloud data.


- You can use any Python modules or algorithms you are comfortable with to achieve this.

<br>

#### 4. Run the Code and Visualize the Results

- After implementing your algorithm, run `run.py` to visualize both the raw and filtered point clouds. The visualization will automatically display the raw PCD in blue and the filtered PCD (with the ground removed) in red.


- If you haven't implemented the ground removal yet, you can still run `run.py` to see the raw PCD.

<br>

#### 5. Measure Inference Time

- The `run.py` script will automatically measure and display the inference time for your ground removal algorithm in the terminal. Ensure that your implementation is efficient.

<br>

#### 6. Save and Document Your Results

- Save the results of your visualization by clicking the "Download plot as png" button on the visualization webpage (located in the top right corner). Save this file in the `result` directory.


- Take a screenshot of the terminal output showing the inference speed and save it in the `result` directory as well.

<br>

#### 7. Submit Your Work  

- Commit your completed work, including your implementation in the `ground_removal.py` file, the saved visualization, the screenshot of the inference speed output, and any relevant documentation to your local repository. Push the changes to your forked repository and create a pull request to submit your work.
