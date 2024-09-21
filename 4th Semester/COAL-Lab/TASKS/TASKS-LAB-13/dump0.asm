.model small
.stack 100h
.386
.data

.code

 ;description
main PROC
    mov ax, @data
    mov ds, ax

    mov si, 0082h
    call hex_in_read ;segmnt address
    push bx

    call hex_out_1
    mov dx, ":"
    mov ah, 02
    int 21h

    inc si

    call hex_in_read
    call hex_out_1
    mov dx, " "
    mov ah, 02
    int 21h

    mov si, bx ;offset address

    pop bx
    mov es, bx
    mov cx, 16
    aa: call hex_out
    mov dx, " "
    mov ah, 02
    int 21h
    inc si
    dec cx
    jnz aa

    mov ah,4ch
    int 21h

    
main ENDP

;description
hex_in_read PROC

    push cx

    mov cx, 4
    mov bx, 0000
    loop1: 
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
        jnz loop1

    pop cx
    ret
    
hex_in_read ENDP

;printing the output output 
hex_out PROC

    push cx
    
    mov cx, 2
    mov bl, es:[si]

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

hex_out_1 PROC

    push cx
    
    mov cx, 4
    loop21:
        rol bx,4
        mov dl, bl
        and dl, 0Fh
        cmp dl, 09
        jle exit_1
        add dl, 37H
        jmp exit_21

        exit_1: 
            add dl, 30h

        exit_21:
            mov ah, 02
            int 21h
            dec cx
            jnz loop21
        
        pop cx
        ret

    
hex_out_1 ENDP

;description
; printing PROC
;     pop bx

;     push es
;     mov es, bx

;     mov cx, 16

;     pri_loop:
;         mov bl ,es:[si]
;         push cx
;         mov cx, 2
;         call hex_out
;         mov dx, " "
;         mov ah, 02
;         int 21h
;         pop cx

;         inc si
;         dec cx

;         jnz pri_loop
    
;     ret

; printing ENDP

end main



;reading the hex
; hex_in_read PROC
    

;     start: mov cx, 4
;     mov bx, 0000

;     while_:
;         mov al, [si]
;         cmp al, 39h
;         jle num

;         jmp ALPHA

;         dec cx
;         jnz while_
;         jmp end_while
        


;     ALPHA:
;         shl bx ,4

;         sub al, 37H
;         or bl, al


;         dec cx
;         jnz while_
;         jmp end_while

;     NUM:
;         shl bx, 4

;         sub al, 30h
;         or bl, Al


;         dec cx
;         jnz while_
;         jmp end_while

    
;     end_while: ret
    
; hex_in_read ENDP

