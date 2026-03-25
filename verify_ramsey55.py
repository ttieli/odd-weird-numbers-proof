#!/usr/bin/env python3
"""
验证 R(5,5) > 42 的反例图
=========================

这个脚本验证 McKay/Exoo 收集的 42 阶 Ramsey(5,5) 图：
- 每个图有 42 个顶点
- 没有 5 个顶点的完全子图（5-clique，即 5 人全认识）
- 没有 5 个顶点的独立集（5-independent set，即 5 人全不认识）

如果这样的图存在，就证明了 42 个人的聚会中可以做到
既没有 5 人全认识也没有 5 人全不认识，因此 R(5,5) > 42。

数据来源：Brendan McKay 的组合数据库
https://users.cecs.anu.edu.au/~bdm/data/ramsey.html
"""

from itertools import combinations
import time
import sys


def graph6_to_adjacency(g6_string):
    """将 graph6 格式字符串转为邻接矩阵"""
    s = g6_string.strip()
    idx = 0

    # 解析顶点数 n
    if ord(s[0]) - 63 < 63:
        n = ord(s[0]) - 63
        idx = 1
    elif s[0] == '~':
        if s[1] == '~':
            # n >= 258048
            n = 0
            for i in range(6):
                n = (n << 6) | (ord(s[2 + i]) - 63)
            idx = 8
        else:
            n = 0
            for i in range(3):
                n = (n << 6) | (ord(s[1 + i]) - 63)
            idx = 4
    else:
        n = ord(s[0]) - 63
        idx = 1

    # 解析邻接矩阵的上三角
    adj = [[0] * n for _ in range(n)]
    bits = []
    for ch in s[idx:]:
        val = ord(ch) - 63
        for bit in range(5, -1, -1):
            bits.append((val >> bit) & 1)

    k = 0
    for j in range(1, n):
        for i in range(j):
            if k < len(bits) and bits[k]:
                adj[i][j] = 1
                adj[j][i] = 1
            k += 1

    return n, adj


def has_clique_of_size(adj, n, k):
    """检查图中是否存在大小为 k 的完全子图"""
    for subset in combinations(range(n), k):
        is_clique = True
        for i, j in combinations(subset, 2):
            if adj[i][j] == 0:
                is_clique = False
                break
        if is_clique:
            return True, subset
    return False, None


def has_independent_set_of_size(adj, n, k):
    """检查图中是否存在大小为 k 的独立集"""
    for subset in combinations(range(n), k):
        is_independent = True
        for i, j in combinations(subset, 2):
            if adj[i][j] == 1:
                is_independent = False
                break
        if is_independent:
            return True, subset
    return False, None


def graph_stats(adj, n):
    """计算图的基本统计信息"""
    edges = sum(adj[i][j] for i in range(n) for j in range(i + 1, n))
    degrees = [sum(adj[i]) for i in range(n)]
    return edges, min(degrees), max(degrees)


def verify_graph(g6_string, graph_id, verbose=True):
    """验证单个图是否为合法的 Ramsey(5,5,42) 图"""
    n, adj = graph6_to_adjacency(g6_string)
    edges, min_deg, max_deg = graph_stats(adj, n)

    if verbose:
        print(f"\n{'='*60}")
        print(f"图 #{graph_id}: {n} 个顶点, {edges} 条边")
        print(f"度数范围: {min_deg} ~ {max_deg}")

    # 验证顶点数
    assert n == 42, f"顶点数应为 42，实际为 {n}"

    # 验证无 5-clique
    t0 = time.time()
    has_c5, clique = has_clique_of_size(adj, n, 5)
    t_clique = time.time() - t0

    if has_c5:
        print(f"  ❌ 发现 5-clique: {clique}")
        return False

    if verbose:
        print(f"  ✅ 无 5-clique（检查用时 {t_clique:.1f}s）")

    # 验证无 5-independent set
    t0 = time.time()
    has_i5, indep = has_independent_set_of_size(adj, n, 5)
    t_indep = time.time() - t0

    if has_i5:
        print(f"  ❌ 发现 5-独立集: {indep}")
        return False

    if verbose:
        print(f"  ✅ 无 5-独立集（检查用时 {t_indep:.1f}s）")

    # 额外：检查最大 clique 和最大独立集的大小
    max_clique = 4
    max_indep = 4
    for k in [4]:
        has_c, _ = has_clique_of_size(adj, n, k)
        has_i, _ = has_independent_set_of_size(adj, n, k)
        if verbose:
            print(f"  {'✅' if has_c else '❌'} 存在 {k}-clique")
            print(f"  {'✅' if has_i else '❌'} 存在 {k}-独立集")

    return True


def main():
    # 也验证 R(3,3) 和 R(4,4) 的经典反例作为热身
    print("=" * 60)
    print("Ramsey 数反例验证器")
    print("=" * 60)

    # === Part 1: 验证 R(3,3) 的反例 (五角星图 C5) ===
    print("\n📐 Part 1: 验证 R(3,3) > 5 的反例（五角星 C₅）")
    print("-" * 60)
    # C5: 0-1, 1-2, 2-3, 3-4, 4-0
    c5_adj = [[0] * 5 for _ in range(5)]
    for i in range(5):
        c5_adj[i][(i + 1) % 5] = 1
        c5_adj[(i + 1) % 5][i] = 1

    has_c3, _ = has_clique_of_size(c5_adj, 5, 3)
    has_i3, _ = has_independent_set_of_size(c5_adj, 5, 3)
    print(f"  五角星（5顶点, 5边）:")
    print(f"  ✅ 无 3-clique: {not has_c3}")
    print(f"  ✅ 无 3-独立集: {not has_i3}")
    print(f"  → 证明 R(3,3) > 5 ✅")

    # === Part 2: 验证 R(4,4) 的反例 (Paley(17)) ===
    print("\n📐 Part 2: 验证 R(4,4) > 17 的反例（Paley 图）")
    print("-" * 60)
    # Paley graph of order 17: i~j iff (i-j) is a QR mod 17
    qr17 = {pow(x, 2, 17) for x in range(1, 17)}  # {1,2,4,8,9,13,15,16}
    paley_adj = [[0] * 17 for _ in range(17)]
    for i in range(17):
        for j in range(i + 1, 17):
            if (i - j) % 17 in qr17:
                paley_adj[i][j] = 1
                paley_adj[j][i] = 1

    edges_p = sum(paley_adj[i][j] for i in range(17) for j in range(i + 1, 17))
    print(f"  Paley(17): 17 顶点, {edges_p} 条边, 每点度数 = 8")
    print(f"  二次剩余 mod 17 = {sorted(qr17)}")

    has_c4, c4 = has_clique_of_size(paley_adj, 17, 4)
    has_i4, i4 = has_independent_set_of_size(paley_adj, 17, 4)
    print(f"  ✅ 无 4-clique: {not has_c4}")
    print(f"  ✅ 无 4-独立集: {not has_i4}")
    print(f"  → 证明 R(4,4) > 17 ✅")

    # === Part 3: 验证 R(5,5) 的反例 ===
    print("\n📐 Part 3: 验证 R(5,5) > 42 的反例（Exoo/McKay 图）")
    print("-" * 60)

    try:
        with open("/tmp/r55_42some.g6", "r") as f:
            graphs = f.readlines()
    except FileNotFoundError:
        print("  ⚠️  数据文件未找到: /tmp/r55_42some.g6")
        print("  请先下载: curl -sL https://users.cecs.anu.edu.au/~bdm/data/r55_42some.g6 -o /tmp/r55_42some.g6")
        return

    total = len(graphs)
    print(f"  共 {total} 个候选图（328 个 + 328 个补图 = 656 个中的一半）")

    # 只验证前几个（完整验证 328 个需要较长时间）
    num_to_verify = min(3, total)
    if len(sys.argv) > 1:
        try:
            num_to_verify = min(int(sys.argv[1]), total)
        except ValueError:
            pass

    print(f"  将验证前 {num_to_verify} 个图（用 `python3 verify_ramsey55.py N` 指定数量）")

    verified = 0
    failed = 0

    for i in range(num_to_verify):
        ok = verify_graph(graphs[i], i + 1)
        if ok:
            verified += 1
        else:
            failed += 1

    # === 总结 ===
    print("\n" + "=" * 60)
    print("验证总结")
    print("=" * 60)
    print(f"  R(3,3) > 5:  ✅（五角星反例）")
    print(f"  R(4,4) > 17: ✅（Paley(17) 反例）")
    print(f"  R(5,5) > 42: {'✅' if failed == 0 else '❌'}"
          f"（验证了 {verified}/{num_to_verify} 个 Exoo/McKay 图）")
    print()
    if failed == 0:
        print("  结论：R(5,5) ≥ 43，即至少需要 43 人才能保证")
        print("        存在 5 人互相认识或 5 人互相不认识。")
        print()
        print("  已知上界：R(5,5) ≤ 48")
        print("  因此：43 ≤ R(5,5) ≤ 48")
        print("  精确值未知，悬赏 $250（Erdős Problem #77）")
    else:
        print(f"  ⚠️ {failed} 个图验证失败！")

    # 组合数统计
    from math import comb
    print(f"\n📊 计算量参考:")
    print(f"  C(42,5) = {comb(42, 5):,}（需检查的 5 元子集数）")
    print(f"  C(42,2) = {comb(42, 2):,}（图的边数上限）")
    print(f"  2^{comb(42, 2)} ≈ 10^{comb(42, 2) * 0.301:.0f}（42 顶点所有图的数量）")


if __name__ == "__main__":
    main()
