# CPU architectures

```c
void add(){
  int a, b, c;
  a = 2;
  b = 2;
  c = a * b;
}
```

## ARM Family

- Apple M1 processors
- Require less transistors, therefore it's good for battery life

```assembly
add:
    sub   sp, sp, #16
    mov   w8, #2
    str   w8, [sp, #12]
    str   w8, [sp, #8]
    ldr   w8, [sp, #12]
    ldr   w9, [sp, #8]
    mul   w8, w8, w9
    str   w8, [sp, #4]
    add   sp, sp, #16
    ret
```

- `RISC` Architecture (Reduced Instruction Set Computing)
  - Offers few instructions, but faster execution

## Intel x86 Family

- Intel & AMD processors
- `64-bit` version: x86-64, x64, x86_64, AMD64, Intel 64
- `32-bit` version: A-32 (Intel Architecture, 32-bit), i386

```assembly
add:
    push  rbp
    mov   rbp, rsp
    mov   dword ptr [rbp - 4], 2
    mov   dword ptr [rbp - 8], 2
    mov   eax, dword ptr [rbp - 4]
    imul  eax, dword ptr [rbp - 8]
    mov   dword ptr [rbp - 12], eax
    pop   rbp
    ret
```

- `CISC` Architecture (Complex Instruction Set Computing)
  - Has more assembly instructions than RISC processors
  - Good for when developers had to write assembly code directly
