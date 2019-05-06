'''
CSCI 5512 - AI 2 - HW 5
Nikki Kyllonen
kyllo089

Problem 6: Find the minimum using gradient descent
'''
import sys, math, copy

'''
df: gradient of f at (a, b, c, d)
'''
def df(x):
  [a,b,c,d] = x
  dfa = 4.0*a*c*c*c*c - b
  dfb = -1.0*a + 4*b*d*d
  dfc = 8*a*a*c*c*c - 9*c*c*d
  dfd = (math.cos(d) + 1)*math.exp(math.sin(d) + d) + 4*b*b*d - 3*c*c*c

  return [dfa, dfb, dfc, dfd]

'''
gradient_descent: use initial guess to find minimum
'''
def gradient_descent(guess, alpha, N):
  pt = guess
  
  for n in range(N):
    # calculate gradient at current guess
    grad = df(pt)
    #print(grad)

    # calculate next guess -- along negative gradient
    for i in range(len(pt)):
      pt[i] = pt[i] - alpha * grad[i]
  # END for n

  return pt

'''
========= MAIN =========
'''
if __name__ == '__main__':
  guess = [0,0,0,0]
  alpha = 0.1
  N = 500

  if (len(sys.argv) > 1):
    alpha = float(sys.argv[1])
    if (len(sys.argv) == 3):
      N = int(sys.argv[2])

  print(gradient_descent(guess, alpha, N))
