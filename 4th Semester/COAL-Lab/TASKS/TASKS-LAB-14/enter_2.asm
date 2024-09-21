.model small
.stack 100h
.386
.data 
    ; arr db 32 dup(0Dh) ;!first i wanted to store the values in the array and then loop through it,
    ;?but eventually i discovered, it was not worthy and was not a good practice


.code

;! INTUITION
;?I wanted to save the values and show them

;!main
main PROC
    mov ax, @data
    mov ds, ax

    mov si, 0082h

    call hex_in_read ;? => segment address
    push bx
    inc si

    call hex_in_read

    mov di, bx  ;? => offset address prra hua hai idher => 2002 for instance

    
    pop bx
    mov ds, bx ;? => the segment address is stored here 

    call save_values


        mov cx , 8
    outer_loop:
        push cx

        mov bx, ds ;?=> Segment Address
        call hex_out_1
        mov dx, ":"
        mov ah, 02
        int 21h

        mov bx, di ;? => Offset Address
        call hex_out_1
        mov dx, "  "
        mov ah, 02
        int 21h
        mov dx, "  "
        mov ah, 02
        int 21h


        mov cx, 16

        inner_loop: 
            call hex_out
            mov dx, " "
            mov ah, 02
            int 21h
            inc di
            dec cx
            jnz inner_loop


            
            mov dx, 0Dh
            mov ah, 02
            int 21h
            mov dx, 0Ah
            mov ah, 02
            int 21h
            pop cx
            dec cx
            jnz outer_loop



    hehe_end: 
        mov ah,4ch
        int 21h

    
main ENDP

;reading the address and storing it to the BX
hex_in_read PROC

    push cx

    mov cx, 4
    mov bx, 0000
    loop1: 
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
        jnz loop1

    pop cx
    ret
    
hex_in_read ENDP

;printing the output 
hex_out PROC

    push cx
    push di
    
    mov cx, 2
    mov bx, 0
    mov bl, [di]

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
            ; inc di
            dec cx
            jnz loop2
        
        pop di
        pop cx
        ret

    
hex_out ENDP

;this is the procedure to store the values in the arr
save_values PROC
    push di
    push es


    mov si, 008ch

    mov bl, 0
    mov al,0
    while_:
        mov bl, es:[si]
        cmp bl, 20h ;?if the value is 20h skip it
        je con2
        cmp bl, 0Dh ;? if the value is the ENTER key end it
        je ex
        rol al, 4


        sub bl, 30h
        cmp bl, 9h
        ja lb
        jmp hehe1

        lb : 
            sub bl, 7h
        hehe1: 
            or al, bl
            inc si
            jmp while_

        con2: 
            mov [di] , al
            inc di
            mov bl, 0
            mov al,0
            inc si
            jmp while_

    ex:
    cmp al, 0
    je skip_store
    mov [di] , al
    inc di



        skip_store:
        mov bl, 0Dh
        mov [di] , bl ;? => for the reference to quit the program
        pop es
        pop di
        ret
    
save_values ENDP

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

end main