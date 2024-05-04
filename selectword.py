import random

def select_word():
    words = ["python","programlama","makine","veri","yapay","zeka"]
    return random.choice(words)

def display_word(word, guessed_letters):
        display = "" 
        for letter in word:
            if letter in guessed_letters:
                display+=letter
            else:
                display+="_"
        return display

def main():
    print("Kelime tahmin oyununa hosgeldiniz...")
    word = select_word()
    guessed_letters = []
    attempts = 6


    while True:
        print("\nTahmin edilen kelime: ",display_word(word,guessed_letters))
        if "_" not in display_word(word,guessed_letters):
            print("Tebrikler kelimeyi buldunuz")
            break
        elif attempts == 0:
            print("Malesef hakkiniz kalmadi.Doğru kelime '{}' idi".format(word))
            break
        guess = input("Bir harf tahmin edin").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Gecersiz giris.Lütfen birharf girin")
            continue
        elif guess in guessed_letters:
            print("Bu harfi zaten tahmin ettiniz.Baska bir harf girin")
            continue
        guessed_letters.append(guess)

        if guess not in word:
            attempts -=1
            print("Yanlis tahmin. {} hakkiniz kaldi.".format(attempts))

if __name__ == " __main__":
    main()            
