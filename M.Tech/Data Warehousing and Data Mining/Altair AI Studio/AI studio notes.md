 # Altair AI Studio Rapid Miner  

## Part 1 Intro to the RapidMiner Studio GUI 

### Overview of RapidMiner Studio GUI
- RapidMiner Studio offers two primary views:
  - **Design View** for building analytics processes
  - **Results View** for inspecting results after execution.
- **Process Panel** (center of Design View) is where users construct processes by connecting operators—modular building blocks for tasks like data loading, cleansing, and modeling.

### Key Interface Elements
- **Operators Panel** (bottom left):
  - Organizes operators into categories (e.g., Data Access, Blending, Cleansing, Modeling), each containing specialized functions for data science tasks.
  - To add an operator, expand the relevant category, drag, and drop into the process panel; searching by name is available for quick access.
- **Parameters Panel** (top right):
  - Shows adjustable settings for the selected operator (such as specifying a data source).
  - Ports like "out" are used to connect operator outputs to the results panel.

### Running and Viewing Results
- Running a process executes the workflow and opens the **Results View**, displaying data tables and options for deeper analysis (statistics, visualizations, annotations).
  - "Attributes" refer to columns and "Examples" to rows in RapidMiner terminology.

### Layout and Panels
- Resize and relocate panels by dragging boundaries or tabs;
  - closing panels is reversible using the View menu's "Show Panel" option.
- Default layout can be restored from the View menu if panels are misplaced or accidentally closed.

### Repository Management
- **Repository Panel** (top left): Used to organize datasets and process files.
- Best practice: Create two folders (“data” and “processes”) in each repository to keep files organized.
- Use the drop-down to create repositories and subfolders.[1]

### Global Search and Help
- Global search function locates processes, extensions, operators, and related actions across the interface.[1]
- **Help Panel** (lower right): Provides documentation and tutorials for each operator, often with sample processes for hands-on learning.

### Summary

- RapidMiner Studio’s interface is designed to support easy data preparation, modeling, and process management, with accessible help and flexible layout customization for efficient workflow.

[Intro to the RapidMiner Studio GUI](https://youtu.be/Gg01mmR3j-g)

***

## Part 2 Introduction to Turbo Prep | RapidMiner

### What is Turbo Prep?
- Turbo Prep in RapidMiner streamlines data preparation tasks such as extraction, transformation, and loading (ETL), reducing manual effort.[1]
- Integrates seamlessly with RapidMiner's Auto Model, allowing for a smooth flow from data preparation to model building.[1]

### Getting Started with Turbo Prep
- Access Turbo Prep from the Views menu in RapidMiner Studio.[1]
- Load data by clicking "Load Data" or the text prompt:
  - Choose from recently used datasets, import new data from the local computer, network drive, or database, or access data via the RapidMiner Repository.[1]
  - Repository functions like a local data folder and can connect to RapidMiner Server or external databases.[1]

### Core Functions in Turbo Prep
- Once data is loaded, transformation options are activated: **Transform**, **Cleanse**, **Generate**, etc..
- Actions are grouped for structured data prep—perform and repeat different actions during the session.
- Example 1: Renaming a column
  - Select the column and transformation, rename (e.g., "sex" to "gender"), and apply; preview updates instantly.
- Example 2: Generating a new column
  - Use the Generate group to create features (e.g., family size as siblings + parents + 1); preview shows the new attribute immediately.

### Process Tracking and Integration
- Turbo Prep tracks and displays session history; previous steps can be rolled back or branched for separate data prep processes.
- All actions in Turbo Prep are transparent and can be exported as a process to RapidMiner's Design View, where operators can be further examined and edited.
- Changes made in the Design View process don't sync back to Turbo Prep unless the process is run directly in the Design View.

### Data Exploration Tools
- Table View presents data with histograms over attributes for quick visualization of distributions.[1]
- Quality indicators under histograms help assess data issues:
  - Red: Missing/infinite values
  - Light Blue: Identities
  - Gray: Stability
  - Green: Valid values
- Right-click for transformation, cleansing, or sorting on columns—sorting affects view only unless committed as a transformation.
- Show column details for stats, histogram, format, and quality breakdowns.

### Transition to Modeling
- Use prepped data instantly in Auto Model by taking a snapshot—no need to save first unless desired.
- Quick demonstration: Generating a decision tree model using the enriched feature (e.g., family size) and observing its impact on model criteria (feature importance, decision paths).

### Key Data Science Concepts Highlighted
- Feature generation: Creating new columns for meaningful model input.
- Feature selection: Choosing optimal input columns; together with generation, forms feature engineering.

Turbo Prep makes ETL, feature engineering, and transition to model building user-friendly and efficient within RapidMiner Studio.

[1](https://www.youtube.com/watch?v=BZRVJMUk4nE)

***

## Part 3 RapidMiner: Importing Excel Data

### 1. Find and Add Read Excel Operator
- Use the search bar to type "Read Excel" and drag the operator into the process panel.

### 2. Configure Excel Import
- Start the Import Configuration Wizard:
    - Select the desired Excel file.
    - Choose the sheet containing your data.
    - Set cell range to skip unwanted rows (e.g., section headers).
    - Adjust header settings for correct column naming.
    - Exclude columns not needed; rename or change data type/role as necessary.
    - Example: Set the “churn” column’s role to Label.

### 3. Run the Process
- Connect the output port to the results port in the process panel.
- Click the Run Process button to load the data into RapidMiner.
    - If the data fails to load, ensure all ports are properly connected.

### 4. Understand Data Loading vs. Importing
- Data is loaded into RAM and available for project usage.
- The source file must stay in its original location; deleting or moving it causes failures.
- To avoid dependency, use the Store operator to save the loaded data into the RapidMiner repository.

### 5. Save Your Process
- Save the workflow by:
    - Using File > Save Process, select folder and name.
    - Or right-click repository folder and select Store Process Here for faster saving.

### 6. Store Data in Repository
- Use the *Store operator* to save the imported data file in a chosen repository folder.
- Define operator parameters, set filename and folder destination.

### 7. Exporting and Importing Processes
- Export: Select process, go to File > Export Process, and choose folder/name (.RMP file).
- Import: Clean the panel, File > Import Process, and select .RMP file. Review settings (especially path references).
- Store imported processes in the repository for easy management.

### 8. Repository Maintenance
- To delete a process or folder: right-click the item and choose Delete.
- Note: Deleting a repository only removes the reference in RapidMiner, not the actual files. Remove files manually from the filesystem if needed.

***

### Data Import Behavior

- **Importing and storing data** in the repository generates a local, static copy of the data set.
    - Any changes to the original file do not update the stored copy in RapidMiner.
    - This method is suitable for archival or repeatable analysis with unchanging data.

- **Using the Read Excel operator** creates a live connection to the source Excel file.
    - Each time the process is run, RapidMiner loads the most current data directly from the file.
    - Changes in the source Excel spreadsheet are immediately reflected in RapidMiner without needing to re-import or update the repository copy.

### Summary Table

| Method                   | Dynamic/Static | Data Update Behavior                                     |
|--------------------------|---------------|---------------------------------------------------------|
| Import and Store         | Static        | No automatic updates from Excel; snapshot only  |
| Read Excel operator      | Dynamic       | Always reflects current file contents; live link   |

Selecting between these methods allows flexibility between stable project archiving and real-time analysis with constantly updated data.[1]

