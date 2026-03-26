#declarar

Dist : float = 0
Dist_Km : float = 0
Tempo : float = 0
Num_Voltas : float = 0
Ext_Circu: float = 0
Temp_Dur: float = 0
Temp_Dur_Min : float = 0
Vel: float = 0

#inicio

Num_Voltas = float (input("Digite o número de voltas: "))
Ext_Circu = float (input ("Digite a extensão do circuito (em metros): "))
Temp_Dur = float (input("Digite a hora do tempo de duração(ex:1): "))
Temp_Dur_Min = float (input("Agora digite os minutos do tempo de duração (ex:30): "))

Dist = (Num_Voltas * Ext_Circu)
Dist_Km = (Dist /1000) 
Temp_Dur = Temp_Dur + (Temp_Dur_Min/60) #vendo as horas e minutos
Vel = Dist_Km / Temp_Dur #velocidade

print("Sua velocidade é", Vel, "km")

#fim