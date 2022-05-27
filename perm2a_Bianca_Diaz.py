import os

#juego de ajedrez

#definiendo el tablero
from importlib.abc import TraversableResources

tablero = [["  ","AA","BB","CC","DD","EE","FF","GG","HH","  "],
           ["01","bT","bP","  ","  ","  ","  ","wP","wT","01"],
           ["02","bC","bP","  ","  ","  ","  ","wP","wC","02"],
           ["03","bA","bP","  ","  ","  ","  ","wP","wA","03"],
           ["04","bQ","bP","  ","  ","  ","  ","wP","wQ","04"],
           ["05","bK","bP","  ","  ","  ","  ","wP","wK","05"],
           ["06","bA","bP","  ","  ","  ","  ","wP","wA","06"],
           ["07","bC","bP","  ","  ","  ","  ","wP","wC","07"],
           ["08","bT","bP","  ","  ","  ","  ","wP","wT","08"],
           ["  ","AA","BB","CC","DD","EE","FF","GG","HH","  "],]

b="="*82

# T = torre
# C = caballo
# A = alfil
# Q = reina
# K = rey
# P = peon
# w = white
# b = black
#dibujando el tablero

def imp_tablero():
  resetear = '\x1b[0m'
  amarillo = '\x1b[1;30;43m'
  rosa = '\x1b[45m'
  blanco = '\x1b[1;30;47m'
  bandera = False
  bandera = ~bandera
  print('|'*26+"Bienvenidos al juego de Aledrez"+'|'*26)
  for c in range(10):
    print(b)
    for a in range(10):
      if c == 0 or c == 9:
        print("||" + blanco + " "*6 + resetear , end="")
      else:
        if a == 0 or a == 9:
          print("||" + blanco + " "*6 + resetear , end="")
        else:
          if(bandera):
            print("||" + amarillo + " "*6 + resetear , end="")
          else:
            print("||" + rosa + " "*6 + resetear, end="")
      bandera = ~bandera
    print("||")
    for f in range(10):
      if c == 0 or c == 9:
        print("||" + blanco + " "*2+tablero[f][c]+" "*2 + resetear,end="")
      else:
        if f == 0 or f == 9:
          print("||" + blanco + " "*2+tablero[f][c]+" "*2 + resetear,end="")
        else:
          if(bandera):
            print("||" + amarillo + " "*2+tablero[f][c]+" "*2 + resetear,end="")
          else:
            print("||" + rosa + " "*2+tablero[f][c]+" "*2 + resetear,end="")
      bandera = ~bandera
    print("||")
    for a in range(10):
      if c == 0 or c == 9:
        print("||" + blanco + " "*6 + resetear , end="")
      else:
        if a == 0 or a == 9:
          print("||" + blanco + " "*6 + resetear , end="")
        else:
          if(bandera):
            print("||" + amarillo + " "*6 + resetear , end="")
          else:
            print("||" + rosa + " "*6 + resetear, end="")
      bandera = ~bandera
    bandera = ~bandera
    print("||")
  print(b)
# Extraemos las coordenadas en base a las letras y numeros en el tablero
def extraer_pos(m,d):
  m_x = ord(m[0])-64
  m_y = int(m[3])

  d_x = ord(d[0])-64
  d_y = int(d[3])
  
  return m_x,m_y,d_x,d_y

# def torres(m_y,m_x,d_y,d_x):
    
     #horizontal o vertical, nada mas
     #no puede saltar fichas
     #no puede 
# movimientos validos del caballo
def caballos(m_y,m_x,d_y,d_x):
 rtn = False
 if (tablero[d_x][d_y]==tablero[m_x + 1][m_y + 2]):
   rtn = True
 elif (tablero[d_x][d_y]==tablero[m_x + 2][m_y + 1]):
   rtn = True
 elif (tablero[d_x][d_y]==tablero[m_x + 1][m_y - 2]):
      rtn = True
 elif (tablero[d_x][d_y]==tablero[m_x - 2][m_y + 1]):
   rtn = True
 elif (tablero[d_x][d_y]==tablero[m_x + 2][m_y - 1]):
   rtn = True
 elif (tablero[d_x][d_y]==tablero[m_x - 1][m_y + 2]):
   rtn = True
 elif (tablero[d_x][d_y]==tablero[m_x - 1][m_y - 2]):
   rtn = True
 elif (tablero[d_x][d_y]==tablero[m_x - 2][m_y - 1]):
   rtn = True
 else:
   rtn = False
 return rtn

#def alfiles():
  #if (m_x == )
#  def Reina():
#movimientos validos de Rey
def Rey(m_y,m_x,d_y,d_x):
  rtn = False
  if (tablero[d_x][d_y]==tablero[m_x + 1][m_y]):
    rtn = True
  elif (tablero[d_x][d_y]==tablero[m_x][m_y + 1]):
    rtn = True
  elif (tablero[d_x][d_y]==tablero[m_x - 1][m_y]):
    rtn = True
  elif (tablero[d_x][d_y]==tablero[m_x][m_y - 1]):
    rtn = True
  elif (tablero[d_x][d_y]==tablero[m_x + 1][m_y + 1]):
    rtn = True
  elif (tablero[d_x][d_y]==tablero[m_x - 1][m_y + 1]):
    rtn = True
  elif (tablero[d_x][d_y]==tablero[m_x - 1][m_y - 1]):
    rtn = True
  elif (tablero[d_x][d_y]==tablero[m_x + 1][m_y - 1]):
    rtn = True
  else:
    rtn = False 
  return rtn
#movimientos validos de los peones
def peones(m_y,m_x,d_y,d_x):
  rtn = False
  if (tablero[d_x][d_y] == tablero[m_x][m_y + 1]):
    rtn = True
  elif (tablero[d_x][d_y] == tablero[m_x][m_y + 2]):
    rtn = True
  elif (tablero[d_x][d_y] == tablero[m_x][m_y - 1]):
    rtn = True
  elif (tablero[d_x][d_y] == tablero[m_x][m_y - 2]):
    rtn = True 
  else:
    rtn = False
    
#  def movimientos(fmov, cdes):
#      if (fmov == "wT"):
#         if torres ==true
#         do lkasmnxjknjks
#      if (fmov == "wC"):
#          #los 8 casos posibles de movimiento
#      if (fmov == "wA"):
#          # i==j solo diagonal
#      if (fmov == "wQ"):
#          #recta o digonal
#      if (fmov == "wK"):
#          #solo 1 casilla recta o digonal
#      if (fmov == "wP"):
#          # 1 casilla solo adelante o 2 cuando se mueve por primera ves 
#como movenmos las piesas en el tablero
def mover(m_y,m_x,d_y,d_x):

  if (tablero[m_x][m_y] == "wC" or tablero[m_x][m_y] == "bC"):
    if(caballos(m_y,m_x,d_y,d_x)==True):
      m = tablero[m_x][m_y]
      tablero[m_x][m_y] = "  "
      tablero[d_x][d_y] = m
      # print(m_x,m_y,d_x,d_y)
    else:
      print("Casilla no valida")
      mover(m_y,m_x,d_y,d_x)
  elif (tablero[m_x][m_y] == "wK" or tablero[m_x][m_y] == "bK"):
    if(Rey(m_y,m_x,d_y,d_x)==True):
      m = tablero[m_x][m_y]
      tablero[m_x][m_y] = "  "
      tablero[d_x][d_y] = m
      # print(m_x,m_y,d_x,d_y)
    else:
      print("Casilla no valida")
      mover(m_y,m_x,d_y,d_x)
  else:
    m = tablero[m_x][m_y]
    tablero[m_x][m_y] = "  "
    tablero[d_x][d_y] = m
    # print(m_x,m_y,d_x,d_y)

def juego():
  bandera = True
  
  ficha_mover = ""
  casilla_destino = ""
 # for i in range(10)
 #   for j in range(10)
 #     if(tablero[i][j])
  while(True):
    imp_tablero()
    if(bandera):
      print("Jugador 1")
      bandera = False
    else:
      print("Jugador 2")
      bandera = True
    
    casilla_mover = input("Ingrese coordenadas a mover segun el tablero Formato(AA01): ")
    casilla_destino = input("Ingrese coordenadas de destino segun el tablero Formato(AA01): ")
    
    m_x,m_y,d_x,d_y = extraer_pos(casilla_mover,casilla_destino)

    mover(m_x,m_y,d_x,d_y)

juego()

# def main():
#   juego()

# main()
