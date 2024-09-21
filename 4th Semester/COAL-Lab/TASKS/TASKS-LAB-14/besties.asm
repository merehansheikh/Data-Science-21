.model small
.stack 100h
.386
.code
MAIN PROC
mov ax, @data
mov ds, ax
mov si, 0082h
call in_hex_cmd



push bx

call hex_re_in
mov dx, ":"
mov ah, 02
int 21h
inc si
call in_hex_cmd
call hex_re_in
mov dx, " "
mov ah, 02
int 21h
mov di, bx
pop bx
mov ds, bx 
call save_d
mov cx, 16
aa_11: call hex_out


mov dx, " "
mov ah, 02
int 21h



inc di
dec cx
jnz aa_11


ed_kt: 
mov ah,4ch
int 21h
MAIN ENDP
in_hex_cmd PROC
push cx
mov cx, 4
mov bx, 0000


l_1_2: 



mov al,0
mov al, es:[si] 
cmp al, 39h 
jle num_ 
sub al,37h 
jmp shhf 
num_: 
sub al, 30h 
shhf: 
shl bx, 4 

or bl, al





inc si
dec cx
jnz l_1_2

pop cx
ret

in_hex_cmd ENDP

hex_re_in PROC
    

push cx
mov cx, 4
l_11:
rol bx,4
mov dl, bl
and dl, 0Fh
cmp dl, 09
jle eexit_11
add dl, 37H
jmp exit_21

eexit_11: 
add dl, 30h

exit_21:
mov ah, 02
int 21h
dec cx
jnz l_11

pop cx
ret

hex_re_in ENDP

hex_out PROC

push cx

mov cx, 2
mov bx, 0
mov bl, [di]
cmp bl, 0Dh
je ed_kt

loop2:
rol bl,4
mov dl, bl
and dl, 0Fh
cmp dl, 09
jle exit_
add dl, 37H
jmp exit_2

exit_: 
add dl, 30h

exit_2:
mov ah, 02
int 21h
dec cx
jnz loop2

pop cx
ret


hex_out ENDP

save_d PROC
push di
push es
mov si, 008ch

mov bl, 0
mov al,0

loop__11:
mov bl, es:[si]
cmp bl, 20h
je sk_sp
cmp bl, 0Dh 
je ex_69
rol al, 4

sub bl, 30h
cmp bl, 9h
ja ll_33


jmp jj_p

ll_33 : 
sub bl, 7h
jj_p: 
or al, bl
inc si
jmp loop__11

sk_sp: 
mov [di] , al
inc di
mov bl, 0
mov al,0
inc si


jmp loop__11

ex_69:
cmp al, 0
je sk_st_val
mov [di] , al
inc di
sk_st_val:


mov bl, 0Dh
mov [di] , bl
pop es
pop di
ret

save_d ENDP



end MAIN
