.model small
.stack 100h
.code

main proc
mov AX,@data
mov DS, AX

;first code

mov DI, offset array1
mov SI, offset array2
mov BX, offset sub_array
mov cx, 05

again1: mov al, [si]
sub al, [di]
mov [bx], al

inc DI
inc SI
inc BX
dec CX

jnz again1

; second code

mov DI, offset array1
mov SI, offset array2
mov cx, 05

again: mov al, [si]
mov bl , [di]

mov [si], bl
mov [di], al

inc DI
inc SI
dec CX

jnz again

mov ah,4ch
int 21h

main endp

.data
array1 db 2, 3, 4, 5, 6
array2 db 7, 7, 8, 9, 9

sub_array db 5 dup(?)


end main