#user se pehle unka naam pucho plus hum unke naame ke aage pice se whitespace hata denge aur unke naam ke initials ko capitalize kar denge
name = input("What's your name? ").strip().title()

# user ne galti se bhot saare space () daal diye apne naam se pehle ya baad me 
#name = name.strip()

# user ne jald baazi mein apne naam ke initials chote likh diye 
#name = name.capitalize() abh ya to fir hum yeh likh sakte hai jisse sirf name ka first word capatilize hoga

# ya fir hum pure dono shabdo ko capitalize kar sakte hai 
#name=name.title()

# Usage of "f string" 
print(f'Hello, {name}')