import logger as logger
import os
import shutil
import collections.abc as collections

def get_logger(print_to_screen = False):
    """
    Uses the logger.py module to create a logger

    Args:
        print_to_screen: for printing to screen as well as file
    """

    return logger.initialize_logger(print_to_screen)


def get_renamed_file_path(logger, existing_name, string_to_find, 
                          string_to_replace, prefix, suffix):
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

    logger.info("Getting renamed file path for: " + existing_name)
    
    # Making string_to_find a list if it isn't already
    if not isinstance(string_to_find, collections.Collection) or isinstance(
        string_to_find, str):
        string_to_find = [string_to_find]

    if not string_to_find:
        logger.warning("string_to_find is empty. No replacements.")

    logger.info("number of strings to replace: " + str(len(string_to_find)))

    # Split the existing name into base name and extension
    base_name, extension = os.path.splitext(existing_name)

    # Replacing all strings in string_to_find with string_to_replace
    for find_str in string_to_find:
        logger.debug(f"Replacing '{find_str}' with '{string_to_replace}' in '
                     {base_name}'")
        base_name = base_name.replace(find_str, string_to_replace)

    # Adding prefix and suffix
    new_name = prefix + base_name + suffix + extension
    logger.debug(f"Adding prefix '{prefix}' and suffix '{suffix}' to '
                 {new_name}'")

    return new_name

def get_files_with_extension(logger, folder_path, extension):
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

    # Making sure the folder exists first
    if not os.path.isdir(folder_path):
        logger.error("Folder path does not exist")
        return []
    
    logger.info("Getting files with extension: " + extension + " in folder: " 
                + folder_path)

    # Getting all files in the folder
    folder_files = next(os.walk(folder_path))[2]

    # List to store all the files with the correct extension
    matching_files = []

    # Iterating through all the files in the folder
    for file in folder_files:
        logger.debug("Working on file: " + file)
        
        # Remove the dot from the extension
        file_extension = os.path.splitext(file)[1][1:]  
        logger.debug("File extension string only: " + file_extension)

        if file_extension == extension:
            matching_files.append(file)
            logger.info("Added a matching file: " + file)

    if not matching_files:
        logger.warning(f"No files found with extension: {extension}")

    return matching_files

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
    if not os.path.exists(existing_name):
        logger.warning(f"File {existing_name} does not exist. Skipping.")
        return

    try:
        if copy:
            shutil.copy(existing_name, new_name)
            logger.info(f"Copied file from {existing_name} to {new_name}")
        else:
            os.rename(existing_name, new_name)
            logger.info(f"Renamed file from {existing_name} to {new_name}")
    except Exception as e:
        logger.error(f"Failed to rename/copy file from {existing_name} to 
                     {new_name}: {e}")

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
    matching_files = get_files_with_extension(logger, folder_path, extension)
    for file in matching_files:
        existing_name = os.path.join(folder_path, file)
        new_name = get_renamed_file_path(logger, file, string_to_find, 
                                         string_to_replace, prefix, suffix)
        new_name = os.path.join(folder_path, new_name)
        logger.debug(f"Renaming file from {existing_name} to {new_name}")
        rename_file(logger, existing_name, new_name, copy)


def main():
    # Logger
    logger = get_logger(True)
    logger.info('Logger Initiated')               

if __name__ == '__main__':
    main()
