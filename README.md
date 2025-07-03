
# Coated Converter

This is a simple Python script to convert Zemax `.txt` files with angle of incidence data into SPEOS-compatible `.coated` format.

---

## ⚙️ Preparing your input files

Converter based on Zemax `.txt` files.  
Create several files in Zemax (**Analyze → Coatings → Reflection vs Wavelength**) for the desired angles of incidence.  
Save these files with names like:  
```
Transm_angle*.txt
```
where `*` is the angle of incidence to the coated surface (e.g., `Transm_angle10.txt`, `Transm_angle20.txt`).

---

## 📥 How to use

1. Place your `.txt` files into the `data` folder.  
   The script will automatically find all files matching:  
   ```
   Transm_angle*.txt
   ```

2. Run the script:
   - Open a terminal in the project folder.
   - Execute:
     ```bash
     python main.py
     ```

   Or simply double-click on `main.py` (if Python is installed).

3. After the script runs, a file called `output.coated` will be created in the project folder.

---

## 📦 Folder structure

```
coated_converter/
├── main.py          # Main script to run
├── utils.py         # Helper function to parse .txt files
├── data/            # Put your .txt files here
├── README.md         # This file
```

---

## ⚠️ Requirements

- Python 3.8+
- No external libraries required (only uses built-in Python modules)

---

## 📝 Example

If your folder looks like this:
```
coated_converter/
├── data/
│   ├── Transm_angle10.txt
│   ├── Transm_angle20.txt
```

Run:
```bash
python main.py
```

Result:
```
Finish. File saved as output.coated
```
