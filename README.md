# Cached search
A tool to search the filesystem that caches the location, the cache file might be fairly big if a lot of files are present in the scanned location, this is not ment to be a production ready software! The nominal usage is to map a disk where access is costly (i.e. slow) and avoid accessing it for the searches as much as possible. 

The tool searches for files, not for directories, and does not follow symlinks

Many platforms have a search facility that is both efficient and fast, if yours does, please use it! 

# Usage
The tool is ment to be interactive, but can be used non interactively.

> python main.py [search_root] [search_pattern]

Care that the `search_pattern` MUST match the whole path, if you are not sure of what this means, just wrap your seach pattern in `*`.
To avoid the interaction use the `yes` utility, or its windows alternative

> yes | python main.py [your_root] [your_pattern]

# Examples

Find all files in `C:\\` that have a `.py` extension

> python main.py 'C:\\\\' '\*.py'

Find all files in `/home` that contain `cache`

> python main.py /home '\*cache\*'
