import os
import shutil

# The directory that contains your test suites
test_suites_dir = './_projekt/'

# Get the list of test suite files in the directory
test_suite_files = [f for f in os.listdir(test_suites_dir) if f.endswith('.robot')]

# For each test suite file...
for test_suite_file in test_suite_files:
    # Get the name of the test suite without the .robot extension
    test_suite_name = os.path.splitext(test_suite_file)[0]
    # Create a new directory with the same name as the test suite
    new_dir = os.path.join(test_suites_dir, test_suite_name)
    os.makedirs(new_dir, exist_ok=True)
    # Move the test suite file to the new directory
    shutil.move(os.path.join(test_suites_dir, test_suite_file), os.path.join(new_dir, test_suite_file))