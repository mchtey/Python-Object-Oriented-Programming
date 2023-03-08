import turtle

# Create a canvas instance
myturtle = turtle.Turtle()
"""
myturtle.forward(100) #100 piksel ilerle
myturtle.left(90) #90 derece sola son
myturtle.forward(200) #200 piksel ilerle

myturtle.left(90)
myturtle.forward(100)

myturtle.left(90)
myturtle.forward(200)
'''
Cizimin basladigi nokta orjin (0,0) yani acilan pencerenin
merkezidir.
'''
turtle.done() #Ekranda tutmak icin:
"""

"""
# --------------------------------------------------------------------
# Hareketi merkezden degil de baska koordinatlarda baslatmak
# Belli bir koordinata git:
myturtle.goto(50,75)
myturtle.forward(100)
myturtle.left(90)
myturtle.forward(200)

myturtle.left(90)
myturtle.forward(100)

myturtle.left(90)
myturtle.forward(200)

turtle.done()
"""
'''
Yukaridaki islem uygulandiginda merkezden 50,75 noktasina
bir cizgi cizilip oyle hareket etmektedir.
Bu cizgiyi istemiyorsak:
'''

myturtle.penup() #kalemi kaldir
myturtle.goto(50,75)
myturtle.pendown() #kalemi indir
myturtle.forward(100)
myturtle.left(90)
myturtle.forward(200)

myturtle.left(90)
myturtle.forward(100)

myturtle.left(90)
myturtle.forward(200)

turtle.done()
