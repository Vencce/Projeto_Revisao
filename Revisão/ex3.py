def analisa_meteorologia(dados):
    maximas = []
    minimas = []
    chuvas = []
    dias_sem_chuva_quente = []
    maior_precipitacao_dia = ""
    menor_temperatura_dia = ""
    maior_precipitacao = 0
    menor_temperatura = float('inf')
    
    for dado in dados:
        data, temperaturas, chuva = dado.split(': ')
        max_temp = int(temperaturas.split(', ')[0].split('=')[1])
        min_temp = int(temperaturas.split(', ')[1].split('=')[1])
        chuva_mm = float(chuva.split('=')[1].replace('mm', ''))

        maximas.append(max_temp)
        minimas.append(min_temp)
        chuvas.append(chuva_mm)

        if chuva_mm > maior_precipitacao:
            maior_precipitacao = chuva_mm
            maior_precipitacao_dia = data
        
        if min_temp < menor_temperatura:
            menor_temperatura = min_temp
            menor_temperatura_dia = data

        if max_temp > 30 and chuva_mm == 0:
            dias_sem_chuva_quente.append(data)
    
    media_maxima = sum(maximas) / len(maximas)
    media_minima = sum(minimas) / len(minimas)

    print(f"Média de temperatura máxima: {media_maxima:.2f}°C")
    print(f"Média de temperatura mínima: {media_minima:.2f}°C")
    print(f"Dia com maior precipitação: {maior_precipitacao_dia} ({maior_precipitacao}mm)")
    print(f"Dia com menor temperatura: {menor_temperatura_dia} ({menor_temperatura}°C)")
    print(f"Dias com máxima > 30°C e sem chuva: {dias_sem_chuva_quente}")

dados_meteorologia = [
    "2023-09-15: Máxima=35, Mínima=22, Chuva=0.5mm",
    "2023-09-16: Máxima=28, Mínima=20, Chuva=1.0mm",
    "2023-09-17: Máxima=32, Mínima=21, Chuva=0mm",
    "2023-09-18: Máxima=29, Mínima=19, Chuva=2.3mm",
    "2023-09-19: Máxima=31, Mínima=18, Chuva=0mm"
]

analisa_meteorologia(dados_meteorologia)
