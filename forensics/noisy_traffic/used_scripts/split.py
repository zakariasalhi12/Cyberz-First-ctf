# split_png.py
def split_png(image_path, num_chunks=10):
    with open(image_path, "rb") as img_file:
        image_data = img_file.read()

    # Calculate the chunk size
    chunk_size = len(image_data) // num_chunks

    # Create the chunks
    chunks = [image_data[i:i + chunk_size] for i in range(0, len(image_data), chunk_size)]

    # If there's leftover data, add it to the last chunk
    leftover = len(image_data) % num_chunks
    if leftover:
        chunks[-1] += image_data[-leftover:]

    # Save each chunk to a separate file
    for i, chunk in enumerate(chunks):
        with open(f"part_{i+1:02d}.bin", "wb") as chunk_file:
            chunk_file.write(chunk)

    print(f"[+] Split into {len(chunks)} parts.")

split_png("image.png")
