import nbformat as nbf

# List of your notebook filenames
notebook_filenames = ["figure6_Neuropixels.ipynb", "figure7_longtermMyelin.ipynb"]

# Loop through each filename in the list
for filename in notebook_filenames:
    try:
        # Load the notebook
        ntbk = nbf.read(filename, nbf.NO_CONVERT)

        # Iterate through cells and add the tag
        count = 0
        for cell in ntbk.cells:
            if cell.cell_type == 'code':
                # Get existing tags or create new list
                tags = cell.metadata.get('tags', [])

                # Add 'hide-input' if not present
                if 'hide-input' not in tags:
                    tags.append('hide-input')
                    cell.metadata['tags'] = tags
                    count += 1

        # Save the notebook
        nbf.write(ntbk, filename)
        print(f"Success: Added 'hide-input' tag to {count} cells in {filename}.")
        
    except FileNotFoundError:
        print(f"Error: Could not find {filename}. skipping...")
