alphabet = 'bcghjklmpqrtvwxyz'
score = 0
names = input("Enter your name: and give space and then enter your friend name- - ->")
for ch in names:
    if ch in 'aeiouAEIOU':
        score+=5
    if ch in 'friends':
        score+=10
    if ch in alphabet:
        score+=alphabet.find(ch)
    else:
        score+=0
if score > 100:
    print("your friendship score is:",score)
    print("Congratulation! you both are best freinds.")
else:
    print("Your friendship score is:",score)