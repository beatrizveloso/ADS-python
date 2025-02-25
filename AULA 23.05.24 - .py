{"nbformat":4,"nbformat_minor":0,"metadata":{"colab":{"provenance":[],"authorship_tag":"ABX9TyMDdrN4SFhiq1+m6StQpFLy"},"kernelspec":{"name":"python3","display_name":"Python 3"},"language_info":{"name":"python"}},"cells":[{"cell_type":"markdown","source":["Arrays = vetores  = ele serve pra armazenar várias informações utilizando apenas um identificador"],"metadata":{"id":"FnexvJbJPMHz"}},{"cell_type":"markdown","source":["Insira os valores do salário de cada mês:"],"metadata":{"id":"S3uIz62hUZ1u"}},{"cell_type":"code","execution_count":7,"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"AKXahnfNN5dJ","executionInfo":{"status":"ok","timestamp":1716465044337,"user_tz":180,"elapsed":31760,"user":{"displayName":"Beatriz Veloso","userId":"00069084993732064588"}},"outputId":"7a16ec87-1df6-4c59-ea80-0f31e1961de5"},"outputs":[{"name":"stdout","output_type":"stream","text":["Digite o salário de Jan R$12\n","Digite o salário de Fev R$32\n","Digite o salário de Mar R$4323\n","Digite o salário de Abr R$54\n","Digite o salário de Mai R$23\n","Digite o salário de Jun R$321\n","Digite o salário de Jul R$34\n","Digite o salário de Ago R$32\n","Digite o salário de Set R$32\n","Digite o salário de Out R$32\n","Digite o salário de Nov R$32\n","Digite o salário de Dez R$76\n"]}],"source":["mes = [\"Jan\", \"Fev\", \"Mar\", \"Abr\", \"Mai\", \"Jun\", \"Jul\", \"Ago\", \"Set\", \"Out\", \"Nov\", \"Dez\"]\n","\n","for i in range(12):\n","  salario = float(input(\"Digite o salário de %s R$\" % mes[i]))"]},{"cell_type":"markdown","source":["Faça um programa em Python que liste 3 nomes:"],"metadata":{"id":"cTxGkAVFUIfb"}},{"cell_type":"code","source":["name = ['Harry', 'Rony', 'Hermione' ]\n","for i in range(3):\n","  print(name[i])"],"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"2CnIInMxTFaQ","executionInfo":{"status":"ok","timestamp":1716465339437,"user_tz":180,"elapsed":439,"user":{"displayName":"Beatriz Veloso","userId":"00069084993732064588"}},"outputId":"e103ee6d-6c63-43b8-fa68-b3d9b2fb826a"},"execution_count":14,"outputs":[{"output_type":"stream","name":"stdout","text":["Harry\n","Rony\n","Hermione\n"]}]},{"cell_type":"markdown","source":["Faça um programa em Python que calcule a média de um aluno apartir de cinco notas :"],"metadata":{"id":"NxzMCWx-T-5m"}},{"cell_type":"code","source":["notas = [5, 6, 7, 8.7, 4.5]\n","qtde = len(notas)\n","\n","# Iterando sobre a lista usando indices\n","soma = 0\n","for i in range(5):\n","  soma = soma + notas[i]\n","media = soma / 5\n","print(\"A média é %f.\" % media)\n","\n","# Iterando sobre os elementos da lista\n","soma = 0\n","for nota in notas:\n","  soma += nota\n","media = soma / 5\n","print(\"A média é %f.\" % media)"],"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"uzZLqkRJUptK","executionInfo":{"status":"ok","timestamp":1716466318555,"user_tz":180,"elapsed":437,"user":{"displayName":"Beatriz Veloso","userId":"00069084993732064588"}},"outputId":"579b1ee5-33fd-4bfc-ef1b-e897cf3201dc"},"execution_count":21,"outputs":[{"output_type":"stream","name":"stdout","text":["A média é 6.240000.\n","A média é 6.240000.\n"]}]},{"cell_type":"markdown","source":["Solicita nomes e os coloca em outra ordem"],"metadata":{"id":"Fml9QfQeYJ1R"}},{"cell_type":"code","source":["nomes = []\n","\n","for i in range(5):\n","  n = input(\"Digite o nome %d: \" % (i + 1))\n","  nomes.insert(5, n)\n","\n","for nome in nomes:\n","  print(nome, end=\" \")"],"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"NCWCaRWKYKYK","executionInfo":{"status":"ok","timestamp":1716467144234,"user_tz":180,"elapsed":9933,"user":{"displayName":"Beatriz Veloso","userId":"00069084993732064588"}},"outputId":"83ec80bd-e241-4e35-ad7b-f153bed77f24"},"execution_count":25,"outputs":[{"output_type":"stream","name":"stdout","text":["Digite o nome 1: A\n","Digite o nome 2: B\n","Digite o nome 3: C\n","Digite o nome 4: D\n","Digite o nome 5: E\n","A B C D E "]}]},{"cell_type":"markdown","source":["Outra forma ..."],"metadata":{"id":"tyzMm9xtcTa4"}},{"cell_type":"code","source":["nomes = []\n","\n","for i in range(5):\n","  n = input(\"Digite o nome %d: \" % (i + 1))\n","  nomes.append(n)\n","\n","for nome in nomes:\n","  print(nome, end=\" \")\n","\n","i = int(input(\"Qual o índice do nome que deseja imprimir? \"))\n","print(nomes[i])"],"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"_3JuHCX8aniS","executionInfo":{"status":"ok","timestamp":1716467526544,"user_tz":180,"elapsed":13704,"user":{"displayName":"Beatriz Veloso","userId":"00069084993732064588"}},"outputId":"124a0099-91a4-4481-f8b9-db12d202721f"},"execution_count":27,"outputs":[{"output_type":"stream","name":"stdout","text":["Digite o nome 1: A\n","Digite o nome 2: B\n","Digite o nome 3: C\n","Digite o nome 4: D\n","Digite o nome 5: E\n","A B C D E Qual o índice do nome que deseja imprimir?4\n","E\n"]}]},{"cell_type":"markdown","source":["Exemplo média de uma quantidade indeterminada de números"],"metadata":{"id":"1tB5r23wdOh6"}},{"cell_type":"code","source":["numeros = []\n","soma = 0\n","\n","resp = 1.0\n","while resp != 0:\n","  resp = float(input(\"Digite um número, 0 para terminar: \"))"],"metadata":{"id":"-82291zNdUGq"},"execution_count":null,"outputs":[]}]}