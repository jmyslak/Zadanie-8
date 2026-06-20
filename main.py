import argparse
from Caesar import encryption_Caesar, decryption_Caesar
from Morse import encryption_Morse, decryption_Morse

def main():
    parser = argparse.ArgumentParser(description="Narzędzie do szyfrowania i deszyfrowania plików.")
    
    parser.add_argument("input_file", help="Plik wejściowy")
    parser.add_argument("output_file", help="Plik wyjściowy")
    
    group_action = parser.add_mutually_exclusive_group(required=True)
    group_action.add_argument("-e", "--encrypt", action="store_true")
    group_action.add_argument("-d", "--decrypt", action="store_true")
    
    group_cipher = parser.add_mutually_exclusive_group(required=True)
    group_cipher.add_argument("-c", "--caesar", action="store_true")
    group_cipher.add_argument("-m", "--morse", action="store_true")
    
    parser.add_argument("-n", "--shift", type=int, default=3)
    

    args = parser.parse_args()

    with open(args.input_file, "r", encoding="utf-8") as f:
        tekst = f.read()
  
    if args.encrypt:
        wynik = encryption_Caesar(tekst, args.shift) if args.caesar else encryption_Morse(tekst)
    else:
        wynik = decryption_Caesar(tekst, args.shift) if args.caesar else decryption_Morse(tekst)

    with open(args.output_file, "w", encoding="utf-8") as f:
        f.write(wynik)
    
    print(f"Gotowe! Wynik zapisano w: {args.output_file}")

if __name__ == "__main__":
    main()

  