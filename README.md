# Simple Advanced Encryption Standard (AES) Coding Algorithm
This coding is to show you a basic code to perform advanced encryption standard using Python language that can be compiled for any platform.

## Table of Contents
* [What is AES](#what-is-aes)
* [AES Modes of Operation](#aes-modes-of-operation)
* [How to use](#how-to-use)


## What is AES
The Advanced Encryption Standard (AES) is a symmetric encryption algorithm widely used across the globe to secure data. Here’s a detailed explanation of its principles, structure, and operation:

1. Principles of AES
* Symmetric Key Encryption: AES uses the same key for both encryption and decryption. This requires secure key management because if the key is compromised, the encrypted data can be decrypted.
* Block Cipher: AES operates on fixed-size blocks of data. The standard block size is 128 bits, though the key size can vary.

2. AES Key Sizes
AES supports three key sizes:

* AES-128: Uses a 128-bit key.
* AES-192: Uses a 192-bit key.
* AES-256: Uses a 256-bit key.

  The key size determines the number of rounds the algorithm will perform:

* AES-128: 10 rounds.
* AES-192: 12 rounds.
* AES-256: 14 rounds.

3. AES Structure
AES consists of several rounds of processing, each involving a series of operations. These operations include:

* SubBytes: A non-linear substitution step where each byte is replaced with another according to a lookup table (S-box).
* ShiftRows: A transposition step where each row of the state is shifted cyclically a certain number of steps.
* MixColumns: A mixing operation which operates on the columns of the state, combining the four bytes in each column.
* AddRoundKey: Each byte of the state is combined with a byte of the round key using bitwise XOR.

4. AES Encryption Process

  i. Initial Round:

  * AddRoundKey: Each byte of the plaintext is XORed with the corresponding byte of the round key.

  ii. Main Rounds (repeated 9, 11, or 13 times depending on key size):

  * SubBytes: Each byte in the state matrix is substituted with the S-box value.
  * ShiftRows: Rows of the state matrix are shifted cyclically.
  * MixColumns: Columns are mixed, transforming the data.
  * AddRoundKey: The current state is XORed with the round key.

  iii. Final Round (same as the main rounds, but without MixColumns):

  * SubBytes
  * ShiftRows
  * AddRoundKey

5. AES Decryption Process

The decryption process of AES is essentially the reverse of the encryption process, using the inverse operations:

  i. Initial Round:

  * Inverse AddRoundKey

  ii. Main Rounds:

  * Inverse ShiftRows
  * Inverse SubBytes
  * Inverse AddRoundKey
  * Inverse MixColumns

  iii. Final Round:

Inverse ShiftRows
Inverse SubBytes
Inverse AddRoundKey

## AES Modes of Operation
AES can be used in different modes to provide various security properties. The mode of operation determines how blocks are processed:

* ECB (Electronic Codebook): Each block of plaintext is encrypted separately. Not recommended due to patterns in the plaintext being visible in the ciphertext.
* CBC (Cipher Block Chaining): Each block of plaintext is XORed with the previous ciphertext block before being encrypted. Requires an initialization vector (IV) for the first block.
* CFB (Cipher Feedback) and OFB (Output Feedback): Turn block ciphers into stream ciphers.
* CTR (Counter): Converts a block cipher into a stream cipher, encrypting successive values of a counter.

## How to use
Here, I will show you guide for beginners to use. First and foremost, you need to download the zip file which content the full code

### Step 1: Set Up Project Environment
1. Choose a Code Editor or IDE: You can use any code editor or integrated development environment (IDE) for Python development. Popular options include Visual Studio Code, PyCharm, Sublime Text, Atom, or IDLE (which comes bundled with Python).
2. Open Your Code Editor or IDE: Launch your chosen code editor or IDE.

In my situation, I am using Python version 3.12 with PyCharm 2024.1.1 (Community Edition)

### Step 2: Open the Python File
Open the File: In your code editor or IDE, open Python file by selecting "File" > "Open" or using the appropriate keyboard shortcut. Then select the file "AES Crypto Project", the file of this code.

The code will open up in your code editor.

### Step 3: Open the Terminal

In your code editor, open the terminal by clicking on "View" > "Tool Windows" > "Terminal".

### Step 2: Install pycryptodome

In the terminal window, type the following command and press Enter to install 'pycryptodome':

    pip install pycryptodome

### Step 3: Verify Installation

After the installation is complete, you can verify that 'pycryptodome' is installed correctly by running the following command in the terminal:

    pip list

Look for 'pycryptodome' in the list of installed packages. If it's listed, it means that the installation was successful.

### Step 4: Restart PyCharm

After installing pycryptodome, it's a good idea to restart PyCharm to ensure that it recognizes the newly installed package.

### Step 5: Run Your Python Script

Once your code editor has restarted, try running your Python script. You should be able to get the output.

