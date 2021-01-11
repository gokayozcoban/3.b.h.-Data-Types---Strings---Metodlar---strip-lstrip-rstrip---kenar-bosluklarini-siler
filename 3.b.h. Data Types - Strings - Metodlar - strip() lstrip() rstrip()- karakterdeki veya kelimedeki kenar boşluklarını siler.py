# strip(), rstrip(), lstrip()
# Bu metod string içerisindeki boşlukları siler. r ile yazılınca sağdaki, l ile
# yazılınca soldaki, sadece strip() yazılınca da her iki taraftaki boşlukları
# siler.
metin = "sağ tarafta boşluk bulunan bir metin>      "
print(metin.rstrip())
# Bunu İDLE'da göstermek daha belirgin yapar çıktıyı:
>>> metin
'sağ tarafta boşluk bulunan bir metin>      '
>>> metin.rstrip()
'sağ tarafta boşluk bulunan bir metin>'
>>>

metin = "     <sol tarafta boşluk bulunan bir metin"
print(metin.rstrip())
>>> metin
'     <sol tarafta boşluk bulunan bir metin'
>>> metin.lstrip()
'<sol tarafta boşluk bulunan bir metin'
>>>

metin= "    <her iki tarafta da boşluk bulunan metin>    "
>>> metin
'    <her iki tarafta da boşluk bulunan metin>    '
>>> metin.strip()
'<her iki tarafta da boşluk bulunan metin>'
>>> 
