N, M = map(int, input().split(' '))

if N-1 != M:
    print('NO')
else:
    u0, v0 = map(int, input().split(' '))
    groups = [[u0, v0]]
    for _ in range(M-1):
        u, v = map(int, input().split(' '))
        not_found = True
        for g in groups:
            if u in g:
                not_found = False
                found = False
                for subg in groups:
                    if v in subg:
                        found = True
                        for ele in subg:
                            g.append(ele)
                        groups.remove(subg)
                        break
                if not found:
                    g.append(v)
            elif v in g:
                not_found = False
                found = False
                for subg in groups:
                    if u in subg:
                        found = True
                        for ele in subg:
                            g.append(ele)
                        groups.remove(subg)
                        break
                if not found:
                    g.append(u)
        if not_found:
            groups.append([u, v])
        
    if len(groups) == 1:
        print('YES')
    else:
        print('NO')
