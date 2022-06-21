function asm
	nasm -f elf64 $argv[1].asm && ld -o $argv[1] $argv[1].o && ./$argv[1]
end  
