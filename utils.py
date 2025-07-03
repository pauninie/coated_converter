
def parse_incident_file(filepath):
    """
    Parses a file and returns a list of wavelengths and their corresponding S-reflection, R-reflection, S-transmittance, R-transmittance
    """
    with open(filepath, 'r', encoding='utf-16', errors='ignore') as file:
        lines = file.readlines()

    angles = []
    angle_data = {}
    idx = 0

    while idx < len(lines):
        if 'Angle of Incidence' in lines[idx]: #read angle value of .txt file
            angle = float(lines[idx].split(':')[1])
            idx += 1

            # Skip lines until the header row
            idx += next(
                (offset for offset, line in enumerate(lines[idx:], start=1)
                 if line.strip().startswith('Wavelength')),
                0
            )

            # Collect data rows
            rows = []
            for row_line in lines[idx + 1:]:
                parts = row_line.split()
                if len(parts) < 5:
                    break
                try:
                    wl, s_ref, p_ref, s_tr, p_tr = map(float, parts[:5])
                    rows.append((wl, s_ref, p_ref, s_tr, p_tr))
                except ValueError:
                    break
            angles.append(angle)
            angle_data[angle] = rows

        idx += 1

    return angles, angle_data
