import untrusted_process

def test_untrusted_process_package():
    # Set the osquery path
    osquery_path = r'C:\Program Files\osquery\osqueryi.exe'
    process_analyzer = untrusted_process.UntrustedProcess()
    process_analyzer.setPath(osquery_path)
    #Visualize the results
    process_analyzer.ShowResults()
if __name__ == "__main__":
    test_untrusted_process_package()
