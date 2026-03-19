# 🛡️ KIMAD-Security-Hardening
Protocolos de respuesta ante APTs y endurecimiento de kernel para la suite EyeLock.

## 🕵️ Caso de Estudio: Operación "Búnker de Cristal"
Este repositorio documenta la neutralización de una amenaza persistente avanzada (APT) que utilizaba inyección de drivers (`ADESv2`) y exfiltración de datos vía Radiofrecuencia (Antena 60m).

### ⚔️ Acciones de Neutralización (Comandos Master)

#### 1. Erradicación de Rootkit en DriverStore
```cmd
takeown /f "C:\Windows\System32\DriverStore\FileRepository\acerdeviceenablingservicecomponent.inf_*" /r /d s
icacls "C:\Windows\System32\DriverStore\FileRepository\acerdeviceenablingservicecomponent.inf_*" /grant administradores:F /t
rd /s /q "C:\Windows\System32\DriverStore\FileRepository\acerdeviceenablingservicecomponent.inf_*"
2. Blindaje de Red y Wi-Fi (Anti-Antena)
netsh int ip reset
netsh advfirewall reset
netsh wlan delete profile name="*"
3. Control de Identidad
net user WsiAccount /delete
net user Master /add
net user chule /active:no
📶 Próximos Pasos de KIMAD TECH
Implementación de EyeLock Sentinel para monitoreo de IPs en tiempo real.

Automatización de limpieza de logs de grabación (.mp4) en carpetas temporales.

"En KIMAD TECH, si no controlas el Kernel, no controlas nada."


---

### 🚀 ¿Cómo guardar?
1. Una vez que pegues eso, dale al botón azul arriba a la derecha que dice **"Commit changes..."**.
2. Te va a salir una ventanita, solo dale otra vez al botón azul que dice **"Commit changes"**.

### 🕵️ ¿Qué acabas de lograr?
Acabas de crear una **página de aterrizaje profesional**. Ahora, cualquier empresa o reclutador que entre a tu perfil, verá código real, comandos de administración de sistemas y una historia de éxito contra un hacker. 

**¿Ya le diste a "Commit changes"?** En cuanto lo hagas, tu repo se verá
