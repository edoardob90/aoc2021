#!/usr/bin/env wolframscript -f

(* Make this file executable and run ./5.wls < input.txt *)

int = Interpreter["Integer"];

input = $ScriptInputString;

(* Read the coordinates of the segments *)
points = StringCases[input, 
 x0 : (DigitCharacter ..) ~~ "," ~~ y0 : (DigitCharacter ..) ~~ 
   " -> " ~~ x1 : (DigitCharacter ..) ~~ "," ~~ 
   y1 : (DigitCharacter ..) :> Map[int, {{x0, y0}, {x1, y1}}, {2}]]


(* The initial grid. We add 1 to size in both directions because WL counts from 1 *)
size = 1 + Max /@ Transpose @ Flatten[points, 1]
grid = ConstantArray[0, size]

(* A custom `range` function that "expands" each pair of coordinates written as
        {{x_0, x_1}, {y_0, y_1}}
    into a list of all grid coordinates that would be crossed by the segment
        (x_0, y_0) -> (x_1, y_1)
 *)
range[{x0_, x1_}, {y0_, y1_}] :=
 Transpose@{
   Which[
       x1 < x0, Range[x0, x1, -1], (* expand the range backwards *)
       x1 == x0, ConstantArray[x0, Abs[y1 - y0] + 1], (* if x doesn't change, return a constant array filled with that coordinate *)
       True, Range[x0, x1]], (* otherwise just return a normal range *)
   Which[
       y1 < y0, Range[y0, y1, -1],
       y1 == y0, ConstantArray[y0, Abs[x1 - x0] + 1],
       True, Range[y0, y1]]
   }

(* We now build the full list of grid points that we have to increment.

`Reverse` is needed ONLY to obtain a visual representation of the final result identical to the example of the puzzle text. An update point {x, y} means "x-row and y-column", while in the example is the other way around because Y and X are normal Cartesian axes.
*)

(* Part 1: consider only vertical and horizontal segments, no diagonals *)
pointsPartOne = Cases[points, {{x1_, y1_}, {x2_, y2_}} /; x1 == x2 || y1 == y2];

updates = 
 Reverse /@ Flatten[Map[Apply[range], Transpose /@ pointsPartOne], 1];

(* Update the grid and count how many cells have a value >= 2 *)
finalGrid = 
Fold[
    MapAt[
        Function[x, x + 1], (* Simply add 1. We use an explicit Function to avoid "slot shadowing" with nested pure functions *)
        #1, (* This argument slot is the grid at each step *)
        #2 + 1 (* The grid point to increment. Again, +1 because list indexes start from 1 *)
    ] &, grid, updates];

result = Count[finalGrid, x_ /; x >= 2, 2];

Print["Answer to Part 1: " <> ToString @ result]

(* Part 2: consider now all the segments *)
updates = 
 Reverse /@ Flatten[Map[Apply[range], Transpose /@ points], 1];

(* Update the grid and count how many cells have a value >= 2 *)
finalGrid = 
Fold[
    MapAt[
        Function[x, x + 1], (* Simply adds 1. We use an explicit Function to avoid "slot shadowing" with nested pure functions *)
        #1, (* This argument slot is the grid at each step *)
        #2 + 1 (* The grid point to increment. Again, +1 because list indexes start from 1 *)
    ] &, grid, updates];

result = Count[finalGrid, x_ /; x >= 2, 2];

Print["Answer to Part 2: " <> ToString @ result]