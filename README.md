# Lunch Menu Fetcher

## Overview
The Lunch Menu Fetcher is a Python tool designed to automate the extraction of lunch menu information from a specified URL and export this data into a well-organized Excel file. This project aims to simplify the process of collecting weekly lunch menu offerings from Fleischerei Huerner which publishes their menu online.

## Features
- **URL-based Menu Extraction:** Allows users to specify the URL of the web page containing the lunch menu.
- **Data Parsing:** Utilizes BeautifulSoup to parse HTML content and extract relevant menu data.
- **Excel Export:** Organizes the fetched menu data into a structured Excel file, with automatic adjustment of column widths based on content.
- **Timestamped Output:** Names the output Excel file with a timestamp, ensuring that each data extraction is uniquely identified.

## Requirements for compiling
- Python 3.x
- Libraries: `requests`, `pandas`, `openpyxl`, `beautifulsoup4`
- To generate a Windows executable you will also need `pyinstaller`
  - Install the required libraries using pip:
    ```sh
    pip install requests pandas openpyxl beautifulsoup4
    ```
## Usage with Windows executable
1. Download executable from dist folder or generate it yourself after setting up the environment by running generateExe.bat
2. Run it either with no arguments and it is going to use the defaults or use the following arguments to specify the behaviour.

### Command-Line Arguments
- `-if` or `--inputFile`: Specifies the URL to the page containing the lunch menu. If not provided, defaults to `https://www.fleischerei-huerner.at/regionales_mittagsmenue/`.
- `-of` or `--outputFile`: Specifies the location and name of the output Excel file without the extension (e.g., `path/to/weekly_lunch_menu`). If not provided, defaults to creating a `weekly_lunch_menu.xlsx` file in the current directory with a timestamp.

### Example
To fetch the lunch menu from Fleischerei Huerner and save it to `C:\temp\this_week_menu.xlsx`, run:
```sh
main.exe --inputFile https://www.fleischerei-huerner.at/regionales_mittagsmenue/ --outputFile C:\temp\this-week-menu
````

## Usage with python code
1. Clone this repository to your local machine.
2. Navigate to the cloned directory in your terminal or command prompt.
3. Run the script using Python and pass the target URL as an argument:
   ```sh
   python main.py -if https://www.fleischerei-huerner.at/regionales_mittagsmenue/ -of C:\temp\this-week-menu
   ```
