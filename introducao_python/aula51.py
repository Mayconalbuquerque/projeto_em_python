velocidade = 100
local_carro = 90

RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega

velocidade_carro_passou_radar_1 = velocidade >= RADAR_1
carro_passou_radar_1 = local_carro == (LOCAL_1 + RADAR_RANGE)
carro_multado = velocidade_carro_passou_radar_1 and carro_passou_radar_1


if velocidade_carro_passou_radar_1:
    print('Velocidade máxima ultrapassada!')

else:
    print('Está abaixo na velocidade máxima!')

if carro_passou_radar_1:
    print('Carro passou pelo radar')

if carro_multado:
    print('Carro foi multado no radar 1')

else:
    print('Carro não foi multado')
