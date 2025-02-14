import logger as logger
import os
from pathlib import Path

def get_logger(print_to_screen = False):
    """
    Uses the logger.py module to create a logger

    Args:
        print_to_screen: for printing to screen as well as file
    """

    return logger.initialize_logger(print_to_screen)


def get_renamed_file_path(existing_name, string_to_find, string_to_replace, 
                          prefix, suffix):
    """
    Returns the target file path given an existing file name and 
    string operations

    Args:
        existing_name: the existing file's name
        string_to_find: a string to find and replace in the existing filename
        string_to_replace: the string you'd like to replace it with
        prefix: a string to insert at the beginning of the file path
        suffix: a string to append to the end of the file path
    """

    '''
    REMINDERS

    This function should only take in strings and return a string.  
    No file renaming/copying/moving should happen here

    Make sure to support string_to_find being an array of multiple strings!  
        Hint: you may need to check its type...
    '''
    pass

def get_files_with_extension(folder_path, extension):

    logger = get_logger(True)

    #making sure the folder exists first
    if os.path.isdir(folder_path) == False:
        logger.error("Folder path does not exist")
        return

    logger.info("Getting files with extension: " + extension + " in folder: " + folder_path)

    #getting all files in the folder
    folder_files = next(os.walk(folder_path))[2]

    #list to store all the files with the correct extension
    matching_files = []

    #iterating through all the files in the folder
    for file in folder_files:
        print("working on file: " + file)
        
        # Remove the dot from the extension
        file_extension = os.path.splitext(file)[1][1:]  
        print("file extension string only: " + file_extension)
        if (file_extension == extension):
            matching_files.append(file)
            logger.info("added a matching file: " + file)

    return matching_files
    """
    Returns a collection of files in a given folder with an extension that 
    matches the provided extension

    Args:
        folder_path: The path of the folder whose files you'd like to search
        extension: The extension of files you'd like to include in the return
    """

    '''
    REMINDERS

    This function should only take in strings and return an array
    No file renaming/copying/moving should happen here

    Make sure to catch and handle errors if the folder doesn't exist!
    '''
    pass

def rename_file(logger, existing_name, new_name, copy=False):
    """
    Renames a file if it exists
    By default, should move the file from its original path to its new path--
    removing the old file
    If copy is set to True, duplicate the file to the new path

    Args:
        logger: logger instance
        existing_name: full filepath a file that should already exist
        new_name: full filepath for new name
        copy_mode: copy instead of rename
    """

    '''
    REMINDERS

    Copy files using shutil.copy
    make sure to import it at the top of the file
    '''
    pass

def rename_files_in_folder(logger, folder_path, extension, string_to_find,
                           string_to_replace, prefix, suffix, copy=False):
    """
    Renames all files in a folder with a given extension
    This should operate only on files with the provided extension
    Every instance of string_to_find in the filepath should be replaced
    with string_to_replace
    Prefix should be added to the front of the file name
    Suffix should be added to the end of the file name

    Args:
        logger: logger instance
        folder_path: the path to the folder the renamed files are in
        extension: the extension of the files you'd like renamed
        string_to_find: the string in the filename you'd like to replace
        string_to_replace: the string you'd like to replace it with
        prefix: a string to insert at the beginning of the file path
        suffix: a string to append to the end of the file path
        copy: whether to rename/move the file or duplicate/copy it
    """

    '''
    REMINDERS
    #
    This function should:
        - Find all files in a folder that use a certain extension
            - Use get_files_with_extension for this
        - *For each* file...
            - Determine its new file path
                - Use get_renamed_file_path for this
            - Rename or copy the file to the new path
                - Use rename_file for this
        - Use the logger instance to document the process of the program
    '''
    pass


def main():
    # Logger
    logger = get_logger(True)
    logger.info('Logger Initiated')

    #   Here are some examples of different logger messages
    
    #logger.warning('This would be a logger warning')
    #logger.error('This would be a logger error!!')
    #logger.critical('This would be a critical log')

    #get_files_with_extension("testing_files", "ma")
    print(get_files_with_extension("testing_files", "ma"))
    print(get_files_with_extension("testing_filess", "ma"))
if __name__ == '__main__':
    main()
