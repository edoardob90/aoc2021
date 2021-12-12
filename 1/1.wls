#!/usr/bin/env wolframscript -f

(* Make this file executable and run ./1.wls < input.txt *)

countPositiveIncrements[list_List] := 
    Count[MovingMap[Apply[Subtract], list, 1], _?Negative]

input = Interpreter["Integer"] /@ StringSplit[$ScriptInputString, "\n"];

(* Part 1 *)
result = countPositiveIncrements[input]
Print["Answer to Part 1: " <> ToString@result]

(* Part 2 *)
result = countPositiveIncrements[MovingMap[Apply @ Plus, input, 2]];
Print["Answer to Part 2: " <> ToString@result]