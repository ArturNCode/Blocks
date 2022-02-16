# Piece Format ( Piece Naming { I = Straight, O = Square, T = T, J & L = L, S & K = Skew } ).

# Straight Piece Two Possible Rotational Representations.
I = [['_____',
      'OOOO_',
      '_____'],
     ['__O__',
      '__O__',
      '__O__',
      '__O__']]

# Square Piece Single Rotational Representation.
O = [['_OO___',
      '_OO___']]

# T Piece Four Possible Rotational Representations.
T = [['_OOO_',
      '__O__'],
     ['__O__',
      '_OO__',
      '__O__'],
     ['__O__',
      '_OOO_'],
     ['__O__',
      '__OO_',
      '__O__']]

# J Piece Four Possible Rotational Representations.
J = [['__O__',
      '__O__',
      '_OO__'],
     ['_O___',
      '_OOO_'],
     ['__OO_',
      '__O__',
      '__O__'],
     ['_OOO_',
      '___O_']]

# L Piece Four Possible Rotational Representations.
L = [['_O___',
      '_O___',
      '_OO__'],
     ['_OOO_',
      '_O___'],
     ['_OO__',
      '__O__',
      '__O__'],
     ['___O_',
      '_OOO_']]

# S Piece Two Possible Rotational Representations.
S = [['__OO_',
      '_OO__'],
     ['__O__',
      '__OO_',
      '___O_']]

# Z Piece Two Possible Rotational Representations.
Z = [['_OO__',
      '__OO_'],
     ['__O__',
      '_OO__',
      '_O___']]

# Array Responsible For Quick Indexing Of Desired Shapes.
pieces = [I, O, T, J, L, S, Z]
# Color = Same As Window Background (Dark Red).
# May Also Add Individual Colors For Each Piece Lieke So : ((0, 255, 255), (255, 255, 0), ... , (255, 0, 0))
piece_color = (0, 0, 0)
