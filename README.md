# Simplify Your VCF Contacts with vcf-filter-app — Only Names and Phone Numbers Retained!

The VCF Filter App is a web-based application designed to clean VCF (vCard) files by filtering out all entries except for those containing phone numbers. It also removes any attached photos from the contacts, ensuring that the output file contains only essential information

For a pure python experience check out [python_executable.py](CONTRIBUTING.md)

## Features

- **Upload VCF Files**: Users can upload their VCF files directly through the web interface.
- **Clean and Download**: After processing, users can download the cleaned VCF file, which includes only the contacts with phone numbers.

## Technology Stack

- **Flask**: A lightweight WSGI web application framework used to serve the web interface and handle file uploads and downloads.
- **Python**: The back-end processing of VCF files is handled by Python scripts.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You need Python 3.x installed on your system. If you do not have Python installed, you can download it from [python.org](https://www.python.org/downloads/).

### Installing

First, clone the repository to your local machine:

```bash
git clone https://github.com/WilCF/vcf-filter-app.git
```

Navigate to the project directory:

```bash
cd vcf-filter-app
```

Install the required packages:

```bash
pip install -r requirements.txt
```

### Running the Application

Run the Flask application with the following command:

```bash
python vcf_filter.py
```

The server will start, and you can access the application in your web browser at:

```
http://localhost:5000
```

## Usage

1. **Upload a VCF File**: Click the "Upload and Clean" button to select a VCF file from your computer.
2. **Download the Cleaned VCF File**: After the file processes, a download button will appear allowing you to save the cleaned VCF file to your device.

## Deployment

This application can be deployed on platforms like Heroku. For detailed instructions on how to deploy Flask applications on Heroku, please refer to [Heroku's official documentation](https://devcenter.heroku.com/articles/getting-started-with-python).


## License

This project is licensed under the MIT License 
