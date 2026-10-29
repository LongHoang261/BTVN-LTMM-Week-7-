def nhandathuc(a, b, n, P):
    bit_cao = 1 << (n - 1);
    quychieu = (1 << n) - 1;
    C = 0;
    while(n != 0):
        if(a & 1) != 0:
            C = C^b
        a = a >> 1
        carry = b & bit_cao
        b = (b << 1) & quychieu
        if(carry != 0):
            b = b^P
        n = n - 1
    return C;

while True:
    n = int(input("Nhập n(4bit hoặc 8bit):"));
    if n == 4:
        P = 0x03 #x^4+x+1
        break;
    elif n == 8:
        P = 0x1B #x^8+x^4+x^3+x+1
        break;
    else:
        print("LỖI(Chỉ nhận n=4 hoặc n=8)");
while True:
    a = int(input("Nhập a(hex): "), 16);
    b = int(input("Nhập b(hex): "), 16);
    if(a >= (1 << n))or(b >= (1 << n)):
        print("LỖI(a hoặc b quá lớn)");
    else:
        C=nhandathuc(a, b, n, P);
        print(f"{a:#x} * {b:#x} = {C:#x}");
        break;
            