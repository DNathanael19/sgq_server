from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Aluno, Experimento_Pratico, CriacaoAluno, CriacaoExperimento
import json
from django.contrib.auth.models import User
from django.contrib.auth import authenticate 
from django.contrib.auth import login as lg
import matplotlib as plt
import numpy as np
#from sklearn.linear_model import LinearRegression 



def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    else: 
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        
        user = User.objects.filter(username=username).first()
        if user:
            return HttpResponse('Já existe um usuario com esse nome')
        
        user = User.objects.create_user(username=username, password=senha)
        user.save()
        return redirect('login')


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha)
        if user:
            lg(request, user)
            return redirect('dash')
        else: 
            return HttpResponse('Erro, tente novamente')



#plataform


def coef(x, y): # Vai receber a concentração e a variação de temperatura 
	# número de observações/pontos
	n = np.size(x)

	# média dos vetores x e y
	m_x = np.mean(x)
	m_y = np.mean(y)

	# calculando desvio cruzado e desvio sobre x
	SS_xy = np.sum(y*x) - n*m_y*m_x
	SS_xx = np.sum(x*x) - n*m_x*m_x

	# cálculo de coeficientes de regressão
	b_1 = SS_xy / SS_xx
	b_0 = m_y - b_1*m_x

	return (b_0, b_1)

def k_raul():
    value = Experimento_Pratico.objects.all()

    for c in value:
        variacao = c.concentracao_p * 0.52 


    lista_dados = []
    for c in value:
        lista_dados.append({"x": c.concentracao_p, "y" : variacao})


    return lista_dados, variacao



def k_otimo():
    value = Experimento_Pratico.objects.all()
    concentracao = []
    temp = []

    for c in value:
        concentracao.append([c.concentracao_p])
        temp.append([c.temp_ebulicao_p])

    concentracao = np.array(concentracao)
    temp = np.array(temp)
    reg1, reg2 = coef(concentracao, 100-temp) # só esse

    lista_dados = []
    for i in value:
        lista_dados.append({"x": i.concentracao_p, "y": (reg2 * i.concentracao_p) + reg1}) # reg1 - intercept_ // reg2 - coef_
    
    aux = (reg2 * i.concentracao_p) + reg1
    return lista_dados, aux
    


def teorico():  #CERTOOO    
    value = Experimento_Pratico.objects.all()
    lista_dados = []

    for c in value:
        lista_dados.append({"x": c.concentracao_p, "y" : 100-c.temp_ebulicao_p})

    return lista_dados



def mean_squared_error(y_true, y_pred):
    e = 0
    for yi, yj in zip(y_true, y_pred):
        e += (yi - yj)**2
    return e



def dash(request):
    if request.user.is_authenticated:
        # Verificar se existem experimentos no banco de dados
        if Experimento_Pratico.objects.exists():
            k_Raul, aux = k_raul()
            k_Otimo, aux2 = k_otimo()
            dados = teorico()
            
            value = Experimento_Pratico.objects.all()
            concentracao = []
            temp = []

            for c in value:
                concentracao.append(c.concentracao_p)
                temp.append(c.temp_ebulicao_p)
            
            k_Raul_json = json.dumps(k_Raul) 
            k_Otimo_json = json.dumps(k_Otimo)
            Dados_json = json.dumps(dados)

            return render(request, 'dash.html', {"dados_json": Dados_json, "k_otimo": k_Otimo_json, "k_raul": k_Raul_json, "listas": Experimento_Pratico.objects.all()})
        
        # Caso não existam experimentos, retornar uma mensagem de erro ou renderizar uma página vazia
        return render(request, 'dash.html', {"dados_json": "[]", "k_otimo": "[]", "k_raul": "[]", "listas": []})
    
    return HttpResponse('Você precisa estar logado')










def naologado():
    return HttpResponse('Você nao esta logado')


def newTeorico(request):
    if request.user.is_authenticated:
        formExp = CriacaoExperimento(request.POST or None)
        
        if formExp.is_valid():
            formExp.save()

        return render(request, 'add.html', {'formExp' : formExp})
    
    naologado()



def delTeorico(request, id):
    lista = Experimento_Pratico.objects.get(experimento_p=id)
    lista.delete()
    return HttpResponseRedirect("../../dash")


