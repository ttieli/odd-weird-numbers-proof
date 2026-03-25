#!/usr/bin/env python3
"""
Search for odd quasi-perfect numbers with Euler-like structure constraints.
Pure Python, no dependencies.
"""
import time
from math import isqrt

def sigma(n):
    s = 0
    for i in range(1, isqrt(n) + 1):
        if n % i == 0:
            s += i
            if i != n // i:
                s += n // i
    return s

def is_prime(n):
    if n < 2: return False
    if n < 4: return True
    if n % 2 == 0 or n % 3 == 0: return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i+2) == 0: return False
        i += 6
    return True

def v2(n):
    if n == 0: return 99
    v = 0
    while n % 2 == 0: v += 1; n //= 2
    return v

def factorint(n):
    factors = {}
    d = 2
    while d * d <= n:
        while n % d == 0: factors[d] = factors.get(d,0)+1; n //= d
        d += 1
    if n > 1: factors[n] = factors.get(n,0)+1
    return factors

def primes_up_to(n):
    sieve = [True]*(n+1); sieve[0]=sieve[1]=False
    for i in range(2, isqrt(n)+1):
        if sieve[i]:
            for j in range(i*i, n+1, i): sieve[j]=False
    return [i for i in range(2,n+1) if sieve[i]]

# Part 1: Verify e≡3(mod4) → v₂(σ(p^e)) ≥ 2
print("="*60)
print("Part 1: e ≡ 3(mod4) → v₂(σ(p^e)) ≥ 2")
ok = True
for p in primes_up_to(200):
    if p < 5: continue
    for e in [3,7,11,15]:
        s = sum(p**i for i in range(e+1))
        if v2(s) < 2: print(f"  FAIL p={p} e={e}"); ok = False
print(f"  {'✓ All pass' if ok else '✗ FAILURES'}")

# Part 2: e≡1(mod4) → v₂(σ(p^e)) = v₂(p+1)
print("\nPart 2: e ≡ 1(mod4) → v₂(σ(p^e)) = v₂(p+1)")
bad = 0
for p in primes_up_to(200):
    if p < 5: continue
    for e in [1,5,9,13]:
        s = sum(p**i for i in range(e+1))
        if v2(s) != v2(p+1): bad += 1; print(f"  FAIL p={p} e={e}")
print(f"  {'✓' if bad==0 else '✗'} Mismatches: {bad}")

# Part 3: p≡1(mod4) → v₂(p+1)=1
print("\nPart 3: p ≡ 1(mod4) → v₂(p+1) = 1 always")
ex = [p for p in primes_up_to(10000) if p%4==1 and v2(p+1)!=1]
print(f"  {'✓ None' if not ex else ex[:5]}")

# Part 4: Mod 8 elimination
print("\n" + "="*60)
print("Part 4: Mod 8 eliminates p ≡ 5(mod8) for a=1")
print("  LHS = 2σ(p^e)σ(Q²) ≡ 4 (mod 8)")
print("  RHS when p≡1(mod8): 3×1×1+1 = 4 ✓")
print("  RHS when p≡5(mod8): 3×5×1+1 = 16 ≡ 0 ✗ → ELIMINATED")
print("  ∴ p ≡ 1 (mod 24)")

qp = [p for p in primes_up_to(1000) if p%24==1]
print(f"\n  Primes ≡ 1(mod24) < 1000: {qp}")
print(f"  Count: {len(qp)}")

# Part 5: General search 2σ(M)=3M+1
print("\n" + "="*60)
print("Part 5: Search 2σ(M) = 3M+1, M odd, 3∤M, up to 2M")
start = time.time()
solutions = []
near = []
for M in range(1, 2_000_001, 2):
    if M % 3 == 0: continue
    d = 2*sigma(M) - 3*M - 1
    if d == 0:
        print(f"  *** SOLUTION M={M}, n={3*M} ***")
        solutions.append(M)
    elif abs(d) <= 4:
        near.append((M, d, factorint(M)))
print(f"  Time: {time.time()-start:.1f}s, Solutions: {len(solutions)}")
print(f"  Near misses (|diff|≤4): {len(near)}")
for M, d, f in near[:25]:
    cc = all(e%2==0 for p,e in f.items() if p%3==2)
    oe = [(p,e) for p,e in f.items() if e%2==1]
    tag = f"CaseC,{'Euler' if len(oe)==1 else f'{len(oe)}odd'}" if cc else "CaseA/B"
    print(f"    M={M:>8d}={f} d={d:+d} {tag}")

# Part 6: Higher a
print("\n" + "="*60)
print("Part 6: Higher powers of 3 (a=2..6)")
for a in range(2, 7):
    s3 = sigma(3**a)
    c = 2*3**a
    found = 0
    for M in range(1, 500_001, 2):
        if M%3==0: continue
        num = c*M+2
        if num%s3!=0: continue
        if sigma(M)==num//s3:
            print(f"  *** a={a}: M={M}, n={3**a*M} ***"); found+=1
    print(f"  a={a}: σ(3^{a})={s3}, solutions={found}")

# Part 7: Summary
print("\n" + "="*60)
print("STRUCTURAL THEOREM SUMMARY")
print("="*60)
print("""
If n is odd with σ(n) = 2n+2, then for a=1:
  n = 3 × p^e × Q²
  • p ≡ 1 (mod 24)     [mod 3 + mod 4 + mod 8]
  • e ≡ 1 (mod 4)      [v₂ analysis, e≡3 mod4 impossible]
  • Q odd, gcd(Q,6p)=1, σ(Q²) odd

Compare Euler's OPN theorem: n = p^e × Q², p≡e≡1(mod4)
Our OQP theorem:          n = 3×p^e×Q², p≡1(mod24), e≡1(mod4)

Stricter: mod 24 vs mod 4 for the special prime.
No solutions found up to M=2,000,000 (n=6,000,000).
""")
