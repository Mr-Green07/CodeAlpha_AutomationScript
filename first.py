import os
import shutil

def organize_jpg_files(source_folder, destination_folder):
 
    print(f"--- Starting JPG File Organizer ---")
    print(f"Source Folder: {source_folder}")
    print(f"Destination Folder: {destination_folder}")

    # 1. Create the destination folder if it doesn't exist
    try:
        os.makedirs(destination_folder, exist_ok=True)
        print(f"Ensured destination folder exists: '{destination_folder}'")
    except OSError as e:
        print(f"Error creating destination folder '{destination_folder}': {e}")
        return # Exit if we can't create the destination folder

    moved_count = 0
    skipped_count = 0

    # 2. Iterate through all items in the source folder
    try:
        for filename in os.listdir(source_folder):
            source_path = os.path.join(source_folder, filename)

            # Check if it's a file and if it's a .jpg or .jpeg
            if os.path.isfile(source_path) and filename.lower().endswith(('.jpg', '.jpeg')):
                destination_path = os.path.join(destination_folder, filename)

                # 3. Move the file
                try:
                    shutil.move(source_path, destination_path)
                    print(f"Moved: '{filename}' to '{destination_folder}'")
                    moved_count += 1
                except shutil.Error as e:
                    print(f"Error moving '{filename}': {e}")
                    skipped_count += 1
                except Exception as e:
                    print(f"An unexpected error occurred while moving '{filename}': {e}")
                    skipped_count += 1
            else:
                # Optionally, you can print what files are being skipped
                # print(f"Skipped: '{filename}' (not a .jpg/.jpeg file)")
                pass # Do nothing for non-JPG/JPEG files
    except FileNotFoundError:
        print(f"Error: Source folder '{source_folder}' not found.")
        return
    except Exception as e:
        print(f"An unexpected error occurred while processing folder: {e}")
        return

    print(f"\n--- Automation Complete ---")
    print(f"Summary:")
    print(f"  Files Moved: {moved_count}")
    print(f"  Files Skipped/Errors: {skipped_count}")
    print(f"---------------------------")

# --- How to Use ---
if __name__ == "__main__":
    
    # Example 1: Relative paths (good for testing in the same directory as script)
    # Make sure 'my_test_source_folder' exists and has some .jpg files
    # and 'my_organized_pictures' will be created/used as destination.
    # source = "my_test_source_folder"
    # destination = "my_organized_pictures"

   
    source = "E:/Student/GLOBAL/CodeAlpha_AutomationScript/one" 
    destination = "E:/Student/GLOBAL/CodeAlpha_AutomationScript/organized_files" 

    # A quick check for a placeholder username if it's left as is
    if "YourUsername" in source or "YourUsername" in destination:
        print("Example: source = 'C:\\Users\\JohnDoe\\Downloads'")
        print("         destination = 'C:\\Users\\JohnDoe\\Pictures\\My_Organized_Photos'")
        print("Exiting without running to prevent errors.")
    else:
        organize_jpg_files(source, destination)