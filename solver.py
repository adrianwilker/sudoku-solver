from pysat.solvers import Glucose4, Solver

sudoku_mapping = {}
sudoku_mapping_inv = {}
counter_mapping = 1
for p in range(0, 3):
  for q in range(0, 3):
    for i in range(0, 3):
      for j in range(0, 3):
        for N in range(0, 9):
          position_string = "sudoku_" + str(i+1) + "_" + str(j+1) + "_" + str(p+1) + "_" + str(q+1) + "_" + str(N+1)
          sudoku_mapping[position_string] = counter_mapping
          sudoku_mapping_inv[counter_mapping] = position_string
          counter_mapping += 1
print(sudoku_mapping_inv)

f = open("input/input.txt", "r")
input = f.read()

formula = []
for p in range(0, 3):
  for q in range(0, 3):
    for i in range(0, 3):
      for j in range(0, 3):
        sudoku_line = []
        for N in range(0, 9):
          if ("sudoku_" + str(i+1) + "_" + str(j+1) + "_" + str(p+1) + "_" + str(q+1) + "_") in input:
            if ("sudoku_" + str(i+1) + "_" + str(j+1) + "_" + str(p+1) + "_" + str(q+1) + "_" + str(N+1)) in input:
              sudoku_line.append(sudoku_mapping["sudoku_" + str(i+1) + "_" + str(j+1) + "_" + str(p+1) + "_" + str(q+1) + "_" + str(N+1)])
              break
          else:
            sudoku_line.append(sudoku_mapping["sudoku_" + str(i+1) + "_" + str(j+1) + "_" + str(p+1) + "_" + str(q+1) + "_" + str(N+1)])
        formula.append(sudoku_line)
print(formula)

for p in range(0, 3):
  for q in range(0, 3):
    for i in range(0, 3):
      for j in range(0, 3):
        for N1 in range(0, 8):
          for N2 in range(N1, 8):
            sudoku_line = []
            if ("sudoku_" + str(i+1) + "_" + str(j+1) + "_" + str(p+1) + "_" + str(q+1) + "_" + str(N2+2)) in input:
              continue
            else:
              sudoku_line.append(-1*sudoku_mapping["sudoku_" + str(i+1) + "_" + str(j+1) + "_" + str(p+1) + "_" + str(q+1) + "_" + str(N1+1)])
              sudoku_line.append(-1*sudoku_mapping["sudoku_" + str(i+1) + "_" + str(j+1) + "_" + str(p+1) + "_" + str(q+1) + "_" + str(N2+2)])
            formula.append(sudoku_line)
print(formula)

for p in range(0, 3):
  for q in range(0, 3):
    sudoku_line = []
    for i in range(0, 3):
      for j in range(0, 3):
        for N in range(0, 9):
          if ("sudoku_" + str(i+1) + "_" + str(j+1) + "_" + str(p+1) + "_" + str(q+1) + "_") in input:
            if ("sudoku_" + str(i+1) + "_" + str(j+1) + "_" + str(p+1) + "_" + str(q+1) + "_" + str(N+1)) in input:
              sudoku_line.append(sudoku_mapping["sudoku_" + str(i+1) + "_" + str(j+1) + "_" + str(p+1) + "_" + str(q+1) + "_" + str(N+1)])
              break
          else:
            sudoku_line.append(sudoku_mapping["sudoku_" + str(i+1) + "_" + str(j+1) + "_" + str(p+1) + "_" + str(q+1) + "_" + str(N+1)])
    formula.append(sudoku_line)
print(formula)

for p in range(0, 3):
  for q in range(0, 3):
    for i1 in range(0, 3):
      for j1 in range(0, 3):
        for N in range(0, 9):
          for i2 in range(0, 3):
            for j2 in range(0, 3):
              if ((str(i1+1) + str(j1+1) + str(p+1) + str(q+1) + str(N+1)) != (str(i2+1) + str(j2+1) + str(p+1) + str(q+1) + str(N+1))):
                sudoku_line = []
                if ("sudoku_" + str(i2+1) + "_" + str(j2+1) + "_" + str(p+1) + "_" + str(q+1) + "_" + str(N+1)) in input:
                  continue
                else:
                  sudoku_line.append(-1*sudoku_mapping["sudoku_" + str(i1+1) + "_" + str(j1+1) + "_" + str(p+1) + "_" + str(q+1) + "_" + str(N+1)])
                  sudoku_line.append(-1*sudoku_mapping["sudoku_" + str(i2+1) + "_" + str(j2+1) + "_" + str(p+1) + "_" + str(q+1) + "_" + str(N+1)])
                  formula.append(sudoku_line)
print(formula)

for p in range(0, 3):
  for i in range(0, 3):
    sudoku_line = []
    for q in range(0, 3):
      for j in range(0, 3):
        for N in range(0, 9):
          if ("sudoku_" + str(i+1) + "_" + str(j+1) + "_" + str(p+1) + "_" + str(q+1) + "_") in input:
            if ("sudoku_" + str(i+1) + "_" + str(j+1) + "_" + str(p+1) + "_" + str(q+1) + "_" + str(N+1)) in input:
              sudoku_line.append(sudoku_mapping["sudoku_" + str(i+1) + "_" + str(j+1) + "_" + str(p+1) + "_" + str(q+1) + "_" + str(N+1)])
              break
          else:
            sudoku_line.append(sudoku_mapping["sudoku_" + str(i+1) + "_" + str(j+1) + "_" + str(p+1) + "_" + str(q+1) + "_" + str(N+1)])
    formula.append(sudoku_line)
print(formula)

for p in range(0, 3):
  for i in range(0, 3):
    for q1 in range(0, 3):
      for j1 in range(0, 3):
        for N in range(0, 9):
          for q2 in range(0, 3):
            for j2 in range(0, 3):
              if (str(i+1) + str(j1+1) + str(p+1) + str(q1+1) + str(N+1)) != (str(i+1) + str(j2+1) + str(p+1) + str(q2+1) + str(N+1)):
                sudoku_line = []
                if ("sudoku_" + str(i+1) + "_" + str(j2+1) + "_" + str(p+1) + "_" + str(q2+1) + "_" + str(N+1)) in input:
                  continue
                else:
                  sudoku_line.append(-1*sudoku_mapping["sudoku_" + str(i+1) + "_" + str(j1+1) + "_" + str(p+1) + "_" + str(q1+1) + "_" + str(N+1)])
                  sudoku_line.append(-1*sudoku_mapping["sudoku_" + str(i+1) + "_" + str(j2+1) + "_" + str(p+1) + "_" + str(q2+1) + "_" + str(N+1)])
                  formula.append(sudoku_line)
print(formula)

for q in range(0, 3):
  for j in range(0, 3):
    sudoku_line = []
    for p in range(0, 3):
      for i in range(0, 3):
        for N in range(0, 9):
          if ("sudoku_" + str(i+1) + "_" + str(j+1) + "_" + str(p+1) + "_" + str(q+1) + "_") in input:
            if ("sudoku_" + str(i+1) + "_" + str(j+1) + "_" + str(p+1) + "_" + str(q+1) + "_" + str(N+1)) in input:
              sudoku_line.append(sudoku_mapping["sudoku_" + str(i+1) + "_" + str(j+1) + "_" + str(p+1) + "_" + str(q+1) + "_" + str(N+1)])
              break
          else:
            sudoku_line.append(sudoku_mapping["sudoku_" + str(i+1) + "_" + str(j+1) + "_" + str(p+1) + "_" + str(q+1) + "_" + str(N+1)])
    formula.append(sudoku_line)
print(formula)

for q in range(0, 3):
  for j in range(0, 3):
    for p1 in range(0, 3):
      for i1 in range(0, 3):
        for N in range(0, 9):
          for p2 in range(0, 3):
            for i2 in range(0, 3):
              if (str(i1+1) + str(j+1) + str(p1+1) + str(q+1) + str(N+1)) != (str(i2+1) + str(j+1) + str(p2+1) + str(q+1) + str(N+1)):
                sudoku_line = []
                if ("sudoku_" + str(i2+1) + "_" + str(j+1) + "_" + str(p2+1) + "_" + str(q+1) + "_" + str(N+1)) in input:
                  continue
                else:
                  sudoku_line.append(-1*sudoku_mapping["sudoku_" + str(i1+1) + "_" + str(j+1) + "_" + str(p1+1) + "_" + str(q+1) + "_" + str(N+1)])
                  sudoku_line.append(-1*sudoku_mapping["sudoku_" + str(i2+1) + "_" + str(j+1) + "_" + str(p2+1) + "_" + str(q+1) + "_" + str(N+1)])
                  formula.append(sudoku_line)
print(formula)

formula_fnc = Glucose4()
for clause in formula:
  formula_fnc.add_clause(clause)

print(formula_fnc.solve())

print(formula_fnc.get_model())

result = formula_fnc.get_model()
output = [i for i in result if i > 0]
for q in output:
  print(sudoku_mapping_inv[q])

for p in range(0, 3):
  for i in range(0, 3):
    for q in range(0, 3):
      for j in range(0, 3):
        for N in range(0, 9):
          if sudoku_mapping["sudoku_" + str(i+1) + "_" + str(j+1) + "_" + str(p+1) + "_" + str(q+1) + "_" + str(N+1)] in output:
            if ("sudoku_" + str(i+1) + "_" + str(j+1) + "_" + str(p+1) + "_" + str(q+1) + "_" + str(N+1)) in input:
              print(f'\033[1;34m{N+1}\033[0;49;39m', end=' ')
            else:
              print(N+1, end=' ')
      print('  ', end='')
    print()
  print()