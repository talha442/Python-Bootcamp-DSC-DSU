import time

song = """  Jab Bhi Koi Ladaki Dekhun Meraa Dil Divaanaa Bole
Ole Ole Ole, Ole Ole Ole
Gaao Taraanaa Yaaraa Jhum Jhum Ke Haule Haule
Ole Ole Ole, Ole Ole Ole
Mujhako Lubhaati Hai Javaaniya Masti Lutaati Zidagaani Yahaan
Maane Na Kahanaa Paagal Mast Pavan Saa Dil Ye Dole
Ole Ole Ole, Ole Ole Ole
Ole Ole Ole, Ole Ole Ole
Jab Bhi Koi Ladaki Dekhun Meraa Dil Divaanaa Bole
Ole Ole Ole, Ole Ole Ole
Gaao Taraanaa Yaaraa Jhum Jhum Ke Haule Haule
Ole Ole Ole, Ole Ole Ole

Koi Maane Yaa Na Maane Mai Hun Aashiq Aavaaraa
Mai Sodai Divaanaa, Mujhako Chaahat Ne Maaraa
Ye Chikane Chikane Chahare Ye Gori-Gori Baahe
Bechain Mujhe Karati Hai Ye Chan Chachal Shok Adaae
Mujhako Mili Hai Ye Bechain Yahaan Likho Khayaalo Me Kahaani Yahaan
Dekhun Jahaan Koi Shamaa Sag Se Gai Haule Haule
Ole Ole Ole, Ole Ole Ole
Ole Ole Ole, Ole Ole Ole
Jab Bhi Koi Ladaki Dekhun Meraa Dil Divaanaa Bole
Ole Ole Ole, Ole Ole Ole
    """
x = song.split(",")

for elements in x:
    time.sleep(1.2)
    print(elements)