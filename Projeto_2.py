#TAD gerador-Representação interna: [b,s]
def cria_gerador(b,s):
    """Esta função cria um gerador de números pseudoaleatórios
    do tipo xorshift.
    
    Args:
        b (int): Numero de bits do gerador
        s (int): Seed ou estado inicial

    Raises:
        ValueError: Levanta erro se b e s nao são inteiros positivos

    Returns:
        TAD Gerador: Gerador
    """
    if not (type(b)==int and type(s)==int \
        and (b==32 or b==64) and 0<s<=(2**b)-1):
        raise ValueError ("cria_gerador: argumentos invalidos")
    return [b,s]

def cria_copia_gerador(g):
    """Esta função cria uma cópia do gerador.

    Args:
        g (TAD Gerador): Gerador

    Returns:
        list: Cópia nova do gerador
    """
    gerador_copia=g[:]
    return gerador_copia

def obtem_estado(g):
    """Esta função obtem o estado atual do gerador. 

    Args:
        g (TAD Gerador): Gerador

    Returns:
        int: Estado atual do gerador g sem o alterar
    """
    return g[1]

def define_estado(g,s):
    """Esta função define um novo estado do gerador

    Args:
        g (TAD Gerador): Gerador
        s (int): Seed ou estado inicial

    Returns:
        int: Novo valor do estado do gerador g
    """
    g[1]=s
    return s

def atualiza_estado(g):
    """Esta função a atualiza o estado do gerador.

    Args:
        g (TAD Gerador): Gerador

    Returns:
        int: Estado do gerador g de acordo com o algoritmo 
        xorshift de geração de números pseudoaleatórios
    """
    if g[0]==32:
        g[1] ^= ( g[1] << 13) & 0xFFFFFFFF
        g[1] ^= ( g[1] >> 17) & 0xFFFFFFFF
        g[1] ^= ( g[1] << 5) & 0xFFFFFFFF
    else:
        g[1] ^= ( g[1] << 13) & 0xFFFFFFFFFFFFFFFF
        g[1] ^= ( g[1] >> 7) & 0xFFFFFFFFFFFFFFFF
        g[1] ^= ( g[1] << 17) & 0xFFFFFFFFFFFFFFFF
    return g[1]

def eh_gerador(arg):
    """Esta função verifica se o argumento é um gerador

    Args:
        arg (universal): Argumento universal

    Returns:
        bool: True caso o seu argumento seja um TAD gerador e 
        False caso contrário
    """
    return type(arg)==list and len(arg)==2 and type(arg[0])==int and type(arg[1])==int \
        and (arg[0]==32 or arg[0]==64) and 0<arg[1]<=(2**arg[0])-1
    
def geradores_iguais(g1,g2):
    """
    Args:
        g1 (TAD Gerador): Gerador 1
        g2 (TAD Gerador): Gerador 2

    Returns:
        bool: True apenas se g1 e g2 são geradores e são iguais
    """
    return eh_gerador(g1) and eh_gerador(g2) and g1==g2

def gerador_para_str(g):
    """Esta função transforma o gerador numa cadeia de caracteres

    Args:
        g (TAD Gerador): Gerador

    Returns:
        str: Cadeia de caracteres do gerador
    """
    return ("xorshift%d(s=%d)" %(g[0],g[1]))

def gera_numero_aleatorio(g,n):
    """Esta função atualiza o estado do gerador e gera um número aleatório

    Args:
        g (TAD Gerador): Gerador
        n (int): Número inteiro

    Returns:
        int: Número aleatório no intervalo [1, n]
    """
    return 1 + atualiza_estado(g) % n

def gera_carater_aleatorio(g,c):
    """Esta função atualiza o estado do gerador e gera um carater aleatório

    Args:
        g (TAD Gerador): Gerador
        c (str): Caratér maiúsculo

    Returns:
        str: Carater aleatório no intervalo entre 'A' e o caráter maiúsculo c
    """
    return chr(ord("A") + atualiza_estado(g)%(ord(c)-ord("A")+1))

#TAD coordenada-Representação interna: (col,lin)    
def cria_coordenada(col,lin):
    """ Esta função recebe os valores correspondentes à coluna col e
    linha lin e devolve a coordenada correspondente.

    Args:
        col (str): Coluna
        lin (int): Linha

    Raises:
        ValueError: Levanta erro se col não for uma string e não estiver 
        entre A e Z; e se lin não for inteiro no intervalo [1,99]

    Returns:
        TAD coordenada: Coordenada
    """
    if not(type(col)==str and type(lin)==int and len(col)==1 \
        and 1<=lin<=99 and 65<=ord(col)<=90):
        raise ValueError ("cria_coordenada: argumentos invalidos")
    return (col,lin)

def obtem_coluna(c):
    """
    Args:
        c (TAD coordenada): Coordenada

    Returns:
        str: Coluna col da coordenada c
    """
    return c[0]

def obtem_linha(c):
    """
    Args:
        c (TAD coordenada): Coordenada

    Returns:
        int: Linha lin da coordenada c
    """
    return c[1]

def eh_coordenada(arg):
    """Esta função verifica se o argumento é uma coordenada

    Args:
        arg (universal): Argumento universal

    Returns:
        bool: True caso o seu argumento seja um TAD coordenada e
        False caso contrário
    """
    return type(arg)==tuple and len(arg)==2 and type(arg[0])==str \
        and len(arg[0])==1 and type(arg[1])==int and 1<=arg[1]<=99 \
            and 65<=ord(arg[0])<=90

def coordenadas_iguais(c1,c2):
    """
    Args:
        c1 (TAD coordenada): Coordenada 1
        c2 (TAD coordenada): Coordenada 2

    Returns:
        bool: True apenas se c1 e c2 são coordenadas e são iguais
    """
    return eh_coordenada(c1) and eh_coordenada(c2) and c1==c2

def coordenada_para_str(c):
    """Esta função transforma uma coordenada para cadeia de carateres 

    Args:
        c (TAD coordenada): Coordenada

    Returns:
        str: Cadeia de carateres da coordenada
    """
    return ("%s%.2d" %(c[0],c[1]))

def str_para_coordenada(s):
    """Esta função transforma uma cadeia de carateres para coordenada

    Args:
        s (str): Cadeia de carateres da coordenada

    Returns:
        TAD coordenada: Coordenada
    """
    return (s[0],int(s[1:]))

def obtem_coordenadas_vizinhas(c):
    """Esta função devolve um tuplo com as coordenadas vizinhas à
    coordenada c

    Args:
        c (TAD coordenada): Coordenada

    Returns:
        tuple: Coordenadas vizinhas à coordenada c, começando pela coordenada na 
        diagonal acima-esquerda de c e seguindo no sentido horário
    """
    coord_vizinhas=()

    if 1<=obtem_linha(c)-1<=99:
        if ord("A")<=ord(obtem_coluna(c))-1<=ord("Z"):
            coord_vizinhas+=(cria_coordenada(chr(ord(obtem_coluna(c))-1),obtem_linha(c)-1),) #adiciona a coordenada na diagonal acima-esquerda de c
        coord_vizinhas+=(cria_coordenada(obtem_coluna(c),obtem_linha(c)-1),)                 #adiciona a coordenada acima de c

    if ord("A")<=ord(obtem_coluna(c))+1<=ord("Z"):
        if 1<=obtem_linha(c)-1<=99:
            coord_vizinhas+=(cria_coordenada(chr(ord(obtem_coluna(c))+1),obtem_linha(c)-1),) #adiciona a coordenada na diagonal acima-direita de c
        coord_vizinhas+=(cria_coordenada(chr(ord(obtem_coluna(c))+1),obtem_linha(c)),)       #adiciona a coordenada à direita de c

    if 1<=obtem_linha(c)+1<=99:
        if ord("A")<=ord(obtem_coluna(c))+1<=ord("Z"):
            coord_vizinhas+=(cria_coordenada(chr(ord(obtem_coluna(c))+1),obtem_linha(c)+1),) #adiciona a coordenada na diagonal abaixo-direita de c
        coord_vizinhas+=(cria_coordenada(obtem_coluna(c),obtem_linha(c)+1),)                 #adiciona a coordenada abaixo de c
        
    if ord("A")<=ord(obtem_coluna(c))-1<=ord("Z"):
        if 1<=obtem_linha(c)+1<=99:
            coord_vizinhas+=(cria_coordenada(chr(ord(obtem_coluna(c))-1),obtem_linha(c)+1),) #adiciona a coordenada na diagonal abaixo-esquerda de c
        coord_vizinhas+=(cria_coordenada(chr(ord(obtem_coluna(c))-1),obtem_linha(c)),)       #adiciona a coordenada à esquerda de c

    return coord_vizinhas

def obtem_coordenada_aleatoria(c,g):
    """Esta função gera uma coordenada aleatória, em sequência,
    primeiro a coluna e depois a linha da coordenada resultado.

    Args:
        c (tuple): Coordenada com maior linha e coluna possíveis
        g (TAD gerador): Gerador

    Returns:
        tuple: Coordenada gerada aleatoriamente
    """
    return cria_coordenada(gera_carater_aleatorio(g,obtem_coluna(c)),\
        gera_numero_aleatorio(g,obtem_linha(c)))

#TAD parcela-Representação interna: {"estado":"tapadas","minada":False}
def cria_parcela():
    """Esta função cria uma parcela

    Returns:
        TAD parcela: Parcela tapada sem mina escondida
    """
    p={"estado":"tapadas","minada":False}
    return p

def cria_copia_parcela(p):
    """
    Args:
        p (TAD parcela): Parcela

    Returns:
        dict: Nova cópia da parcela
    """
    p1={}
    for chave in p :
        p1[chave] = p[chave]
    return p1

def limpa_parcela(p):
    """Esta função modifica destrutivamente a parcela p modificando o 
    seu estado para limpa

    Args:
        p (TAD parcela): Parcela

    Returns:
        dict: Parcela limpa
    """
    p["estado"]="limpas"
    return p

def marca_parcela(p):
    """Esta função modifica destrutivamente a parcela p modificando o 
    seu estado para marcada com uma bandeira

    Args:
        p (TAD parcela): Parcela

    Returns:
        dict: Parcela Marcada
    """
    p["estado"]="marcadas"
    return p

def desmarca_parcela(p):
    """Esta função modifica destrutivamente a parcela p modificando o 
    seu estado para tapada

    Args:
        p (TAD parcela): Parcela

    Returns:
        dict: Parcela tapada
    """
    p["estado"]="tapadas"
    return p

def esconde_mina(p):
    """Esta função modifica destrutivamente a parcela p escondendo uma
    mina na parcela

    Args:
        p (TAD parcela): Parcela

    Returns:
        dict: Parcela minada
    """
    p["minada"]=True
    return p

def eh_parcela(arg):
    """
    Args:
        arg (universal): Argumento universal

    Returns:
        bool: True caso o seu argumento seja um TAD parcela e
        False caso contrário
    """
    return type(arg)==dict and "estado" in arg and "minada" in  arg \
        and len(list(arg.values()))==2 and type(arg["minada"])==bool \
            and type(arg["estado"])==str and ("tapadas" in arg["estado"] or\
                "marcadas" in arg["estado"] or "limpas" in arg["estado"])

def eh_parcela_tapada(p):
    """
    Args:
        p (TAD parcela): Parcela

    Returns:
        bool: True caso a parcela p se encontre tapada e False
        caso contrário
    """
    return eh_parcela(p) and "tapadas" in p["estado"]

def eh_parcela_marcada(p):
    """
    Args:
        p (TAD parcela): Parcela

    Returns:
        bool: True caso a parcela p se encontre marcada com 
        uma bandeira e False caso contrário
    """
    return eh_parcela(p) and "marcadas" in p["estado"]

def eh_parcela_limpa(p):
    """
    Args:
        p (TAD parcela): Parcela

    Returns:
        bool: True caso a parcela p se encontre limpa e False
        caso contrário
    """
    return eh_parcela(p) and "limpas" in p["estado"]

def eh_parcela_minada(p):
    """
    Args:
        p (TAD parcela): Parcela

    Returns:
        bool: True caso a parcela p esconda uma mina e False
        caso contrário
    """
    return eh_parcela(p) and p["minada"]

def parcelas_iguais(p1,p2):
    """
    Args:
        p1 (TAD parcela): Parcela 1
        p2 (TAD parcela): Parcela 2

    Returns:
        bool: True apenas se p1 e p2 são parcelas e são iguais
    """
    return eh_parcela(p1) and eh_parcela(p2) and p1==p2

def parcela_para_str(p):
    """Esta função transforma uma parcela numa cadeia de caracteres

    Args:
        p (TAD parcela): Parcela

    Returns:
        str: Cadeia de caracteres que representa a parcela
        em função do seu estado
    """
    if eh_parcela_tapada(p):
        return "#"
    elif eh_parcela_marcada(p):
        return "@"
    elif eh_parcela_limpa(p) and not eh_parcela_minada(p):
        return "?"
    elif eh_parcela_limpa(p) and eh_parcela_minada(p):
        return "X"

def alterna_bandeira(p):
    """Esta função modifica destrutivamente uma parcela.

    Args:
        p (TAD parcela): Parcela

    Returns:
        bool: Se modifica a parcela devolve True e caso contrário False
    """
    p1=cria_copia_parcela(p)
    if eh_parcela_marcada(p):
        return p1 != desmarca_parcela(p)
    elif eh_parcela_tapada(p):
        return p1 != marca_parcela(p)
    else:
        return p1!=p

#TAD campo-Representação interna: {TAD coordenada: TAD parcela}
def cria_campo(c,l):
    """Esta função cria um campo

    Args:
        c (str): Última coluna de um campo de minas
        l (int): Última linha de um campo de minas

    Raises:
        ValueError: Levanta erro se o tipo de c não é string e se
        o tipo de l não é inteiro

    Returns:
        TAD campo: Campo do tamanho pretendido formado por parcelas 
        tapadas sem minas
    """
    if not (type(c)==str and type(l)==int and len(c)==1 and 65<=ord(c)<=90 and 1<=l<=99):
        raise ValueError ("cria_campo: argumentos invalidos")
    m={}
    al="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for j in range(al.find(c)+1):
        for i in range(1,l+1):
            m[cria_coordenada(al[j],i)]=cria_parcela()
    return m
    
def cria_copia_campo(m):
    """
    Args:
        m (TAD campo): Campo

    Returns:
        dict: Nova cópia do campo
    """
    m1={}
    for c in m:
        m1[c]=cria_copia_parcela(obtem_parcela(m,c))
    return m1

def obtem_ultima_coluna(m):
    """
    Args:
        m (TAD campo): Campo

    Returns:
        str: Cadeia de caracteres que corresponde à
        última coluna do campo de minas
    """
    return obtem_coluna(list(m.keys())[-1])

def obtem_ultima_linha(m):
    """
    Args:
        m (TAD campo): Campo

    Returns:
        str: Cadeia de caracteres que corresponde à
        última linha do campo de minas
    """
    return obtem_linha(list(m.keys())[-1])

def obtem_parcela(m, c):
    """
    Args:
        m (TAD campo): Campo
        c (TAD coordenada): Coordenada

    Returns:
        dict: Parcela do campo m que se encontra na coordenada c
    """
    return m[c]

def obtem_coordenadas(m,s):
    """Esta função devolve o tuplo formado pelas coordenadas ordenadas 
    em ordem ascendente de esquerda à direita e de cima a baixo das parcelas
    dependendo do valor de s

    Args:
        m (TAD campo): Campo
        s (str): Estado inicial

    Returns:
        tuple: Tuplo de coordenadas
    """
    res=()
    for c in m:
        if (s=="tapadas" and eh_parcela_tapada(obtem_parcela(m,c))) or\
            (s=="marcadas" and eh_parcela_marcada(obtem_parcela(m,c))) or\
                (s=="limpas" and eh_parcela_limpa(obtem_parcela(m,c))) or\
                    (s=="minadas" and eh_parcela_minada(obtem_parcela(m,c))):
                    res+=(c,)
    return tuple(sorted(res, key=lambda c: (obtem_linha(c), obtem_coluna(c))))

def obtem_numero_minas_vizinhas(m,c):
    """
    Args:
        m (TAD campo): Campo
        c (TAD coordenada): Coordenada

    Returns:
        int: Número de parcelas vizinhas da parcela na 
        coordenada c que escondem uma mina
    """
    contador=0
    for coordenada in m:
        if eh_parcela_minada(obtem_parcela(m,coordenada))\
            and coordenada in obtem_coordenadas_vizinhas(c):
            contador+=1
    return contador

def eh_campo(arg):
    """
    Args:
        arg (universal): Argumento Universal

    Returns:
        bool: True caso o seu argumento seja um TAD campo e
        False caso contrário.
    """
    return type(arg)==dict and len(arg)>=1 and all([eh_coordenada(chave)\
        for chave in list(arg.keys())]) and all([eh_parcela(valores)\
            for valores in list(arg.values())])

def eh_coordenada_do_campo(m,c):
    """
    Args:
        m (TAD campo): Campo
        c (TAD coordenada): Coordenada

    Returns:
        bool: True se c é uma coordenada válida dentro do campo m
    """
    return eh_coordenada(c) and c in m

def campos_iguais(m1,m2):
    """
    Args:
        m1 (TAD campo): Campo 1
        m2 (TAD campo): Campo 2

    Returns:
        bool: True apenas se m1 e m2 forem campos e
        forem iguais
    """
    sao_iguais = False
    if eh_campo(m1) and eh_campo(m2) and len(m1) == len(m2):
        m1_keys,m2_keys = sorted(list(m1.keys())),sorted(list(m2.keys()))
        for i in range(len(m2_keys)):
            if not coordenadas_iguais(m1_keys[i], m2_keys[i]):
                return sao_iguais 
        for coordenada in m2:   
            if not parcelas_iguais(obtem_parcela(m1, coordenada),obtem_parcela(m2, coordenada)):
                return sao_iguais
        sao_iguais = True
        return sao_iguais
    return sao_iguais

def campo_para_str_aux(m,lst):
    if lst == []:
        return ""
    elif parcela_para_str(obtem_parcela(m,lst[0]))=="?" and\
        obtem_numero_minas_vizinhas(m,lst[0])!=0:
        return "%d"%(obtem_numero_minas_vizinhas(m,lst[0])) + campo_para_str_aux(m,lst[1:]) 
    elif parcela_para_str(obtem_parcela(m,lst[0]))=="?" and\
        obtem_numero_minas_vizinhas(m,lst[0])==0: 
        return " " + campo_para_str_aux(m,lst[1:])
    else:
        return parcela_para_str(obtem_parcela(m,lst[0])) + campo_para_str_aux(m,lst[1:])

def campo_para_str(m):
    """Esta função devolve a representação do campo em cadeia de carateres

    Args:
        m (TAD campo): Campo

    Returns:
        str: Cadeia de caracteres que representa o campo de minas
    """
    alfabeto="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    meio=""
    inicio=("   %s\n  " + "+" + "-"*len(alfabeto[:alfabeto.find(obtem_ultima_coluna(m))+1]) + "+\n")\
        %(alfabeto[:alfabeto.find(obtem_ultima_coluna(m))+1])
    fim = "  +" + "-"*len(alfabeto[:alfabeto.find(obtem_ultima_coluna(m))+1]) + "+"
    for i in range(1,obtem_ultima_linha(m)+1):
        lst=[]
        for coordenadas in m:
            if obtem_linha(coordenadas)==i:
                lst+=[coordenadas]
        meio +=("%.2d|"%(i)) + campo_para_str_aux(m,lst) + "|\n"
    return inicio + meio + fim

def coloca_minas(m,c,g,n):
    """Esta função modifica destrutivamente o campo m escondendo n minas 
    em parcelas dentro do campo

    Args:
        m (TAD campo): Campo
        c (TAD coordenada): Coordenada
        g (TAD gerador): Gerador
        n (int): Número de minas
    """
    def coloca_minas_aux(m,c,g,n,nova_coordenada):
        if n==0:
            return m
        elif not coordenadas_iguais(nova_coordenada,c) and nova_coordenada not \
            in obtem_coordenadas_vizinhas(c)\
            and not eh_parcela_minada(obtem_parcela(m,nova_coordenada)):
                return esconde_mina(obtem_parcela(m,nova_coordenada)) and\
                    coloca_minas_aux(m,c,g,n-1,obtem_coordenada_aleatoria(cria_coordenada\
                (obtem_ultima_coluna(m),obtem_ultima_linha(m)),g))
        else:
            return coloca_minas_aux(m,c,g,n,obtem_coordenada_aleatoria(cria_coordenada\
                (obtem_ultima_coluna(m),obtem_ultima_linha(m)),g))
    return coloca_minas_aux(m,c,g,n,obtem_coordenada_aleatoria(cria_coordenada(\
        obtem_ultima_coluna(m),obtem_ultima_linha(m)),g))

def limpa_campo_aux(m,coordenadas_vizinhas): #Função auxiliar das coordenadas vizinhas
    if coordenadas_vizinhas==():
        return m
    return limpa_campo_aux2(m,coordenadas_vizinhas[0]) and \
        limpa_campo_aux(m,coordenadas_vizinhas[1:])
        
def limpa_campo_aux2(m,c): #Função auxiliar para limpar as parcelas
    if eh_coordenada_do_campo(m,c) and eh_parcela_tapada(obtem_parcela(m,c)):
        limpa_parcela(obtem_parcela(m,c))
        if obtem_numero_minas_vizinhas(m,c) !=0 or eh_parcela_minada(obtem_parcela(m,c)):
            return m
        return limpa_campo_aux(m,obtem_coordenadas_vizinhas(c))
    return m

def limpa_campo(m,c):
    """Esta função modifica destrutivamente o campo limpando a parcela 
    na coordenada c e o devolvendo-a

    Args:
        m (TAD campo): Campo
        c (TAD coordenada): Coordenada
    """
    if eh_coordenada_do_campo(m,c) and eh_parcela_tapada(obtem_parcela(m,c)):
        return limpa_campo_aux2(m,c)
    
    elif eh_coordenada_do_campo(m,c) and eh_parcela_marcada(obtem_parcela(m,c)):
        limpa_parcela(obtem_parcela(m,c))
        if obtem_numero_minas_vizinhas(m,c) !=0 or eh_parcela_minada(obtem_parcela(m,c)):
            return m
        return limpa_campo_aux(m,obtem_coordenadas_vizinhas(c))
    return m

def jogo_ganho(m):
    """Esta função é uma função auxiliar

    Args:
        m (TAD campo): Campo do jogo das minas

    Returns:
        bool: True se todas as parcelas sem minas se encontram
        limpas, ou False caso contrário
    """
    jogo_limpo=True
    coordenadas=()
    for c in obtem_coordenadas(m,"tapadas"):
        coordenadas+=(c,)
    for c in obtem_coordenadas(m,"marcadas"):
        coordenadas+=(c,)
    for c in coordenadas:
        if not eh_parcela_minada(obtem_parcela(m,c)):
            jogo_limpo=False
            return jogo_limpo
    return jogo_limpo

def turno_jogador(m):
    """Esta função modifica destrutivamente o campo de acordo 
    com ação escolhida

    Args:
        m (TAD campo): Campo de minas

    Returns:
        bool: False caso o jogador tenha limpo
        uma parcela que continha uma mina, ou True caso contrário
    """
    acao,coordenada=""," 0"
    numeros= ['0','1','2','3','4','5','6','7','8','9']
    while acao!="L" and acao!="M":
        acao=input("Escolha uma ação, [L]impar ou [M]arcar:")
    while len(coordenada)!=3 or not all([n in numeros for n in coordenada[1:]]) or\
        not (65<=ord(coordenada[0])<=ord(obtem_ultima_coluna(m)) \
            and 1<=int(coordenada[1:])<=obtem_ultima_linha(m)):
        coordenada=input("Escolha uma coordenada:")
    if acao=="L":
        limpa_campo(m,str_para_coordenada(coordenada))
        return not eh_parcela_minada(obtem_parcela(m,str_para_coordenada(coordenada)))
    else:
        if not eh_parcela_limpa(obtem_parcela(m,str_para_coordenada(coordenada))):
            return alterna_bandeira(obtem_parcela(m,str_para_coordenada(coordenada)))
        return not alterna_bandeira(obtem_parcela(m,str_para_coordenada(coordenada)))

def verifica_erros(c,l,n,d,s):
    if not (type(c)==str and type(l)==int and type(n)==int and type(d)==int \
        and type(s)==int and len(c)==1 and (ord(c)-65+1)*l-9>n>0 and(d==32 or d==64) \
            and 0<s<=(2**d)-1 and 1<=l<=99 and 65<=ord(c)<=90): #(ord(c)-65+1)*l-9 ---> Número de parcelas-9
        raise ValueError ("minas: argumentos invalidos")

def minas(c,l,n,d,s):
    """Esta função é a função principal que permite jogar ao jogo das minas.

    Args:
        c (str): Última coluna
        l (int): Última linha
        n (int): Número de parcelas com minas
        d (int): Dimensão do gerador de números
        s (int): Estado inicial ou seed

    Raises:
        ValueError: Levanta erro caso os seus argumentos não sejam válidos

    Returns:
        bool: True se o jogador conseguir ganhar o jogo, ou False caso contrário
    """
    verifica_erros(c,l,n,d,s)
    def minas_aux():
        print("   [Bandeiras %d/%d]" %(len(obtem_coordenadas(m,"marcadas")),n))
        print(campo_para_str(m))
    m=cria_campo(c,l)
    g=cria_gerador(d,s)
    coordenadas=" 0"
    numeros= ['0','1','2','3','4','5','6','7','8','9']
    minas_aux() #Inicio do jogo
    while len(coordenadas)!=3 or not all([n in numeros for n in coordenadas[1:]]) or \
        not (65<=ord(coordenadas[0])<=ord(obtem_ultima_coluna(m)) \
            and 1<=int(coordenadas[1:])<=obtem_ultima_linha(m)):
        coordenadas=input("Escolha uma coordenada:") #Primeira jogada
    coordenadas=str_para_coordenada(coordenadas)
    print("   [Bandeiras %d/%d]" %(len(obtem_coordenadas(m,"marcadas")),n))
    print(campo_para_str(limpa_campo(coloca_minas(m,coordenadas,g,n),coordenadas)))
    while turno_jogador(m): #Ciclo de jogadas
        minas_aux()
        if jogo_ganho(m):
            print("VITORIA!!!")
            return jogo_ganho(m)
    minas_aux()
    print("BOOOOOOOM!!!")
    return jogo_ganho(m)