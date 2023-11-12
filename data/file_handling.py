# File handling

'''
Python can open simple files (ex. '.txt' files) without any external modules. However,
by importing specific external modules, nearly all files can be opened. This will be
covered later in the 'modules' folder.
'''

# There are two ways to open a file...

# Manually open and close a file:
# `open()` is the function to open the file - it takes the path to the file and the mode as arguments
file = open('data/test_files/test.txt', 'r')

'''
Here are the modes and what they mean when opening a file.

'r' (read): it opens the file for reading. The file pointer is placed at the beginning of the file. If the file does 
            not exist, it raises a `FileNotFoundError` exception.

'w' (write): Opens the file for writing. If the file already exists, it truncates the file to zero length.
             If the file does not exist, it creates a new file. Be cautious, as this mode will overwrite the existing content.

'a' (append): Opens the file for writing. If the file already exists, the file pointer is at the end of the file. If the file 
              does not exist, it creates a new file.

'b' (binary): Used in conjunction with other modes (e.g., 'rb' or 'wb') to specify binary mode. It is important when working 
              with non-text files, like images or executables.

'x' (exclusive creation): Creates the file, but if the file already exists, the FileExistsError is raised.

'+' (read and write): Opens the file for both reading and writing. The file pointer is placed at the beginning of the file.
'''

# If test.txt was already in the same folder, it can be opened with 'test.txt' instead of 'data/test_files/test.txt'

# Printing the file will print data about the file, not the contents inside of the file
print(file) # Output: <_io.TextIOWrapper name='data/test_files/test.txt' mode='r' encoding='UTF-8'>

# Converting it to a list will show the contents of the file as a list
print(list(file)) # Output: ['This is a basic text file. Not much to this file in particular!\n']

# Once the file is opened through this method, it will need to be closed manually
file.close()

# Most of the time, files should be opened and closed automatically using the `with` keyword:
with open('data/test_files/test.txt', 'r') as text_file:
  # Instead of converting the file to a list, files should be read with the `read()` method
  # `read()` returns a string with the file's content
  print(text_file.read()) # Output: This is a basic text file. Not much to this file in particular!

# Example of appending to a file (`a+` so that the file can be appended to and read from)
with open('data/test_files/test.txt', 'a+') as og_file:
  # Use the `write()` method to write to the file
  og_file.write('\nXXXXX MORE TEXT HERE XXXXX')
  
  # After appending the extra text, the pointer will be at the end of the file.
  # This means that reading the file from this point will print out nothing.
  # To fix this, set the pointer back to the beginning of the file
  og_file.seek(0)
  
  # Now, read and print the content of the file
  print(og_file.read())
  '''
  Output:
  
  This is a basic text file. Not much to this file in particular!
  XXXXX MORE TEXT HERE XXXXX
  '''

# Other modes are used very similarly so experiment with the modes to see how they work.
# This file will not go over the rest to keep everything down to the basics.
