program oldschool;

const
   flag: array[1..30] of byte = (224, 242, 231, 244, 202, 252, 202, 249, 166,
                                 227, 240, 202, 165, 164, 241, 202, 230, 246, 
                                 253, 165, 165, 164, 202, 230, 165, 202, 248, 
                                 192, 160, 253);

var
   d, i: integer;

begin
   writeln('Secret storage');
   writeln;
   writeln('Enter key:');
   readln(d);
   
   if (d and 37 = 36) then
        for i := 1 to 30 do
            write(chr(flag[i] xor 149))
   else
        writeln('fail!');
end.