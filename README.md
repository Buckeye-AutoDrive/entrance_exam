# Entrance Exam
Autodrive Challenge Year 4 Perception Entrance Exam

Welcome to the Autodrive Challenge Year 4 Perception Entrance Exam. This exam is designed to assess your fundamental problem-solving skills in areas critical to our team's success. You have the option to choose from three different tasks, each focusing on a specific aspect of perception: 2D image detection, 3D lidar data processing, and visualization skills. You are encouraged to use all available resources to complete the tasks to the best of your ability. The deadline for submission is **September 4, 11:59 PM**.

## Repository Overview

This repository contains everything you need to complete the entrance exam. The exam is structured into three distinct tasks, each within its own directory:

- **Task 1: 2D Image Detection**
- **Task 2: 3D Point Cloud Ground Removal**
- **Task 3: Visualization Skills**

You can choose to complete one or more of these tasks based on your interests and expertise. Each task has its own README file with specific instructions.

## Environment Setup

Before you begin working on any of the tasks, you'll need to set up your Python environment. This ensures that you have all the necessary dependencies to run the provided code and complete the tasks.

### IDE Setup

We primarily use **PyCharm** or **Visual Studio Code (VSC)** for development. However, if you have a different IDE preference, feel free to use it. Follow these steps to get started:

1. **Open the Repository in Your IDE:**
   - Clone the repository and open it in your preferred IDE.

2. **Set Up Your Python Environment:**
   - Open the terminal in your IDE.
   - Copy and paste each line from the environment setup instructions below into your IDE's terminal, running them one by one to ensure proper setup.

### Using Conda

#### Why Use Conda?

Conda allows you to manage dependencies and create isolated environments for different projects. This helps avoid conflicts between projects and ensures that your work environment is consistent with what is expected for this exam.

#### 1. Installing Miniconda

To get started, you'll need to install Miniconda. Follow these steps:

1. Visit the [Miniconda installation page](https://docs.conda.io/en/latest/miniconda.html).
2. Download the installer for your operating system (Windows, macOS, or Linux).
3. Follow the instructions provided on the website to install Miniconda on your system.

#### 2. Setting Up the Environment with Conda

1. **Create and configure the environment using the provided `environment.yml` file:**

    <br>

   `conda env create -f environment.yml`

    <br>
   
    This command will create a new environment named `entrance_exam` with all the necessary dependencies.


2. **Activate the environment:**

    <br>
   
   `conda activate entrance_exam`
   
    <br>
   
   Activating the environment ensures that all subsequent work is done within this isolated environment.

## Submitting Your Work

After completing your selected tasks, follow the instructions below to submit your work:

1. **Prepare Your Files for Submission:**
   - For each task you complete, compress the corresponding task directory into a ZIP file. For example, if you completed Task 2, zip the entire `task_2` directory.
   - If you worked on multiple tasks, zip each task separately.


2. **Submit Your Files:**
   - Submit your zipped files through the provided Google Form link. Ensure that all necessary files, such as code implementations, screenshots, and any other requested documentation, are included.

## Important Notes

- Make sure to thoroughly test your code before submission.
- Incomplete or improperly submitted tasks may not be considered.
- Refer to the individual task READMEs for specific instructions related to each task.

Good luck, and we look forward to reviewing your submission!
