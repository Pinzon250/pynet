# pynet

Framework CLI y SDK para proyectos Python (especialmente RPA) en
NetApplications.

## Instalación (desarrollo)

```bash
# Crear y activar entorno virtual
python -m venv .venv
source .venv/bin/activate            # Linux / macOS
.venv\Scripts\activate               # Windows

# Instalar pynet en modo editable, con tools de dev
pip install -e ".[dev]"

# Verificar
pynet --version
pynet-admin --version
pytest -v
```

## Entry points

pynet expone **dos CLIs separados** con audiencias distintas:

| CLI            | Audiencia       | Comandos principales                                |
| -------------- | --------------- | --------------------------------------------------- |
| `pynet`        | Developers      | `create app`, `sync`                                |
| `pynet-admin`  | Administradores | `client add/list/show/remove`, `token issue/list/revoke` |

El dev jamás necesita `pynet-admin`. El admin usa ambos.

## Modelo de autenticación

**Tokens de un solo uso.** Los admins emiten tokens individuales con
`pynet-admin token issue --client <X> --for <dev>`. El dev los usa una
única vez en `pynet create` o `pynet sync`. Tras usarlo, queda como
auditoría y no se puede reutilizar. Si necesita otro proyecto/sync,
otro token.

El token llega por dos vías (en orden de precedencia):

1. Flag `--token <X>` en el comando.
2. Variable de entorno `PYNET_TOKEN`.

No hay `pynet login` ni archivos de config con tokens — sería contrario
al modelo de un solo uso.

## Flujo de uso (visión general)

```bash
# ── Día 1: Juan crea un proyecto nuevo ──
pynet create app MiBot --template rpa --token pynet_ot_juan_xxx

# Se genera ./MiBot/ con:
#   pynet.yaml         (SÍ va al repo: dice qué cliente usa el proyecto)
#   .env               (NO va al repo: tiene las credenciales del KV)
#   Config/, HU/, ...

git init && git push                  # sube todo MENOS .env

# ── Día 2: María clona el repo ──
git clone <repo> && cd MiBot
pynet sync --token pynet_ot_maria_yyy
# → lee pynet.yaml, consume el token, escribe bloque BEGIN/END PYNET SYNC
#   en .env con las credenciales del cliente.
python main.py                        # corre con sus propias credenciales
```

## Instalación con extras (para bots reales)

Los proyectos generados necesitan ciertos módulos del SDK. Cada uno
es un extra opcional:

```bash
pip install "pynet[azure]"     # SDK: cargar secretos de Azure KV
pip install "pynet[database]"  # SDK: clientes de SQL Server, Postgres, MySQL
pip install "pynet[sap]"       # SDK: automatización SAP (solo Windows)
pip install "pynet[email]"     # SDK: SMTP + Outlook/Graph
pip install "pynet[data]"      # SDK: helpers de pandas/excel/csv
pip install "pynet[config]"    # Pydantic Settings (para Config de proyectos)

pip install "pynet[rpa]"       # Bundle completo para bots RPA
pip install "pynet[all]"       # Todo + tools de dev
```

## Estado actual

🚧 En construcción. Roadmap:

- [x] **Paso 1 — Esqueleto:** estructura del paquete, CLI mínimo.
- [x] **Paso 2 — Refactor con auth y backends:** `pynet/admin/` separado,
      `pynet sync`, `core/auth.py`, `core/backends/base.py`,
      excepciones ampliadas. **(Estamos aquí.)**
- [ ] **Paso 3 — Modelos:** `ProjectContext`, `ProjectManifest` (pynet.yaml).
- [ ] **Paso 4 — Backend Azure KV:** implementar `AzureKeyVaultBackend`
      con consumo atómico de tokens.
- [ ] **Paso 5 — Generator + plantilla RPA:** `pynet create app` end-to-end.
- [ ] **Paso 6 — Sync:** `pynet sync` con escritura de bloque BEGIN/END.
- [ ] **Paso 7 — CLI admin:** `pynet-admin client/token` funcionales.
- [ ] **Paso 8 — SDK runtime:** credentials, db, sap, data, email, logging, files.

## Estructura del repositorio

```
pynet/
├── pyproject.toml
├── README.md
├── tests/
│   ├── test_cli.py            ← smoke tests del CLI dev
│   ├── test_admin_cli.py      ← smoke tests del CLI admin
│   └── test_auth.py           ← tests de resolución de tokens
└── pynet/
    ├── __version__.py
    │
    ├── cli/                   ← CLI dev (`pynet`)
    │   ├── app.py
    │   └── commands/
    │       ├── create.py      ← pynet create app
    │       └── sync.py        ← pynet sync
    │
    ├── admin/                 ← CLI admin (`pynet-admin`)
    │   ├── app.py
    │   └── commands/
    │       ├── client.py      ← client add/list/show/remove
    │       └── token.py       ← token issue/list/revoke
    │
    ├── core/                  ← lógica del framework
    │   ├── auth.py            ← resolve_token() — precedencia flag > env
    │   └── backends/
    │       ├── base.py        ← CredentialsBackend (ABC) + dataclasses
    │       ├── azure_kv.py    ← implementación Azure KV (esqueleto)
    │       └── __init__.py    ← get_backend() factory
    │
    ├── sdk/                   ← código que importan los proyectos generados
    │
    ├── templates/             ← plantillas Jinja2 (próximamente)
    │
    └── utils/
        └── exceptions.py      ← jerarquía PynetError → Auth/Backend/...
```

## Tests

```bash
pytest                  # todos
pytest -v               # verbose
pytest --cov=pynet      # con cobertura
pytest tests/test_auth.py -v   # solo uno
```
