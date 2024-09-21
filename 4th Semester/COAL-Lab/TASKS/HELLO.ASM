
.model small
.stack 100h
.data 
msg db "Hello$"

.code

main proc

    mov ax,@data
    mov ds, ax

    lea dx, msg
    mov ah,09
    int 21H

    mov ah,4CH
    int 21H

main endp
    end main