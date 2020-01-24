#imports go here

#functions and classes go here
def rotate13(text):

    decrypt = 'a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'
    crypt = 'n o p q r s t u v q x y z a b c d e f g h i j k l m N O P Q R S T U V W X Y Z A B C D E F G H I J K L M'

    d = decrypt.split()
    c =  crypt.split()

    z = zip(d, c)
    dic = dict(z)

    encryption = []

    for x in text:
        if x in dic:
            encryption.append(dic[x]) 
        else:
            encryption.append(x)

    return "".join(encryption)

#main code goes here
def main():
    user_option = input("Press 1 to decrypt text: \nPress 2 to encrypt text: \n")
    user_option = int(user_option)

    user_text = input("Enter your text below:\n")

    print(rotate13(user_text))

if __name__ == "__main__":
    main()