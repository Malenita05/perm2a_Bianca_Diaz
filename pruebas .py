import os

"""def construye_tabla_formatos():
    for estilo in range(8):
        for colortexto in range(30,38):
            cad_cod = ''
            for colorfondo in range(40,48): 
                fmto = ';'.join([str(estilo), 
                                 str(colortexto),
                                 str(colorfondo)]) 
                cad_cod+="\033["+fmto+"m "+fmto+" \033[0m" 
            print(cad_cod)
        print('\n')

construye_tabla_formatos()
"""
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
print('|'*26+"Bienvenidos al juego de Aledrez"+'|'*26)
def imp_tablero():
  resetear = '\x1b[0m'
  amarillo = '\x1b[1;30;43m'
  rosa = '\x1b[45m'
  blanco = '\x1b[1;30;47m'
  bandera = False
  bandera = ~bandera
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

def extraer_pos(m,d):
  m_x = ord(m[0])-64
  m_y = int(m[3])

  d_x = ord(d[0])-64
  d_y = int(d[3])
  
  return m_x,m_y,d_x,d_y
  
def mover(m_y,m_x,d_y,d_x):
  m = tablero[m_x][m_y]
  tablero[m_x][m_y] = "  "
  tablero[d_x][d_y] = m
  # print(m_x,m_y,d_x,d_y)

def juego():
  bandera = True
  
  ficha_mover = ""
  casilla_destino = ""

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

def main():
  juego()

main()

