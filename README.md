# Nostalgia
Simple Python Scripts for finding and deleting duplicate images that might be present in a directory.

# Usecase
There are multiple copies of the same kind of files scattered across many directories inside a root directory. This might have happened because one might copy over their images from their phones and then forget that you already have and do it again in a different sub directory.

# How to use
Run `find_duplicates.py` and pass in the directory you want to scan recursively.
```
python3 find_duplicates.py -d /path/to/directory
```

This will generate 
- `image_index.csv` containing the path and the hash of all files in the directory.
- `duplicate_images.csv` containing the path to the two identical files it found.

Now you can run `delete_duplicates.py` which will read the `duplicate_images.csv` and delete all the files specified in the second column.
```
python3 delete_duplicates.py
```

# Warnings and Unexpected behaviour
I am not responsible for any data loss. These scripts were written over the span of a few hours and have not gone through any testing.

Note that this script does not do any checkes for the file types to ensure only images are deleted. While it is trivial to add, I find it less useful. So if you're running this for the whole of your filesystem, it might cause some problems

The script is not designed to handle more than two copies of the same file. While it might be perfectly fine running them, I cannot gurantee it.

PR with features such as multiprocessing support or robustly dealing with more than two copies of the file are welcome.

# Extra scripts
`ui.py` was added to visualise the images after running `find_duplicates.py`. I did not find it useful.

`disk_space.py` was added to check the disk space taken up by different file types. This was to see what percentage of my files were jpeg as opposed to png or even videos.
