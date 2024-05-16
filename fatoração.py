try:
    a = float(input ('Digite valor de \033[36ma\033[m: '))
    b = float(input ('Digite valor de \033[36mb\033[m: '))
    x = float(input ('Digite valor de \033[36mx\033[m: '))
    y = float(input ('Digite valor de \033[36my\033[m: '))
    ax = a * x
    bx = b * x
    ay = a * y
    by = b * y
    ab = a + b
    ab2 = ab * ab
    abn = a - b
    abn2 = abn * abn
    abb = 2 * a * b + (b ** 2)
    abab = ab * ab
    abnabn = abn * abn
    ababn = ab * abn
    abnp = (a ** 2) - (b ** 2)
    xy = x + y
    axbxayby = ax + bx + ay + by
    xabyab = x * ab + y * ab
    abxy = ab * xy
    axbx = ax + bx
    xab = x * (a + b)
    a2 = a * a
    b2 = a * a
    a2abb = a2 + abb
    a2abbn = a2 - abb
    aabb = (a * a) + a * b + (b * b)
    aabbn = (a * a) - a * b + (b * b)
    a3 = a * a * a
    b3 = b * b * b
    a3b3 = a3 + b3
    a3b3n = a3 - b3
    abnaabb = abn * aabb
    abaabbn = ab * aabbn
    ababab = ab * ab * ab
    abababn = abn * abn * abn
    p4 = a3 + 3 * a2 * b + 3 * a * b2 + b3
    n4 = a3 - 3 * a2 * b + 3 * a * b2 - b3
except ValueError:
    print ('\033[31mVocê não digitou ou digitou dados não numéricos!\033[m')
else:
    print (' ')
    print ('#' * 45)
    print ('\033[4;30;46m##################FATORAÇÃO##################\033[m')
    print ('#' * 45)
    print (' ')
    print ('-' * 29)
    print ('\033[4;30;46m---------FATOR COMUM---------\033[m')
    print ('-' * 29)
    print ('\033[36m{}*{}+{}*{}={}*({}+{})\033[m'.format(a, x, b, x, x, a, b))
    print ('\033[36m{}+{}={}*({}+{})\033[m'.format(ax, bx, x, a, b))
    print ('\033[36m{}={}*({}+{})\033[m'.format(axbx, x, a, b))
    print ('\033[36m{}={}\033[m'.format(axbx, xab))
    print (' ')
    print ('-' * 29)
    print ('\033[4;30;46m---------AGRUPAMENTO---------\033[m')
    print ('-' * 29)
    print ('\033[36m{}*{}+{}*{}+{}*{}+{}*{}=>{}*({}+{})+{}*({}+{})=>({}+{})*({}+{})\033[m'.format(a, x, b, x, a, y, b, y, x, a, b, y, a, b, a, b, x, y))
    print ('\033[36m{}+{}+{}+{}=>{}*({}+{})+{}*({}+{})=>({}+{})*({}+{})\033[m'.format(ax, bx, ay, by, x, a, b, y, a, b, a, b, x, y))
    print ('\033[36m{}+{}+{}+{}=>{}*{}+{}*{}=>{}*{}\033[m'.format(ax, bx, ay, by, x, ab, y, ab, ab, xy))
    print ('\033[36m{}=>{}=>{}\033[m'.format(axbxayby, xabyab, abxy))
    print (' ')
    print ('-' * 30)
    print ('\033[4;30;46m----DIFERENÇA DE QUADRADOS----\033[m')
    print ('-' * 30)
    print ('\033[36m{}²-{}²=({}+{})*({}-{})\033[m'.format(a, b, a, b, a, b))
    print ('\033[36m{}={}*{}\033[m'.format(abnp, ab, abn))
    print ('\033[36m{}={}\033[m'.format(abnp, ababn))
    print (' ')
    print ('-' * 29)
    print ('\033[4;30;46m------QUADRADO PERFEITO------\033[m')
    print ('-' * 29)
    print ('\033[36m{}²+2*{}*{}+{}²=>({}+{})*({}+{})=>({}+{})²\033[m'.format(a, a, b, b, a, b, a, b, a, b, a, b))
    print ('\033[36m{}²+2*{}*{}+{}²=>({})*({})=>({})²\033[m'.format(a, a, b, b, ab, ab, ab))
    print ('\033[36m{}²+2*{}*{}+{}²=>{}=>{}²\033[m'.format(a, a, b, b, abab, ab))
    print ('\033[36m{}+{}=>{}=>{}²\033[m'.format(a2, abb, abab, ab))
    print ('\033[36m{}=>{}=>{}\033[m'.format(a2abb, abab, ab2))
    print ('\033[36m{}²-2*{}*{}+{}²=>({}-{})*({}-{})=>({}-{})²\033[m'.format(a, a, b, b, a, b, a, b, a, b, a, b))
    print ('\033[36m{}²-2*{}*{}+{}²=>({})*({})=>({})²\033[m'.format(a, a, b, b, abn, abn, abn))
    print ('\033[36m{}²-2*{}*{}+{}²=>{}=>{}²\033[m'.format(a, a, b, b, abnabn, abn))
    print ('\033[36m{}-{}=>{}=>{}²\033[m'.format(a2, abb, abnabn, abn))
    print ('\033[36m{}=>{}=>{}\033[m'.format(a2abbn, abnabn, abn2))
    print (' ') 
    print ('-' * 29)
    print ('\033[4;30;46m--SOMA E DIFERENÇA DE CUBOS--\033[m')
    print ('-' * 29)
    print ('\033[36m{}³+{}³=>({}+{})*({}²-{}*{}+{}²)\033[m'.format(a, b, a, b, a, a, b, b))
    print ('\033[36m{}=>{}*{}\033[m'.format(a3b3, ab, aabbn))
    print ('\033[36m{}=>{}\033[m'.format(a3b3, abaabbn))
    print ('\033[36m{}³-{}³=>({}-{})*({}²+{}*{}+{}²)\033[m'.format(a, b, a, b, a, a, b, b))
    print ('\033[36m{}=>{}*{}\033[m'.format(a3b3n, abn, aabb))
    print ('\033[36m{}=>{}\033[m'.format(a3b3n, abnaabb))
    print (' ')
    print ('-' * 29)
    print ('\033[4;30;46m--------CUBO PERFEITO--------\033[m')
    print ('-' * 29)
    print ('\033[36m{}³+3*{}²*{}+3*{}*{}²+{}³=>({}+{})*({}+{})*({}+{})=>({}+{})³\033[m'.format(a, a, b, a, b, b, a, b, a, b, a, b, a, b))
    print ('\033[36m{}³+3*{}²*{}+3*{}*{}²+{}³=>{}*{}*{}=>{}³\033[m'.format(a, a, b, a, b, b, ab, ab, ab, ab))
    print ('\033[36m{}³+3*{}²*{}+3*{}*{}²+{}³=>{}=>{}\033[m'.format(a, a, b, a, b, b, ababab, ababab))
    print ('\033[36m{}=>{}=>{}\033[m'.format(p4, ababab, ababab))
    print ('\033[36m{}³-3*{}²*{}+3*{}*{}²-{}³=>({}-{})*({}-{})*({}-{})=>({}-{})³\033[m'.format(a, a, b, a, b, b, a, b, a, b, a, b, a, b))
    print ('\033[36m{}³-3*{}²*{}+3*{}*{}²-{}³=>{}*{}*{}=>{}³\033[m'.format(a, a, b, a, b, b, abn, abn, abn, abn))
    print ('\033[36m{}³-3*{}²*{}+3*{}*{}²-{}³=>{}=>{}\033[m'.format(a, a, b, a, b, b, abababn, abababn))
    print ('\033[36m{}=>{}=>{}\033[m'.format(n4, abababn, abababn))
    print (' ')
finally:
    print ('\033[36mA CATEC agradece a sua consulta!\033[m')
