# sudoku-solver

  <h1>:man_technologist: About it</h1>
    <p>The solver in Python language uses the PySAT toolkit to solve the sudoku using formulas in the Conjunctive Normal Form (CNF) of Boolean Logic.</p>
  <h1> &#x2699 How it works</h1>
  <p>The sudoku is divided into nine large quadrants referenced with rows and columns from 1 to 3. Each quadrant contains nine small squares, identified by rows and columns numbered from 1 to 3.</p>
  <p>The program takes as input a file with strings in the format "<em>sudoku_i_j_p_q_N</em>", where:</p>
  <ul type="disc">
    <li><em>N</em> is the value (from 1 to 9) that will fill the small square;</li>
    <li><em>i</em> is the row value of the position of N on the quadrant;</li>
    <li><em>j</em> is the column value of the position of N on the quadrant;</li>
    <li><em>p</em> is the row value of the quadrant;</li>
    <li><em>q</em> is the column value of the quadrant.</li>
  </ul>
  <p>The following example shows the input for the "world's most difficult Sudoku" designed by Arto Inkala.</p>

  <p>sudoku_1_3_1_1_5 <br>
  sudoku_2_1_1_1_8 <br>
  sudoku_3_2_1_1_7 <br>
  sudoku_1_1_1_2_3 <br>
  sudoku_3_2_1_2_1 <br>
  sudoku_2_2_1_3_2 <br>
  sudoku_3_1_1_3_5 <br>
  sudoku_1_1_2_1_4 <br>
  sudoku_2_2_2_1_1 <br>
  sudoku_3_3_2_1_3 <br>
  sudoku_1_3_2_2_5 <br>
  sudoku_2_2_2_2_7 <br>
  sudoku_3_1_2_2_2 <br>
  sudoku_1_1_2_3_3 <br>
  sudoku_2_3_2_3_6 <br>
  sudoku_3_2_2_3_8 <br>
  sudoku_1_2_3_1_6 <br>
  sudoku_2_3_3_1_4 <br>
  sudoku_1_1_3_2_5 <br>
  sudoku_3_3_3_2_9 <br>
  sudoku_1_3_3_3_9 <br>
  sudoku_2_2_3_3_3 <br>
  sudoku_3_1_3_3_7 </p>
    
  <table>
    <tr>
      <td colspan="2" rowspan="2"></td>
      <td colspan="3" class="q">1</td>
      <td colspan="3" class="q">2</td>
      <td colspan="3" class="q">3</td>
    </tr>
    <tr>
      <td class="j">1</td>
      <td class="j">2</td>
      <td class="j">3</td>
      <td class="j">1</td>
      <td class="j">2</td>
      <td class="j">3</td>
      <td class="j">1</td>
      <td class="j">2</td>
      <td class="j">3</td>
    </tr>
    <tr>
      <td rowspan="3" class="p">1</td>
      <td class="i">1</td>
      <td></td>
      <td></td>
      <td>5</td>
      <td>3</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td class="i">2</td>
      <td>8</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>2</td>
      <td></td>
    </tr>
    <tr>
      <td class="i">3</td>
      <td></td>
      <td>7</td>
      <td></td>
      <td></td>
      <td>1</td>
      <td></td>
      <td>5</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td rowspan="3" class="p">2</td>
      <td class="i">1</td>
      <td>4</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>5</td>
      <td>3</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td class="i">2</td>
      <td></td>
      <td>1</td>
      <td></td>
      <td></td>
      <td>7</td>
      <td></td>
      <td></td>
      <td></td>
      <td>6</td>
    </tr>
    <tr>
      <td class="i">3</td>
      <td></td>
      <td></td>
      <td>3</td>
      <td>2</td>
      <td></td>
      <td></td>
      <td></td>
      <td>8</td>
      <td></td>
    </tr>
    <tr>
      <td rowspan="3" class="p">3</td>
      <td class="i">1</td>
      <td></td>
      <td>6</td>
      <td></td>
      <td>5</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>9</td>
    </tr>
    <tr>
      <td class="i">2</td>
      <td></td>
      <td></td>
      <td>4</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>3</td>
      <td></td>
    </tr>
    <tr>
      <td class="i">3</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>9</td>
      <td>7</td>
      <td></td>
      <td></td>
    </tr>
  </table>
