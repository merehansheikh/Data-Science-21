.model small
.stack 100h
.data
.386
.code
main proc
mov si,0082h
call hex_in
mov ds,bx
call hexadecimal_4
mov dx,":"
mov ah,02
int 21h
mov si,0087h
call hex_in
call hexadecimal_4
mov dx," "
mov ah,02
int 21h
mov si,008ch
mov di,bx
push di
push ds
call fill_data
pop ds
pop di
main_loop:
mov bl,[di]
cmp bl,0dh
je end_program
call hexadecimal_2
mov dl," "
mov ah,02
int 21h
jmp continue_main_loop


continue_main_loop:
inc di
jmp main_loop

end_program:
mov ah,4ch
int 21h
main endp


fill_data proc
mov bl,0
data_loop:
mov al,es:[si]
cmp al,0dh
je end_proc
cmp al," "
je skip_element
rol bl,4
sub al,30h
cmp al, 9
ja alphabet
jmp skip_dec

alphabet:
sub bl,7h


skip_dec:
or bl,al

jmp loop_control
skip_element:
mov [di],bl
mov al,0
mov bl,0
inc di
loop_control:
inc si
jmp data_loop
end_proc:
cmp bl,0
je skip_a
mov [di],bl
inc di
skip_a:
mov [di],al
ret
fill_data endp



hex_in proc
mov bx,0
mov cx,4
loop2:
mov al,0
mov al,es:[si]
shl bx,1
shl bx,1
shl bx,1
shl bx,1
cmp al,39h
ja alpha
sub al,48
or bl,al
jmp exit
alpha:
sub al,55
or bl,al
exit:
inc si
dec cx 
jnz loop2
ret
hex_in endp

hexadecimal_2 proc
push cx
push bx
mov cx,2
loop4:
rol bl,1
rol bl,1
rol bl,1
rol bl,1
mov al,bl
and al,0fh
cmp al,9
ja alpha1
mov dl,al
add dl,30h
mov ah,02
int 21h
jmp end2

alpha1:
mov dl,al
add dl,55
mov ah,02
int 21h
end2:
dec cx
jnz loop4
pop bx
pop cx
ret
hexadecimal_2 endp

hexadecimal_4 proc
push cx
push bx
mov cx,4
output_loop:
rol bx,1
rol bx,1
rol bx,1
rol bx,1
mov al,bl
and al,0fh
cmp al,9
ja alpha2
mov dl,al
add dl,30h
mov ah,02
int 21h
jmp end3

alpha2:
mov dl,al
add dl,55
mov ah,02
int 21h
end3:
dec cx
jnz output_loop
pop bx
pop cx
ret
ret
hexadecimal_4 endp

end main