.model small
.stack 100h
.code

.data
array1 db 2, 3, 4, 5, 6
array2 db 7, 7, 8, 9, 9

main proc
    mov AX,@data
    mov DS, AX

    mov DI, offset array1
    mov SI, offset array2
    mov cx, 05

    again:
        mov al, [si]
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


    end main