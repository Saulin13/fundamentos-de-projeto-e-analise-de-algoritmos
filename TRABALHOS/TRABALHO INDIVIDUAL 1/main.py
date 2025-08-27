from __future__ import annotations

def karatsuba(x: int, y: int) -> int:
    sign = -1 if (x < 0) != (y < 0) else 1
    x, y = abs(x), abs(y)

    if x < 10 or y < 10:
        return sign * (x * y)

    n = max(len(str(x)), len(str(y)))
    m = n // 2

    base = 10 ** m

    a, b = divmod(x, base)
    c, d = divmod(y, base)

    z2 = karatsuba(a, c)
    z0 = karatsuba(b, d)
    z1 = karatsuba(a + b, c + d) - z2 - z0

    result = (z2 * (base ** 2)) + (z1 * base) + z0
    return sign * result


def main():
    print("Karatsuba CLI")
    print("Informe dois inteiros (p.ex.: 1234 e 5678).")
    try:
        x = int(input("x = ").strip())
        y = int(input("y = ").strip())
    except ValueError:
        print("Entrada inválida: digite inteiros.")
        return

    prod = karatsuba(x, y)
    print(f"\nResultado: {prod}")

    correto = (prod == x * y)
    print(f"Confere com x*y nativo? {'SIM' if correto else 'NÃO'}")
    
    print(f"Tempo de execução: {tempo_execucao:.6f} segundos")


if __name__ == "__main__":
    main()
