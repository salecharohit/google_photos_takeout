# Google Photos Takeout Consolidation

This guide provides a step-by-step process for consolidating photos from multiple Google Photos accounts using a Google Takeout and a Python script to preserve the original photo metadata.

## Steps to Download Your Google Photos

1. Initiate a [Google Takeout](https://takeout.google.com/settings/takeout) from the account you wish to download or move photos from. Select the necessary items and request a takeout.
2. You will receive an email with a link to download your Google Photos archive.
3. After downloading and extracting the archive, your photos will be organized by year within the `Takeout/Google Photos` directory.

## The Problem

When you download photos via Google Takeout, the `created date` is modified, and the original metadata is stored in a separate `.json` file for each image. This can disrupt the chronological order of your photos when re-uploading them to Google Photos.

## The Solution

A Python script, converted from a PowerShell solution provided by [TheOriginalBvF](https://www.reddit.com/user/TheOriginalBvF/) on [Reddit](https://www.reddit.com/r/googlephotos/comments/yjru9e/google_photos_fix_for_downloaded_images_using_the/), can be used to address this issue. The script performs the following functions:

- Traverses directories for unique file extensions, excluding `.json`.
- Collects file extensions and sorts them in descending order.
- Reads the `timestamp` from `.json` files associated with each non-JSON file.
- Converts the `timestamp` to a `datetime` object.
- Updates the last modified time of the original file to match the `timestamp`.
- Moves non-JSON files to the script's current working directory, avoiding duplicates.
- Handles JSON decoding errors and unexpected JSON structures.
- Prints error messages for any issues encountered during processing.

## Disclaimer

- **Backup**: Ensure you take a backup of the entire `Takeout` folder before running the script.
- **Responsibility**: The script is not battle tested and hence the author is not responsible for any data loss that may occur.

## How to Execute

1. Copy the Python script into the `Google Photos` folder within your `Takeout` directory.
2. Run the script using Python 3 by executing the following command in your terminal:

```bash
python3 photos.py
```

## Conclusion

By following these instructions, you can maintain the original metadata of your photos and keep your Google Photos timeline intact when consolidating your accounts.