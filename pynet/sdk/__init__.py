"""
Subpaquete sdk: librerías que se importan dentro de los proyectos generados.

A diferencia de `pynet.core` (que el framework usa internamente), `pynet.sdk`
es código que viaja con el paquete instalado y los bots importan en runtime.

Estructura final prevista:

    pynet/sdk/
    ├── credentials/      → CargarVault() para descargar secretos de Azure KV
    │   └── azure.py
    ├── db/               → DatabaseClient (ABC) + drivers (sqlserver, postgres, mysql)
    │   ├── base.py
    │   ├── factory.py
    │   └── drivers/
    ├── sap/              → automatización SAP GUI
    ├── data/             → helpers de pandas, excel, csv
    ├── email/            → SMTP + Outlook/Graph
    ├── logging/          → Logger estandarizado de la empresa
    └── files/            → rutas estándar (insumo/resultado/temp/logs)

Cada módulo es opcional: requiere su extra correspondiente para funcionar.
Ejemplo:
    pip install "pynet[azure]"     → habilita pynet.sdk.credentials.azure
    pip install "pynet[database]"  → habilita pynet.sdk.db
    pip install "pynet[rpa]"       → bundle completo para RPA
"""
