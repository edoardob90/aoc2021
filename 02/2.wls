#!/usr/bin/env wolframscript -f

(* Make this file executable and run ./2.wls < input.txt *)

int = Interpreter["Integer"]

input = $ScriptInputString;

(* Read the three sets of instructions *)
forward = 
  StringCases[input, 
   "forward" ~~ Shortest[__] ~~ x : DigitCharacter .. :> int@x];

down = StringCases[input, 
   "down" ~~ Shortest[__] ~~ x : DigitCharacter .. :> int@x];

up = StringCases[input, 
   "up" ~~ Shortest[__] ~~ x : DigitCharacter .. :> int@x];

(* Part 1 *)
result = Total[forward] * Map[Total] /* Apply[Plus] @ {down, -up}
Print["Answer to Part 1: " <> ToString @ result]

(* Part 2 *)

(* Read the instructions and keep track the index of each 
   The result will be a list of this kind:
   {
        {1, f, 5},
        {2, d, 5},
        {3, f, 8},
        ...
    }
    where each element contains the index, the type (forward, down, up), and the amount
*)
i = 0;
instructions = 
  StringCases[input, 
   l : (LetterCharacter) ~~ Shortest[__] ~~ 
     x : DigitCharacter .. :> {++i, l, int@x}];

(* Create the three "vectors" with forward, up, and down instructions *)
With[{length = instructions[[-1, 1]]},
 {fList, uList, dList} = 
  ReplacePart[ConstantArray[0, length], 
     Cases[instructions, {x_, #, y_} :> (x -> y)]] & /@ {"f", "u", "d"}
 ];

 (* Build the vector for the "aim" instruction *)
 aimList = FoldList[Plus, dList - uList];

 (* Build the "depth" vector, but keep only the last element *)
 depth = Fold[Plus, fList * aimList];

result = Total[fList] * depth;
Print["Answer to Part 2: " <> ToString @ result]