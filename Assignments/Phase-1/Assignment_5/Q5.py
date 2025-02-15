tlds = {'Canada': 'ca', 'United States': 'us', 'Mexico': 'mx'}
print("Yes" if 'Canada' in tlds else 'No')
print("Yes" if 'France' in tlds else 'No')
print(f'{"Country":<17} Short')
for i in tlds:
    print(f'{i:<17} {tlds[i]}')
tlds['Sweden']='sw'
print(tlds)
tlds['Sweden']='se'
print(tlds)
tlds2={sf:lf for lf,sf in tlds.items()}
print(tlds2)