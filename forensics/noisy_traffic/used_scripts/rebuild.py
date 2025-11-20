# rebuild_png.py
import glob

output_file = "reconstructed_image.png"  # Name of the final image
part_files = sorted(glob.glob("part_*.bin"))  # Find all the part files

# Rebuild the image
with open(output_file, "wb") as out:
    for part in part_files:
        with open(part, "rb") as f:
            out.write(f.read())

print(f"[+] Rebuilt {output_file} from {len(part_files)} parts.")
