# 🔐 pyEnigma

A Python-based simulator of the **Enigma cipher machine**, faithfully replicating the classic WWII encryption device used by the Germans. This project is inspired by historical cryptographic machinery and is intended for educational and demonstration purposes.

---

## 🛠️ Features

- Simulates a 3-rotor Enigma machine with a plugboard and reflector.
- Accurate rotor stepping and double-stepping behavior.
- Supports custom rotor settings, plugboard configurations, and ring settings.
- Python 3 compatible (with fallback for Python 2).

---

## 🧠 How It Works

The simulator takes a message as input and processes each character through:

1. A **plugboard** (substitution cipher).
2. Three **rotors** (with individual wiring and notch mechanics).
3. A **reflector** (bounces signal back).
4. Then reverses the path back through the rotors and plugboard.

Each rotor advances in a sequence mimicking the historical Enigma machine's mechanics, including turnover and double-stepping.

---

## 📦 Requirements

- Python 3.x (Python 2.x fallback is included via `maketrans`)
- `rotor.py` module (must define `Rotor` and `Reflector` classes used in `Enigma`)

---

## 🚀 Getting Started

Clone the repository and ensure `rotor.py` is in the same directory as `enigma.py`.

```bash
git clone https://github.com/yourusername/pyEnigma.git
cd pyEnigma
```

---

### 🚀 Example Usage

Make sure you have both `enigma.py` and `rotor.py` in the same directory. Here's a sample script to demonstrate how to use the Enigma machine:

```python
from enigma import Enigma
from rotor import Rotor, Reflector  # Ensure these are defined in rotor.py

# Define rotors and reflector (example wirings; adjust as needed)
r1 = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", turnover='Q')
r2 = Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", turnover='E')
r3 = Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", turnover='V')
ref = Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")

# Set up the Enigma machine
enigma = Enigma(ref, r1, r2, r3, key="ABC", plugs="AB CD EF")

# Encrypt a message
cipher = enigma.encipher("Hello Enigma!")
print(cipher)
```

---

### 🔑 Expected Output

The output of the encryption will be:
Wlfwb Jzrzxl!


> **Note:** The actual ciphertext will vary depending on your rotor settings, plugboard configuration, and the key you use to initialize the Enigma machine.

---

### 🔄 Decryption

To decrypt a message, simply pass the encrypted text back through the Enigma machine with the **same configuration** (i.e., same rotors, key, and plugboard settings).

Example:

```python
# Decrypt the ciphertext
decrypted_text = enigma.encipher("Wlfwb Jzrzxl!")
print(decrypted_text)
```

---

### 🔑 Expected Output

The output of the encryption will be:
Hello Enigma!

---

### 📁 Project Structure
pyEnigma/
├── href="pyEnigma/enigma.py">enigma.py # Main Enigma machine logic
├── href="pyEnigma/rotor.py">rotor.py # Contains Rotor and Reflector classes
├── href="pyEnigma/README.md">README.md # Project documentation









---

### 👨‍💻 Author

- **Christophe Goessen** (Original Author)
- **Cédric Bonhomme**

---

### 📄 License

This project is licensed under the **GNU GPLv3** License. See the `LICENSE` file for details.

---

### 📚 Disclaimer

This project is intended for **educational and illustrative purposes only**. It is **not suitable** for modern cryptographic use.




