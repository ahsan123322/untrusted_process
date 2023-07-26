untrusted_process Package

The untrusted_process package is a Python library that allows users to analyze and visualize untrusted processes using osquery. It provides a simple interface to set the osquery path, run the analysis query, and display the results in the form of a pie chart and a table.
Installation

You can install the package via pip:


pip install untrusted_process

Usage

    Import the untrusted_process module and create an instance of the UntrustedProcess class.


import untrusted_process

process_analyzer = untrusted_process.UntrustedProcess()

    Set the osquery path using the setPath method. Make sure to provide the correct path to the osquery executable on your system.



osquery_path = r'C:\Program Files\osquery\osqueryi.exe'
process_analyzer.setPath(osquery_path)

    Run the analysis using the get_results method, which internally runs the osquery command and returns a DataFrame containing the results.


commands = 'SELECT process.pid, process.path, signature.issuer_name, signature.subject_name, signature.result FROM processes as process LEFT JOIN authenticode AS signature ON process.path = signature.path;'
df = process_analyzer.get_results(commands)

    Display the results using the display_pie_chart_and_table method, which shows a pie chart representing the distribution of trusted and untrusted processes and a table containing the paths of each category.


process_analyzer.display_pie_chart_and_table(df)

Example

python

import untrusted_process

# Set the osquery path
osquery_path = r'C:\Program Files\osquery\osqueryi.exe'
process_analyzer = untrusted_process.UntrustedProcess()
process_analyzer.setPath(osquery_path)

# Run the analysis and display the results
commands = 'SELECT process.pid, process.path, signature.issuer_name, signature.subject_name, signature.result FROM processes as process LEFT JOIN authenticode AS signature ON process.path = signature.path;'
df = process_analyzer.get_results(commands)
process_analyzer.display_pie_chart_and_table(df)

Dependencies

The package depends on the following libraries:

    pandas
    matplotlib
    tkinter

These dependencies will be automatically installed during the package installation process.
License

This project is licensed under the MIT License. See the LICENSE file for details.
Contributing

Contributions to the project are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request on the GitHub repository.
Authors

    Ahsan_Ali(misterj503@gmail.com)

Note: Please make sure to replace placeholders like your_username, your_email@example.com, and Your Name with your actual details in the README.md file. Additionally, if you have any additional sections to add or specific instructions for users, feel free to include them in the README as needed.