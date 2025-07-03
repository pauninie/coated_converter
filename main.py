
from utils import parse_incident_file


def generate_coated_file(input_folder, output_file):
    """
    Reads Zemax .txt files and converts them to .coated format for SPEOS.
    """
    import glob
    import os

    input_pattern = os.path.join(input_folder, "Transm_angle*.txt")
    files = glob.glob(input_pattern)

    angle_data_map = {}
    all_angles = set()
    all_wavelengths = set()

    for filepath in files:
        angles, data = parse_incident_file(filepath)
        for angle in angles:
            if angle not in angle_data_map:
                angle_data_map[angle] = data[angle]
                all_angles.add(angle)
                all_wavelengths.update(row[0] for row in data[angle])

    sorted_angles = sorted(all_angles)
    sorted_wavelengths = sorted(all_wavelengths)

    with open(output_file, 'w') as f:
        f.write("COATED_FORMAT\n\n")
        f.write(f"{len(sorted_angles)} {len(sorted_wavelengths)}\n")
        f.write("\t" + "\t".join(f"{wl * 1000:.1f}" for wl in sorted_wavelengths) + "\n")

        for angle in sorted_angles:
            rows = {row[0]: row for row in angle_data_map[angle]}
            p_row = "\t".join(
                f"{round(rows[wl][2] * 100, 2):.2f}\t{round(rows[wl][4] * 100, 2):.2f}"
                for wl in sorted_wavelengths if wl in rows
            )
            s_row = "\t".join(
                f"{round(rows[wl][1] * 100, 2):.2f}\t{round(rows[wl][3] * 100, 2):.2f}"
                for wl in sorted_wavelengths if wl in rows
            )
            f.write(f"{angle}\t{p_row}\n\t{s_row}\n")


if __name__ == "__main__":
    input_folder = "data"  # Folder with your txt files
    output_file = "output.coated"
    generate_coated_file(input_folder, output_file)
    print(f"Finish. File saved as {output_file}")
